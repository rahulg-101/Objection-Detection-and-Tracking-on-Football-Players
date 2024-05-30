

ARTIFACTS_DIR = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION Var Name,
this is useful when you want to change your directories or URL from which you are receiving the files.

"""

DATA_INGESTION_DIR_NAME = "data_ingestion"      # Store downloaded data in this directory

DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"      #Unzip the data here

DATA_DOWNLOAD_URL = 'https://drive.google.com/file/d/1i8QEQEjZwy_9jZJyVn6K1_B1y98-1UeH/view?usp=sharing'



"""
Data Validation related constant start with DATA_VALIDATION Var Name
"""

DATA_VALIDATION_DIR_NAME = "data_validation"    # Create data_validation folder

DATA_VALIDATION_STATUS_FILE = "status.txt"      # Return status as False or True

DATA_VALIDATION_ALL_REQUIRED_FILES = ["test",
                                    "train",
                                    "valid",
                                    "data.yaml",
                                    "README.dataset.txt",
                                    "README.roboflow.txt"]     # Look for files that are in this list


"""
Model trainer related consstant start with MODEL_TRAINER VAR Name
"""

MODEL_TRAINER_DIR_NAME = "model_trainer"    # Create model_trainer folder

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME = "yolov8n.pt"

MODEL_TRAINER_NO_EPOCHS = 1

MODEL_TRAINER_BATCH_SIZE = 16

MODEL_TRAINER_IMAGE_SIZE = 640