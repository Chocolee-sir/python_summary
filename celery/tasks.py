#!/usr/bin/env python
__author__ = 'Chocolee'

from celery import Celery

app = Celery('tasks',
             broker='redis://192.168.31.100',
             backend='redis://192.168.31.100')

@app.task
def add(x,y):
    print("running...",x,y)
    return x+y