## BioVenture Intelligence API

The BioVenture Intelligence API is a Flask-based API that simulates a venture capital analytics system for tracking biotech startups. It provides access to startup data, investment history, sector allocation and performance scoring to help analyse portfolio performance across different therapeutic areas.

### Key features

- Retrieve all startups and individual startup details
- Analyse total investment per startup
- Rank startups based on funding and activity
- Evaluate investment distribution across therapeutic areas
- Add new startups via POST requests
- Delete startups via DELETE requests
- Visualise VC scores using a Python client

### Project Structure

- `app.py` – Flask API routes  
- `db_utils.py` – Database query functions  
- `config.py` – Database connection setup  
- `main.py` – Console client and visualisation  
- `.env` – Environment variables (not committed)  

### Database Design

The system is backed by a MySQL database called BioVenture_Intelligence containing startups, investments and therapeutic area relationships:
Database file -  Bioventure_Intelligence_DB.sql

The system uses a relational MySQL database with the following structure:

- **Startups** – core company information (name, technology, stage)
- **Investments** – funding rounds and amounts
- **Therapeutic_Areas** – disease/sector categories
- **Startup_Areas** – many-to-many relationship between startups and sectors

Primary keys and foreign keys are used to maintain referential integrity, and `AUTO_INCREMENT` is implemented to support dynamic data insertion via API requests.

### API Endpoints

#### Core Endpoints
- `GET /` – API status message  
- `GET /startups` – List all startups  
- `GET /startups/<startup_id>` – Get a specific startup  

#### Analytics Endpoints
- `GET /startups/top-startups` – Rank startups by total investment  
- `GET /startups/scores` – VC scoring system  
- `GET /sectors/allocation` – Investment by therapeutic area  

#### Data Modification
- `POST /startups` – Add a new startup  
- `DELETE /startups/<id>` – Delete a startup  

### VC Scoring System

Each startup is assigned a **VC Score** based on:

- Total funding raised  
- Number of funding rounds  
- Investment stage (weighted from Seed to Series C)  
- Number of therapeutic areas  

This provides a simplified model for ranking startups based on investment attractiveness.

VC scores are calculated dynamically within the API using aggregated database values.

Please note - New startups added via POST are inserted only into the Startups table.
Sector allocation and VC scoring depend on related records in the Startup_Areas and Investments tables which is not covered here. Therefore, newly created startups will not appear in analytics endpoints until additional relational data is added.

### How to run:

1. Open MySQL (via DBeaver or terminal)

2. Run the provided SQL script:
   Bioventure_Intelligence_DB.sql

   This will:
   - Create the database: BioVenture_Intelligence
   - Create all required tables
   - Populate them with sample data

3. Next create a `.env` file in the root directory to store your database credentials securely. Make sure this file is included in `.gitignore` so it is not uploaded to GitHub. Ensure your .env file contains:

   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_NAME=BioVenture_Intelligence

4. Activate your virtual environment and install the required Python dependencies using pip. You will need Flask, PyMySQL, Requests, Matplotlib and python-dotenv.

5. To start the API, run `flask run` in your terminal. The server will start locally at `http://127.0.0.1:5000`.

6. Once running, you can test the API using a browser for GET requests, Postman for POST and DELETE requests, or the provided `main.py` file, which acts as a simple frontend client. This script demonstrates example API endpoints and also generates a VC score visualisation using Matplotlib.


### Dependencies

The project requires the following Python packages:

- Flask  
- PyMySQL  
- Requests  
- Matplotlib  
- python-dotenv  

Install them using:

pip install flask pymysql requests matplotlib python-dotenv