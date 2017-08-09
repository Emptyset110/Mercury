# mercury
A multi-processing communication wrapper using redis PUB/SUB

## Installation
```bash
pip install mercury-client
```

## Usage
```python
import mercury

mercury_app = mercury.MercuryApp()

# A MercuryApp class is defined to be a singleton, so
# mercury_app_2 = mercury.MercuryApp() will get you exactly the same instance
# as mercury_app

# The first purpose is to conveniently communicate with other mercury clients.
# Let's set the channel name to be "mercury.pub"
channel = "mercury.pub"

# subscribe a channel
mercury_app.subscribe(channel=channel)

# publish some messages to a redis channel
message = {"error_code": 0, "data": 100}
mercury_app.publish(channel=channel, message=message)
``` 

A Full Demo:
```python
# coding: utf-8
import mercury
import threading
import time

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

mercury_app.start()

while True:
    time.sleep(10)
```

## TODO
- A mercury monitor