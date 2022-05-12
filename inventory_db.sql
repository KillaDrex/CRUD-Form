CREATE DATABASE  IF NOT EXISTS `inventory_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `inventory_db`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: inventory_db
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `brnch_id` int NOT NULL AUTO_INCREMENT,
  `com_id` int DEFAULT NULL,
  `brnch_address` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`brnch_id`),
  KEY `FK_BRANCH` (`com_id`),
  CONSTRAINT `FK_BRANCH` FOREIGN KEY (`com_id`) REFERENCES `branch` (`brnch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES (10,NULL,'30 F. Cabahug St, Cebu City, Cebu, Philippines'),(14,10,'Juan Luna, Mabolo 6000 Cebu City, Philippines'),(15,10,'Osmena Boulevard, 6000 Cebu City, Philippines'),(16,10,'30 F. Cabahug St, Cebu City, Cebu, Philippines');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_id` int NOT NULL AUTO_INCREMENT,
  `outlet_id` int NOT NULL,
  `cust_lname` varchar(35) DEFAULT NULL,
  `cust_fname` varchar(35) DEFAULT NULL,
  `phone_num` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`cust_id`),
  KEY `outlet_id` (`outlet_id`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`outlet_id`) REFERENCES `branch` (`brnch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,14,'Dizon','Jepoy','09453569865');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `emp_id` int NOT NULL AUTO_INCREMENT,
  `brnch_id` int NOT NULL,
  `pos_code` int NOT NULL,
  `emp_lname` varchar(35) DEFAULT NULL,
  `emp_fname` varchar(35) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  KEY `brnch_id` (`brnch_id`),
  KEY `pos_code` (`pos_code`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`brnch_id`) REFERENCES `branch` (`brnch_id`),
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`pos_code`) REFERENCES `position` (`pos_code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,10,1,'Aquino','Andre','2022-07-14'),(2,10,2,'Banez','Luis','2022-08-17'),(3,14,4,'Bautista','Rae','2021-08-17'),(4,15,4,'Bautista','Elmric','2020-05-17'),(5,14,4,'Santos','Julio','2021-03-15');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `package`
--

DROP TABLE IF EXISTS `package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `package` (
  `pckge_no` int NOT NULL AUTO_INCREMENT,
  `brnch_id` int NOT NULL,
  `item_code` varchar(25) DEFAULT NULL,
  `batch_code` int DEFAULT NULL,
  `pckg_price` float DEFAULT NULL,
  `manufac_date` date DEFAULT NULL,
  `prep_date` date DEFAULT NULL,
  `expr_date` date DEFAULT NULL,
  PRIMARY KEY (`pckge_no`),
  UNIQUE KEY `item_code` (`item_code`,`batch_code`),
  KEY `brnch_id` (`brnch_id`),
  CONSTRAINT `package_ibfk_1` FOREIGN KEY (`brnch_id`) REFERENCES `branch` (`brnch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `package`
--

LOCK TABLES `package` WRITE;
/*!40000 ALTER TABLE `package` DISABLE KEYS */;
/*!40000 ALTER TABLE `package` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `position` (
  `pos_code` int NOT NULL AUTO_INCREMENT,
  `pos_class` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`pos_code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES (1,'Supervisor'),(2,'Purchaser'),(3,'Dispatcher'),(4,'Front-of-house'),(5,'Back-of-house');
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supply_order`
--

DROP TABLE IF EXISTS `supply_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supply_order` (
  `order_no` int NOT NULL AUTO_INCREMENT,
  `com_id` int NOT NULL,
  `supplier` varchar(100) DEFAULT NULL,
  `material_name` varchar(30) DEFAULT NULL,
  `qty` float DEFAULT NULL,
  `qty_unit` varchar(30) DEFAULT NULL,
  `supply_price` float DEFAULT NULL,
  `approval_status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`order_no`),
  KEY `com_id` (`com_id`),
  CONSTRAINT `supply_order_ibfk_1` FOREIGN KEY (`com_id`) REFERENCES `branch` (`brnch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supply_order`
--

LOCK TABLES `supply_order` WRITE;
/*!40000 ALTER TABLE `supply_order` DISABLE KEYS */;
INSERT INTO `supply_order` VALUES (1,10,'Jupoy\'s Butchershop','Raw beef',30,'kg',700.32,'approved'),(2,10,'Marina & More','Raw salmon',25,'kg',500.32,'approved'),(3,10,'Grocer\'s Inc.','Wild truffles',35,'kg',100000,'disapproved');
/*!40000 ALTER TABLE `supply_order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-29 18:00:55
