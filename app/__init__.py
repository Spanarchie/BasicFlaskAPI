__author__ = 'colinmoore-hill'

import os
from flask import Flask
from py2neo import Graph


from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, \
    MAIL_PASSWORD, GRAPHENEdb1


app = Flask(__name__)
app.config.from_object('config')
gdb = Graph( GRAPHENEdb1 )



from app import views, models