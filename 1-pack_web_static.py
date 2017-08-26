#!/usr/bin/python3

'''Fabric script that generates a .tgz archive from the contents of'''

# Import Fabric's API module

from Fabric.api import *
from time import strftime

def do_pack():
    make_dir = local("mkdir -p versions")
    time = strftime("%Y%m%d%H%M%S")
    archive = local("tar -cvzf versions/web_static_{}.tgz web_static".format(time))

    if folder is not None:
        return ("versions/web_static.{}".format(time)
    else:
        return None
