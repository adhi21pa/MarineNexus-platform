from flask import Flask,render_template,request,redirect,url_for
#from public import public
from admin import admin 


app=Flask(__name__)
app.secret_key="AG"

#app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')


app.run(debug=True,port=5030)   