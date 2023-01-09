# Copyright 2022 iiPython

# Modules
import os
import json
from flask import Flask

# Initialization
config_file = os.path.join(os.path.dirname(__file__), "config.json")
if not os.path.isfile(config_file):
    exit("Missing configuration file!")

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
