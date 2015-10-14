# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, request

from flask_login import login_required, current_user
from {{cookiecutter.app_name}}.utils import flash_errors, render_extensions
from {{cookiecutter.app_name}}.models.post import Post

blueprint = Blueprint('admin', __name__, static_folder="../static")


@blueprint.route("/new_blog", methods=["GET", "POST"])
@login_required
def new_blog():
    if not current_user.is_admin:
        return render_extensions('401.html')

    if request.method == 'POST':
        try:
            content = str(request.form['content'])
        except Exception:
            content = ''

        try:
            slug = str(request.form['slug'])
        except Exception:
            slug = ''

        try:
            title = str(request.form['title'])
        except Exception:
            title = ''

        post = Post(title=title, body=content, slug=slug)
        post.save()

        current_user.posts.append(post)
        current_user.save()

    return render_extensions('admin/new_blog.html')
