#!/usr/bin/env python
from __future__ import with_statement

import os
import time
import subprocess

from datetime import datetime as dt
from datetime import timedelta
from socket import gethostname

HOST = gethostname()

def run(command):
    proc = subprocess.Popen(command,
                            shell=True,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    return "\n".join(proc.communicate())

def write_log(fname, data, number):
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    path = "logs/%s-%s.log" % (HOST, fname)
    with open(path, 'a') as f:
        f.write("\n\nRun: %s\nDate: %s\n\n" % (number, dt.now()))
        f.write(data)
    os.system("git add %s" % path)


if __name__ == "__main__":
    u_cmd = "cd unixbench-5.1.2 && time ./Run"

    start = dt.now()
    for i in range(1, 10000):
        print "Running %s" % i

        write_log('unix_benchmark', run(u_cmd), i)

        os.system('git pull')
        os.system('git commit -m "Logging run %s (%s)"' % (i, HOST))
        # os.system('git push')

        while dt.now() - start < timedelta(hours=3):
            time.sleep(10)
        start = dt.now()
