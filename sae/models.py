from flask import current_app
from sae import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    characters = db.relationship('Character', backref='author', lazy=True)

    def __repr__(self):
        return f'User("{self.username}, {self.email}")'

association_table = db.Table('attacks',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True),
    db.Column('attack_id', db.Integer, db.ForeignKey('attack.id'), primary_key=True)
)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(100), nullable=False)
    character_class = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    background = db.Column(db.String(100), nullable=False)
    player_name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(100), nullable=False)
    alignment = db.Column(db.String(100), nullable=False)
    exp = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    inspiration = db.Column(db.Boolean, nullable=False)
    prof = db.Column(db.Integer, nullable=False)
    st_str = db.Column(db.Boolean, nullable=False)
    st_dex = db.Column(db.Boolean, nullable=False)
    st_con = db.Column(db.Boolean, nullable=False)
    st_wis = db.Column(db.Boolean, nullable=False)
    st_int = db.Column(db.Boolean, nullable=False)
    st_cha = db.Column(db.Boolean, nullable=False)
    acrobatics = db.Column(db.Boolean, nullable=False)
    animal_handling = db.Column(db.Boolean, nullable=False)
    arcana = db.Column(db.Boolean, nullable=False)
    athletics = db.Column(db.Boolean, nullable=False)
    deception = db.Column(db.Boolean, nullable=False)
    history = db.Column(db.Boolean, nullable=False)
    insight = db.Column(db.Boolean, nullable=False)
    intimidation = db.Column(db.Boolean, nullable=False)
    investigation = db.Column(db.Boolean, nullable=False)
    medicine = db.Column(db.Boolean, nullable=False)
    nature = db.Column(db.Boolean, nullable=False)
    perception = db.Column(db.Boolean, nullable=False)
    performance = db.Column(db.Boolean, nullable=False)
    persuation = db.Column(db.Boolean, nullable=False)
    religion = db.Column(db.Boolean, nullable=False)
    sleight_of_hand = db.Column(db.Boolean, nullable=False)
    stealth = db.Column(db.Boolean, nullable=False)
    survival = db.Column(db.Boolean, nullable=False)
    armor_class = db.Column(db.Integer, nullable=False)
    initiative = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    hp_max = db.Column(db.Integer, nullable=False)
    hp_current = db.Column(db.Integer, nullable=False)
    hp_temp = db.Column(db.Integer, nullable=False)
    hd_total = db.Column(db.String(100), nullable=False)
    hd_current = db.Column(db.Integer, nullable=False)
    ds_success1 = db.Column(db.Integer, nullable=False)
    ds_success2 = db.Column(db.Integer, nullable=False)
    ds_success3 = db.Column(db.Integer, nullable=False)
    ds_failure1 = db.Column(db.Integer, nullable=False)
    ds_failure2 = db.Column(db.Integer, nullable=False)
    ds_failure3 = db.Column(db.Integer, nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    sp = db.Column(db.Integer, nullable=False)
    ep = db.Column(db.Integer, nullable=False)
    gp = db.Column(db.Integer, nullable=False)
    pp = db.Column(db.Integer, nullable=False)
    equipment = db.Column(db.Text, nullable=False)
    personality  = db.Column(db.Text, nullable=False)
    ideals = db.Column(db.Text, nullable=False)
    bonds = db.Column(db.Text, nullable=False)
    flaws = db.Column(db.Text, nullable=False)
    features_traits = db.Column(db.Text, nullable=False)
    other_prof_lang = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    attacks = db.relationship('Attack', secondary=association_table, lazy='subquery',
        backref=db.backref('characters', lazy=True))

    def __repr__(self):
        return f'Character("{self.character_name}")'



class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    atk_bonus = db.Column(db.Integer, nullable=False)
    dmg = db.Column(db.String(100), nullable=False)