import os.path
import sys
import yaml
import base64

from YOLO_Object_Detection_and_Tracking.logger import logging
from YOLO_Object_Detection_and_Tracking.exception import CustomException

def read_yaml(file_path:str) -> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise CustomException(e,sys)
    
