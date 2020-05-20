from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from sae import db
from sae.models import Character
from sae.characters.forms import CharacterForm

characters = Blueprint("characters", __name__)

@characters.route("/character/new")
@login_required
def new_character():
    user = current_user
    form = CharacterForm()
    if form.validate_on_submit():
        #filling the table with values
        character = Character(character_name=form.character_name,
                            character_class=form.character_class,
                            level=form.level,
                            background=form.background,
                            player_name=form.player_name,
                            race=form.race,
                            alignment=form.alignment,
                            exp=form.exp,
                            strength=form.strength,
                            dexterity=form.dexterity,
                            constitution=form.constitution,
                            wisdom=form.wisdom,
                            intelligence=form.intelligence,
                            charisma=form.charisma,
                            inspiration=form.inspiration,
                            prof=form.prof,
                            st_str=form.st_str,
                            st_dex=form.st_dex,
                            st_con=form.st_con,
                            st_wis=form.st_wis,
                            st_int=form.st_int,
                            st_cha=form.st_cha,
                            acrobatics=form.acrobatics,
                            animal_handling=form.animal_handling,
                            arcana=form.arcana,
                            athletics=form.athletics,
                            deception=form.deception,
                            history=form.history,
                            insight=form.insight,
                            intimidation=form.intimidation,
                            investigation=form.investigation,
                            medicine=form.medicine,
                            nature=form.nature,
                            perception=form.perception,
                            performance=form.performance,
                            persuation=form.persuation,
                            religion=form.religion,
                            sleight_of_hand=form.sleight_of_hand,
                            stealth=form.stealth,
                            survival=form.survival,
                            armor_class=form.armor_class,
                            initiative=form.initiative,
                            speed=form.speed,
                            hp_max=form.hp_max,
                            hp_current=form.hp_current,
                            hp_temp=form.hp_temp,
                            hd_total=form.hd_total,
                            hd_current=form.hd_current,
                            ds_success1=form.ds_success1,
                            ds_success2=form.ds_success2,
                            ds_success3=form.ds_success3,
                            ds_failure1=form.ds_failure1,
                            ds_failure2=form.ds_failure2,
                            ds_failure3=form.ds_failure3,
                            cp=form.cp,
                            sp=form.sp,
                            ep=form.ep,
                            gp=form.gp,
                            pp=form.pp,
                            equipment=form.equipment,
                            personality=form.personality,
                            ideals=form.ideals,
                            bonds=form.bonds,
                            flaws=form.flaws,
                            features_traits=form.features_traits,
                            other_prof_lang=form.other_prof_lang,
                            user_id=user.id
                            )
        #adding the table to the db                                                                                                                                                                                  Ich hasse mein Leben
        db.session.add(character)
        db.session.commit()
        flash("The Character has been created!", "success")
        return redirect(url_for("main.home"))
    return render_template("character_sheet.html", form=form)


@characters.route("/character/<int:character_id>")
@login_required
def character_sheet(character_id):
    user = current_user
    character = Character.query.filter_by(id=character_id).first_or_404()
    if character.author.id is not user.id:
        flash("You do not have access to this Character", "danger")
        return redirect(url_for("main.home"))
    return redirect(url_for(characters))
    form = Characterform()
