import os

from fabric.api import *

# Set this before dragonfab imports, because it will then set up logging for you
env.DEBUG=False

# This is needed for allowing fabric to be run anywhere in the project directory structure
env.local_dir = os.path.dirname(__file__)

# This will make all environments available as root fabric commands
from dragonfab.env import *
# Utilities for deb building and deployment
from dragonfab import deb

# Package dir specifies where .deb file will go
env.package_dir = os.path.join(env.local_dir, '..')

# This is the name of the deb pacakage that will be built, and where it ends up
env.package_name = 'exampleapp'


@task
def init():
    """ Perform initial server setup if necessary/desired """
    local("python setup.py bdist_wheel")


@task
def test():
    """ Run all tests """
    with prefix("workon lavender"):
        pass


@task
def deploy():
    """ Full deployment """
    put('dist/lavender-1.0-py27-none-any.whl', '/tmp')
    with prefix("source /home/deployhub/.virtualenvs/lavender/bin/activate"):
        run("pip install /tmp/lavender-1.0-py27-none-any.whl")
