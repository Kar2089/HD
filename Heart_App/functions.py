import pickle
import config
import json
import numpy as np
with open(config.pkl_path,'rb') as f:
    model = pickle.load(f)
with open(config.jsn_path, 'r') as j:
    columns = json.load(j).get('columns')
def predict():
    pass
