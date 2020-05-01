from .controller import app

if __name__ == "__main__":
    '''
    Usage:  1. Set app env variable: $ export FLASK_APP=app
            2. Set the run environment to development: $ export FLASK_ENV=development
            3. Set port: $ export FLASK_RUN_PORT= <desired port> (especially for multi-processes) other skip this step to run on default port 5000
            4. Run app: $ python app.py

            (NB) All above can be run as a single command:
            $ FLASK_RUN_PORT=5001 FLASK_ENV=development FLASK_APP=app flask run
    '''
    app.run()