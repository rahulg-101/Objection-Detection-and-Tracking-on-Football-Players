import os,sys
import yaml
from YOLO_Object_Detection_and_Tracking.utils.main_utils import read_yaml

from YOLO_Object_Detection_and_Tracking.logger import logging
from YOLO_Object_Detection_and_Tracking.exception import CustomException

from YOLO_Object_Detection_and_Tracking.entity.config_entity import ModelTrainerConfig
from YOLO_Object_Detection_and_Tracking.entity.artifacts_entity import ModelTrainerArtifacts,DataIngestionArtifact

import ultralytics
import supervision as sv
# ultralytics.checks()

from ultralytics import YOLO



class ModelTrainer :
    def __init__(self,model_trainer_config:ModelTrainerConfig):
        
        self.model_trainer_config = model_trainer_config
        


    def initiate_model_trainer(self) -> ModelTrainerArtifacts:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            # logging.info("Unzipping Data")
            # os.system("unzip data.zip")
            # os.system("rm data.zip")
            # print(os.system('pwd'))
            os.chdir(r"C:\Users\rahul gupta\Documents\Learning\Projects\Yolo Object Detection and Tracking\Objection-Detection-and-Tracking-on-Football-Players")
            # os.system(f'yolo train model={self.model_trainer_config.weight_name} data={os.path.normpath(os.path.join("artifacts", "feature_store", "data.yaml"))} epochs={self.model_trainer_config.no_epochs} imgsz={self.model_trainer_config.imgsz} batch={self.model_trainer_config.batch_size}')
            data_yaml_path = os.path.join(os.getcwd(),'artifacts','feature_store', "data.yaml")
            if os.path.exists(data_yaml_path):
                os.system(f'yolo train model={self.model_trainer_config.weight_name} data="{data_yaml_path}" epochs={self.model_trainer_config.no_epochs} imgsz={self.model_trainer_config.imgsz} batch={self.model_trainer_config.batch_size} device="cpu"')
            else:
                print(f"Error: {data_yaml_path} does not exist.")
            
            os.makedirs(self.model_trainer_config.model_trainer_dir,exist_ok=True)
            os.system(f"cp runs/detect/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

            # os.system("rm -rf train")
            # os.system("rm -rf valid")
            # os.system("rm -rf test")
            # os.system("rm -rf data.yaml")
            # os.system("rm -rf README.dataset.txt")
            # os.system("rm -rf README.roboflow.txt")     # These files which are being removed can be changed based on your dataset.

            A = os.path.join(self.model_trainer_config.model_trainer_dir,"best.pt")
            model_trainer_artifact = ModelTrainerArtifacts(trained_model_file_path=A)

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise CustomException(e, sys)
             
                                    
