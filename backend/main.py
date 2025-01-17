# Start the application on the configured port (default 8081)
# Look in api.routes for the actual api code
import sys
from os import environ
from api import app
import config

reload = False if len(sys.argv) > 1 and sys.argv[1] == 'production' else True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.apiPort, use_reloader=reload)
