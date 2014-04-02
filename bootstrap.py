#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if "--all" in sys.argv:
        u_dir = "unixbench-5.1.2"
        if not os.path.isdir(u_dir):
            u = "http://www.hermit.org/Linux/Benchmarking/unixbench-5.1.2.tar.gz"
            cmd = "wget %s && tar xzf %s.tar.gz && " + \
                  "patch -p0 -i %s.patch && cd %s && make all"
            os.system(cmd % (u, u_dir, u_dir, u_dir))

    g_dir = "GChartWrapper"
    if not os.path.isdir(g_dir):
        u = "http://google-chartwrapper.googlecode.com/svn/trunk/%s" % g_dir
        os.system("svn co %s" % u)
