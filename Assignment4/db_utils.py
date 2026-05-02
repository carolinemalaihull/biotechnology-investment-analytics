import pymysql
from config import get_db_connection

def get_portfolio():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT * 
                FROM Startups
                """)
            return cursor.fetchall()


def get_top_startups():
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
        
def get_sector_allocation():
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
        
def get_startup_by_id(startup_id):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                 SELECT *
                FROM Startups
                WHERE startup_id = %s
                """, (startup_id))
            return cursor.fetchall()


def get_score():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                                SELECT s.name,
                    SUM(i.investment_Amount_millions) AS total_funding,
                    COUNT(i.investment_id) AS rounds,
                    COUNT(DISTINCT sa.area_id) AS areas,
                            
                    CASE
                        WHEN s.latest_investment_stage = "Seed" THEN 5
                        WHEN s.latest_investment_stage = "Series A" THEN 10
                        WHEN s.latest_investment_stage = "Series B" THEN 15
                        WHEN s.latest_investment_stage = "Series C" THEN 20
                    END AS stage_score
                            
                FROM Startups s
                JOIN Investments i ON s.startup_id = i.startup_id 
                JOIN Startup_Areas sa ON s.startup_id = sa.startup_id 
                GROUP BY s.startup_id;
                """)
            return cursor.fetchall()



    
if __name__ == "__main__":
    conn = get_db_connection()
    print("Connected successfully!")
    conn.close()