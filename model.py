from app import db

class SeasonalFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_name = db.Column(db.String(100), nullable=False)
    allergens = db.Column(db.String(250), nullable=False)

class Allergen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_id = db.Column(db.Integer, db.ForeignKey('seasonal_flavor.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
