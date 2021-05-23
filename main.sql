-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cliente` (
  `idcliente` INT NOT NULL,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`marca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`marca` (
  `idmarca` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idmarca`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tipo` (
  `idtipo` INT NOT NULL,
  PRIMARY KEY (`idtipo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`clase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`clase` (
  `idclase` INT NOT NULL,
  PRIMARY KEY (`idclase`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`articulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`articulo` (
  `idarticulo` INT NOT NULL,
  `TIPO_idTIPO` INT NOT NULL,
  `clase_idclase` INT NOT NULL,
  PRIMARY KEY (`idarticulo`),
  INDEX `fk_articulo_TIPO1_idx` (`TIPO_idTIPO` ASC) VISIBLE,
  INDEX `fk_articulo_clase1_idx` (`clase_idclase` ASC) VISIBLE,
  CONSTRAINT `fk_articulo_TIPO1`
    FOREIGN KEY (`TIPO_idTIPO`)
    REFERENCES `mydb`.`tipo` (`idtipo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_articulo_clase1`
    FOREIGN KEY (`clase_idclase`)
    REFERENCES `mydb`.`clase` (`idclase`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cotizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cotizacion` (
  `idcotizacion` INT NOT NULL,
  `cliente_idcliente` INT NOT NULL,
  PRIMARY KEY (`idcotizacion`),
  INDEX `fk_cotizacion_cliente_idx` (`cliente_idcliente` ASC) VISIBLE,
  CONSTRAINT `fk_cotizacion_cliente`
    FOREIGN KEY (`cliente_idcliente`)
    REFERENCES `mydb`.`cliente` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`listaArticulos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`listaArticulos` (
  `idlistaArticulos` INT NOT NULL,
  `cotizacion_idcotizacion` INT NOT NULL,
  `articulo_idarticulo` INT NOT NULL,
  PRIMARY KEY (`idlistaArticulos`),
  INDEX `fk_listaArticulos_cotizacion1_idx` (`cotizacion_idcotizacion` ASC) VISIBLE,
  INDEX `fk_listaArticulos_articulo1_idx` (`articulo_idarticulo` ASC) VISIBLE,
  CONSTRAINT `fk_listaArticulos_cotizacion1`
    FOREIGN KEY (`cotizacion_idcotizacion`)
    REFERENCES `mydb`.`cotizacion` (`idcotizacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_listaArticulos_articulo1`
    FOREIGN KEY (`articulo_idarticulo`)
    REFERENCES `mydb`.`articulo` (`idarticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`modelo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`modelo` (
  `idmodelo` INT NOT NULL,
  `marca_idmarca` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `clase_idclase` INT NOT NULL,
  PRIMARY KEY (`idmodelo`),
  INDEX `fk_modelo_marca1_idx` (`marca_idmarca` ASC) VISIBLE,
  INDEX `fk_modelo_clase1_idx` (`clase_idclase` ASC) VISIBLE,
  CONSTRAINT `fk_modelo_marca1`
    FOREIGN KEY (`marca_idmarca`)
    REFERENCES `mydb`.`marca` (`idmarca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_modelo_clase1`
    FOREIGN KEY (`clase_idclase`)
    REFERENCES `mydb`.`clase` (`idclase`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
