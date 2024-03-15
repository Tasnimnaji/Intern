from app.views import app  # pylint: disable=C0413
import sys
sys.path.append('.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
