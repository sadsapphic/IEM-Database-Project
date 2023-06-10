from flask import Flask 
import psycopg2
from flask import current_app
from flask_login import LoginManager
from .models import User

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234' 
    # Establish a database connection

    login_manager = LoginManager() 
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app) 

    @login_manager.user_loader 
    def load_user(user_id): 
        return User.get_by_id(user_id)
        

    conn = psycopg2.connect(
        dbname="IEM",
        user="postgres",
        password="root",
        host="localhost"
    )
    # Open a cursor to perform database operations
    cur = conn.cursor()

    app.config['DATABASE_CONNECTION'] = conn
    app.config['DATABASE_CURSOR'] = cur


    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager() 
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app) 

    @login_manager.user_loader 
    def load_user(id): 
        return User.get_by_id(int(id))
        

    return app 

