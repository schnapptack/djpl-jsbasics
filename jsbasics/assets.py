

def refine_STATICS(original):
    original['PUBLIC']['js']['files'] += [
        'jquery/js/jquery-1.12.4.min.js',
        'jquery/js/jquery.migrate.1.4.1.min.js',
        'jquery/js/jquery-ui.1.11.4.min.js',
        'jquery/js/jquery.mobile.custom.min.js',
        'jquery/js/django-csrf.js',
        'underscore-min.js',
        'js.cookie.min.js',
    ]
    return original
