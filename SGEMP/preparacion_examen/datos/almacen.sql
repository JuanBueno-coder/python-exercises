-- Simulacro S8, ejercicio 3
CREATE DATABASE IF NOT EXISTS `almacen` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `almacen`;
DROP TABLE IF EXISTS `producto`;
CREATE TABLE `producto` (
  `codigo` varchar(10) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `stock` int NOT NULL,
  `precio` decimal(6,2) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT INTO `producto` VALUES
('A01', 'Aceite de oliva 1L', 20, 8.95),
('A02', 'Aceitunas aliñadas', 5, 3.20),
('B01', 'Picos de Estepa', 12, 1.50),
('B02', 'Torta de Inés Rosales', 3, 2.10),
('C01', 'Mantecados', 0, 4.75);
