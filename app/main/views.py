from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''

	general = get_sources('general')
	# sports_sources = get_sources('sports')
	# technology_sources = get_sources('technology')
	# entertainment_sources = get_sources('entertainment')
	title = "News Highlighter"

	return render_template('index.html',title = title,general=general) #business = sources,sports = sports_sources,technology = technology_sources,entertainment = entertainment_sources)

@main.route('/articles/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = "News articles"

	return render_template('articles.html',title= title,articles = articles)