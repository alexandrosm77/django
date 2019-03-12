Welcome to the AWS CodeStar sample web application
==================================================

This application has been bootstrapped using a pre built Django 1.11 template on AWS Codestart

To run the application locally, you need virtualenv installed (https://virtualenv.pypa.io/en/latest/)

1. Create a Python virtual environment for your Django project. This virtual
   environment allows you to isolate this project and install any packages you
   need without affecting the system Python installation. At the terminal, type
   the following command:

        $ virtualenv .venv

2. Activate the virtual environment:

        $ activate ./venv/bin/activate

3. Install Python dependencies for this project:

        $ pip install -r requirements.txt

4. Run migrations (will use a local sqlite db)

        $ python manage.py migrate

5. Start the Django development server:

        $ python manage.py runserver

6. Open http://127.0.0.1:8000/ in a web browser to view your application.



Spent about 6-8 hours on this project, as I had to do some research on Django's Class Based Views (CBV) which I haven't used before.
Overall experience with CBVs is that they will save all of time when writing simple applications.

The app is using internal Django's template as front end
