import os
import sys
import zipfile
import ntpath
import gdown
from YOLO_Object_Detection_and_Tracking.logger import logging
from YOLO_Object_Detection_and_Tracking.exception import CustomException
from YOLO_Object_Detection_and_Tracking.entity.artifacts_entity import DataIngestionArtifact
from YOLO_Object_Detection_and_Tracking.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self,data_ingestion_config= DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)

    def download_data(self):
        """
        Fetch data from URL

        """
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir =  self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir,exist_ok = True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_file_path)
            logging.info(f"Downloaded data from {dataset_url} into {zip_file_path}")
            
            return zip_file_path

        except Exception as e:
            raise CustomException(e,sys)

    def extract_zip_file(self,zip_file_path):
        """
        zip_file_path : str
        Extracts the zip file into data directory
        Function returns none
        """
        try:
            feature_store_path = os.path.join(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_path, exist_ok=True)
            
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                for zipinfo in zip_ref.infolist():
                    targetpath = os.path.normpath(os.path.join(feature_store_path))
                    zip_ref.extract(zipinfo,targetpath)
            logging.info(f"Extracted zip file {zip_file_path} into {feature_store_path}")

            return feature_store_path

        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        """
        This function will return zip_file_path and feature_store_path
        for our artifacts_entity.py file's DataIngestionArtifact class
        """
        logging.info(f"Entered initiate_data_ingestion method of DataIngestion class")

        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path = zip_file_path,
                feature_store_path =  feature_store_path
            )

            logging.info("Exited initiate_data_ingestion method of DataIngestion classs"
            )
            logging.info(f"Data ingestion artifact : {data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e,sys)
        




            