-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024 年 06 月 05 日 21:26
-- 伺服器版本： 10.4.27-MariaDB
-- PHP 版本： 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `ganai_database`
--

-- --------------------------------------------------------

--
-- 資料表結構 `ganai_user`
--

CREATE TABLE `ganai_user` (
  `User_ID` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `User_Password` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `user_data`
--

CREATE TABLE `user_data` (
  `User_ID` char(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `gender` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `age` int(100) DEFAULT NULL,
  `height` int(6) DEFAULT NULL,
  `weight` int(6) DEFAULT NULL,
  `exercise_days_per_week` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `ganai_user`
--
ALTER TABLE `ganai_user`
  ADD PRIMARY KEY (`User_ID`);

--
-- 資料表索引 `user_data`
--
ALTER TABLE `user_data`
  ADD PRIMARY KEY (`User_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
