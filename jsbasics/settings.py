
def refine_INSTALLED_APPS(original):
    """prepend jsbasics to INSTALLED_APPS"""
    return ['jsbasics'] + list(original)
