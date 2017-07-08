# Flask Project Template

Fork from [cookiecutter](https://github.com/wdm0006/cookiecutter-flask)

依个人口味对原项目做了部分修改

Use it now
----------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/yzongyue/cookiecutter-flask.git
    $ cd yourproject && pip install requirements.txt
    or
    $ docker-compose up

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

 * Bootstrap 3 and Font Awesome 4 with starter templates
 * 3 Bootstrap themes included (standard, dark, and paper)
 * Flask-SQLAlchemy with basic User model
 * Easy database migrations with Flask-Migrate
 * Flask-WTForms with login and registration forms
 * Flask-Mail for forgotten password emails
 * Username/Password reset and unsubscribe functionality baked in
 * Flask-Login for authentication
 * Flask-Bcrypt for password hashing
 * Out-of-the-box ready for deploying to a PaaS (e.g. Heroku)
 * pytest and Factory-Boy for testing (example tests included)
 * A simple ``manage.py`` script.
 * CSS and JS minification using Flask-Assets
 * Caching using Flask-Cache
 * Useful debug toolbar
 * sitemap.xml and robots.txt built in
 * Utilizes best practices: [Blueprints](http://flask.pocoo.org/docs/blueprints/) and [Application Factory](http://flask.pocoo.org/docs/patterns/appfactories/) patterns


Inspiration
-----------

- [Sloria](https://github.com/sloria/cookiecutter-flask.git)
- [wdm0006](https://github.com/wdm0006/cookiecutter-flask.git)

License
-------

BSD licensed.