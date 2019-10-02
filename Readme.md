# CYBER

Displays a website with a counter that is updated via websockets from the cyberserver.

Used to track the number of times cyber has been said during a talk and give live statistics.

## Install

Replace `ENTER_IP` in `cyberclient.html` with actual server IP

Host the html file on any webserver and run `cyberserver.py`

```bash
virtualenv -p python3 env
source env/bin/activate
pip install websockets
./cyberserver.py
```

