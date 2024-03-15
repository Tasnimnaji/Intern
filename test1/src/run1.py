#Flask
import sys
from app.views import app

sys.path.append('.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
