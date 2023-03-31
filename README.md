# Demo to dockerize Flask+Streamlit

## Clone the project and go to the app folder

Git clone the project:
```bash
git clone https://github.com/panayo/demo-basic.git
```

Then go the app folder :
```bash
cd app/
```

## Launching Flask API Standalone
Activate the virtual environment (prerequisite to have pipenv ```pip install pipenv```) and run the API script inside the virtual environment:
```bash
pipenv install
pipenv shell
python backend.py
```

In another terminal test the endpoint :

For MacOs & Linux:
```bash 
curl -X POST http://localhost:6000/predict -H "Content-Type: application/json" -d '{"text":"This is a sample text made with love."}'
```
For Windows using Windows PowerShell:
```bash 
Invoke-WebRequest -Method POST -Uri http://localhost:6000/predict -Headers @{"Content-Type"="application/json"} -Body '{"text":"This is a sample text made with love."}'
```

## Running the Standalone API with a Docker Image
Give permission to the shell script :

```bash
sudo chmod 755 start_api.sh
```
Build the docker image for the Standalone API :
```bash
sudo docker build -t standlone_api:test -f Dockerfile_api .
```
Run the docker image :
```bash
sudo docker run -d -p 6000:6000 standlone_api:test
```
In another terminal test the endpoint :
For MacOs & Linux:
```bash 
curl -X POST http://localhost:6000/predict -H "Content-Type: application/json" -d '{"text":"This is a sample text made with love."}'
```
For Windows using Windows PowerShell:
```bash 
Invoke-WebRequest -Method POST -Uri http://localhost:6000/predict -Headers @{"Content-Type"="application/json"} -Body '{"text":"This is a sample text made with love."}'
```

## Interactive Testing of the Models with the Streamlit Interface using a Docker Image

Give permission to the shell script :
```bash
sudo chmod 755 start.sh
```
Build the docker image :
```bash
sudo docker build -t nlpproject:test -f Dockerfile .
```
Run the docker image :
```bash
sudo docker run -d -p 8501:8501 nlpproject:test
```
Go to the following address on the browser to test the API:

`http://localhost:8501/`

You must wait a few seconds for the Flask server to set up before querying.


## Text Data Exploration, Preprocessing, and Model Evaluation using Machine Learning

The entire machine learning process can be divided into three main stages: text data exploration and cleaning, text preprocessing and machine learning, and machine learning model comparison and evaluation.

In the first stage, the Text Data Exploration and Cleaning Notebook is used to explore and clean the text data by performing various data cleaning techniques such as removing irrelevant characters, converting text to lowercase, and removing stop words.

In the second stage, the Text Preprocessing and Machine Learning Notebook is used to preprocess the cleaned text data, prepare it for machine learning, and build machine learning models. This stage involves various techniques such as vectorizing text data and selecting appropriate machine learning algorithms.

In the final stage, the Machine Learning Model Comparison and Evaluation Notebook is used to compare and evaluate the performance of the different machine learning models built in the previous stage. 

It is important to note that training machine learning models can require a significant amount of computational resources, which can be a limitation for some users. As a result, the [Text Preprocessing and Machine Learning](notebooks/2.%20Text%20Preprocessing%20and%20Machine%20Learning%20Notebook.ipynb) includes only one example with errors due to the lack of local resources. To address this issue, the models were trained on an adapted virtual machine that provided the necessary resources for successful model training.


END

