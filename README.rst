cookiecutter-flask (plus some stuff)
====================================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. image:: https://travis-ci.org/sloria/cookiecutter-flask.svg
    :target: https://travis-ci.org/sloria/cookiecutter-flask
    :alt: Build Status

Modified from the version authored by Github user: sloria at https://github.com/sloria/cookiecutter-flask.git

Goals
-----

The primary goal is to have a different logical split of files (models, views and services instead of public, user, etc), which
is purely personal preference.

Secondary is a slight expansion in scope to include other common pages and functionality, including:

- Forgotten password handling
- Username change
- Password change
- Unsubscribe
- Basic admin
- Contact forms
- Blog page (possibly)
- Google Analytics Integration
- Etc.

A live example can be found here: `CookieCutter Flask Demo <https://cookiecutterflask.herokuapp.com>`_


Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/wdm0006/cookiecutter-flask.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- Bootstrap 3 and Font Awesome 4 with starter templates
- Flask-SQLAlchemy with basic User model
- Easy database migrations with Flask-Migrate
- Flask-WTForms with login and registration forms
- Flask-Mail for forgotten password emails
- Username/Password reset and unsubscribe functionality baked in
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Procfile for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- A simple ``manage.py`` script.
- CSS and JS minification using Flask-Assets
- Optional bower support for frontend package management
- Caching using Flask-Cache
- Useful debug toolbar
- sitemap.xml and robots.txt built in
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns


Inspiration
-----------

- `Sloria <https://github.com/sloria/cookiecutter-flask.git>`_

License
-------

BSD licensed.