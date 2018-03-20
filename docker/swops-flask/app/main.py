# pylint: disable=missing-docstring,invalid-name,

import time
import ctypes
import random
from flask import Flask  # pylint: disable=import-error

#left obvious http request bugs unfixed to demonstrate kibana/lb
#print to stdout to capture alongside nginx output

app = Flask(__name__, static_folder="static")


@app.route("/health")
def health():
    print("SWOPSFLASK-Condition: 05 invalid response")
    return None


@app.route("/")
def root():
    value = random.random()
    print("value: " + str(value))

    if value > .9:
        print("SWOPSFLASK-Condition: 02 invalid string")
        return str(None / 1)

    if value < .1:
        pointer = ctypes.pointer(ctypes.c_char.from_address(5))
        pointer[0] = "5"
        print("SWOPSFLASK-Condition: 03 invalid format func")
        return "Type of value is now {}".format(type(5))

    if value > .2 or value < .5:
        randInt = random.randint(0, 3)
        print("SWOPSFLASK-Condition: 04 sleeping " + str(randInt) )
        time.sleep(randInt)

    print("SWOPSFLASK-Condition: 01 success")
    return "Hello, world!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
