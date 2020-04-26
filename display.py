import config


def get_warnings(water_level):
    # this is a bit "sketchy" since it relies on the fact that dicts are implicitly ordered in Python 3.6
    for name, bound in config.warning_levels_upper.items():
        if water_level < bound:
            return name


def emojify(string):
    print(string)
    return f'{config.emojis[string]} {string}'