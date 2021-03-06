#!/usr/bin/env python

import subprocess
import sys
import time


def grep_log_for_start_cmd(container_id):
    return "docker logs %s 2>&1 | grep 'Jenkins is fully up and running'" % container_id


def started(container_id):
    grep_cmd = grep_log_for_start_cmd(container_id)
    try:
        result = subprocess.check_output(grep_cmd, shell=True)
        return bool(result and result.strip())
    except subprocess.CalledProcessError:
        return False


def wait_till_started(container_id):
    while not started(container_id):
        sys.stdout.write('.')
        time.sleep(1)
    print('Done.')


def main():
    if len(sys.argv) != 3:
        sys.exit("expected 2 arguments, got %d" % (len(sys.argv) - 1))
    container_id = sys.argv[1]
    jenkins_port = sys.argv[2]
    try:
        wait_till_started(container_id)
        print "Jenkins running at http://%s" % jenkins_port
    except:
        print sys.exc_info()[0]
        sys.exit(1)

main()
