#        Automated User Clean Up System


## Installation For Server Side

#### 1-  First of all clone this repo

        git clone git@github.com:AyushTmg/Automated-UserCleanUp-System.git


#### 2- Navigate to the server directory
        cd server 

#### 3-Setup a virtual enviroment 

        python -m venv venv


#### 4- Install all dependencies from the requirements.txt in a virtual enviroment


        pip install -r requirements.txt



#### 5-Add .env File or configure example.env

    EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 2525
    DELETE_INACTIVE_USERS_AFTER_DAYS=7
    SECRET_KEY = 'Add your secret key here'
    POSTGRES_DB=your_database_name
    POSTGRES_USER=your_database_user
    POSTGRES_PASSWORD=your_database_password
    POSTGRES_HOST=127.0.0.1
    POSTGRES_PORT=5432
    JOB_RUN_INTERVAL_MINUTES=1


#### 6- Migrate the changes to your database

        python manage.py makemigrations 
        python manage.py migrate

#### 7- Run Application with celery worker and beat

        python manage.py runserver
        celery -A beat worker -l info
        celery -A main worker -l info






## Installation For Client Side

#### 1- Navigate to the client directory
        cd client 

#### 2- Install dependencies
        npm install

#### 3- Run the development server
        npm run dev 

# Design Choices & Project Structure

The project is built with a focus on readability, reusability, and scalability. Each feature 
is organized into separate modules and directories to keep the code clean and easy to follow. 
This structure makes it simple to update or add new features, while keeping the project well-organized and maintainable.

# API Endpoints Documentation

This document provides a brief overview of the available API endpoints and their usage.





## User Authentication & Management

### 1. Register User
- **Endpoint:** `/register/`
- **Method:** POST
- **Description:** Used for user registration. Accepts user details and creates a new user account.

### 2. Login User
- **Endpoint:** `/login/`
- **Method:** POST
- **Description:** Used for user login. Generates JWT access and refresh tokens if credentials are valid; otherwise, returns an error.

### 3. Change Password
- **Endpoint:** `/change-password/`
- **Method:** POST
- **Description:** Used to change the password of a logged-in user. Requires authentication.

### 4. Token Refresh
- **Endpoint:** `/token/refresh/`
- **Method:** POST
- **Description:** Used to refresh the access token using a valid refresh token.






## Cleanup Reports & Actions

### 5. Latest Reports
- **Endpoint:** `/reports/latest/`
- **Method:** GET
- **Description:** Returns a list of cleanup reports, sorted with the most recent reports at the top.

### 6. Manual Cleanup Trigger
- **Endpoint:** `/cleanup/trigger/`
- **Method:** POST
- **Description:** Used to manually trigger a user cleanup process.

---







