
from pathlib import Path
import joblib
import pandas as pd
import numpy as np
import argparse

BASE_DIR = Path("model.py").resolve(strict=True).parent

def sample_generator(id):
    """
    Sample generator, receives an integer as input and
    returns a tuple with a sample in dataframe format and a string with the type of network event.
    """
    sample_data_name = "X_red_new_test_cat.csv"
    labels_data_name  = "y_red_new_test_cat.csv"
    # sample_data_path = Path(BASE_DIR).joinpath(sample_data_name)
    samples = pd.read_csv(sample_data_name)
    labels = pd.read_csv(labels_data_name)
    results_dict =    {
                        1: 'Blackhole',
                        2: 'Diversion',
                        3: 'Normal',
                        4: 'Overflow',
                        5: 'PortScan',
                        0: 'TCP-SYN'
                        }
    if id in range(samples.shape[0]):
        sample = samples.iloc[[id]]
        label = results_dict[int(labels.iloc[[id]].values)]
        return sample , label
    else:
        print("Sample ID excedes number of samples")


def sample_generator2():
    """
    Sample generator prompts for an integer as input and
    returns a tuple with a sample in dataframe tuple[0] format and a string tuple[1] with the type of network event.
    """
    id = int(input("Enter id: "))

    sample_data_name = "X_red_new_test_cat.csv"
    labels_data_name  = "y_red_new_test_cat.csv"
    # sample_data_path = Path(BASE_DIR).joinpath(sample_data_name)
    samples = pd.read_csv(sample_data_name)
    labels = pd.read_csv(labels_data_name)
    results_dict =    {
                        1: 'Blackhole',
                        2: 'Diversion',
                        3: 'Normal',
                        4: 'Overflow',
                        5: 'PortScan',
                        0: 'TCP-SYN'
                        }
    if id in range(samples.shape[0]):
        sample = samples.iloc[[id]]
        label = results_dict[int(labels.iloc[[id]].values)]
        return sample , label
    else:
        print("Sample ID excedes number of samples")        

# generate a sample for testing
# must check the data path or make it automatic
# X_samples = pd.read_csv("../data/processed/X_red_new_test_cat.csv")
# sample_number = 534
# sample = X_samples.iloc[[sample_number]]




def predi(sample):
    """
    predi function: takes a sample network interaction in the form of a dataframe and 
    retuns string with the prediction of the network event.
    
    """
    model_name = "model_jg_01.joblib"
    model_file = Path(BASE_DIR).joinpath(model_name)
    
    if not model_file.exists():
        return False

    model = joblib.load(model_file)

    results_dict =    {
                        1: 'Blackhole',
                        2: 'Diversion',
                        3: 'Normal',
                        4: 'Overflow',
                        5: 'PortScan',
                        0: 'TCP-SYN'
                        }

    result_sample = results_dict[model.predict(sample)[0]]   #result_sample = results_dict[model.predict(sample)[0]]

    return result_sample   # use this for model
    #return print(result_sample) #use this for testing

#predi(sample) #use for testing


