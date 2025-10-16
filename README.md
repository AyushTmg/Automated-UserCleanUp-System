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






