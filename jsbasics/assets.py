

def refine_STATICS(original):
    original['GENERAL']['js']['files'] += [
        'jquery/js/jquery-1.12.4.min.js',
        'jquery/js/jquery.migrate.1.4.1.min.js',
        'jquery/js/jquery-ui.1.11.4.min.js',
        'jquery/js/jquery.mobile.custom.min.js',
        'jquery/js/django-csrf.js',
        'underscore-min.js',
        'js.cookie.min.js',

        # select2
        'select2/4.0.3/select2.min.js',
        'select2/4.0.3/de.js',
    ]

    original['GENERAL']['css']['files'] += [
        'select2/4.0.3/select2.min.css',
    ]

    return original
