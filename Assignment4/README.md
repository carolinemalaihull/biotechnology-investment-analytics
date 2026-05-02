BioVenture Deal Intelligence Platform


1. Open MySQL (via DBeaver or terminal)

2. Run the provided SQL script:
   setup_database.sql

   This will:
   - Create the database: BioVenture_Intelligence
   - Create all required tables
   - Populate them with sample data

3. Ensure your .env file contains:

   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_NAME=BioVenture_Intelligence


Dependencies:

config.py

import pymysql
import os
from dotenv import load_dotenv