from os import environ

base_config = dict(
    num_demo_participants=1,
    app_sequence=['ios']
    )

SESSION_CONFIGS = [
    dict(base_config,
         name='continuous_ios',
         display_name="Continuous IOS scale",
         ios_type='continuous',
         ),
    dict(base_config,
         name='step_choice_ios',
         display_name="Step-choice IOS scale",
         ios_type='step-choice',
         ),
    dict(base_config,
         name='original_ios',
         display_name="Original IOS scale",
         ios_type='original',
         )
    ]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
    )

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'd5@33)b3zl*a0k^2)j@is=3p9x9yzu1-w)+z5!(1&!8dj7#26('

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
