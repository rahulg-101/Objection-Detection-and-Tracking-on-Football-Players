# Objection-Detection-and-Tracking-on-Football-Players
We are using Yolov8 to detect &amp; track objects which are players,refree,goalkeeper and football itself in this project

### Step 0 - Booting Up
- Create Github Repo > Clone repository > change directory to the directory cloned from previous step using `cd` command > Open VSCODE or your favorite editor 

### Step 1 - Creating Template
- Run the template.py, this template can be reused with any kind of project you are working with, you might need to add one `data_transformation` file in components, in case your data requires some preprocessing before being passed into the model.
- the `/_/_init/_/_.py` method in every subdirectory is added because it will let us treat that directory as a package(library) in itself, being a constructor letting the python know that this directory is acting as a package. 

### Step 2 - Setup.py
- Create the setup.py file, which is basically used to find all the packages, that you have created using template.py

### Step 3 - Run requirements.txt
- Install packages from requirements.txt using pip

### Step 4 - Start experimentation in the notebook
- You can either choose to run the notebook file in "Trial Notebook" directory inside the VS-Code only or can use any other notebook editor which you like, since this project involves a lot of image processing, it is advised to use a notebook editor which enables the use of GPU, preferably **Collab or Kaggle Notebooks**
- At this step, you have the data, you can try different experiments by first preprocessing, then transformation,splitting the data then modelling but this YOLO architecture model has extremely simplified those steps by removing the first 3 steps on its own.
- Once you achieve the best results, save the notebook and its results inside the "Trial Notebook" directory which will act as a reference when you start modular coding

### Step 5 - Setup Logging,Exception and Utils
1. Logging - It is a way to identify till which part our project, worked smoothly and from where the issue started to arise
2. Exception - It is an efficient way to raise errors and write our modular code using the exception handling way of writing code
3. Utils - This can be setup later on as well, as per the necessity arises as you go through with the project.It ideally contains essential and reusable functions for which you may otherwise need to write redundant codes