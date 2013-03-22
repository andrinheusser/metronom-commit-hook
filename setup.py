#!/usr/bin/python

import os
import shutil


def shell(commands):
    for c in commands.splitlines():
        if not c:
            continue
        print c
        os.system(c)

cwd = os.getcwd()
metronom_baseurl = 'http://metronom.feinheit.ch/'

print 'Welcome to the gitronom setup\n\n'

print 'Project root (absolute path!) [%s]:' % cwd
project_root = raw_input() or cwd

print 'Metronom Base URL [%s]' % metronom_baseurl
metronom_baseurl = raw_input() or metronom_baseurl

print 'Metronom API Key:'
apikey = raw_input()

print 'Metronom Job/Project ID:'
jobid = raw_input()

print 'Copy the postcommit script to %s/.git/hooks/postcommit' % project_root
#shell('cp postcommit %s/.git/hooks/postcommit' % project_root)
shutil.copy2('post-commit', '%s/.git/hooks/post-commit' % project_root)
os.chdir(project_root)
print 'Configure the script...'
shell('git config metronom.baseurl %s' % metronom_baseurl)
shell('git config metronom.apikey %s' % apikey)
shell('git config metronom.job %s' % jobid)
print '''\n
-----------------------------------------
    Setup done.

    Usage:
    git commit -m "nubbel.#0.1#backend"
-----------------------------------------
'''
