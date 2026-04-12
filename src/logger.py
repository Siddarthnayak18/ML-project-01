# purpose of logger is to store all the execution that happens in the file in some way to refer later


import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    # file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)   # create a file
os.makedirs(logs_path,exist_ok=True) # keep on appending the file even though there is a file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # file format
    level=logging.INFO,


)

