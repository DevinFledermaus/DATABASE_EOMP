-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: Lifechoices_Online
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Kin`
--

DROP TABLE IF EXISTS `Kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Surname` varchar(30) NOT NULL,
  `Phone_number` int NOT NULL,
  `User_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `User_id` (`User_id`),
  CONSTRAINT `Kin_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `Login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kin`
--

LOCK TABLES `Kin` WRITE;
/*!40000 ALTER TABLE `Kin` DISABLE KEYS */;
INSERT INTO `Kin` VALUES (2,'Dean','Winchester',219879938,1);
/*!40000 ALTER TABLE `Kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Log`
--

DROP TABLE IF EXISTS `Log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `ID_Number` varchar(50) NOT NULL,
  `UserID` int unsigned NOT NULL,
  `Time_in` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `Log_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Log`
--

LOCK TABLES `Log` WRITE;
/*!40000 ALTER TABLE `Log` DISABLE KEYS */;
INSERT INTO `Log` VALUES (4,'Devin','9705105019082',1,'2021-07-10 21:04:20');
/*!40000 ALTER TABLE `Log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Login`
--

DROP TABLE IF EXISTS `Login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Login` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Surname` varchar(100) NOT NULL,
  `Id_number` varchar(13) NOT NULL,
  `Phone_number` int NOT NULL,
  `Time_out` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Time_in` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Login`
--

LOCK TABLES `Login` WRITE;
/*!40000 ALTER TABLE `Login` DISABLE KEYS */;
INSERT INTO `Login` VALUES (1,'Devin','Fledermaus','9705105019082',780384562,'2021-07-10 18:56:44','2021-07-10 21:04:20');
/*!40000 ALTER TABLE `Login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 11:25:55
