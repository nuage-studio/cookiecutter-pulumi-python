import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    print("DELETING", filepath)


if __name__ == '__main__':

    if '{{cookiecutter.use_base_class}}' != 'yes':
        remove_file(os.path.join('{{cookiecutter.project_slug|snakecase}}/base_dynamic_provider.py'))
