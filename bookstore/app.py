from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

categories = [
    {"categoryid": 1, "categoryname": "Horror"},
    {"categoryid": 2, "categoryname": "Fantasy"},
    {"categoryid": 3, "categoryname": "Literary Fiction"},
    {"categoryid": 4, "categoryname": "Non Fiction"},
]

books = [
    # horror
    {
        "title": "A Head Full of Ghosts",
        "author": "Paul Tremblay",
        "isbn": "9780062363244",
        "price": 14.99,
        "categoryid": 1,
        "image": "a_head_full_of_ghosts.jpg",
        "readNow": True,
    },
    {
        "title": "Behind Her Eyes",
        "author": "Sarah Pinborough",
        "isbn": "9781250111173",
        "price": 13.99,
        "categoryid": 1,
        "image": "behind_her_eyes.jpg",
        "readNow": False,
    },
    {
        "title": "Rosemary's Baby",
        "author": "Ira Levin",
        "isbn": "9780451194008",
        "price": 12.99,
        "categoryid": 1,
        "image": "rosemarys_baby.jpg",
        "readNow": False,
    },
    {
        "title": "The Haunting of Hill House",
        "author": "Shirley Jackson",
        "isbn": "9780143039983",
        "price": 11.99,
        "categoryid": 1,
        "image": "the_haunting_of_hill_house.jpg",
        "readNow": True,
    },

    # fantasy
    {
        "title": "Piranesi",
        "author": "Susanna Clarke",
        "isbn": "9781635575637",
        "price": 16.99,
        "categoryid": 2,
        "image": "piranesi.jpg",
        "readNow": True,
    },
    {
        "title": "Babel",
        "author": "R. F. Kuang",
        "isbn": "9780063021426",
        "price": 19.99,
        "categoryid": 2,
        "image": "babel.jpg",
        "readNow": False,
    },
    {
        "title": "American Gods",
        "author": "Neil Gaiman",
        "isbn": "9780062472106",
        "price": 17.99,
        "categoryid": 2,
        "image": "american_gods.jpg",
        "readNow": False,
    },
    {
        "title": "The Night Circus",
        "author": "Erin Morgenstern",
        "isbn": "9780307744432",
        "price": 15.99,
        "categoryid": 2,
        "image": "the_night_circus.jpg",
        "readNow": False,
    },

    # literary fiction
    {
        "title": "Greek Lessons",
        "author": "Han Kang",
        "isbn": "9780593305485",
        "price": 17.00,
        "categoryid": 3,
        "image": "greek_lessons.jpg",
        "readNow": False,
    },
    {
        "title": "A Month in the Country",
        "author": "J. L. Carr",
        "isbn": "9780940322479",
        "price": 14.00,
        "categoryid": 3,
        "image": "a_month_in_the_country.jpg",
        "readNow": True,
    },
    {
        "title": "On Earth We're Briefly Gorgeous",
        "author": "Ocean Vuong",
        "isbn": "9780525562047",
        "price": 18.00,
        "categoryid": 3,
        "image": "on_earth_were_briefly_gorgeous.jpg",
        "readNow": False,
    },
    {
        "title": "Normal People",
        "author": "Sally Rooney",
        "isbn": "9781984822178",
        "price": 17.00,
        "categoryid": 3,
        "image": "normal_people.jpg",
        "readNow": False,
    },

    # nonfiction
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "isbn": "9781594631931",
        "price": 18.00,
        "categoryid": 4,
        "image": "the_kite_runner.jpg",
        "readNow": False,
    },
    {
        "title": "Midnight in the Garden of Good and Evil",
        "author": "John Berendt",
        "isbn": "9780679751526",
        "price": 17.00,
        "categoryid": 4,
        "image": "midnight_in_the_garden_of_good_and_evil.jpg",
        "readNow": False,
    },
    {
        "title": "The Lady Tasting Tea",
        "author": "David Salsburg",
        "isbn": "9780805071344",
        "price": 16.00,
        "categoryid": 4,
        "image": "the_lady_tasting_tea.jpg",
        "readNow": False,
    },
    {
        "title": "The Devil in the White City",
        "author": "Erik Larson",
        "isbn": "9780375725609",
        "price": 18.99,
        "categoryid": 4,
        "image": "the_devil_in_the_white_city.jpg",
        "readNow": False,
    },
]

# set up routes
@app.route('/')
def home():
    return render_template("index.html", categories=categories)

@app.route('/category/<int:categoryid>')
def category(categoryid):
    selected_books = [b for b in books if b["categoryid"] == categoryid]
    return render_template("category.html", selectedCategory=categoryid, categories=categories, books=selected_books)

@app.route('/search', methods=['POST'])
def search():
    term = request.form.get("search", "").strip().lower()
    if not term:
        return redirect(url_for("home"))

    matched_books = [b for b in books if term in b["title"].lower()]

    return render_template("category.html", categories=categories, books=matched_books, selectedCategory=None)

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template

if __name__ == "__main__":
    app.run(debug = True)
