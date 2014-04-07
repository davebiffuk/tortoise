tortoise
========

tortoise environment monitoring with Raspberry Pi

create_rrd.py - create empty RRD database files
crontab - entries to run regular tasks
do_webcam - grab a webcam image and put it into the web directory
fix_uvcvideo_module - ensure video module correctly set up
graph.py - update RRD graphs
lcd_temps.py - main script; polls sensors and updates display
message2.py - LCD display library from Matt Hawkins
update_rrd.py - polls sensors and updates RRD files

Notes
-----

BRANCH=next firmware may be necessary; see:
https://github.com/raspberrypi/linux/issues/470
https://github.com/raspberrypi/linux/issues/552

To do
-----

* refactor the code duplication between lcd_temps.py and update_rrd.py
