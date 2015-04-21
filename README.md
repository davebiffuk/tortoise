tortoise
========

Tortoise environment monitoring with a Raspberry Pi. You can see the
result at http://tortoise.biff.org.uk

* create_rrd.py - create empty RRD database files
* crontab - entries to run regular tasks
* do_webcam - grab a webcam image and put it into the web directory
* fix_uvcvideo_module - ensure video module correctly set up
* graph.py - update RRD graphs
* lcd_temps.py - main script; polls sensors and updates display
* message2.py - LCD display library from Matt Hawkins
* update_rrd.py - polls sensors and updates RRD files

Notes
-----

Beware of the GPIO pin changes between revision 1 and revision 2
Raspberry Pi boards! These scripts are for r2.
http://elinux.org/RPi_Low-level_peripherals#General_Purpose_Input.2FOutput_.28GPIO.29

To install software prerequisites:

```
sudo apt-get install apache2 fswebcam python-rrdtool
```

To get the 1-wire/GPIO interface working, recent Raspbian images might
need

```dtoverlay=w1-gpio,gpiopin=4```

adding to `/boot/config.txt`

BRANCH=next firmware used to be necessary; see:
https://github.com/raspberrypi/linux/issues/470 and
https://github.com/raspberrypi/linux/issues/552
but the important USB fix should now be in the main kernel (so do
"sudo rpi-update"):
https://github.com/raspberrypi/linux/issues/548#issuecomment-42947030

To do
-----

* refactor the code duplication between lcd_temps.py and update_rrd.py
