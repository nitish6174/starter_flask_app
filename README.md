# Starter flask app

This repo serves as the base setup for developing your flask application, with some of the best practices and easy-to-scale code structure.


### Features
* Create views with re-usable Jinja templates
* CSS & JS bundles defined to enable loading only the required files page-wise
* Easy to configure/enable the following:
  * MongoDB connection and querying
  * Uploading & downloading of static files
* Gzip compression
* CSS, JS minification

**Note** : Tested with Python 3.6


## Setting up project

1. Clone the repo

2. Create virtual environment for the project and install pip dependencies
   ```bash
   cd starter_flask_app
   virtualenv -p python3 venv
   # Source the virtual env
   # zsh/fish users need to use activate.zsh/activate.fish files instead
   source venv/bin/activate
   pip install -r requirements.txt
   ```


## Running the server

```bash
python run.py
```

Supported arguments:
* ```--host``` : To set the app host (defaults to 0.0.0.0)
* ```--port``` : To set the app port (defaults to 5000)
* ```--debug``` : Pass this flag to enable debugging

Now open ```http://localhost:5000``` in your browser to view the app.


## Developing your app from the base code

* Enabling mongo:
  * Set the appropriate constants in ```flaskapp/config.py```
  * Uncomment the mentioned line in ```flaskapp/app.py```
* Enabling static file downloading:
  * Set the variable ```DOWNLOADS_DIR``` in ```flaskapp/config.py```
  * Uncomment the mentioned function in ```flaskapp/app.py```
  * Modify the route in this function as appropriate.
* Define templates for your pages in ```flaskapp/templates/``` dir.  
  See ```home.html``` for reference which inherits the basic structure from ```layout.html```
  and just defines the required parts.
* Define route for the pages in ```flaskapp/routes/view_routes.py```
* Define API related routes in ```flaskapp/routes/api_routes.py```
* Add the CSS & JS files in ```flaskapp/static/``` in appropriate subdir.  
  Then, define the suitable bundle page-wise in ```flaskapp/assets.py```.  
  Refer the existing bundles in the file.
