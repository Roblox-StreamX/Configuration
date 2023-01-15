# StreamX/Configuration

### Information

This is the repository for the StreamX Configuration Server, a very simple Python-powered configuration hosting server. It is intended for multi-server setups, and is not recommended for use in a single-server StreamX setup.

### Installation

### Configuration

The configuration sent to all StreamX servers is contained inside `config.json`, expected to be inside the root folder. Most options are **NOT** optional, and required for delivery to actually launch.  

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