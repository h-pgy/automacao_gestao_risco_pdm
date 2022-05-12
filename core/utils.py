import os


def solve_path(child, parent=None):

    if parent:
        child = os.path.join(parent, child)

    return os.path.abspath(child)


def solve_dir(dir_name, parent=None):

    dir_name = solve_path(dir_name, parent)

    if not os.path.exists(dir_name):

        os.mkdir(dir_name)

    return os.path.abspath(dir_name)

def list_files(dir_name, extension=None):

    if extension.startswith('.'):
        extension = extension[1:]

    content = os.listdir(solve_dir(dir_name))
    if extension:
        content = [f for f in content if f.split('.')[-1] == extension]
    
    return [solve_path(f, dir_name) for f in content]