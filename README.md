# python-oslc-example
Python project to implement and oscl adapter.

1. Create a Flask API.
   localhost:5000/api

2. Create two namespaces (blueprint) for managing QM and RM domains
   localhost:5000/api/qm
   localhost:5000/api/rm

3. Create two endpoints for each domains for getting and posting resouces.
   responses should be rdf format (turtle, rdf+xml, or json-ld)



# Run application 
$ cd python-oslc-example
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install flask
$ pip install flask-resplus
$ python3 main.py
