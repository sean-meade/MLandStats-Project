# Machine Learning and Statistics - Project

This repository contains my submission for Machine Learning and Statistics, a module as part of the H.Dip in data analytics with GMIT (2020).

The file *trainingModel.ipynb* contains an explaination of the data set found in *powerproduction.csv*, attempts at training two models to predict the power output for a given wind speed, and an analysis of their accuracy.

The *Dockerfile* file is used to implement a Dockker container utilizing *.dockerignore* to ignore unnecessary files for implementation.

*powerproduction.py* contains a Flask app that uses the model developed in *trainingModel.ipynb* and can be used to create a web locally (as shown below) or can be used by the *Dockerfile*.

*requirements.txt* contains all the packages required to run *powerproduction.py*.

The *imgs* folder contains images used for explaination in *trainingModel.ipynb* and the *static* folder contains *index.html*.

*index.html* is the template used by the Flask app *powerproduction.py*.

*ProjectPDF.pdf* contains the instructions for the project given by lecture Ian McLoughlin.

Below is an example of the app in the browser:
![image of plan my run](imgs/app-example.png)

## Implementing power production prediction app
---
### Windows
cd into working directory and then copy and paste the following command:
#### Flask
```
python powerproduction.py
```
#### Docker
```
docker build . -t powerproduction-app .
docker run -d -p 5000:5000 rando-image
```

### Linux
```
export FLASK_APP=powerproduction.py
python3 -m flask run
```
