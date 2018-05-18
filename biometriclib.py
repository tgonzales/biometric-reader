#!/usr/bin/python3

import threading
import time
import sqlite3
import urllib.request

CMD = 0
STREAM = 'AWAIT'
TMPL = None
TMPLS = []

def run_thread_process():
    global CMD
    while True:
        if CMD == 3:
            ify()
        if CMD == 4:
            vfy()
        if CMD == 5:
            enr()

t = threading.Thread(target=run_thread_process)
t.daemon = True
threads = []

def init():
    global t
    threads.append(t)
    t.start()

def close():
    t._stop()

def run(cmd, data=False):
    global CMD, TMPL
    if cmd == 4:
        TMPL = data
    CMD = cmd

def stream():
    return STREAM

def ify():
    # 1:N
    global CMD, STREAM

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    tmp_list = c.fetchall()

    while True:
        msg = 'IFY: Coloque a mao no sensor > '
        for i in tmp_list:
            STREAM = msg + i[1]

        if CMD == 2:
            break

def vfy():
    # 1:1
    global CMD, TMPL, STREAM
    while True:
        time.sleep(0.2)
        if CMD == 2:
            break

        # compara TMPL com biometric
        STREAM = 'VFY: Coloque a mao no sensor ' + TMPL

def enr():
    global CMD, STREAM
    while True:
        #time.sleep(0.2)
        if CMD == 2:
            break
        STREAM = 'ENR: Coloque a mao no sensor '
