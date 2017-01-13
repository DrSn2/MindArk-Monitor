CREATE TABLE `mamonitor`.`jobentries` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `found` DATETIME NOT NULL,
  `name` NVARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `nameindex` (`name` ASC));