# ml_querier
ML querier is a web app based on Django (Python) web development framework.
The main purpose of this app is to use the mercadolibre public API to request public and private data, then store it into a relational database.

## Running in Development Mode (Local)

* Install Python, remember, never install python from the Microsoft Store or other weird site. Always install it from the official webpage.


* Initialize the virtual enviroment

In order to run this project it must be contained inside a virutal enviroment, if there isn't any then run:

````cmd
python -m venv /path/to/new/virtual/environment
````
Activate the virtual enviroment
```cmd
D:\path\to\virtual\env\ml_querier\Scripts>activate.bat
````

* Clone the repo from github
````bash
git clone https://github.com/guillermojleonr/mercadolibre_API_querier.git
````

* Install the dependencies if they aren't already installed


````cmd
cd \path\to\repository\

pip install -r requirements.txt
````

* Check enviroment variables from the underlying Windows OS.

```cmd
set PATH
```

* Set the following enviroment variable. 

````cmd
set DEVELOPMENT_MODE=True
````
When you lift the server the file setting.py will set all the enviroment variables needed to run the application. Becasue the enviroment variable DEVELOPMENT_MODE is set to True, setting.py will use the development enviroment variables.

* Run the ssl webserver.
````cmd
python manage.py runsslserver
````

Now the app should be running without issues.

>Watching for file changes with StatReloader
>Validating models...
>System check identified no issues (0 silenced).
March 25, 2023 - 21:33:48
Django version 4.1, using settings 'ml_querier.settings'
Starting development server at https://127.0.0.1:8000/
Using SSL certificate: C:\Users\guill\AppData\Local\Programs\Python\Python310\lib\site-packages\sslserver\certs\development.crt
Using SSL key: C:\Users\guill\AppData\Local\Programs\Python\Python310\lib\site-packages\sslserver\certs\development.key
Quit the server with CTRL-BREAK.

* Check the web app at this url (https://127.0.0.1:8000/)

## Running in production enviroment
There are multiple configuration and tasks to do to deploy on a remote server. I used to deploy using github actions on a PaaS service named render. But it is not longer available for free.

The following instructions are for manual deployment on a regular remote server.

Server characteristics: Shared hosting server with cpanel administrator.

Because this is a shared host, we can't run some commands or configure some features from terminal. We need to use cpanel.

* Create a subdomain in the Cpanel "Domains" section. Specify the subdomain name and the root directory it is goint to point.

* Create an "A" DNS record in the Cpanel "Zone Editor" section. Specidy the subdomain name and the host shared IP address. The DNS new "A" records might take hours to propagate you can check it in https://mxtoolbox.com

* Inside the root directory from your new app, create an index.html file with "Hello World" in it.

After a few hours you should see the webpage being served.



Note: forgive me if this two steps has nothing to do with eachother, I did both.


...
...

