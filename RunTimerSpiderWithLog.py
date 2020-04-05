import os
import time
import subprocess

errorlogfile    = f'ErrorLog.log'
ordilogfile     = f'OrdiLog.log'
run_spider_command = 'python3 TimerSpider.py'

current_folder = os.getcwd()  #表示当前所处的文件夹
# this script is used to start spider by shell

def simple_rum_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, encoding='utf-8')
    if p.poll():
        return 1
    p.wait()

def rum_saveshell2log(cmd,ordilogfile,errorlogfile):
    fdout = open(ordilogfile, 'a')
    fderr = open(errorlogfile, 'a')
    p = subprocess.Popen(cmd, stdout=fdout, stderr=fderr, shell=True, encoding='utf-8')
    if p.poll():
        return 1
    p.wait()
    return 0

if __name__ == '__main__':
    print('the steam rank spider is started\nlog recording...')
    simple_rum_cmd(f'cd {current_folder}')
    errorlog_open = open(errorlogfile,'w+')
    errorlog_open.close()
    status = rum_saveshell2log(run_spider_command, ordilogfile, errorlogfile)