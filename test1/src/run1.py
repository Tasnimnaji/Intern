#This module contains code to run a Flask application.
import sys
sys.path.append('.')
from app.views import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
