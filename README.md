# app

<p>The application predicts stroke based on information about a patient.</p>

<h2>Data description</h2>
<p>According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.
This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient. </p>
<br>Data source - https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

<h2>Project Structure</h2>
<code>
    
    app
    ├── data                        - contains train and validation data
    │   ├── train.csv               - train set 
    │   └── val.csv                 - validation set 
    ├── models                      - this folder contains a trained estimator
    │   └── <name>.pickle           - trained estimator
    │
    ├── settings                    - contains constant values, connection parameters, etc.
    │   ├── constants.py            - multiple constants storage for their convenient usage
    │   └── specifications.json     - specifications of data preprocessing operations  
    │   
    ├── utils                       - this folder contains instruments to work with dataset
    │   ├── __init__.py             - init file for the package 
    │   ├── dataloader.py           - dataloader 
    │   ├── dataset.py              - class dedicated for giving info about the dataset
    │   ├── predictor.py            - predictor
    │   └── trainer.py              - train script
    │ 
    ├── app.py                      - route, app
    │
    ├── requirements.txt            - list of libraries used for Dockerization 
    │
    └── Dockerfile                  - commands used for Dockerization
</code>

    
<h2>Data Preprocessing</h2>
<p>This stage consists of 4 preprocessing steps:</p>
    <ol>
    <li>Drop id column</li>
    <li>Fill nan`s in bmi column with mean value</li>
    <li>Encode categorical values in columns gender, ever_married, work_type, Residence_type, smoking_status using LabelEncoder from sklearn.preprocessing</li>
    <li>Normalize numerical values in columns avg_glucose_level and bmi</li>
  </ol>
    
<h2>Training a model</h2>    
    
    
    
<h2>API</h2>
    
    
    
<h2>How to use</h2>
    
    
    
    
    
    
    
    
