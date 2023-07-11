from fabric.api import *

def host_type():
    run('uname -s')

def say_Hello(name="World"):
    print("Hello {}".format(name))
