# python-oslc-example
Python project to implement and oscl adapter.

1. Create a Flask API.
   ```
   localhost:5000/api
   ````

2. Create two namespaces (blueprint) for managing QM and RM domains
   ```
   localhost:5000/api/qm
   localhost:5000/api/rm
   ````

3. Create two endpoints for each domains for getting and posting resouces.
   ```
   responses should be rdf format (turtle, rdf+xml, or json-ld)
   ````


# Run application

1. Clone the project.

2. Go into the folder
   ```bash
   cd python-oslc-example
   ```

3. Create the virtual environment
   ```bash
   python3 -m venv venv
   ```

4. Activate the new virtual environment
   ```bash
   venv/bin/activate
   ```

5. Install the libraries.
   ```bash
   pip install -r requirements.txt
   ```

6. Execute the project
   ```bash
   export FLASK_APP=main.py
   flask run
   ```