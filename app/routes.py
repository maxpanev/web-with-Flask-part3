from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')

        post = {
            'title': f"{name}, {age} года",
            'content': f"Город: {city}. Хобби: {hobby}"
        }

        posts.append(post)
        return redirect(url_for('index'))

    return render_template('blog.html', posts=posts)