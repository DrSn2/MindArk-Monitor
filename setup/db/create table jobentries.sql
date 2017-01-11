CREATE TABLE `mamonitor`.`jobentries` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `encountered` DATETIME NOT NULL,
  `jobName` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));
