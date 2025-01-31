from src.MLProject.logger import logging
from src.MLProject.exceptions import CustomException
import sys


if __name__=="__main__":
    logging.info("THE EXECUTION HAS STARTED")

try:
    a=1/0
except Exception as e:
    logging.error(f"An error occurred: {e}")
    raise CustomException(e, sys)