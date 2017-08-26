#!/usr/bin/python3

"""sendig files to two different web servers"""

import os
import time
from fabric.api import local, hosts, env, run, put
env.use_ssh_config=True
env.hosts = ["66.70.187.58", "54.221.183.295"]


def do_deploy(archive_path):
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_arc = archive_path.split("/")[-1]
        new_dir = ("/data/web_static/releases/" + new_arc.split(".")[0])
        new_path = "/tmp/" + archive
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releass/{}/".format(new_dir))
        run("sudo tar -xzf /tmp/{} -C /{}/{}/".format(new_arc,new_path,new_dir))
        run("sudo rm -rf" + new_path)
        run("sudo mv" + new_arc + "web_static/*" + new_dir)
        run("sudo rm -rf" + new_dir + "web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_dir))
        return True
    except:
        return False
