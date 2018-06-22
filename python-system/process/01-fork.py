#!/usr/env python
#_*_ coding:utf-8 _*_

import os
import time
ret = os.fork()

if ret == 0:
	while True:
		print("--1--")
		print("--1--")
		print("--1--")
		time.sleep(1)
else:
	while True:
		print("--2--")
		time.sleep(1)
