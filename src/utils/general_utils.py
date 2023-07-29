import yaml
import os
#import json
import shutil # will be having a copy function
from tqdm import tqdm # get a progress bar to check the progress in for loops
import logging

class General_Utils:
    def __init__(self):
        pass

    def read_yaml(self, path_to_yaml: str) -> dict :
        """
        A function to read a yaml file.
        Args: 
        path_to_yaml : path to the yaml file.

        Return: a dictionary with the content of the yaml file
        """
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
        return content


    def create_directory(self, dirs: list):
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"directory created at {dir_path}")


    def save_local_df(self, df, df_path, index_status=False):
        """
        We use this function to store train and test data
        args:
        df: is the dataframe we want to save/store
        df_path: is the path where we want to store the dataframe df
        """
        df.to_csv(df_path,index=index_status)
        logging.info(f"data is saved at: {df_path}")


    def copy_file(self, source, local):
        """
        A function that would help us copy files from a directory to another. 
        (e.g. copy only validated data files from Training_Batch_Files to Good_data Folder.
        Args:
        source: data source path
        local: path where to download data locally
        """

        list_of_files = os.listdir(source)
        num_of_files = len(list_of_files)
        for file in tqdm(list_of_files, total = num_of_files, 
                        desc = f"Copying file from {source} to {local}", 
                        colour = "green" ):
            src = os.path.join(source,file)
            dest = os.path.join(local,file)
            shutil.copy(src,dest)