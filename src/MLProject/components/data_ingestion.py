import os
import sys
from src.MLProject.exceptions import CustomException
from src.MLProject.logger import logging
import pandas as pd
from src.MLProject.utils import read_sql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    tips_data_path: str = os.path.join('artifacts', 'tips.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
        
            df = read_sql_data()
            logging.info('Reading data from SQL completed')

            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

          
            df.to_csv(self.ingestion_config.tips_data_path, index=False, header=True)
            logging.info('Raw data saved to tips.csv')

           
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info('Data split into train and test sets')

      
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Train and test data saved to CSV files')

            logging.info('Data Ingestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error(f'Error during data ingestion: {e}')
            raise CustomException(f"Error during data ingestion: {e}", sys)
