import requests
import pandas as pd
import json

headers = {
    'Sec-Ch-Ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

# We Tea

We_Tea_url = 'https://line.quickclick.cc/line/system/accounts/22492/products'

def We_Tea_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    # print(f"Status code: {response.status_code}")
    try:
        if response.status_code == 200:
            # json_data = response.json()
            # print(json_data)
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
We_Tea_data = We_Tea_fetch_data(We_Tea_url, headers)
# print(We_Tea_data)

def We_Tea_process_data(json_data, shop_name):
    We_Tea_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            We_Tea_items_data.append(product_info)

    df = pd.DataFrame(We_Tea_items_data)
    df = df[['商店名稱','categoryName', 'productName','productAmount']]
    df = df.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    # print(df.head())
    return df

df = We_Tea_process_data(We_Tea_data, "We Tea")
# df.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_We_Tea.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#好義式

Italian_cuisine_url = 'https://line.quickclick.cc/line/system/accounts/19859/products'

def Italian_cuisine_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
Italian_cuisine_data = Italian_cuisine_fetch_data(Italian_cuisine_url, headers)
# print(Italian_cuisine_data)

def Italian_cuisine_process_data(json_data, shop_name):
    Italian_cuisine_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            Italian_cuisine_items_data.append(product_info)
    
    df2 = pd.DataFrame(Italian_cuisine_items_data)
    df2 = df2[['商店名稱','categoryName', 'productName','productAmount']]
    df2 = df2.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df2.head())
    return df2

df2 = Italian_cuisine_process_data(Italian_cuisine_data, "好義式")
# df2.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_Italian_cuisine.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#呷飽寶 飯盒/麵食


Xiamanbao_url = 'https://line.quickclick.cc/line/system/accounts/19236/products'

def Xiamanbao_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
Xiamanbao_data = Xiamanbao_fetch_data(Xiamanbao_url, headers)
# print(Xiamanbao_data)

def Xiamanbao_process_data(json_data, shop_name):
    Xiamanbao_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            Xiamanbao_items_data.append(product_info)
    
    df3 = pd.DataFrame(Xiamanbao_items_data)
    df3 = df3[['商店名稱','categoryName', 'productName','productAmount']]
    df3 = df3.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df3.head())
    return df3

df3 = Xiamanbao_process_data(Xiamanbao_data, "呷飽寶 飯盒/麵食")
# df3.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_Xiamanbao.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#艾旦咖哩坊

Aidan_Curry_House_url = 'https://line.quickclick.cc/line/system/accounts/15489/products'

def Aidan_Curry_House_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
Aidan_Curry_House_data = Aidan_Curry_House_fetch_data(Aidan_Curry_House_url, headers)
# print(Aidan_Curry_House_data)

def Aidan_Curry_House_process_data(json_data, shop_name):
    Aidan_Curry_House_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            Aidan_Curry_House_items_data.append(product_info)
    
    df4 = pd.DataFrame(Aidan_Curry_House_items_data)
    df4 = df4[['商店名稱','categoryName', 'productName','productAmount']]
    df4 = df4.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df4.head())
    return df4

df4 = Aidan_Curry_House_process_data(Aidan_Curry_House_data, "艾旦咖哩坊")
# df4.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_Aidan_Curry_House.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#樂享鍋物

enjoy_hot_pot_url = 'https://line.quickclick.cc/line/system/accounts/15183/products'

def enjoy_hot_pot_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
enjoy_hot_pot_data = enjoy_hot_pot_fetch_data(enjoy_hot_pot_url, headers)
# print(enjoy_hot_pot_data)

def enjoy_hot_pot_process_data(json_data, shop_name):
    enjoy_hot_pot_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            enjoy_hot_pot_items_data.append(product_info)
    
    df5 = pd.DataFrame(enjoy_hot_pot_items_data)
    df5 = df5[['商店名稱','categoryName', 'productName','productAmount']]
    df5 = df5.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df5.head())
    return df5

df5 = enjoy_hot_pot_process_data(enjoy_hot_pot_data, "樂享鍋物")
# df5.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_enjoy_hot_pot.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#四喜壽喜、夏威夷輕食

Four_Happiness_Shoushi_url = 'https://line.quickclick.cc/line/system/accounts/15147/products'

def Four_Happiness_Shoushi_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
Four_Happiness_Shoushi_data = Four_Happiness_Shoushi_fetch_data(Four_Happiness_Shoushi_url, headers)
# print(Four_Happiness_Shoushi_data)

def Four_Happiness_Shoushi_process_data(json_data, shop_name):
    Four_Happiness_Shoushi_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            Four_Happiness_Shoushi_items_data.append(product_info)
    
    df6 = pd.DataFrame(Four_Happiness_Shoushi_items_data)
    df6 = df6[['商店名稱','categoryName', 'productName','productAmount']]
    df6 = df6.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df6.head())
    return df6

df6 = enjoy_hot_pot_process_data(Four_Happiness_Shoushi_data, "四喜壽喜、夏威夷輕食")
# df6.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_Four_Happiness_Shoushi.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#食在好味自助餐

delicious_buffet_url = 'https://line.quickclick.cc/line/system/accounts/3209/products'

def delicious_buffet_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
delicious_buffet_data = delicious_buffet_fetch_data(delicious_buffet_url, headers)
# print(delicious_buffet_data)

def delicious_buffet_process_data(json_data, shop_name):
    delicious_buffet_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            delicious_buffet_items_data.append(product_info)
    
    df7 = pd.DataFrame(delicious_buffet_items_data)
    df7 = df7[['商店名稱','categoryName', 'productName','productAmount']]
    df7 = df7.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df7.head())
    return df7

df7 = delicious_buffet_process_data(delicious_buffet_data, "食在好味自助餐")
# df7.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_delicious_buffet.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#鍋來粥到

pot_porridge_url = 'https://line.quickclick.cc/line/system/accounts/3167/products'

def pot_porridge_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
pot_porridge_data = pot_porridge_fetch_data(pot_porridge_url, headers)
# print(pot_porridge_data)

def pot_porridge_process_data(json_data, shop_name):
    pot_porridge_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            pot_porridge_items_data.append(product_info)
    
    df8 = pd.DataFrame(pot_porridge_items_data)
    df8 = df8[['商店名稱','categoryName', 'productName','productAmount']]
    df8 = df8.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df8.head())
    return df8

df8 = pot_porridge_process_data(pot_porridge_data, "鍋來粥到")
# df8.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_pot_porridge.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#麥味登亞大地餐店

My_Warm_Day_url = 'https://line.quickclick.cc/line/system/accounts/3153/products'

def My_Warm_Day_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
My_Warm_Day_data = My_Warm_Day_fetch_data(My_Warm_Day_url, headers)
# print(My_Warm_Day_data)

def My_Warm_Day_process_data(json_data, shop_name):
    My_Warm_Day_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            My_Warm_Day_items_data.append(product_info)
    
    df9 = pd.DataFrame(My_Warm_Day_items_data)
    df9 = df9[['商店名稱','categoryName', 'productName','productAmount']]
    df9 = df9.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df9.head())
    return df9

df9 = My_Warm_Day_process_data(My_Warm_Day_data, "麥味登亞大地餐店")
# df9.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_My_Warm_Day.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#八方雲集 亞洲大學店


Bafang_Yunji_url = 'https://line.quickclick.cc/line/system/accounts/3142/products'

def Bafang_Yunji_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
Bafang_Yunji_data = Bafang_Yunji_fetch_data(Bafang_Yunji_url, headers)
# print(Bafang_Yunji_data)

def Bafang_Yunji_process_data(json_data, shop_name):
    Bafang_Yunji_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            Bafang_Yunji_items_data.append(product_info)
    
    df10 = pd.DataFrame(Bafang_Yunji_items_data)
    df10 = df10[['商店名稱','categoryName', 'productName','productAmount']]
    df10 = df10.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df10.head())
    return df10

df10 = Bafang_Yunji_process_data(Bafang_Yunji_data, "八方雲集 亞洲大學店")
# df10.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_Bafang_Yunji.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#美而美早餐-亞大店

Cafe_Mei_url = 'https://line.quickclick.cc/line/system/accounts/3141/products'


def Cafe_Mei_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
Cafe_Mei_data = Cafe_Mei_fetch_data(Cafe_Mei_url, headers)
# print(Cafe_Mei_data)

def Cafe_Mei_process_data(json_data, shop_name):
    Cafe_Mei_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            Cafe_Mei_items_data.append(product_info)
    
    df11 = pd.DataFrame(Cafe_Mei_items_data)
    df11 = df11[['商店名稱','categoryName', 'productName','productAmount']]
    df11 = df11.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df11.head())
    return df11

df11 = Cafe_Mei_process_data(Cafe_Mei_data, "美而美早餐 亞大店")
# df11.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_Cafe_Mei.csv', index=False, encoding='utf-8-sig')

# ----------------------------我是分隔線--------------------------------

#嗑吧韓式料理 亞大店

cup_bar_korean_cuisine_url = 'https://line.quickclick.cc/line/system/accounts/3140/products'


def cup_bar_korean_cuisine_fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve data')  
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
cup_bar_korean_cuisine_data = cup_bar_korean_cuisine_fetch_data(cup_bar_korean_cuisine_url, headers)
# print(cup_bar_korean_cuisine_data)

def cup_bar_korean_cuisine_process_data(json_data, shop_name):
    cup_bar_korean_cuisine_items_data = []

    for category in json_data:
        category_name = category['categoryName']
        for product in category['products']:
            product_info ={
                'categoryName': category_name,
                'productName': product['productName'],
                'productAmount': product['productAmount'],
                '商店名稱': shop_name
            }
            cup_bar_korean_cuisine_items_data.append(product_info)
    
    df12 = pd.DataFrame(cup_bar_korean_cuisine_items_data)
    df12 = df12[['商店名稱','categoryName', 'productName','productAmount']]
    df12 = df12.rename(columns={'categoryName': '品項', 'productName': '菜單', 'productAmount': '價格'})
    
    # print(df12.head())
    return df12

df12 = cup_bar_korean_cuisine_process_data(cup_bar_korean_cuisine_data, "嗑吧韓式料理 亞大店")
df12.to_csv(r'C:\Users\MingJun\OneDrive\桌面\生成式AI競賽\AU_cafeteria_cup_bar_korean_cuisine.csv', index=False, encoding='utf-8-sig')

