from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sae.models import Character

class CharacterForm(FlaskForm):
    character_name = StringField("Character Name", validators=[DataRequired(), Length(min=2, max=20)])
    character_class = StringField("Class", validators=[DataRequired(), Length(min=2, max=20)])
    level = IntegerField("Level", validators=[DataRequired(), Length(min=2, max=20)])
    background = StringField("Background", validators=[DataRequired(), Length(min=2, max=20)])
    player_name = StringField("Payer Name", validators=[DataRequired(), Length(min=2, max=20)])
    race = StringField("Race", validators=[DataRequired(), Length(min=2, max=20)])
    alignment = StringField("Alignment", validators=[DataRequired(), Length(min=2, max=20)])
    exp = IntegerField("Experience Points", validators=[DataRequired(), Length(min=2, max=20)])
    strength = IntegerField("Strength", validators=[DataRequired(), Length(min=2, max=20)])
    dexterity = IntegerField("Dexterity", validators=[DataRequired(), Length(min=2, max=20)])
    constitution = IntegerField("Constitution", validators=[DataRequired(), Length(min=2, max=20)])
    wisdom = IntegerField("Wisom", validators=[DataRequired(), Length(min=2, max=20)])
    intelligence = IntegerField("Intelligence", validators=[DataRequired(), Length(min=2, max=20)])
    charisma = IntegerField("Charisma", validators=[DataRequired(), Length(min=2, max=20)])
    inspiration = BooleanField("Inspiration")
    prof = IntegerField("Proficiency Bonus", validators=[DataRequired(), Length(min=2, max=20)])
    st_str = BooleanField("Strength")
    st_dex = BooleanField("Dexterity")
    st_con = BooleanField("Constitution")
    st_wis = BooleanField("Wisdom")
    st_int = BooleanField("Intelligence")
    st_cha = BooleanField("Charisma")
    acrobatics = BooleanField("Acrobatics")
    animal_handling = BooleanField("Animal Handling")
    arcana = BooleanField("Arcana")
    athletics = BooleanField("Athletics")
    deception = BooleanField("Deception")
    history = BooleanField("History")
    insight = BooleanField("Insight")
    intimidation = BooleanField("Intimidation")
    investigation = BooleanField("Investigation")
    medicine = BooleanField("Medicine")
    nature = BooleanField("Nature")
    perception = BooleanField("Perception")
    performance = BooleanField("Performance")
    persuation = BooleanField("Persuasion")
    religion = BooleanField("Religion")
    sleight_of_hand = BooleanField("Sleight of Hand")
    stealth = BooleanField("Stealth")
    survival = BooleanField("Survival")
    armor_class = IntegerField("Armor Class", validators=[DataRequired(), Length(min=2, max=20)])
    initiative = IntegerField("Initiative", validators=[DataRequired(), Length(min=2, max=20)])
    speed = IntegerField("Speed", validators=[DataRequired(), Length(min=2, max=20)])
    hp_max = IntegerField("Hit Point Maximum", validators=[DataRequired(), Length(min=2, max=20)])
    hp_current = IntegerField("Current Hit Points", validators=[DataRequired(), Length(min=2, max=20)])
    hp_temp = IntegerField("Temporary Hit Points", validators=[DataRequired(), Length(min=2, max=20)])
    hd_total = StringField("Total", validators=[DataRequired(), Length(min=2, max=20)])
    hd_current = StringField("Hit Dice", validators=[DataRequired(), Length(min=2, max=20)])
    ds_success1 = BooleanField("ds_success1")
    ds_success2 = BooleanField("ds_success2")
    ds_success3 = BooleanField("ds_success3")
    ds_failure1 = BooleanField("ds_failure1")
    ds_failure2 = BooleanField("ds_failure2")
    ds_failure3 = BooleanField("ds_failure3")
    cp = IntegerField("CP", validators=[DataRequired(), Length(min=2, max=20)])
    sp = IntegerField("SP", validators=[DataRequired(), Length(min=2, max=20)])
    ep = IntegerField("EP", validators=[DataRequired(), Length(min=2, max=20)])
    gp = IntegerField("GP", validators=[DataRequired(), Length(min=2, max=20)])
    pp = IntegerField("PP", validators=[DataRequired(), Length(min=2, max=20)])
    equipment = TextAreaField("Equipment", validators=[DataRequired()])
    personality  = TextAreaField("Personality", validators=[DataRequired()])
    ideals = TextAreaField("Ideals", validators=[DataRequired()])
    bonds = TextAreaField("Bonds", validators=[DataRequired()])
    flaws = TextAreaField("Flaws", validators=[DataRequired()])
    features_traits = TextAreaField("Features & Traits", validators=[DataRequired()])
    other_prof_lang = TextAreaField("Other Proficiencies and Languages", validators=[DataRequired()])
    submit = SubmitField("Save")