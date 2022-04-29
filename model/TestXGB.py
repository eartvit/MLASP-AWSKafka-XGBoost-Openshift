import pandas as pd
import joblib
import xgboost as xgb

class TestXGB(object):
  def __init__(self):
    self.model = joblib.load("xgbModel.pkl")
    self.features = ['BackgroundThreads', 'LogCleanerThreads', 'NumIoThreads','NumNetworkThreads', 'NumPartitions', 'NumNodes', 'NumReplicaFetchers','ThreadsClient', 'MessageSize']


  def predict(self, X, features_names):
    print(f'Got X={X} of type {type(X)}, feature_names={self.features} \\n')
    record = pd.DataFrame(X, columns=self.features)
    print(f'Record is {record}')
    resp = self.model.predict(record)
    return resp


  def metrics(self):
    return [
      {"type": "COUNTER", "key": "mycounter", "value": 1}, # a counter which will increase by the given value
      {"type": "GAUGE", "key": "mygauge", "value": 100},   # a gauge which will be set to given value
      {"type": "TIMER", "key": "mytimer", "value": 20.2},  # a timer which will add sum and count metrics - assumed millisecs
    ]
  
