# Demo to dockerize Flask+Streamlit

## Clone the project and go to the app folder

Git clone the project:
```bash
git clone https://github.com/panayo/docker-template.git
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

END

