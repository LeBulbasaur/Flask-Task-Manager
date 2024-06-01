### Flask Task Manager Project

This project is a web application built using the Flask framework. It serves as a task manager where users can create, update, and delete tasks. It also allows for account creation, promoting and demoting different team members via admin account. The application consists of several modules, each responsible for different functionalities.

Modules:
- auth: This module is responsible for user authentication. It uses login_manager for managing user sessions.

- tasks: This module is responsible for managing user tasks. It allows users to create, update, and delete tasks.

- users: This module is responsible for user management. It allows for the management of user profiles (only available for superadmin (user: admin, pass: admin)).

Features:

The application uses a SQLAlchemy database for data storage and a Flask-Bootstrap for simple user interface creation. The task manager feature allows users to keep track of their tasks, making it a useful tool for productivity.
