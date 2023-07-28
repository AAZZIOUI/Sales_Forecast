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
## STEP 2: inializations:
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
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/user_name/dvc-ML-demo-AIOps",
    author_email="user_name@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn',
        'Flask'
    ]
)
```
### Create requirement file and install dependencies
```bash
touch requirements.txt
pip install -r requirements.txt
```

