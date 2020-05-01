# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 64.227.54.240 (MySQL 5.5.5-10.3.21-MariaDB-1:10.3.21+maria~bionic-log)
# Database: dbfel2
# Generation Time: 2020-02-07 10:24:23 PM +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table estados
# ------------------------------------------------------------

DROP TABLE IF EXISTS `estados`;

CREATE TABLE `estados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clave` varchar(2) NOT NULL,
  `name` varchar(45) NOT NULL DEFAULT '',
  `abrev` varchar(16) NOT NULL,
  `abrev_pm` varchar(16) NOT NULL DEFAULT 'xD' COMMENT 'Campo para Círculo de Crédito Empresarial.',
  `id_country` tinyint(3) DEFAULT NULL,
  `risk` decimal(5,2) DEFAULT 0.00,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='Tabla de Estados de la República Mexicana';

LOCK TABLES `estados` WRITE;
/*!40000 ALTER TABLE `estados` DISABLE KEYS */;

INSERT INTO `estados` (`id`, `clave`, `name`, `abrev`, `abrev_pm`, `id_country`, `risk`)
VALUES
	(1,'01','AGUASCALIENTES','AGS','AGS',1,1.00),
	(2,'02','BAJA CALIFORNIA','BC','BCN',1,0.50),
	(3,'03','BAJA CALIFORNIA SUR','BCS','BCS',1,0.50),
	(4,'04','CAMPECHE','CAMP','CAM',1,0.20),
	(5,'05','COAHUILA','COAH','COA',1,0.20),
	(6,'06','COLIMA','COL','COL',1,1.00),
	(7,'07','CHIAPAS','CHIS','CHS',1,1.00),
	(8,'08','CHIHUAHUA','CHIH','CHI',1,1.00),
	(9,'09','CIUDAD DE MEXICO','CDMX','CDMX',1,1.00),
	(10,'10','DURANGO','DGO','DGO',1,0.50),
	(11,'11','GUANAJUATO','GTO','GTO',1,1.00),
	(12,'12','GUERRERO','GRO','GRO',1,1.00),
	(13,'13','HIDALGO','HGO','HGO',1,1.00),
	(14,'14','JALISCO','JAL','JAL',1,1.00),
	(15,'15','MEXICO','MEX','EM',1,1.00),
	(16,'16','MICHOACAN DE OCAMPO','MICH','MICH',1,1.00),
	(17,'17','MORELOS','MOR','MOR',1,1.00),
	(18,'18','NAYARIT','NAY','NAY',1,1.00),
	(19,'19','NUEVO LEON','NL','NL',1,0.50),
	(20,'20','OAXACA','OAX','OAX',1,1.00),
	(21,'21','PUEBLA','PUE','PUE',1,1.00),
	(22,'22','QUERETARO','QRO','QRO',1,1.00),
	(23,'23','QUINTANA ROO','QROO','QR',1,1.00),
	(24,'24','SAN LUIS POTOSI','SLP','SLP',1,1.00),
	(25,'25','SINALOA','SIN','SIN',1,0.50),
	(26,'26','SONORA','SON','SON',1,0.50),
	(27,'27','TABASCO','TAB','TAB',1,1.00),
	(28,'28','TAMAULIPAS','TAMP','TAM',1,0.50),
	(29,'29','TLAXCALA','TLAX','TLAX',1,1.00),
	(30,'30','VERACRUZ','VER','VER',1,1.00),
	(31,'31','YUCATAN','YUC','YUC',1,0.20),
	(32,'32','ZACATECAS','ZAC','ZAC',1,0.50);

/*!40000 ALTER TABLE `estados` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
