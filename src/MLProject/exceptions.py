import sys
from src.MLProject.logger import logging

def error_message_detail(error, error_detail):
    """
    Returns a formatted error message including file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"ERROR OCCURRED IN PYTHON SCRIPT: [{file_name}] LINE: [{line_number}] MESSAGE: [{str(error)}]"
    else:
        error_message = str(error)
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        """
        Custom Exception class to provide detailed error messages.
        """
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)
    
    def __str__(self):
        return self.error_message
