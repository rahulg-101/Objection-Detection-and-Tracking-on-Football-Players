# Objection-Detection-and-Tracking-on-Football-Players
We are using Yolov8 to detect &amp; track objects which are players,refree,goalkeeper and football itself in this project

### Step 0 - Booting Up
- Create Github Repo > Clone repository > change directory to the directory cloned from previous step using `cd` command > Open VSCODE or your favorite editor 

### Step 1 - Creating Template
- Run the template.py, this template can be reused with any kind of project you are working with, you might need to add one `data_transformation` file in components, in case your data requires some preprocessing before being passed into the model.
- the `/_/_init/_/_.py` method in every subdirectory is added because it will let us treat that directory as a package(library) in itself, being a constructor letting the python know that this directory is acting as a package. 

### Step 2 - Setup.py
- Create the setup.py file, which is basically used to find all the packages, that you have created using template.py
- **Now before moving forward, make sure you create & start your conda environment at this stage before going on the next step**

### Step 3 - Run requirements.txt
- Install packages from requirements.txt using pip

### Step 4 - Start experimentation in the notebook
- You can either choose to run the notebook file in "Trial Notebook" directory inside the VS-Code only or can use any other notebook editor which you like, since this project involves a lot of image processing, it is advised to use a notebook editor which enables the use of GPU, preferably **Collab or Kaggle Notebooks**
- Creating a new notebook called `notebook.ipynb` to download files from your google drive into your system as zip file
- At this step, you have the data,now create a new notebook (we have `yolov8-implementation.ipynb` for this purpose), you can try different experiments by first preprocessing, then transformation,splitting the data then modelling but this YOLO architecture model has extremely simplified those steps by removing the first 3 steps on its own.
- Once you achieve the best results, save the notebook and its results inside the "Trial Notebook" directory which will act as a reference when you start modular coding

### Step 5 - Setup Logging,Exception and Utils
1. Logging - It is a way to identify till which part our project, worked smoothly and from where the issue started to arise
2. Exception - It is an efficient way to raise errors and write our modular code using the exception handling way of writing code
3. Utils - This can be setup later on as well, as per the necessity arises as you go through with the project.It ideally contains essential and reusable functions for which you may otherwise need to write redundant codes

### Step 6 - Defining Workflow for Data Ingestion
- We will follow the following workflow after we have setup the initial requirements and configuration till step 5:
    1. constants
    2. entity
    3. components
    4. pipeline
    5. app.py

### Step 7 - constants
- In `constants/training_pipeline` we have this \_\_init\_\_ method, we will be defining the what are our major directories such as:       
    - `artifacts` which is the main directory to store the data files
    - `data ingestion directory (DATA_INGESTION_DIR_NAME)` which will later on have the structure "artifact/data_ingestion_directory" is the name of the directory which will contain the downloaded zip file from drive
    - `data ingestion feature store (DATA_INGESTION_FEATURE_STORE_DIR)` which  will later on have the structure "artifact/data_integration_feature_store" is the name of the directory which will contain the unzip file from data_ingest_directory
    - `data url (DATA_DOWNLOAD_URL)` that has the link of the URL from where our file will be downloaded

### Step 8 - entity 
- It has two files `config_entity.py` and `artifacts_entity.py`:
    - `config_entity.py` is used to config the paths of directories defined in constants
    - `artifacts_entity.py` contains the class DataIngestionArtifact which only have the variables name that will store paths to directories containing the downloaded zip file and unzip feature store

### Step 9 - Components
- #### In `data_ingestion.py`
    1. Here we will first create a class called DataIngestion and store the config files from config_entity.py,
    2. Then we will create a function that will create the directory where we store the data files and download them from google drive into this and return the directory
    3. Since the downloaded files are in zip format, we will create second function to create another directory called feature_store where we will unzip and store the data files and return the feature_store directory
    4. As a final step, we will create a function that will run both these function and store the path to both the directory in the dataclass object created in `artifacts_entity`.

### Step 10 - Pipeline
- #### In training_pipeline.py : 
    1. We have created a function that will take the config file and execute the function from data_ingestion.py that will return the path to downloaded data and unzipped data directory.
    
### Step 11 - app.py
- Here we can create an object of TrainingPipeline class and use the run method to execute our data ingestion

### Step 12 - Workflow for Data Validation
- We will follow the following workflow steps for Data Validation after we are done with the data ingestion process:
    1. constants
    2. entity
    3. components
    4. pipeline
    5. app.py

### Step 13 - Constants
- Similar to what we had done for data ingestion, define data_validation_folder name, data_validation_status file name and a list of files that should be present after data ingestion process

### Step 14 - Entity
- in `config_entity.py` we create a class called DataValidationConfig : 
    - `data_validation_dir` (str): The directory path for data validation.
    - `valid_status_file_dir` (str): The directory path for storing validation status files.
    - `required_file_list` (list): A list of required files for data validation.

- in `artifacts_entity.py` we create a class called DataValidationArtifacts which stores the status of data validation process (True or False)

### Step 15 - Components 
- We create a class called DataValidation which takes data_ingestion_artifacts and data_validation_config info to get construted
- We define a logic function where we validate the files we have received in the feature store of data ingestion artifacts
- We create another function where we run the above validation function and return the data validation result in DataValidationArtifacts object type

### Step 16 - Pipeline 
- Here we update the config with data_validation_config 
- Create a function that will run the last function from previous step and stores the result in the DataValidationArtifacts 
- We just add the above function in the run_pipeline function for execution in our app.

> No changes in the app.py 



