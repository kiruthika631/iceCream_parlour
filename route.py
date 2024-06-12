from flask import render_template, request, redirect, url_for # type: ignore
from app import app, db
from app.models import SeasonalFlavor, Ingredient, CustomerSuggestion, Allergen, Cart

@app.route('/')
def index():
    flavors = SeasonalFlavor.query.all()
    return render_template('index.html', flavors=flavors)

@app.route('/cart')
def cart():
    cart_items = Cart.query.all()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/manage')
def manage():
    flavors = SeasonalFlavor.query.all()
    return render_template('manage.html', flavors=flavors)

@app.route('/add_to_cart/<int:flavor_id>')
def add_to_cart(flavor_id):
    cart_item = Cart(flavor_id=flavor_id, quantity=1)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/allergens', methods=['GET', 'POST'])
def allergens():
    if request.method == 'POST':
        allergen_name = request.form['allergen']
        if not Allergen.query.filter_by(name=allergen_name).first():
            new_allergen = Allergen(name=allergen_name)
            db.session.add(new_allergen)
            db.session.commit()
        return redirect(url_for('allergens'))
    allergens = Allergen.query.all()
    return render_template('allergens.html', allergens=allergens)
