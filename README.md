# test-seldon-s2i
Test Seldon XGB s2i deployment with openshift. This example is provided as-is just as a model. The XGB is a regressor trained with some private dataset. Please do not ask for the dataset or details about the regression problem the model is trained for.

Once service is deployed test with `curl -s -k -d '{"data": {"ndarray":[[180, 150, 400, 11, 2000, 10, 10, 10000, 2, 30000, 6]]}}' -X POST https://<openshift_route_name>/predict -H "Content-Type: application/json"`

For using the above values the response should be `{"data":{"names":[],"ndarray":[143634.953125]},"meta":{}}`
