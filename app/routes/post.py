from flask import Blueprint, render_template, redirect, request
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)


@post.route('/')
def all():
    posts = Post.query.all()
    return render_template('post/all.html', posts=posts)

@post.route('/post/create', methods=['GET', 'POST'])
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
