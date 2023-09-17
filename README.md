https://flask.palletsprojects.com/en/2.3.x/
Flash is a tool for developing servers

https://flask.palletsprojects.com/en/2.3.x/installation/#install-flask
Make a venv for the server
* mkdir myproject
* cd myproject
* py -3 -m venv .venv

To install flask type: pip3 install Flask

If you get a error in vscode on windows run:  Set-ExecutionPolicy RemoteSigned

turn on  .venv\Scripts\activate


#theirs a flask and django framework
https://www.djangoproject.com/

To run the server
flask --app web_server run

#css needs to go in a static folder.  The folder should be static/style
# this allows you to use python code inside of a html file in flask
{{ }}