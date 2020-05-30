import sys

project_home = '/home/covid19bangladesh/covid19bangladeshAPI'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from api import create_app
application = create_app()
