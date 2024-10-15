<?php
session_start();

// 檢查用戶是否已經登錄
if (!isset($_SESSION['user_id'])) {
    echo "請先登錄。";
    exit;
}

// 資料庫連接設定
$servername = "localhost"; // 資料庫伺服器名稱
$username = "root"; // 資料庫使用者名稱
$password = ""; // 資料庫密碼
$dbname = "ganai_database"; // 資料庫名稱

// 建立連接
$conn = new mysqli($servername, $username, $password, $dbname);

// 檢查連接
if ($conn->connect_error) {
    die("連接失敗: " . $conn->connect_error);
}

// 取得用戶 ID
$user_id = $_SESSION['User_ID'];

// 刪除用戶記錄
$sql = "DELETE FROM users WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $user_id);

if ($stmt->execute()) {
    echo "帳號已成功刪除。";
    // 登出用戶
    session_destroy();
    // 重定向到登錄頁面或首頁
    header("Location: login.html");
    exit;
} else {
    echo "刪除失敗: " . $stmt->error;
}

// 關閉連接
$stmt->close();
$conn->close();