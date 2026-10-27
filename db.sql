-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema VoluntaMe
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema VoluntaMe
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `VoluntaMe` DEFAULT CHARACTER SET utf8 ;
USE `VoluntaMe` ;

-- -----------------------------------------------------
-- Table `VoluntaMe`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VoluntaMe`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `updated_at` DATETIME NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VoluntaMe`.`misiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VoluntaMe`.`misiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `voluntario_necesario` INT NULL,
  `descripcion` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_misiones_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_misiones_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `VoluntaMe`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VoluntaMe`.`usuarios_has_misiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VoluntaMe`.`usuarios_has_misiones` (
  `usuario_id` INT NOT NULL,
  `mision_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `mision_id`),
  INDEX `fk_usuarios_has_misiones_misiones1_idx` (`mision_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_misiones_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_misiones_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `VoluntaMe`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_misiones_misiones1`
    FOREIGN KEY (`mision_id`)
    REFERENCES `VoluntaMe`.`misiones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
