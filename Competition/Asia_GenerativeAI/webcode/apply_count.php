<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="utf-8">
    <title>註冊帳號</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .sussess-message {
            color: #ff0000;
            margin-bottom: 10px;
        }

    </style>
</head>
<body>
<?php 
$dsn = "mysql:host=127.0.0.1;port=3306;dbname=ganai_database;charset=utf8";
$username = 'root';
$password = '';
// $password = '123456';  # 歐的密碼

try {
    $link = new PDO($dsn, $username, $password);
    $link->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    

    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        if (isset($_POST["apply"])) {

            $User_ID = $_POST['User_ID'];
            $User_Password = $_POST['User_Password'];
            
            // 檢查帳號是否已存在
            $checkSql = 'SELECT * FROM GanAI_User WHERE User_ID = ?';
            $checkRecord = $link->prepare($checkSql);
            $checkRecord->execute(array($User_ID));
            if ($checkRecord->rowCount() > 0) {
                echo '<div class="error-message">帳號已存在，請選擇其他帳號</div>';
            } else {
                // 插入帳號資料到 GanAI_User 資料表
                $sql = 'INSERT INTO GanAI_User (User_ID, User_Password) VALUES (?, ?)';
                $link->query('SET NAMES utf8');
                $record = $link->prepare($sql);
                $record->execute(array($User_ID, $User_Password));

                // 插入 User_ID 到 user_data 資料表，初始化記錄
                $sql = 'INSERT INTO user_data (User_ID, gender, age, height, weight, exercise_days_per_week) VALUES (?, "", 0, 0, 0, 0)';
                $record = $link->prepare($sql);
                $record->execute(array($User_ID));

                echo '<div class="success-message">註冊成功，您現在可以登入</div>';
                echo '<a href="welcomepage.html">返回主頁</a>';
            }
        }
    }
} catch (PDOException $e) {
    echo "<p>資料庫連線錯誤：" . $e->getMessage() . "</p>";
}
?>
</body>
</html>
