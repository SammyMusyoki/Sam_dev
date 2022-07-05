from flask import Blueprint, render_template

views = Blueprint("views", __name__)



@views.route('/')
def home():
    return render_template('index.html')

@views.route('/Portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')


@views.route('/Contact')
def contact():
    return render_template('contact.html')

@views.route('/Resume')
def resume():
    return render_template('resume.html')

@views.route('/Portfolio')
def portfolio():
    return render_template('portfolio.html')


