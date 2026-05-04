# db_utils imports database connection from config file
# Stores python functions that contain SQL queries

# pymysql is a python package that lets you talk to SQL databases and run SQL queries and return results to python

import pymysql
from config import get_db_connection

# 1. Define a function to return all startups
def get_startups():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT startup_id, name, technology, latest_investment_stage
                    FROM Startups
                """)
                rows = cursor.fetchall()

        # Format database rows into consistent API response structure, returning id and and name first rather than alphabetical
        return [
            {
                "startup_id": row["startup_id"],
                "name": row["name"],
                "technology": row["technology"],
                "latest_investment_stage": row["latest_investment_stage"]
            }
            for row in rows
        ]
    
    except Exception as e:
        print(f"Error fetching startups: {e}")
        return []

# 2. Define a function that orders startups in descending order based on total investment
def get_top_startups():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT s.name, SUM(i.investment_amount_millions) AS total
                    FROM Startups s
                    JOIN Investments i ON s.startup_id = i.startup_id
                    GROUP BY s.name
                    ORDER BY total DESC
                    """)
                return cursor.fetchall()
            
    except Exception as e:
        print(f"Error fetching top-startups: {e}")
        return []

# 3. Define a function that returns sectors in descending order based on total investment
def get_sector_allocation():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT t.area_name, SUM(i.investment_amount_millions) AS total_investment
                    FROM Therapeutic_Areas t
                    JOIN Startup_Areas sa ON t.area_id = sa.area_id
                    JOIN Investments i ON sa.startup_id = i.startup_id
                    GROUP BY t.area_name
                    ORDER BY total_investment DESC
                    """)
                return cursor.fetchall()
            
    except Exception as e:
        print(f"Error fetching sector allocations: {e}")
        return []

# 4. Define a function that returns all information on a specific startup based on its startup_id
def get_startup_by_id(startup_id):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT *
                    FROM Startups
                    WHERE startup_id = %s
                    """, (startup_id,))
                row = cursor.fetchone()
                return dict(row) if row else None
            
    except Exception as e:
        print(f"Error fetching startup: {e}")
        return None

# 5. Define a function that calculates a "VC score" for each startup based on total investment, number of rounds, diversity of portfolio (number of therapeutic areas) and investment stage
def get_score():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                        SELECT s.name,
                        SUM(i.investment_amount_millions) AS total_funding,
                        COUNT(i.investment_id) AS rounds,
                        COUNT(DISTINCT sa.area_id) AS areas,
                                
                        CASE
                            WHEN s.latest_investment_stage = "Seed" THEN 5
                            WHEN s.latest_investment_stage = "Series A" THEN 10
                            WHEN s.latest_investment_stage = "Series B" THEN 15
                            WHEN s.latest_investment_stage = "Series C" THEN 20
                            ELSE 0
                        END AS stage_score
                                
                    FROM Startups s
                    JOIN Investments i ON s.startup_id = i.startup_id 
                    JOIN Startup_Areas sa ON s.startup_id = sa.startup_id 
                    GROUP BY s.startup_id;
                    """)
                return cursor.fetchall()
            
    except Exception as e:
        print(f"Error generating VC scores: {e}")
        return []

# 6. Define a function that adds a new startup to the database
def post_new_startup(data):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Startups (name, technology, latest_investment_stage)
                    VALUES (%s, %s, %s)
                """, (
                    data["name"],
                    data["technology"],
                    data["latest_investment_stage"]
                ))
                new_id = cursor.lastrowid
            conn.commit()

        return {
            "startup_id": new_id,
            "message": "Startup created successfully"
        }
    
    except Exception as e:
        print(f"Error adding startup: {e}")
        return {
            "message": "Failed to add startup",
            "error": str(e)
        }
    

# 7. Define a function that deletes an entry from the database using its startup_id
def delete_startup(startup_id):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM Startups
                    WHERE startup_id = %s
                """, (startup_id,))
                
                # Check if anything was actually deleted
                if cursor.rowcount == 0:
                    return {"message": "Startup not found"}
            
                conn.commit()
        
        return {"message": f"Startup {startup_id} deleted"}
    
    except Exception as e:
        print(f"Error deleting startup: {e}")
        return {"error": "Failed to delete startup"}

        
if __name__ == "__main__":
    conn = get_db_connection()
    print("Connected successfully!")
    conn.close()