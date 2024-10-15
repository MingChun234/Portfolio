from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import openai
import os
import pandas as pd
import logging
import random
import mysql.connector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("CUSTOM_API_KEY")

if openai.api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")
if API_KEY is None:
    raise ValueError("Please set the CUSTOM_API_KEY environment variable")

# 读取CSV文件
CSV_PATH = os.getenv('CSV_PATH', 'AU_cafeteria_Bafang_Yunji-v3.csv')
df = pd.read_csv(CSV_PATH, encoding='utf-8-sig')
# df.replace('', pd.NA, inplace=True)
# df.fillna(0, inplace=True)

app = Flask(__name__)
CORS(app)

# 獲取MySQL數據庫連接
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  
        user='root',       
        password='',      
        database='ganai_database'
    )

def calculate_daily_caloric_need(gender, height, weight, age, exercise_days_per_week):
    if gender == '男性':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女性':
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    else:
        return None

    if exercise_days_per_week == 0:
        activity_level = 1.2
    elif 0 < exercise_days_per_week <= 3:
        activity_level = 1.375
    elif 3 < exercise_days_per_week <= 5:
        activity_level = 1.55
    elif exercise_days_per_week == 6:
        activity_level = 1.725
    elif exercise_days_per_week == 7:
        activity_level = 1.9
    else:
        print("請輸入有效的運動天數（0-7）")

    daily_caloric_need = bmr * activity_level
    return daily_caloric_need

def calculate_macronutrients(tdee):
    carbs_calories = tdee * 0.55
    protein_calories = tdee * 0.15
    fat_calories = tdee * 0.25

    carbs_grams = carbs_calories / 4 
    protein_grams = protein_calories / 4 
    fat_grams = fat_calories / 9 

    return {
        'carbohydrates': carbs_grams,
        'protein': protein_grams,
        'fat': fat_grams
    }

def calculate_bmi(weight, height):
    height_m = height / 100  # 将身高从厘米转换为米
    bmi = weight / (height_m ** 2)
    return bmi


def generate_food_recommendations(daily_caloric_need, macronutrients, gender, age, height, weight, df, bmi):
    recommendations = []
    for index, row in df.iterrows():
        selected_recommendations = []
        if bmi < 18.5:
            if row['熱量'] >= daily_caloric_need/4:
                recommendations.append({'store': row['商店名稱'],
                                        'name': row['菜名'],
                                        'calories': row['熱量'],
                                        'protein': row['蛋白質(g)'],
                                        'fat': row['脂肪(g)'],
                                        'carbs': row['碳水化合物(g)']
                                        })       
        elif 18.5 <= bmi < 24:
                recommendations.append({'store': row['商店名稱'],
                                        'name': row['菜名'],
                                        'calories': row['熱量'],
                                        'protein': row['蛋白質(g)'],
                                        'fat': row['脂肪(g)'],
                                        'carbs': row['碳水化合物(g)']
                                       })        
        elif bmi >= 24:
            if row['熱量'] <= daily_caloric_need/4:
                recommendations.append({'store': row['商店名稱'],
                                        'name': row['菜名'],
                                        'calories': row['熱量'],
                                        'protein': row['蛋白質(g)'],
                                        'fat': row['脂肪(g)'],
                                        'carbs': row['碳水化合物(g)']
                                       })

    selected_recommendations = random.sample(recommendations, 3)
    recommendations = []

    prompt = f"根據推薦的食物生成詳細的分析，描述這些食物的營養價值和特徵，並結合用戶的年齡、性別、身高、體重、BMI、每日基礎代謝熱量、每日建議營養需求進行回應，請特別加強BMI、每日基礎代謝熱量、每日建議營養需求的回應：\n"
    prompt += f"用戶資料：性別: {gender}, 年齡: {age}, 身高: {height} cm, 體重: {weight} kg, BMI: {bmi:.1f}, 每日基礎代謝熱量: {daily_caloric_need}, 每日建議營養需求: {macronutrients}\n\n"

    for rec in selected_recommendations:
        prompt += (
            f"食物名稱：{rec['name']}\n"
            f"商店名稱：{rec['store']}\n"
            f"熱量：{rec['calories']} 卡\n"
            f"蛋白質：{rec['protein']} g\n"
            f"脂肪：{rec['fat']} g\n"
            f"碳水化合物：{rec['carbs']} g\n"
            # f"食材：{rec['ingredients']}\n"
            # f"烹飪方法：{rec['cooking_method']}\n"
            # f"營養特徵：{rec['nutritional_features']}\n"
            # f"地區特色：{rec['regional_features']}\n\n"
        )

    # 增加提示以生成更自然的分析和总结
    prompt += (
        "請根據用戶的BMI和每日總熱量消耗（TDEE），生成一段詳細的分析，描述推薦食物的營養價值和特徵，"
        "請以自然、專業且吸引人的語言描述這道菜的特點，解釋其食材、烹飪方法和地區文化如何影響其風味和口感。詳細說明其營養價值如何滿足用戶的需求，並根據用戶的健康狀況（如BMI）和生活方式和每日總熱量消耗（TDEE）提供針對性的建議。不要只重複數據，要深入解釋每種營養素的作用和益處\n"
        "特別注意：如果用戶的BMI過低，應強調增加營養攝取和高熱量食物的適量攝入。如果用戶的BMI在正常範圍，應強調均衡飲食。如果用戶的BMI過高，應強調控制高熱量食物的攝取。\n"
        "最後，以自然的語句進行總結，不要使用任何特殊符號或標記。\n"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一位營養學專家和美食評論家和營養師，擅長解釋食物的營養價值及推廣正確的營養觀念給大家。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        summary = response['choices'][0]['message']['content']
        descriptions = summary.split('\n\n')
    except Exception as e:
        return {'error': f"Error generating OpenAI response: {e}"}

    for i in range(len(selected_recommendations)):
        if i < len(descriptions):
            selected_recommendations[i]['description'] = descriptions[i]
        else:
            selected_recommendations[i]['description'] = "沒有可用的詳細描述。"

    return {
        'daily_caloric_need': daily_caloric_need,
        'macronutrients': macronutrients,
        'recommendations': selected_recommendations,
        'summary': summary,
        'bmi': round(bmi, 2)
    }

@app.route('/recommend_food', methods=['POST'])

def api_recommend_food():
    data = request.json
    gender = data.get('gender')
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    exercise = data.get('exercise')

    if not all([gender, height, weight, age, exercise]):
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        height = float(height)
        weight = float(weight)
        age = int(age)
        exercise = int(exercise)
    except ValueError:
        return jsonify({'error': 'Invalid parameter format'}), 400

    daily_caloric_need = calculate_daily_caloric_need(gender, height, weight, age, exercise)
    bmi = calculate_bmi(weight, height)

    if daily_caloric_need is None:
        return jsonify({'error': 'Invalid gender input'}), 400

    macronutrients = calculate_macronutrients(daily_caloric_need)
    recommendation = generate_food_recommendations(daily_caloric_need, macronutrients, gender, age, height, weight, df, bmi)

    return jsonify(recommendation)
@app.route('/update_user_data', methods=['POST'])

def update_user_data():
    data = request.get_json()
    # print("Received data:", data)  # 添加這行來檢查接收到的資料
    user_id = data['User_ID']
    gender = data['gender']
    age = data['age']
    height = data['height']
    weight = data['weight']
    exercise_days_per_week = data['exercise_days_per_week']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE user_data
        SET gender = %s, age = %s, height = %s, weight = %s, exercise_days_per_week = %s
        WHERE User_ID = %s
    ''', (gender, age, height, weight, exercise_days_per_week, user_id))

    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'status': 'success'})

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    user_id = request.args.get('user_id')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM user_data WHERE User_ID = %s', (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

