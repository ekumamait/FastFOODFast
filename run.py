""" Application run file/bot """

from app import app
from app import routes
from app.models import Database

if __name__ == '__main__':
    Database().table()
    app.run(debug=True)
