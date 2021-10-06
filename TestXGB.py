import pandas as pd
import joblib


class TestXGB(object):
  def __init__(self):
    self.model = joblib.load("xgbModel.pkl")


  def predict(self,X,features_names):
    print(f'Got X={X} of type {type(X)}, df={pd.DataFrame(X).to_numpy()} \\n')
    resp = self.model.predict(pd.DataFrame(X))
    return resp

