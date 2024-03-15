#This module contains code to run a Flask application.
from app.views import app
import sys
sys.path.append('.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
