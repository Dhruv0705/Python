# Create Django Project
    # django-admin startproject (name of project)

# Server Components: 
    # Run Server
        # python manage.py runserver

    # Create Admin Account
        # python manage.py createsuperuser

    # Package Model Changes
        # python manage.py makemigrations {foldername}

    # Sync All Changes In Projects to database
        # python manage.py migrate

    # ERROR: "no such table" / fix db Run:
        # python manage.py migrate --run-syncdb

# App Components: 
    # Create Admin User Account
        # python manage.py createsuperuser

    # Create NEW Custom App In Directory
        # python manage.py startapp (app name)

# Create Product Objects
    # Python Shell
        # python manage.py shell

    # Import Object Module App
        # from {foldername.models} import {Class}
        # {Class}.objects.all()

    # Create New Objects
        # {Class}.objects.create()        
