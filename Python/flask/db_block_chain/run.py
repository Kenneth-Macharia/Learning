from controller import app

if __name__ == "__main__":

    '''
    Runing app:

        $ FLASK_ENV=developmentpython run.py
            (use 'filename' to import modules)

            or

        $ FLASK_RUN_PORT=5000 FLASK_ENV=development FLASK_APP=run flask run
            (use '.filename' to import modules) (Allows parallel processes on sep ports)
    '''
        # host 0.0.0.0 allows the app to be accessed from outside its container.
    app.run(host='0.0.0.0')