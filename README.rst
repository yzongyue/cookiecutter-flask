cookiecutter-flask (plus some stuff)
====================================

A(nother) Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

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

Full example for pushing app to Heroku `here <http://willmcginnis.com/2015/09/28/cookiecutter-flask-and-some-other-stuff/>`_

![screenshot](https://github.com/wdm0006/cookiecutter-flask/blob/master/screenshots/cookiecutterflask.png "Template Screenshot")

Features
--------

- Bootstrap 3 and Font Awesome 4 with starter templates
- 3 Bootstrap themes included (standard, dark, and paper)
- Flask-SQLAlchemy with basic User model
- Easy database migrations with Flask-Migrate
- Flask-WTForms with login and registration forms
- Flask-Mail for forgotten password emails
- Username/Password reset and unsubscribe functionality baked in
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Out-of-the-box ready for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- A simple ``manage.py`` script.
- CSS and JS minification using Flask-Assets
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