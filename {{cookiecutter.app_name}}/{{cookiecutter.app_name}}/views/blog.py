# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, flash, url_for, send_from_directory, make_response,
                   redirect, current_app)
import datetime

from flask_login import login_user, login_required, logout_user

from myflaskapp.extensions import login_manager
from myflaskapp.models.user import User
from myflaskapp.forms.public import LoginForm
from myflaskapp.utils import flash_errors, render_extensions
from myflaskapp.database import db

blueprint = Blueprint('blog', __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@blueprint.route("/blog/<page>/", methods=["GET", "POST"])
def blog_page(page=None):
    """

    :param page:
    :return:
    """
    page = int(page)
    _num_posts = 3
    if page is None:
        start = 0
        end = start + _num_posts
        next_page = 0
        prev_page = 1
        current = True
    else:
        start = _num_posts * page
        end = start + _num_posts
        if page > 0:
            next_page = page - 1
            prev_page = page + 1
            current = False
        else:
            next_page = 0
            prev_page = 1
            current = True

    posts = [
        {'id': 1, 'title': 'Blog Post 1', 'author': 'Will M.', 'date': '2015-10-01 12:00', 'slug': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore, veritatis, tempora, necessitatibus inventore nisi quam quia repellat ut tempore laborum possimus eum dicta id animi corrupti debitis ipsum officiis rerum.'},
        {'id': 2, 'title': 'Blog Post 2', 'author': 'Will M.', 'date': '2015-10-01 12:00', 'slug': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore, veritatis, tempora, necessitatibus inventore nisi quam quia repellat ut tempore laborum possimus eum dicta id animi corrupti debitis ipsum officiis rerum.'},
        {'id': 3, 'title': 'Blog Post 3', 'author': 'Will M.', 'date': '2015-10-01 12:00', 'slug': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore, veritatis, tempora, necessitatibus inventore nisi quam quia repellat ut tempore laborum possimus eum dicta id animi corrupti debitis ipsum officiis rerum.'}
    ]
    return render_extensions("blog/blog_page.html", posts=posts, next_page=next_page, prev_page=prev_page, current=current)


@blueprint.route("/post_detail/<pk>/", methods=["GET", "POST"])
def blog_detail(pk):
    """

    :param pk:
    :return:
    """

    post = {
        'id': 1,
        'title': 'Blog Post 1',
        'author': 'Will M.',
        'date': '2015-10-01 12:00',
        'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore, veritatis, tempora, necessitatibus inventore nisi quam quia repellat ut tempore laborum possimus eum dicta id animi corrupti debitis ipsum officiis rerum.'
    }

    return render_extensions("blog/blog_detail.html", post=post)