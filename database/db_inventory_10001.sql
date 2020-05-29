-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2019 at 12:14 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_inventory_10001`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_assign_suki_card`
--

CREATE TABLE `tbl_assign_suki_card` (
  `assign_suki_id` int(11) NOT NULL,
  `suki_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `date_assign` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_customer`
--

CREATE TABLE `tbl_customer` (
  `customer_id` int(11) NOT NULL,
  `customer_fname` varchar(100) NOT NULL,
  `customer_mname` varchar(100) NOT NULL,
  `customer_lname` varchar(100) NOT NULL,
  `customer_address` varchar(200) NOT NULL,
  `customer_contact` varchar(15) NOT NULL,
  `customer_birthday` date NOT NULL,
  `customer_work` varchar(100) NOT NULL,
  `customer_gender` varchar(10) NOT NULL,
  `customer_email` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_invoice`
--

CREATE TABLE `tbl_invoice` (
  `invoice_id` int(11) NOT NULL,
  `invoice_no` varchar(20) NOT NULL,
  `invoice_date` date NOT NULL,
  `user_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_product`
--

CREATE TABLE `tbl_product` (
  `product_id` varchar(30) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_details` varchar(500) NOT NULL,
  `product_brand` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_product`
--

INSERT INTO `tbl_product` (`product_id`, `product_name`, `product_details`, `product_brand`) VALUES
('1', 'Ladys Choice Real Mayonnaises', 'Ladys Choice Real Mayonnaise (220 ml)', 'Ladys Choice '),
('2', 'Nestle CHUCKIE Chocolate Milk Drink ', 'Nestle CHUCKIE Chocolate Milk Drink (1000 ml)', 'Nestle'),
('3', 'Hershey\'s Nuggets Milk Chocolate with Almonds', 'Hershey\'s Nuggets Milk Chocolate with Almonds', 'Hershey'),
('4', 'Nescafe Clasico Dark Roast Instant Coffee', 'Dark roast, rich, bold flavor in every cup', 'Nescafe'),
('5', 'Bear Brand Powdered Filled Milk 900g', 'Nestle Bear Brand Fortified 900g, Contains adult level nutrients, High in Calcium, Plus Vitamin D, and Phosphorous', 'Bear Brand');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_sales`
--

CREATE TABLE `tbl_sales` (
  `sales_id` int(11) NOT NULL,
  `sales_quantity` int(11) NOT NULL,
  `sales_date` date NOT NULL,
  `sales_price` double NOT NULL,
  `invoice_id` int(11) NOT NULL,
  `product_id` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_stock_in`
--

CREATE TABLE `tbl_stock_in` (
  `stock_in_id` int(11) NOT NULL,
  `stock_in_quantity` int(11) NOT NULL,
  `stock_price` double NOT NULL,
  `stock_in_date` date NOT NULL,
  `product_id` varchar(30) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_stock_in`
--

INSERT INTO `tbl_stock_in` (`stock_in_id`, `stock_in_quantity`, `stock_price`, `stock_in_date`, `product_id`, `user_id`) VALUES
(13, 100, 50, '2019-10-02', '1', 1),
(14, 100, 60, '2019-10-02', '2', 1),
(15, 50, 100, '2019-10-02', '3', 1),
(16, 100, 80, '2019-10-02', '4', 1),
(17, 60, 90, '2019-10-02', '5', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_suki_card`
--

CREATE TABLE `tbl_suki_card` (
  `suki_id` int(11) NOT NULL,
  `suki_card_no` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_suki_card`
--

INSERT INTO `tbl_suki_card` (`suki_id`, `suki_card_no`) VALUES
(1, 'aa-0000000001'),
(2, 'aa-0000000002'),
(4, 'aa-0000000003'),
(5, 'aa-0000000004'),
(6, 'aa-0000000005'),
(7, 'aa-0000000006'),
(8, 'aa-0000000007'),
(9, 'aa-0000000008'),
(10, 'aa-0000000009'),
(11, 'aa-0000000010');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `user_id` int(11) NOT NULL,
  `user_username` varchar(30) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_name` varchar(200) NOT NULL,
  `user_gender` varchar(10) NOT NULL,
  `user_address` varchar(400) NOT NULL,
  `user_contact` varchar(15) NOT NULL,
  `user_position` tinyint(1) NOT NULL,
  `user_status` tinyint(2) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`user_id`, `user_username`, `user_password`, `user_name`, `user_gender`, `user_address`, `user_contact`, `user_position`, `user_status`) VALUES
(1, 'admin', 'admin', 'rudy canana', 'Male', 'Sagay city, Neg. Occ.', '09123143225', 1, 1),
(2, 'ronald', 'ronald', 'Ronald Dogomeo', 'Male', 'Toboso, Neg. Occ.', '09078697428', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_assign_suki_card`
--
ALTER TABLE `tbl_assign_suki_card`
  ADD PRIMARY KEY (`assign_suki_id`),
  ADD KEY `suki_id` (`suki_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `tbl_customer`
--
ALTER TABLE `tbl_customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tbl_invoice`
--
ALTER TABLE `tbl_invoice`
  ADD PRIMARY KEY (`invoice_id`),
  ADD UNIQUE KEY `invoice_no` (`invoice_no`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `tbl_product`
--
ALTER TABLE `tbl_product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `tbl_sales`
--
ALTER TABLE `tbl_sales`
  ADD PRIMARY KEY (`sales_id`),
  ADD KEY `invoice_id` (`invoice_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `tbl_stock_in`
--
ALTER TABLE `tbl_stock_in`
  ADD PRIMARY KEY (`stock_in_id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `stock_in_user_id` (`user_id`),
  ADD KEY `product_id_2` (`product_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `user_id_2` (`user_id`);

--
-- Indexes for table `tbl_suki_card`
--
ALTER TABLE `tbl_suki_card`
  ADD PRIMARY KEY (`suki_id`),
  ADD UNIQUE KEY `suki_card_no` (`suki_card_no`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_username` (`user_username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_assign_suki_card`
--
ALTER TABLE `tbl_assign_suki_card`
  MODIFY `assign_suki_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_customer`
--
ALTER TABLE `tbl_customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_invoice`
--
ALTER TABLE `tbl_invoice`
  MODIFY `invoice_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_sales`
--
ALTER TABLE `tbl_sales`
  MODIFY `sales_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_stock_in`
--
ALTER TABLE `tbl_stock_in`
  MODIFY `stock_in_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `tbl_suki_card`
--
ALTER TABLE `tbl_suki_card`
  MODIFY `suki_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_assign_suki_card`
--
ALTER TABLE `tbl_assign_suki_card`
  ADD CONSTRAINT `tbl_assign_suki_card_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `tbl_customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_assign_suki_card_ibfk_2` FOREIGN KEY (`suki_id`) REFERENCES `tbl_suki_card` (`suki_id`);

--
-- Constraints for table `tbl_customer`
--
ALTER TABLE `tbl_customer`
  ADD CONSTRAINT `tbl_customer_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_invoice`
--
ALTER TABLE `tbl_invoice`
  ADD CONSTRAINT `tbl_invoice_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_invoice_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `tbl_customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_sales`
--
ALTER TABLE `tbl_sales`
  ADD CONSTRAINT `tbl_sales_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `tbl_invoice` (`invoice_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_sales_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_stock_in`
--
ALTER TABLE `tbl_stock_in`
  ADD CONSTRAINT `tbl_stock_in_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_stock_in_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
