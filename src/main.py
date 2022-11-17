
from fastapi import FastAPI, Query, HTTPException  # why are we importing Query? it is not used.
from pydantic import BaseModel , Json
from model import predi, sample_generator2 , sample_generator
from typing import Dict, List
import pandas as pd  #just for converting back the dict to a  dataframe
import joblib
from fastapi import File, UploadFile # for testing sending files through the API


app = FastAPI()

# pydantic models
class Samplein(BaseModel):
    sample: Dict[str , float]

class Result(BaseModel):
    result: str


@app.get("/ping")
def pong():
    return {"ping": "pong!"} , print("aleluya")  # added print command to see how it works in the swagger ui.

@app.post("/testeo") # a test function to check the format of the input data
def testeo(datos : Samplein):
    return datos.sample    
    

@app.post("/sendfile")  #takes a pd.DataFrame.to_csv() file and returns the prediction
async def sendfile(file: UploadFile = File(...)):
    try:
        #contents = file.file.read()
        #print(contents)
        # with open(file.filename, 'wb') as f:
        #     f.write(contents)
        sample = pd.read_csv(file.file)
        #file.file.close()
        result = predi(sample)
        
    except Exception:
        return {"message": "There was an error uploading the file"}

    #sample = pd.read_csv(f)
    #file.file.close()
    #result = predi(sample)

    return result

    #return {"message": f"Successfully uploaded {file.filename}"}



@app.post("/predict") # takes a dicttionary with "" in the keys, wer are using  in sample1.to_json(orient="records") format but take only the dict part of the list and returns the prediction
def get_prediction(payload : Samplein):   #def get_prediction(payload: Samplein):
    """
    This function takes in a sample and returns the predicted class.
    """

    # the data samples are comming as a dictionary, to convert them into the dataframe expected
    # by the model wefirst need to reconvert it into a format that the df.from_dict will understand

    data_init = payload.sample  #to retreive the dictionary
    data_final = []
    data_final.append(data_init) #the from_dict expects a list of dictionaries

    sample = pd.DataFrame.from_dict(data_final) #convert the dictionary into a dataframe
    
    #sample = pd.read_json(payload.sample,orient="records") #the data is not comming as json
    
    result = predi(sample) #have to define sample
    
    if not result:
        raise HTTPException(status_code=400, detail="Model not found.")

    return result  



@app.post("/all_in_prediction") # waits for the entry of an id value (of the sample in the test set) and returns the prediction and the sample's label.
def get_sample_prediction():
    sample = sample_generator2()
    result = predi(sample[0])

    return print("The predicted nature of the network status is: {} and the actual status is: {}.".format(result , sample[1]))

    
@app.post("/all_in_prediction2") # receives an id value (integer) (of the sample in the test set) and returns the prediction and the sample's label.
def get_sample_prediction(id: int):
    sample = sample_generator(id)
    result = predi(sample[0])

    return print("The predicted nature of the network status is: {} and the actual status is: {}.".format(result , sample[1]))  , result, sample[1]  #print out and two objects as returns




