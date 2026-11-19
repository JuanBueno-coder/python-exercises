-- Simulacro S7, ejercicio 3
CREATE DATABASE IF NOT EXISTS `feria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `feria`;
DROP TABLE IF EXISTS `pedido`;
CREATE TABLE `pedido` (
  `num_pedido` int NOT NULL,
  `mesa` int NOT NULL,
  `producto` varchar(100) NOT NULL,
  `precio` decimal(6,2) NOT NULL,
  `unidades` int NOT NULL,
  `fecha_hora` datetime NOT NULL,
  PRIMARY KEY (`num_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
