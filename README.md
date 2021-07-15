# app

Application that predicts stroke 
<br>data source - https://www.kaggle.com/fedesoriano/stroke-prediction-dataset




<h2>Project Structure</h2>
<code>
<br>app
<br>├── data                        - contains train and validation data
<br>│   ├── train.csv               - train set <br>
<br>│   └── val.csv                 - validation set (must contain target values)<br>
<br>├── models                      - this folder contains a trained estimator.<br>
    │   └── <name>.pickle           - trained estimator. <br>
    │<br>
    ├── settings                    - here you can store different constant values, connection parameters, etc.<br>
    │   ├── constants.py            - multiple constants storage for their convenient usage.<br>
    │   └── specifications.json     - specifications of your data preprocessing operations.   <br>
    │   <br>
    ├── utils                       - this folder contains instruments we'll use to work with dataset.<br>
    │   ├── __init__.py             - init file for the package. <br>
    │   ├── dataloader.py           - dataloader. <br>
    │   ├── dataset.py              - class dedicated for giving info about the dataset.<br>
    │   ├── predictor.py            - predictor.<br>
    │   └── trainer.py              - train script.<br>
    │ <br>
    ├── app.py                      - route, app.<br>
    │<br>
    ├── requirements.txt			- list of libraries used for Dockerization <br>
    │<br>
    └── Dockerfile					- commands used for Dockerization<br>
</code>
