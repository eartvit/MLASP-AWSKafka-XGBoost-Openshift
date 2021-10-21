import pandas as pd
import joblib


class TestXGB(object):
  def __init__(self):
    self.model = joblib.load("xgbModel.pkl")


  def predict(self,X,features_names):
    print(f'Got X={X} of type {type(X)}, df={pd.DataFrame(X).to_numpy()} \\n')
    resp = self.model.predict(pd.DataFrame(X))
    return resp


  def metrics(self):
    return [
      {"type": "COUNTER", "key": "mycounter", "value": 1}, # a counter which will increase by the given value
      {"type": "GAUGE", "key": "mygauge", "value": 100},   # a gauge which will be set to given value
      {"type": "TIMER", "key": "mytimer", "value": 20.2},  # a timer which will add sum and count metrics - assumed millisecs
    ]
  
  
  def init_metadata(self):
    meta = {
            "name": "xgb-bne-time-series",
            "versions": ["v-0.1"],
            "platform": "seldon",
            "inputs": [
                {
                    "messagetype": "ndarray",
                    "schema": {"names": ["DURATION", "THREADS_1", "TPS", "queueProcess.allocating.processThreads", "queueProcess.allocating.queueSize", "queueProcess.bulk.batchSize", "queueProcess.bulk.processThreads",
                                        "queueProcess.bulk.queueSize", "queueProcess.message.processThreads", "queueProcess.message.queueSize", "nb_immNodes"]},
                }
            ],
            "outputs": [{"messagetype": "ndarray"}],
            "custom": {"author": "eartvit", "extra": "test example"},
    }
    return meta
  
