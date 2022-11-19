Capstone_MLE9
==============================

## this is now on the container branch.

Renato, this is a summary of what is currently in my src folder and the model.py and main.py files.
currently everything is working (with more or less intervention) through fastapi and uvicorn.

# model.py
at the very end is the predi (i changed the name to not get confused or tricked with the endpoint),
i also added two sample generator functions: sample_generator() takes an integer and returns a tuple with the sample data in dataframe form and also a string with the label for that sample.
the sample_generator2() prompts you to input the id of the sample and then works just like the sample_generator() function.

we can make the sample_generators return a csv if we end up needing it.

# main.py
there are several @app.post functions here (i will refer to them through their endpoint, and from top to bottom).

testeo: tests that a dictionary is received as a dictionary (fastapi only takes in dictionaries with " " quotes), check that i have defined the pydantic class Samplein as a Dict.  

sendfile: uses UploadFile and File from fastapi to send files across.  i did not use any pydantic classes here.  it uploads a file (the swagger interface of fastapi asks you to upload from a file) in pd.DataFrame.to_csv() form (i have added a sample data file to the src directory for this purpose), converts is back into a dataframe, calls the predi function and returns the predicion as a string.

predict: is the old version that we were using on sunday toguether. it takes a sample in the form of a dictionary (with ""), converts it back to a dataframe and returns the prdiction as a string.  the problem with this approach is that there is no easy way of generating the sample.  all pd to dictionary functions use ' ' which are rejected by fastapi, and all pd to json include fields or came as lists and i could not make them convert into the dict that we need as import.  involves significant manipulation to enter a sample.

all_in_prediction: combines the sample generator and the predi functions. it is clean but i am not sure how the entry id feature will work.  running it you get prompted in the command line.

all_in_prediction2: same as above but you enter the id as a required data at the time of calling the app.





uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000


