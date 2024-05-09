import os
from controllers.flask_context import app


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(port=port, debug=True, host="0.0.0.0")