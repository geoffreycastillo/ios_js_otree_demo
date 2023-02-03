from otree.api import *

author = "Geoffrey Castillo"

doc = """
ios.js oTree demo.
"""


# models
class C(BaseConstants):
    NAME_IN_URL = 'ios'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    # the IOS type is specified in the session config (in settings.py) and saved in the subsession
    # this allows to use the same app for all IOS types or even to change the IOS type mid-experiment
    # if you don't need that you can simply set the IOS type in the Constants above
    # then simply use C.ios_type in the template
    ios_type = models.StringField()


def creating_session(subsession):
    subsession.ios_type = subsession.session.config['ios_type']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ios_distance = models.FloatField()
    ios_overlap = models.FloatField()
    ios_number = models.IntegerField()


# pages
class IOSPage(Page):

    @staticmethod
    def vars_for_template(player):
        ios_type = player.session.config['ios_type']

        return {
            # those are just helpers to make the template work with all IOS types
            'is_ios_continuous': True if ios_type == 'continuous' else False,
            'is_ios_discrete': True if ios_type in ['step-choice', 'original'] else False,
            'is_ios_original': True if ios_type == 'original' else False
            }


class IOSIntro(IOSPage):
    pass


class IOS(IOSPage):
    form_model = 'player'

    @staticmethod
    # again, this is just to make the app work with all IOS types
    # if you know that you'll use, say, only the Continuous IOS scale, you can skip this method
    # and simply add below form_model:
    # form_fields = ['ios_distance', 'ios_overlap']
    def get_form_fields(player):
        form_fields = ['ios_distance', 'ios_overlap']
        if player.session.config['ios_type'] != 'continuous':
            form_fields.append('ios_number')
        return form_fields


page_sequence = [IOSIntro, IOS]
