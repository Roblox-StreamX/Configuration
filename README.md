# StreamX/Configuration

### Information

This is the repository for the StreamX Configuration Server, a very simple Python-powered configuration hosting server. It is intended for multi-server setups, and is not recommended for use in a single-server StreamX setup.  

Please note: the server currently uses [Flask](https://flask.palletsprojects.com/en/2.2.x/), which is not ideal. It will be migrated to [aiohttp](https://docs.aiohttp.org/en/stable/) soon.

### Installation

To fetch the latest dev build, fetch directly from Github:
```sh
git clone https://github.com/Roblox-StreamX/Configuration
cd Configuration
python3 -m pip install -r reqs.txt
```

Alternatively, download the latest binary from [Github Releases](https://github.com/Roblox-StreamX/Configuration/releases):
```sh
wget https://github.com/Roblox-StreamX/Configuration/releases/latest/download/configserver
```

---

You can now either run the server manually by executing `python3 launch.py` (or `configserver`).  
If preferred, you can setup a systemd config file:
```
# /lib/systemd/system/streamx-config.service
[Unit]
Description=StreamX Configuration Server
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=python3 /path/to/launch.py

# If using a compiled binary:
#ExecStart=/path/to/configserver

# You can optionally change the binding host and port:
#Environment="HOST=localhost"
#Environment="PORT=8080"

[Install]
WantedBy=multi-user.target
```
Then you can simply:
```sh
sudo systemctl daemon-reload
sudo systemctl enable streamx-config
sudo systemctl start streamx-config
```

### Configuration

The configuration sent to all StreamX servers is contained inside `config.json`, expected to be inside the same folder as `launch.py` (or `configserver` if using the binary). Most options are **NOT** optional, and required for delivery to actually launch.  

Here are the available config options:
- `mongo` (dictionary)    -- Everything MongoDB related
    - `username` (string) -- The MongoDB authentication username
    - `password` (string) -- The MongoDB authentication password
    - `address` (string) -- Address of MongoDB instance(s), can be comma seperated
- `webhook_url` (string) -- Discord webhook URL for 401's and other logging messages

And an example configuration:
```json
{
    "mongo": {
        "username": "StreamX",
        "password": "super secure password",
        "address": "localhost"
    },
    "webhook_url": "https://discordapp.com/api/webhooks/abc/xyz123"
}
```