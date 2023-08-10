# Sales_Forecast
## Problem statement:
Build a predictive model and find out the sales of each product at a particular store.

## Data description:
 - Item_Identifier: Unique product ID
 - Item_Weight: Weight of product
 - Item_Fat_Content: Whether the product is low fat or not
 - Item_Visibility: The % of total display area of all products in a store allocated to the particular product
 - Item_Type: The category to which the product belongs
 - Item_MRP: Maximum Retail Price (list price) of the product
 - Outlet_Identifier: Unique store ID
 - Outlet_Establishment_Year: The year in which store was established
 - Outlet_Size: The size of the store in terms of ground area covered
 - Outlet_Location_Type: The type of city in which the store is located
 - Outlet_Type: Whether the outlet is just a grocery store or some sort of supermarket
 - Item_Outlet_Sales: Sales of the product in the particulat store. This is the outcome variable to be predicted.

 Apart from training files, we also required a "schema" file from the client (schema_training.json), which contains all the relevant information about the training files such as:
Name of the files, Length of Date value in FileName, Length of Time value in FileName, Number of Columns, Name of the Columns, and their datatype.

## STEP 1: Create and activate conda environment:
In the local active directory of the repository:

```bash
  - conda create --prefix ./env python=3.6 -y
  - conda activate env/
```
## STEP 2: Inializations:
### create a setup file
```bash
touch setup.py
```
paste the below content in the setup.py file and make the necessary changes as per your user ID-
```bash
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dvc-ML-demo-AIOps",
    version="0.0.1",
    author="USER_NAME",
    description="A package for Sales prediction using ML and dvc for retraining",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AAZZIOUI/Sales_Forecast",
    author_email="user_name@gmail.com",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn',
        'Flask'
    ]
)
```
### Create requirements file and install dependencies
```bash
touch requirements.txt
pip install -r requirements.txt
```
### Initialize dvc
```bash
dvc init
```

### create the basic directory structure
```bash
mkdir -p src/utils config
```
all_utils.py: will have all the files that are required.

### create config.yaml file
```bash
touch config/config.yaml
```
config.yaml :  will be used and accessed by all files that need data. All data will be configured here so that if we change anything related to data, we will have to change it only in this file.

### create __init__.py files
 src folder is going to be treated as a package.

### create artifacts folder
This is where we will be storing all kinds of data: Raw, Processed, Validated, Archived ...etc.

### create dvc.yaml file
This is where we will be adding dvc stages (DAG)

### create params.yaml file
This file is responsible for all training parameters: seed, test size, hyperparams...etc

## STEP 3: Data validation:
In this step, we perform different sets of validation on the given set of training files:
  - **1: Name Validation** - We validate the name of the files based on the given name in the schema file. We have created a regex pattern as per the name given in the schema file to use for validation. After validating the pattern in the name, we check for the length of date in the file name as well as the length of time in the file name. If all the values are as per requirement, we move such files to "Good_Data_Folder" else we move such files to "Bad_Data_Folder."

  - **2: Number of Columns** - We validate the number of columns present in the files, and if it doesn't match with the value given in the schema file, then the file is moved to "Bad_Data_Folder."

  - **3: Name of Columns** - The name of the columns is validated and should be the same as given in the schema file. If not, then the file is moved to "Bad_Data_Folder".

  - **4: The datatype of columns** - The datatype of columns is given in the schema file. This is validated when we insert the files into Database. If the datatype is wrong, then the file is moved to "Bad_Data_Folder".

  - **5: Null values in columns** - If any of the columns in a file have all the values as NULL or missing, we discard such a file and move it to "Bad_Data_Folder".

## STEP 3: Data insertion in DB:
  - **1. Database Creation and connection** - Create a database with the given name passed. If the database is already created, open the connection to the database.
  - **2. Table creation in the database** - Table with name - "Good_Data", is created in the database for inserting the files in the "Good_Data_Folder" based on given column names and datatype in the schema file. If the table is already present, then the new table is not created and new files are inserted in the already present table as we want training to be done on new as well as old training files.
  - **3. Insertion of files in the table** - All the files in the "Good_Data_Folder" are inserted in the above-created table. If any file has invalid data type in any of the columns, the file is not loaded in the table and is moved to "Bad_Data_Folder".