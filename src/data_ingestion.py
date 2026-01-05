import logging
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import logger_add

logger=logger_add("logs","data_ingestion")

def load_data(path):
    try:
        data=pd.read_csv(path)
        logger.debug("Data Loaded Successfully")
        return data
    except Exception as e:
        logger.error("Error: %s",e)
        raise
def traintestsplit(data,train_size):
    try:
        traindata,testdata=train_test_split(data,train_size=train_size,random_state=42)
        logger.debug(f"Data splitted train size: {round(train_size*100)}% and test size: {round((1-train_size)*100)}% ")
        return traindata,testdata
    except Exception as e:
        logger.error("Error: %s",e)
        raise
def save_data(traindata,testdata,path):
    try:
        dirname="raw"
        dirpath=os.path.join(path,dirname)
        os.makedirs(dirpath,exist_ok=True)
        traindata.to_csv(os.path.join(dirpath,"train.csv"),index=False)
        testdata.to_csv(os.path.join(dirpath,"test.csv"),index=False)
        logger.debug(f"raw data saved in {dirpath}")
    except Exception as e:
        logger.error("Error: %s",e)
        raise
def main():
    try:
        trainsize=0.8
        path="data/raw/heart_failure_clinical_records_dataset.csv"
        savepath="data"
        data=load_data(path)
        traindata,testdata=traintestsplit(data,trainsize)
        save_data(traindata,testdata,savepath)
    except Exception as e:
        logger.error("Error: %s",e)
        raise
if __name__=="__main__":
    main()