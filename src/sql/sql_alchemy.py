import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = ":memory:"
DATABASE_URL = "src/sql/test.db"

# Create an engine to connect to a SQLite in-memory database
engine = create_engine(f"sqlite:///{DATABASE_URL}", echo=False)

# Create a base class for declarative class definitions
Base = declarative_base()


# Define a User class representing a table in the database
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"


# Define a class to manage database operations for the User model
class UserDatabaseManager:
    def __init__(self, engine):
        self.engine = engine
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def add_user(self, name, email):
        session = self.Session()
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.close()

    def get_all_users(self):
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return users

    # Add more methods for other database operations as needed


def main():
    # Usage example:
    user_manager = UserDatabaseManager(engine)
    user_manager.add_user("Alice", "alice@example.com")
    user_manager.add_user("Bob", "bob@example.com")

    users = user_manager.get_all_users()
    for user in users:
        print(user)


if __name__ == "__main__":
    main()
