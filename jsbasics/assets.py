

def refine_STATICS(original):
    original['GENERAL']['js']['files'] += [
        'jquery/js/jquery-3.1.1.min.js',
        'jquery/js/jquery-migrate-3.0.0.min.js',
        'jquery/js/jquery-ui.1.12.1.min.js',
        'jquery/js/jquery.mobile.custom.min.js',
        'jquery/js/django-csrf.js',
        'underscore-min.js',
        'js.cookie.min.js',
        'jquery.mjs.nestedSortable.js',


        # select2
        'select2/4.0.3/select2.min.js',
        'select2/4.0.3/de.js',
    ]

    original['GENERAL']['css']['files'] += [
        'select2/4.0.3/select2.min.css',
    ]

    return original
