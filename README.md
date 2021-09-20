# BDS Assignment 2
Deliverables:
- Working code (in Python, Java or any preferred language) for the 2 programs (a) data loader (b) data query.
- At least 4 test cases (one for each query type) with the command line parameters that yield results to demonstrate.
## Bringing up mongo environment
This brings up mongodb and mongo express. You can visit http://localhost:8081 to play with the database
```
PS Y:\git\bds> docker compose up
[+] Running 2/0
 - Container bds_mongo-express_1  Created                                                                          0.0s
 - Container bds_mongo_1          Created                                                                          0.0s
Attaching to mongo-express_1, mongo_1
mongo_1          | {"t":{"$date":"2021-09-16T15:48:40.100+00:00"},"s":"I",  "c":"NETWORK",  "id":4915701, "ctx":"thread1","msg":"Initialized wire specification","attr":{"spec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":13},"incomingInternalClient":{"minWireVersion":0,"maxWireVersion":13},"outgoing":{"minWireVersion":0,"maxWireVersion":13},"isInternalClient":true}}}
mongo_1          | {"t":{"$date":"2021-09-16T15:48:40.100+00:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"thread1","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
mongo-express_1  | Welcome to mongo-express
mongo-express_1  | ------------------------
```
## Running your data loader
For windows
```
PS Y:\git\spa> py -m venv env
PS Y:\git\spa> .\env\Scripts\activate
(env) PS Y:\git\spa> pip install -r requirements.txt
(env) PS Y:\git\spa> python data_loader.py
```

## Running your data query 
For windows
```
(env) PS Y:\git\spa> python data_queryapp.py

```
This will ask for option for which question you want to run you can choose either 1,2,3 or 4
and pretty straightforward from there on.

Note: All queries have been made case insensitive

indexes used : restaurants.create_index([('address', TEXT)], default_language='english')