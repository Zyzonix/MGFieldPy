# MGFieldPy - Magnetic field measurement
This software has been developed for OCSILY - for more details, please contact OCISLY-ds

#### Installation
```
$ git clone https://github.com/Zyzonix/MGFieldPy.git
$ cd MGField/
```
To install the service type:
```
$ sudo cp static/MGFieldPy.service /lib/systemd/system/
$ sudo systemctl enable MGFieldPy.service
```
#### Execution
Directly over the console (the programm will interrupt when the window will be closed)
```
$ python3 init.py
```
Or via the system service
```
$ sudo systemctl start MGFieldPy.service
```

#### Settings
The software can be configured through the config-file under static
