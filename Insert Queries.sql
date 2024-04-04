/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

SET SQL_SAFE_UPDATES = 0;

-- --------------------------------------------
DROP TABLE IF EXISTS `hospital`.`patient`;
CREATE TABLE `hospital`.`patient` (
  `patient_name` varchar(45) NOT NULL,
  `patient_dob` date NOT NULL,
  `patient_address` varchar(150) NOT NULL,
  `patient_phone` varchar(10) NOT NULL,
  `patient_email` varchar(50) DEFAULT 'N/A',
  PRIMARY KEY (`patient_phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



INSERT INTO `hospital`.`patient` (`patient_name`,`patient_dob`,`patient_address`,`patient_phone`,`patient_email`) VALUES ('Aakash Prajapati','2001-04-20','12 Deep Bungalows, A\'bad, 380015','8401364728','aakash.20042001@gmail.com');
INSERT INTO `hospital`.`patient` (`patient_name`,`patient_dob`,`patient_address`,`patient_phone`,`patient_email`) VALUES ('Test 1','2005-05-12','A\'bad, 369874','8401631899','test1@gmail.comm');
INSERT INTO `hospital`.`patient` (`patient_name`,`patient_dob`,`patient_address`,`patient_phone`,`patient_email`) VALUES ('Aakash P.','2004-01-20','12 Deep, A\'bad','9824302215','a@gmail.com');
SELECT * FROM hospital.patient;

-- --------------------------------------------

DROP TABLE IF EXISTS `hospital`.`doctor`;
CREATE TABLE `hospital`.`doctor` (
  `doc_name` varchar(45) NOT NULL,
  `doc_edu` varchar(45) NOT NULL,
  `doc_days` varchar(85) NOT NULL,
  `doc_phone` varchar(10) NOT NULL,
  PRIMARY KEY (`doc_phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO `hospital`.`doctor` (`doc_name`,`doc_edu`,`doc_days`,`doc_phone`) VALUES ('Dr. Batra','M.B.B.S.','Tue, Thu','7016235353');
INSERT INTO `hospital`.`doctor` (`doc_name`,`doc_edu`,`doc_days`,`doc_phone`) VALUES ('Dr. Reddy','M.D.','Mon, Fri','9427953145');
SELECT * FROM hospital.doctor;

-- -------------------------------------------- 

DROP TABLE IF EXISTS `hospital`.`appointment`;
CREATE TABLE `hospital`.`appointment` (
  `patient_name` varchar(45) NOT NULL,
  `patient_phone` varchar(10) NOT NULL,
  `doctor_name` varchar(45) NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `hospital`.`appointment` (`patient_name`,`patient_phone`,`doctor_name`,`appointment_date`,`appointment_time`) VALUES ('Aakash Prajapati','8401364728','Dr. Reddy','2024-04-05','12:15:00');
SELECT * FROM hospital.appointment;