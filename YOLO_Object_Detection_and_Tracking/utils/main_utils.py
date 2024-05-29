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
    
def write_yaml(file_path:str,content:object,replace:bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,'w') as file:
            yaml.dump(content,file)
            logging.info("Write yaml file successfully")

    except Exception as e:
        raise CustomException(e,sys)

def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')
