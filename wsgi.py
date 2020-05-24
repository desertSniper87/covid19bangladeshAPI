import sys
from flask import  Flask

path = '/home/covid19bangladesh/covid19bangladeshAPI'
if path not in sys.path:
   sys.path.insert(0, path)

app = Flask('__api__')

from api import app as application

if __name__ == '__main__':
    app.run()
