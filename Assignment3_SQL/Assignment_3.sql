
-- ------------------------------
-- BioVenture_Intelligence ------
-- Caroline Hull ----------------
-- April 15th 2026 --------------
-- ------------------------------

-- This database simulates a venture capital firm tracking biotech startups across multiple therapeutic areas and funding rounds

-- --
-- DATABASE SETUP
-- --

-- Create Database and use it ;

DROP DATABASE IF EXISTS BioVenture_Intelligence ;
CREATE DATABASE BioVenture_Intelligence ;
USE BioVenture_Intelligence ;

-- --
-- TABLE CREATION
-- --

-- Create a table called Therapeutic_Areas storing information about targeted diseases/disorders


CREATE TABLE Therapeutic_Areas (
			area_id INT PRIMARY KEY,
			area_name VARCHAR(255) NOT NULL UNIQUE
);

-- Create a table called Startups storing core information about startups such as technology and latest investment stage

CREATE TABLE Startups (
			startup_id INT PRIMARY KEY,
			name VARCHAR(255) NOT NULL,
			latest_investment_stage VARCHAR(20) NOT NULL,
			technology VARCHAR(50) NOT NULL,
			CHECK (latest_investment_stage IN ('Seed', 'Series A', 'Series B', 'Series C'))
);

-- Create a table called Investments storing information about each funding round a startup has achieved

CREATE TABLE Investments (
			investment_id INT PRIMARY KEY,
			startup_id INT NOT NULL,
			investment_amount_millions INT NOT NULL,
			investment_date DATE NOT NULL,
			FOREIGN KEY (startup_id) REFERENCES Startups (startup_id)
);

-- Junction table linking startups to therapeutic areas representing a many-to-many relationship

CREATE TABLE Startup_Areas (
			area_id INT NOT NULL,
			startup_id INT NOT NULL,
			PRIMARY KEY (startup_id, area_id),
			FOREIGN KEY (startup_id) REFERENCES Startups (startup_id),
			FOREIGN KEY (area_id) REFERENCES Therapeutic_Areas (area_id)
			
);

DESCRIBE Therapeutic_Areas 
DESCRIBE Startups
DESCRIBE Investments
DESCRIBE Startup_Areas

