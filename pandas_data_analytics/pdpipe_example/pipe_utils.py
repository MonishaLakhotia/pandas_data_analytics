import os


def set_full_paths(config, directory):
    for key, value in config['file_locations'].items():
        config['file_locations'][key] = os.path.join(directory, value)


def size(n):
    if n <= 4:
        return 'Small'
    elif 4 < n <= 6:
        return 'Medium'
    else:
        return 'Big'


def toInt(f):
    return int(f)
