from flask import Flask, jsonify, make_response
from database import db
from models import User
from werkzeug.security import generate_password_hash
from blueprints.auth import auth, login_manager
from blueprints.tasks import tasks
from blueprints.users import users
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login_site'
login_manager.login_message = "User needs to be logged in to view this page"

app.register_blueprint(users)
app.register_blueprint(auth)
app.register_blueprint(tasks)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            hashed_password = generate_password_hash('admin', method='pbkdf2')
            admin = User(username='admin', password=hashed_password, role='superadmin')
            db.session.add(admin)
            db.session.commit() 
    app.run(debug=True)