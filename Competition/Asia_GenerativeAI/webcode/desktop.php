<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>亞洲大學AI餐食推薦系統登入</title>
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

        .error-message {
            color: #ff0000;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <?php
    // 資料庫連線設定
    $dsn = "mysql:host=127.0.0.1;port=3306;dbname=ganai_database;charset=utf8";
    $username = "root";
    $password = "";
    // $password = '123456';  # 歐的密碼
    
    try {
        $db = new PDO($dsn, $username, $password);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        die("連線失敗: " . $e->getMessage());
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // 獲取表單提交的資料
        $User_ID = $_POST['User_ID'];
        $User_Password = $_POST['User_Password'];

        // 在資料庫中驗證用戶
        $query = "SELECT * FROM GanAI_User WHERE User_ID = ? AND User_Password = ?";
        $stmt = $db->prepare($query);
        $stmt->execute([$User_ID, $User_Password]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user) {
            // header("Location: homepage.html");// 用戶驗證成功，轉向選課系統
            echo '<script type="text/javascript">
                alert("登入成功");
                localStorage.setItem("User_ID", "' . $User_ID . '");
                window.location.href = "homepage.html";
            </script>';
            exit;
        } else {
            echo '<div class="error-message">登入失敗，請輸入正確的帳號密碼。</div>';// 用戶驗證失敗，顯示錯誤訊息
            echo '<a href="desktop.html">返回主頁</a>'; // 新增一個返回主頁的按鈕
        }
    }
    ?>
</body>
</html>
