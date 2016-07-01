# -*- coding: utf-8 -*- 
__author__ = "ZhangYanguang"

import sys
import click
import time

import utils

@click.command()
@click.option('-m', '--msg')
@click.option('--dry-run', is_flag=True, help=u'输出指令不执行')

def run(**options):
	utils.DRY_RUN = options["dry_run"];
	msg = options['msg']
	log(msg)

#日志
def log(msg):
    print '[%s:%s] %s'%(sys.argv[0],time.strftime('%Y-%m-%d %H:%M:%S'), msg);

if __name__=='__main__':
    run()