# -*- coding: utf-8 -*- 
__author__ = "ZhangYanguang"

import sys
import subprocess
import time
import log

DRY_RUN = False

#执行Shell命令，执行成功时返回输出结果
def runShell(cmd, noRet=True):
    log.log(cmd);
    if not DRY_RUN:
        if noRet:
            return subprocess.check_output(cmd, shell=True);
        else:
            subprocess.check_call(cmd, shell=True);

