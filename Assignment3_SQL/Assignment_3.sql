
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
			stage VARCHAR(20) NOT NULL,
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

-- DESCRIBE Therapeutic_Areas 
-- DESCRIBE Startups
-- DESCRIBE Investments
-- DESCRIBE Startup_Areas


INSERT INTO Therapeutic_Areas (area_id, area_name)
VALUES
(1, 'Oncology'),
(2, 'Cardiovascular Diseases'),
(3,	'Infectious Diseases'),
(4,	'Neurology'),
(5,	'Nephrology'),
(6,	'Endocrinology and Metabolic Disorders'),
(7,	'Immunology and Autoimmune Diseases'),
(8,	'Pulmonology'),
(9,	'Inflammatory Diseases'),
(10, 'Psychiatry') ;

INSERT INTO Startups (startup_id, name, latest_investment_stage, technology)
VALUES
(1,	'HexemBio',	'Seed', 'Cell therapies'),
(2,	'Stipple Bio','Series A',	'Antibody-drug conjugates'),
(3,	'Ambrosia Biosciences', 'Series B', 'Small molecules'),
(4,	'Terrestrial Bio', 'Series C', 'Vaccines'),
(5,	'Immutrin', 'Series A', 'Monoclonal antibody'),
(6,	'Gilgamesh Pharma', 'Series A', 'Small molecules'),
(7,	'Oryon Cell Therapies', 'Series A', 'Cell therapies'),
(8,	'R1 Therapeutics', 'Series A', 'Small molecules'),
(9,	'Crossbow Therapeutics', 'Series B', 'Bispecific antibody'),
(10, 'Excalipoint Therapeutics', 'Seed', 'T-cell engager'),
(11, 'Korro Bio', 'Series C', 'GLP-1 receptor agonist'),
(12, 'Prolium Biosciences', 'Series A', 'T-cell engager'),
(13, 'Altesa BioSciences', 'Series B', 'Small molecules'),
(14, 'QuantX Biosciences', 'Series B', 'Small molecules'),
(15, 'Exciva', 'Series B', 'Small molecules') ;

INSERT INTO Investments (startup_id, investment_id, stage, investment_amount_millions, investment_date)
VALUES
(1, 1, 'Seed round', 10.4, '2026-04-07'),
(2, 2, 'Seed round', 12.0, '2021-04-07'),
(2, 3, 'Series A', 100.0, '2026-04-06'),
(3, 4, 'Series A', 25.0, '2024-12-10'),
(3, 5, 'Series B', 100.0, '2026-03-31'),
(4, 6, 'Seed round', 3.0, '2022-01-01'),
(4, 7, 'Series A', 12.0, '2023-06-01'),
(4, 8, 'Series C', 50.0, '2026-03-26'),
(5, 9, 'Seed round', 3.0, '2022-02-01'),
(5, 10, 'Series A', 87.0, '2026-03-24'),
(6, 11, 'Seed round', 5.0, '2021-04-04'),
(6, 12, 'Series A', 60.0, '2026-03-24'),
(7, 13, 'Seed round', 2.0, '2021-05-30'),
(7, 14, 'Series A', 21.0, '2026-03-23'),
(8, 15, 'Seed round', 8.0, '2021-08-30'),
(8, 16, 'Series A', 77.5, '2026-03-17'),
(9, 17, 'Seed round', 10.0, '2019-02-01'),
(9, 18, 'Series A', 80.0, '2023-07-01'),
(9, 19, 'Series B', 77.0, '2026-03-18'),
(10, 20, 'Seed round', 68.7, '2026-03-18'),
(11, 21, 'Seed round', 8.5, '2019-02-01'),
(11, 22, 'Series A', 91.5, '2020-09-10'),
(11, 23, 'Series B', 116.0, '2022-01-05'),
(11, 24, 'Series C', 72.0, '2026-03-02'),
(12, 25, 'Seed round', 8.0, '2026-06-01'),
(12, 26, 'Series A', 50.0, '2026-03-03'),
(13, 27, 'Seed round', 8.5, '2019-02-12'),
(13, 28, 'Series A', 38.0, '2020-06-04'),
(13, 29, 'Series B', 75.0, '2026-02-19'),
(14, 30, 'Series A', 40.0, '2023-01-01'),
(14, 31, 'Series B', 85.0, '2026-02-09'),
(15, 32, 'Series A', 10.0, '2021-10-10'),
(15, 33, 'Series B', 59.0, '2026-01-20') ;

INSERT INTO Startup_Areas (startup_id, area_id)
VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 2),
(6, 4),
(7, 4),
(8, 5),
(9, 1),
(10, 1),
(11, 6),
(12, 7),
(13, 8),
(14, 9),
(14, 7),
(15, 4),
(15, 10)