import os
import sys
from src.MLProject.exceptions import CustomException
from src.MLProject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

def read_sql_data():
    logging.info('Reading from MySQL database')
    try:
        host = os.getenv('host')
        port = os.getenv('port')  
        user = os.getenv('user')
        password = os.getenv('password')
        db = os.getenv('database')

        if not all([host, port, user, password, db]):
            raise ValueError("One or more environment variables are missing or empty.")
        
        port = int(port)

        logging.info(f"Connecting to MySQL database: host={host}, port={port}, user={user}, database={db}")

        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM datascience_salaries_2024")  # Updated table name
            result = cursor.fetchall()
            df = pd.DataFrame(result)
        
        conn.close()
        logging.info("Data read successfully from MySQL")
        
        if not df.empty:
            print(df.sample(5))

        return df

    except pymysql.err.OperationalError as ex:
        logging.error(f"Operational error while connecting to MySQL: {ex}")
        raise CustomException(f"Operational error while connecting to MySQL: {ex}", sys)
    except pymysql.err.ProgrammingError as ex:
        logging.error(f"SQL syntax or table error: {ex}")
        raise CustomException(f"SQL syntax or table error: {ex}", sys)
    except Exception as ex:
        logging.error(f"Unexpected error reading SQL data: {ex}")
        raise CustomException(f"Unexpected error reading SQL data: {ex}", sys)
