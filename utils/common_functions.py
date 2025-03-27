import os
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import pandas as pd

logger = get_logger(__name__)
import yaml
from pathlib import Path

def read_yaml(file_path: str):
    """Read and return YAML file contents.
    
    Args:
        file_path (str): Path to the YAML file
        
    Returns:
        dict: Parsed YAML content
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise Exception(f"Error reading YAML file {file_path}: {str(e)}")

        
def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not in the given path")
        
        with open(file_path,"r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Succesfully read the YAML file")
            return config
    
    except Exception as e:
        logger.error("Error while reading YAML file")
        raise CustomException("Failed to read YAMl file" , e)
    

def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)
    