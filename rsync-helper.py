#!/usr/bin/python
import threading,sys,os,time
rsync_output = ""

def start_rsync():
    os.system("dmesg -C")
    rsync_output = os.popen("rsync -av --progress --delete --ignore-errors --exclude-from '/tmp/exclude_list' /mnt/damageddisk/data /backup/data > /tmp/.output 2>&1 ").read()

def check_logs():
    flag = 1
    while flag:
      output = os.popen("dmesg | grep -i 'I/O error' ").read()
      if output:
          os.system("killall rsync")
          print "Killing rsync"
          filename = os.popen("cat /tmp/.output | grep -viE 'xfer|rsync|kB\/s|mb\/s|incremental' | tail -n 1").read()
          print filename
          os.popen("echo '{0}' >> /tmp/exclude_list".format(filename))
          break;

threading.Thread(target=start_rsync).start()
threading.Thread(target=check_logs).start()
