from flask import Blueprint, render_template, redirect, request
from flask_login import login_required

from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)


@post.route('/')
def all():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('post/all.html', posts=posts)


@post.route('/post/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        teacher = request.form.get('teacher')
        student = request.form.get('student')
        subject = request.form.get('subject')

        post = Post(teacher=teacher, student=student, subject=subject)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"An error occurred: {e}")
            db.session.rollback()

    else:
        return render_template('post/create.html')


@post.route('/post/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    post = Post.query.get(id)

    if request.method == 'POST':
        post.teacher = request.form.get('teacher')
        post.student = request.form.get('student')
        post.subject = request.form.get('subject')
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"An error occurred: {e}")
            db.session.rollback()
    else:
        return render_template('post/update.html', post=post)


@post.route('/post/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete(id):
    post = Post.query.get(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f"An error occurred: {e}")
        db.session.rollback()
