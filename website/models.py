from . import current_app
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, email, password, first_name):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name

    def save(self):
        conn = current_app.config['DATABASE_CONNECTION']
        cur = current_app.config['DATABASE_CURSOR']

        # Insert a new user
        cur.execute(
            "INSERT INTO Users (email, password, first_name) VALUES (%s, %s, %s) RETURNING id",
            (self.email, self.password, self.first_name)
        )
        self.id = cur.fetchone()[0]
        conn.commit()

    @staticmethod
    def get_by_email(email):
        conn = current_app.config['DATABASE_CONNECTION']
        cur = current_app.config['DATABASE_CURSOR']

        cur.execute(
            "SELECT * FROM Users WHERE email = %s", (email,)
        )

        user_data = cur.fetchone()

        if user_data is None:
            return None

        return User(id=user_data[0], email=user_data[1], password=user_data[2], first_name=user_data[3])
    
    @staticmethod
    def get_by_id(user_id):
        conn = current_app.config['DATABASE_CONNECTION']
        cur = current_app.config['DATABASE_CURSOR']

        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cur.fetchone()
        if user_data:
            user = User(id=user_data[0], email=user_data[1], password=user_data[2], first_name=user_data[3])
            return user
        else:
            return None

    def get_id(self):
        return self.id








    