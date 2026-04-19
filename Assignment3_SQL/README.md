# BioVenture Intelligence Database

## Overview

This project simulates a venture capital (VC) firm tracking biotech startups across multiple therapeutic areas and funding rounds.

The database is designed to support portfolio analysis, enabling insights into capital allocation, funding trends and startup activity across different biotech sectors.

While the most recent funding rounds are based on real data, earlier rounds are a combination of real and simulated data to create a realistic investment dataset.

------------------------------------

## Objectives

The goal of this project is to design a relational database that allows a VC firm to:

* Track startup investment activity over time
* Analyse total capital deployed across the portfolio
* Identify high-performing or highly funded companies
* Understand sector-level investment trends
* Assess portfolio diversification across therapeutic areas

------------------------------------

## Database Structure

The database consists of four tables:

### 1. Startups

Stores core information about each company:

* Name
* Latest investment stage
* Technology focus

### 2. Investments

Tracks funding rounds for each startup:

* Investment stage
* Capital raised (in millions ($))
* Investment date

### 3. Therapeutic_Areas

Defines disease areas and sectors:

* Oncology
* Neurology
* Immunology, etc.

### 4. Startup_Areas

A junction table enabling a many-to-many relationship between startups and therapeutic areas.

------------------------------------

## Key Features & Analysis

The database supports a range of analytical queries relevant to venture capital decision-making:

* **Portfolio Performance**
  Calculate total capital raised per startup to identify top-funded companies

* **Sector Allocation**
  Analyse total investment by therapeutic area to understand where capital is concentrated

* **Investment Activity**
  Measure number of funding rounds per startup to identify active or mature companies

* **Diversification Analysis**
  Evaluate how broadly startups operate across multiple therapeutic areas

* **Funding Trends Over Time**
  Aggregate investment data by year to observe changes in capital deployment

* **Largest Funding Rounds**
  Identify major capital events within the portfolio

------------------------------------

## Example Insight

The database can be used to answer questions such as:

* Which biotech sectors are attracting the most investment?
* Which startups have raised the most capital overall?
* What is the average size of a funding round?
* Which companies are most active in raising capital?

------------------------------------

## Technical Skills Demonstrated

* Relational database design
* Primary and foreign key implementation
* Many-to-many relationship modelling
* SQL joins and aggregations
* Use of built-in SQL functions (e.g. `SUM`, `AVG`, `COUNT`, `YEAR`, `UPPER`)
* Stored procedure creation for reusable analysis

------------------------------------

## How to Run

1. Open the SQL script in DBeaver
2. Execute the full script to create and populate the database
3. Run individual queries to explore portfolio insights 
4. Note - to run procedure, the script must be run top-to-bottom

------------------------------------

## Data Source

Recent funding data sourced from:
https://www.labiotech.eu/biotech-funding-2026-tracker

***Most recent round of funding for each company is real while all previous rounds are a mix of real and fabricated

------------------------------------

## Author

Caroline Hull
April 2026
