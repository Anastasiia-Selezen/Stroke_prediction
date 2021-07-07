import pandas as pd
import numpy as np
import re

from sklearn.preprocessing import LabelEncoder


class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()


