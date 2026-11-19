-- Simulacro S5: restaurar en phpMyAdmin (pestaña Importar) o en la consola de MySQL
CREATE DATABASE IF NOT EXISTS `pena` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `pena`;
DROP TABLE IF EXISTS `socio`;
CREATE TABLE `socio` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `cuota` decimal(6,2) NOT NULL,
  `fecha_alta` date NOT NULL,
  `activo` char(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT INTO `socio` VALUES (4, 'Paco Merte', 60.00, '2022-06-30', 'S');
