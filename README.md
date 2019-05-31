# blueiris-geofence
This project was created for the need to use the BlueIris geofence features for free, using some Life360 app APIs (available for both Android and IOS) and BlueIris.
You can configure what kind of operations blueiris-geofence should be performed when Life360 Circle's members are away or inside of their Home.

I would like to mention the sources from which I took some material:
https://github.com/harperreed/life360-python 
https://github.com/magapp/blueiriscmd

## Requirements
- python3
- python3-yaml
- python3-requests

## Linux Install:
- Debian Base: apt-get install python3 python3-yaml python3-requests
- Centos/Red Hat: yum install python3 python3-yaml python3-requests

## Windows Install:

- https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe
navigating to your Python folder via CMD worked
- cd C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37-32
- python -m pip install --upgrade pip
- python -m pip install requests
- python -m pip install pyyaml

## Install blueiris-geofence as a service:
### Linux
Create a custom systemd service script:
- vim /lib/systemd/system/blueiris-geofence.service<br>

[Unit]<br>
Description=BlueIris Geofence Service<br>
After=network.target<br>

[Service]<br>
Type=idle<br>
User=root<br>
WorkingDirectory=/opt/blueiris-geofence/<br>
ExecStart=/usr/bin/python3 /opt/blueiris-geofence/geofence.py > /var/log/bluiris-geofence.log 2>&1<br>
Restart=on-failure<br>

[Install]<br>
WantedBy=multi-user.target<br>

- chmod 644 /lib/systemd/system/blueiris-geofence.service
- systemctl daemon-reload
- systemctl enable blueiris-geofence.service
- systemctl start blueiris-geofence.service
- systemctl stus blueiris-geofence.service

### Windows
WORK IN PROGRESS....
