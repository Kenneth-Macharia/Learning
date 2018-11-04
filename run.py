from sqlalchemy_init import db_obj
from app import app

db_obj.init_app(app)

@app.before_first_request
def setup_dB():
    db_obj.create_all()

''' For testing locally '''
#app.run(debug=True)
