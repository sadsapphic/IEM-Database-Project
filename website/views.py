from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .forms import SearchForm
from . import current_app
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .plots import plot_preference, compare_iems

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    form = SearchForm()
    search_results = []
    contributors = []
    unique_contributors = []  # Create a new list to store unique contributors
    plot_file = None
    show_compare_search = False

    if form.validate_on_submit():
        cur = current_app.config['DATABASE_CURSOR']

        # Query the main table
        main_query = "SELECT * FROM main WHERE IEM_name ILIKE %s"
        cur.execute(main_query, (f'%{form.search_term.data}%',))
        search_results = cur.fetchall()

        if form.compare_term.data and search_results:
            cur.execute(main_query, (f'%{form.compare_term.data}%',))
            search_results += cur.fetchall()

        # Query the contributors table
        contributors_query = "SELECT contributor, credit FROM contributors WHERE IEM_name ILIKE %s"
        cur.execute(contributors_query, (f'%{form.search_term.data}%',))
        contributors = cur.fetchall()

        if form.compare_term.data and search_results:
            cur.execute(contributors_query, (f'%{form.compare_term.data}%',))
            contributors += cur.fetchall()


        # Remove duplicates from the contributors list
        for contributor in contributors:
            if contributor not in unique_contributors:
                unique_contributors.append(contributor)

        # if there is no result, return an error message
        if len(search_results) == 0:
            flash(f'No results found for "{form.search_term.data}" :(', category='error')

        if len(search_results) > 0:
            show_compare_search = True

        # When the user searches for an IEM, plot the preference curve
        if search_results:
            if form.compare_term.data:
                compare_iems(form.search_term.data, form.compare_term.data)
                plot_file = f'{form.search_term.data}_{form.compare_term.data}.png'
            else:
                plot_preference(form.search_term.data)
                plot_file = f'{form.search_term.data}.png'
        else:
            plot_file = None
        
        #cur.close()

    return render_template("home.html", user=current_user, form=form, search_results=search_results, contributors=unique_contributors, plot_file=plot_file, show_compare_search=show_compare_search)
