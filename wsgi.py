# wsgi.py
# uWSGI entry point

from pkmngo import application

if __name__ == '__main__':
    application.run()
