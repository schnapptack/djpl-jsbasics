

def refine_STATICS(original):
    original['PUBLIC']['js']['files'] += [
        'jquery/js/jquery-1.9.1.js',
        'jquery/js/jquery.migrate.1.3.0.js',
        'jquery/js/jquery-ui-1.10.1.js',
        'jquery/js/django-csrf.js',
        'underscore-min.js',
    ]
    return original
