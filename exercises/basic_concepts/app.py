from flask import Flask, jsonify
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Set up logging configuration
set_logging(log_file='app.log')

class UserRepository:
    """
    Repository component that handles user data access.

    Implements the Repository design pattern to abstract data retrieval.
    """

    def get_users(self):
        """
        Returns a static list of user dictionaries.

        In a real application, this would query a database.
        """
        plog("Fetching users from repository", DEBUG)
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]


class UserService:
    """
    Service component that contains business logic.

    Uses dependency injection to receive a repository instance.
    """

    def __init__(self, repository: UserRepository):
        """Initializes the service with a given repository."""
        plog("Initializing UserService with repository", DEBUG)
        self.repository = repository

    def list_users(self):
        """Retrieves the list of users from the repository."""
        plog("Listing users from service", INFO)
        return self.repository.get_users()


app = Flask(__name__)
user_service = UserService(UserRepository())

@app.route("/users")
def get_users():
    """HTTP endpoint that returns a JSON list of users."""
    plog("Received request for /users endpoint", INFO)
    users = user_service.list_users()
    return jsonify(users)


if __name__ == "__main__":
    # Entry point: runs the Flask development server in debug mode.
    plog("Starting Flask app", INFO)
    app.run(debug=True)