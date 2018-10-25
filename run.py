<<<<<<< HEAD
""" Application run file/bot """

from app import app
from app import routes
from app.models import Database

if __name__ == '__main__':
    Database().table()
    app.run(debug=True)
=======
""" Application run file """

from app import app

if __name__=='__main__':
    app.run(debug=True) 
>>>>>>> fd785df93e7e94d95f11562329ab42e870685ac1
