# coding: utf-8
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

import mercury
import threading
import time
import pickle

from datetime import datetime

def print_msg(msg):
    """
    Customized message handler
    :param msg:
    :return:
    """
    print("{} print_msg: {}".format(datetime.now(),msg))

def publish_msg(mercury_app):
    for i in range(0, 10):
        time.sleep(1)
        msg= {"content": i}
        mercury_app.publish(
            "mercury.pub",
            msg
        )

mercury_app = mercury.MercuryApp()

mercury_app.subscribe(channel="mercury.pub")

t = threading.Thread(target=publish_msg, args=(mercury_app,), daemon=True)
t.start()

# add a handler to handle messages from channel: mercury.pub
mercury_app.add_handler("mercury.pub", print_msg)

# To test if it's a singleton
mercury_app_2 = mercury.MercuryApp()
print(mercury_app, mercury_app_2)

mercury_app_2.start()

while True:
    time.sleep(10)