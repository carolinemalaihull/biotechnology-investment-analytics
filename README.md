# Biotech Investment Analytics

## Overview

This repository brings together three connected computational workflows developed during my data science training, using a fictional biotechnology venture capital scenario to explore practical applications of Python, SQL, APIs and data analysis.

The workflows progress from retrieving and processing real-world drug safety data, through relational database design, to development of a REST API for accessing and analysing biotechnology investment data.

My professional background is in translational drug discovery and immunology, and this repository forms part of my independent computational portfolio exploring how data science can be applied to biotechnology-focused questions.

> **Note:** This is independent portfolio work and is entirely separate from my professional employment. It uses public and/or simulated data only and contains no proprietary data or materials.

---

## Workflows

### 1. BioSafety Check

**Python | REST API | Data Processing**

BioSafety Check is a Python workflow for retrieving and summarising real-world safety data from the FDA Adverse Event Reporting System (FAERS).

The workflow accepts a drug or biologic as user input, queries the openFDA API and processes returned adverse-event reports to generate a concise safety summary.

**Key functionality:**

- Retrieves up to 500 adverse-event reports for a specified search term
- Processes JSON data returned by the openFDA API
- Counts and ranks commonly reported adverse reactions
- Identifies reports containing serious outcomes
- Generates a readable text-based safety summary
- Can be reused with different drug or biologic search terms

**Example output:**

```text
CAR T Cell Safety Summary:
----------------------------------------
Total reports analyzed: 500

Top reported reactions:
 - Fatigue (49)
 - White blood cell count increased (43)
 - White blood cell count decreased (43)
 - Anaemia (39)
 - Platelet count decreased (39)

Serious reactions found: 26
Details: Death
----------------------------------------
```

The workflow demonstrates how publicly available pharmacovigilance data can be retrieved programmatically and converted into a structured summary for initial landscape assessment.

**Data interpretation:** FAERS is a spontaneous reporting system and has important limitations, including reporting bias, incomplete information and duplicate reports. Report frequencies should not be interpreted as incidence rates or evidence that a drug caused a reported event. The workflow is therefore intended for exploratory signal review rather than comparative safety assessment.

**Data source:** openFDA / FDA Adverse Event Reporting System (FAERS)

[View BioSafety Check](BioSafety-Check/)

---

### 2. BioVenture Intelligence Database

**SQL | MySQL | Relational Database Design | Portfolio Analytics**

The BioVenture Intelligence Database simulates a venture capital portfolio tracking biotechnology companies across therapeutic areas and funding rounds.

The database was designed to explore how relational data structures and SQL can be used to answer investment-focused questions about funding activity, portfolio composition and sector allocation.

The relational structure contains four connected tables:

- **Startups** – company name, technology focus and latest investment stage
- **Investments** – investment stage, capital raised and investment date
- **Therapeutic_Areas** – disease and sector categories
- **Startup_Areas** – junction table linking companies with multiple therapeutic areas

**Key functionality:**

- Tracks funding rounds across biotechnology companies
- Calculates total capital raised by individual companies
- Analyses investment allocation across therapeutic areas
- Identifies the largest funding rounds
- Examines investment activity over time
- Evaluates portfolio diversification
- Uses stored procedures to support reusable analysis

The workflow demonstrates relational database design, primary and foreign keys, many-to-many relationships, SQL joins, aggregation and analytical querying.

The dataset combines publicly available recent funding information with simulated historical investment data created for the purposes of the analysis.

[View BioVenture Intelligence Database](BioVenture-Intelligence-Database/)

---

### 3. BioVenture Intelligence API

**Python | Flask | REST API | MySQL | Data Visualisation**

The BioVenture Intelligence API extends the relational database into a Flask-based REST API for accessing and analysing biotechnology investment data programmatically.

The API connects Python with the MySQL database and provides endpoints for retrieving company information, analysing investment activity, examining sector allocation and generating a simplified venture capital scoring metric.

**Key functionality:**

- Retrieves all startups or individual company records
- Ranks companies according to total investment
- Calculates investment allocation across therapeutic areas
- Generates simplified VC scores using funding and portfolio characteristics
- Adds new startup records using POST requests
- Deletes records using DELETE requests
- Uses environment variables to separate database credentials from source code
- Includes a Python client for interacting with the API
- Generates a visualisation of company VC scores

### Example API endpoints

```text
GET    /startups
GET    /startups/<startup_id>
GET    /startups/top-startups
GET    /startups/scores
GET    /sectors/allocation
POST   /startups
DELETE /startups/<id>
```

The simplified VC score incorporates:

- Total funding raised
- Number of funding rounds
- Investment stage
- Number of therapeutic areas

This is an illustrative scoring framework developed to demonstrate how multiple database features can be combined into an analytical output; it is not intended as a validated investment model.

[View BioVenture Intelligence API](BioVenture-Intelligence-API/)

---

## Workflow Progression

The three workflows demonstrate a progression from individual data-processing tasks towards an integrated data system:

```text
Public Data Source
       ↓
External API
       ↓
Python Data Processing
       ↓
Relational SQL Database
       ↓
Flask REST API
       ↓
Analytics & Visualisation
```

Together, they demonstrate how Python, SQL, databases and APIs can be combined to retrieve, structure, analyse and communicate biotechnology-focused data.

---

## Technical Skills Demonstrated

### Python
- Data processing and transformation
- API requests and JSON handling
- Modular code structure
- File input/output
- Database interaction
- Data visualisation

### SQL & Databases
- Relational database design
- Primary and foreign keys
- Many-to-many relationships
- Joins and aggregations
- Analytical queries
- Stored procedures
- MySQL

### APIs
- External REST API integration
- Flask API development
- GET, POST and DELETE requests
- JSON responses
- Database-backed endpoints

### Development Practices
- Git and GitHub version control
- Branch-based development
- Dependency management
- Environment variables
- `.gitignore` configuration
- Technical documentation

---

## Repository Structure

```text
biotech-investment-analytics/
│
├── BioSafety-Check/
│   └── Python workflow for exploring FDA adverse-event data
│
├── BioVenture-Intelligence-Database/
│   └── MySQL database and biotechnology investment analytics
│
├── BioVenture-Intelligence-API/
│   └── Flask REST API and Python analytics client
│
├── requirements.txt
└── README.md
```

---

## Development

These workflows were originally developed through a series of assignments during my data science training and were subsequently organised into a single biotechnology-focused repository.

The repository reflects the progression of my computational training from Python through relational databases and API development. My wider computational work includes transcriptomic analysis, statistical modelling and machine-learning approaches to biological and pharmacological datasets.

---

## Author

**Caroline Hull, PhD**

Translational Drug Discovery | Immunology | Computational Biology | AI for Drug Discovery