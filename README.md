# Productivity Notes API
## Project Description
Productivity Notes API is a secure Flask API that allows users to signUp,login and manage their personal notes.The app uses JWT(JSON Web Tokens) tokens to ensure  user's identity and allows users to only make changes or modify their own resource.
The app supports full CRUD operations on notes,pagination,secure password hashing using Flask_Bcrypt and database seeding with sample data.

## Features
- User registration
- User login with JWT authentication
- Password hashing using Bcrypt
- Check user session authenticated
- Create,update and delete notes
- View paginated notes
- Protected routes using @jwt_required decorator

## Technologies Used
- Python
- Flask
- Flask_RESTful
- Flask_jwt_extended
- Flask Bcrypt
- Marshmallow

## Installation Instructions
Clone the repository
```bash
git clone https://github.com/munirasheikh-rgb/Productivity-notes-app-and-jwt-clients.git
```
Navigate to the project
```bash
cd productivity-notes-app-and-jwt-clients
```
install the dependencies
```bash
pipenv install
```
Activate the virtual environment
```bash 
pipenv shell
```
# Database SetUp
Initialize the database and run migrations
```bash
flask --app server.app db init
flask --app server.app db migrate -m "Initial migration"
flask --app server.app db upgrade head
```
## Run Application
Start flask server
```bash
python -m server.app
```
The API runs on port
```
 http://127.0.0.1:5555
 ```

## API Endpoints
## Authentication Routes
- Register User
```
POST/signup
```
Registers a new user to the system
- Login User
```
POST/login
```
Authenticates a user and return jwt token.
- Check Session
```
GET/me
```
Returns the existing authenticated user

## Notes Routes
- Retrieve user notes
```
GET/notes?page=1&per_page=5
```
Returns all notes(paginated) belonging to the authenticated user

- Create note
```
POST/notes
```
Create new note for the authenticated user
- Update note
```
PATCH/notes/<id>
```
Updates a note belonging to an authenticated user

- Delete note
```
DELETE/notes/<id>
```
Deletes a note owned by the authenticated user

# Testing APIs
The APIs can be tested using:
- Postman
- Thunder Client on VS code

## Author 
Munira Sheikh