from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    name: str = Field(min_length=1)
    email: Optional[EmailStr] = None


class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user):
        if user_id in self.users:
            raise ValueError(f"User with ID '{user_id}' already exists.")
        self.users[user_id] = user

    def get_user(self, user_id):
        if user_id not in self.users:
            raise ValueError(f"User with ID '{user_id}' does not exist.")
        return self.users[user_id]

    def update_user(self, user_id, new_user_data):
        if user_id not in self.users:
            raise ValueError(f"User with ID '{user_id}' does not exist.")
        self.users[user_id].name = new_user_data.name
        if new_user_data.email is not None:
            self.users[user_id].email = new_user_data.email

    def delete_user(self, user_id):
        if user_id not in self.users:
            raise ValueError(f"User with ID '{user_id}' does not exist.")
        del self.users[user_id]


def main():
    # Create a repository instance
    user_repository = UserRepository()

    # Add users to the repository
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")
    user_repository.add_user(1, user1)
    user_repository.add_user(2, user2)

    # Get a user from the repository
    print(user_repository.get_user(1).name)  # Output: Alice

    # Update a user in the repository
    user_repository.update_user(1, User(name="Alice Smith"))
    # user_repository.update_user(1, {"name": "Alice Smith"})
    print(user_repository.get_user(1))  # name='Alice Smith' email='alice@example.com'

    # Delete a user from the repository
    user_repository.delete_user(1)
    try:
        user_repository.get_user(1)
    except ValueError as e:
        print(e)  # Output: User with ID '1' does not exist.


if __name__ == "__main__":
    main()
