from src.exception import CustomException
from src.logger import logging
import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



@dataclass
class DataIngestionConfig :
       data_path : str = os.path.join('artifacts','raw_data.csv')
       train_path : str = os.path.join('artifacts','train_data.csv')
       test_path : str = os.path.join('artifacts','test_data.csv')

class DataIngestion :
       def __init__(self):
            self.data_ingestion_obj_config = DataIngestionConfig()

       def data_ingestion_method(self):
            
            logging.info("Entered the data ingestion method or component")
            try:

                df = pd.read_csv("notebook\data\predictive_maintenance.csv" ,)
                logging.info("Data Read from the CSV")
                os.makedirs(os.path.dirname(self.data_ingestion_obj_config.train_path), exist_ok=True)
                df.to_csv(self.data_ingestion_obj_config.data_path , index = False , header = True)
                logging.info("Initiating Train Test Split")
                train_data , test_data = train_test_split(df, test_size=0.2 , random_state=42)
                train_data.to_csv(self.data_ingestion_obj_config.train_path , index = False , header = True)
                test_data.to_csv(self.data_ingestion_obj_config.test_path , index = False , header = True)
                logging.info("Train Test Data Saved ")

                return(
                      self.data_ingestion_obj_config.train_path,
                      self.data_ingestion_obj_config.test_path
                )



            except Exception as e:
                  raise CustomException(e,sys)


