# MLASP on OpenShift crash course demo
This repository is a basic example of ML Workloads on Red Hat OpenShift, reusing the data and model inference application from the [MLASP](https://github.com/SPEAR-SE/mlasp) research paper. Please keep in mind the code in this repository is just for demonstration purposes.

Before starting, it is assumed you have access to an OpenShift cluster with the Open Data Hub operator installed and instantiated with Jupyter Hub, Prometheus and Grafana projects. The notebooks are supposed to be executed inside Jupyter Hub.

The resulting model is packaged in the ```model``` folder and uses Seldon core.

The model is integrated with the ```test-app``` application which provides both a simple HTML as well as a REST-ful interface for model inferencing.
The REST-ful interface may be accessed using Postman using the following structure:
```
{
 "FeatureList": "BackgroundThreads, LogCleanerThreads, NumIoThreads, NumNetworkThreads, NumPartitions, NumNodes, NumReplicaFetchers, ThreadsClient, MessageSize",
 "BackgroundThreads": "5, 25",
 "LogCleanerThreads": "1, 3",
 "NumIoThreads": "1, 4",
 "NumNetworkThreads": "1, 6",
 "NumPartitions": "1, 2",
 "NumNodes": "1, 5",
 "NumReplicaFetchers": "1, 2",
 "ThreadsClient": "5, 15",
 "MessageSize": "10240, 10240",
 "Epochs": "150",
 "SearchTargetValue": "484695",
 "Precision": "2.9"
}
```

The details about the parameters are provided in the [MLASP](https://github.com/SPEAR-SE/mlasp) research paper. The structure above is detailed in the ```test-app.py``` file.

Deployments of both the ```model``` and ```test-app``` are supposed to be done from OpenShift using the Developer view ```Add->GitRepository->From DockerFile``` providing the appropriate context directory for each deployment.

The ```test-app``` requires two environment parameters to be declared in the deployment configuration of openshift (see the values from the code).

