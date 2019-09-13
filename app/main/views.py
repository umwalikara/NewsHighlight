from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
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