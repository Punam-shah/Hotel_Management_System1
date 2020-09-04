-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 06:23 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `check_out`
--

CREATE TABLE `check_out` (
  `id` int(50) NOT NULL,
  `Date` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Room_no` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `check_out`
--

INSERT INTO `check_out` (`id`, `Date`, `Name`, `Room_no`) VALUES
(24, '8/31/20-5:40-PM', 'Rijan Shrestha', 102),
(25, '9/1/20-2:00-PM', 'Jenisha Pokheral', 105),
(27, '8/30/20-1:10-PM', 'Punam Shah', 118);

-- --------------------------------------------------------

--
-- Table structure for table `guest_list`
--

CREATE TABLE `guest_list` (
  `id` int(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Room_no` int(50) NOT NULL,
  `Date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `guest_list`
--

INSERT INTO `guest_list` (`id`, `Name`, `Room_no`, `Date`) VALUES
(42, 'Punam Shah', 101, '8/30/20-1:10-PM'),
(43, 'Rijan Shrestha', 102, '8/31/20-12:00-AM'),
(44, 'Bishnu Shah', 103, '8/31/20-1:12-PM'),
(45, 'Puja Shah', 104, '8/31/20-1:30-PM'),
(46, 'Jenisha Pokheral', 105, '8/31/20-1:40-PM'),
(47, 'Dimpal Shah', 107, '9/3/20-9:15-PM'),
(48, 'Dimpal Shah', 107, '9/3/20-9:15-PM'),
(49, 'Dimpal Shah', 107, '9/3/20-9:15-PM');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_management_system`
--

CREATE TABLE `hotel_management_system` (
  `id` int(50) NOT NULL,
  `Date` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Contact` varchar(20) NOT NULL,
  `No_of_days` varchar(100) NOT NULL,
  `Payment_method` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel_management_system`
--

INSERT INTO `hotel_management_system` (`id`, `Date`, `Name`, `Address`, `Contact`, `No_of_days`, `Payment_method`) VALUES
(53, '8/31/20-1:12-PM', 'Bishnu Shah', 'ktm', '+9779874563210', '2', 'Card-30000'),
(54, '8/31/20-1:30-PM', 'Puja Shah', 'ktm', '+9779874563210', '1', 'Card-'),
(59, '9/3/20-9:15-PM', 'Dimpal Shah', 'ktm', '+9779874563210', '2', 'Card-30000');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `id` int(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Room_no` varchar(50) NOT NULL,
  `Room_Type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`id`, `Name`, `Room_no`, `Room_Type`) VALUES
(46, 'Punam Shah', ' 101', 'Deluxe'),
(48, 'Bishnu Shah', ' 103', 'Deluxe'),
(49, 'Puja Shah', ' 104', 'Deluxe'),
(50, 'Jenisha Pokheral', ' 105', 'Full_Deluxe'),
(51, 'Punam Shah', '101', 'Deluxe'),
(54, 'Dimpal Shah', '107', 'Deluxe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `check_out`
--
ALTER TABLE `check_out`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `guest_list`
--
ALTER TABLE `guest_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_management_system`
--
ALTER TABLE `hotel_management_system`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `check_out`
--
ALTER TABLE `check_out`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `guest_list`
--
ALTER TABLE `guest_list`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `hotel_management_system`
--
ALTER TABLE `hotel_management_system`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
