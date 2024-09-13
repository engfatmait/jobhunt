"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from jobhunt import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html', title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/job-list')
def joblist():
    """Renders the contact page."""
    return render_template(
        'job-list.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/job-detail')
def jobdetail():
    """Renders the contact page."""
    return render_template(
        'job-detail.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
