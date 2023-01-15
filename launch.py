# Copyright 2022 iiPython

# Modules
import os
import sys
import json
from flask import Flask

# Initialization
tdir = os.path.dirname(__file__ if not getattr(sys, "frozen", False) else sys.executable)
config_file = os.path.join(tdir, "config.json")
if not os.path.isfile(config_file):
    sys.exit("Missing configuration file!")

with open(config_file, "r") as fh:
    data = json.loads(fh.read())

# Flask init
app = Flask("StreamX Configuration")

@app.route("/", methods = ["GET"])
def send_config() -> None:
    return data

# Launch server
if __name__ == "__main__":
    app.run(
        host = os.getenv("HOST", "0.0.0.0"),
        port = os.getenv("PORT", "4070")
    )
