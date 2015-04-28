#coding: utf-8
from fabric.api import *
import time
import sys
import ast
env.use_ssh_config = True

env_variables="-e RAILS_ENV=production"

def docker_tag(tag):
    return "ductoanle/saleswhale_doc" + ":" + tag

@task
@hosts('arsene.local')
def deploy(dockerTag=None, codeTag=None):
    if dockerTag is None:
        print("You must give a docker tag to deploy")
        sys.exit()
    if codeTag is None:
        codeTag = "master"

    with settings(warn_only=True):
        if "cannot" in run ("ls ~/.dockercfg"):
            run("docker login")

    with settings(warn_only=True):
        print("Bring down docker with name saleswhale_doc")
        run("docker rm -f saleswhale_doc")

    run("docker run --name saleswhale_doc -t -e BRANCH=%s %s -p 4567:4567 %s" % (codeTag, env_variables, docker_tag(dockerTag)))
