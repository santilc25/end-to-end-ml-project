import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.paths import RAW_DATA_DIR, TRANSFORMED_DATA_DIR

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

import kaggle
from dotenv import load_dotenv

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join(RAW_DATA_DIR,'train.csv')
    test_data_path:str = os.path.join(RAW_DATA_DIR,'test.csv')
    raw_data_path:str = os.path.join(RAW_DATA_DIR,'data.csv')
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            logging.info('Download data from kagle API')
            load_dotenv("../../.env")
            dataset_name = 'spscientist/students-performance-in-exams'
            kaggle.api.dataset_download_files(dataset_name,path=RAW_DATA_DIR,unzip=True)
            
            logging.info('Read the dataset as dataframe')
            df=pd.read_csv(f'{RAW_DATA_DIR}/StudentsPerformance.csv')
            df.columns = [col.replace(" ","_").replace("/","_") for col in df.columns]
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train and test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")
            
            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)
            
        except Exception as e:
            raise CustomException(e,sys)