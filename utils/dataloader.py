import pandas as pd
import numpy as np
import re

from sklearn.preprocessing import LabelEncoder


class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    def load_data(self):
        # fill Nan with mode
        self.dataset['bmi'] = self.dataset['bmi'].fillna(self.dataset['bmi'].mean())

        # drop columns
        drop_elements = ['id']

        self.dataset = self.dataset.drop(drop_elements, axis=1)

        # encode labels
        le = LabelEncoder()

        le.fit(self.dataset['gender'])
        self.dataset['gender'] = le.transform(self.dataset['gender'])

        le.fit(self.dataset['ever_married'])
        self.dataset['ever_married'] = le.transform(self.dataset['ever_married'])

        le.fit(self.dataset['work_type'].values)
        self.dataset['work_type'] = le.transform(self.dataset['work_type'].values)

        le.fit(self.dataset['Residence_type'])
        self.dataset['Residence_type'] = le.transform(self.dataset['Residence_type'])

        le.fit(self.dataset['smoking_status'])
        self.dataset['smoking_status'] = le.transform(self.dataset['smoking_status'])

        # scale numerical data
        self.dataset['avg_glucose_level'] = (self.dataset['avg_glucose_level'] -
                                             self.dataset['avg_glucose_level'].min()) \
                                            / (self.dataset['avg_glucose_level'].max() -
                                               self.dataset['avg_glucose_level'].min())
        self.dataset['bmi'] = (self.dataset['bmi'] -
                               self.dataset['bmi'].min()) \
                            / (self.dataset['bmi'].max() -
                               self.dataset['bmi'].min())
        return self.dataset
