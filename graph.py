#!/usr/bin/python
# coding=utf-8


"""Update RRD files and graphs from temperature information."""


import rrdtool
import re
from lcd_temps import read_sensor, sensors


# Update RRD files for graphs
rrdtool.update("temps.rrd", "N:%s:%s:%s" % (read_sensor(sensors["white"]),
    read_sensor(sensors["black"]), read_sensor(sensors["ambient"])));


# Generate the actual images
for sched, period in ("hourly", "h"), ("daily", "d") , ("weekly", "w"), ("monthly", "m"):
    rrdtool.graph( "/var/www/temps/metrics-%s.png" % sched,
        "--start", "-1%s" % period, "--vertical-label=°C",
        "-w 800",
        "DEF:m1=temps.rrd:black:AVERAGE",
        "DEF:m2=temps.rrd:white:AVERAGE",
        "DEF:m3=temps.rrd:ambient:AVERAGE",
        "LINE2:m2#FF0000:basking",
        "GPRINT:m2:LAST:Cur bask\: %4.1lf  ",
        "GPRINT:m2:AVERAGE:Avg bask\: %4.1lf  ",
        "GPRINT:m2:MIN:Min bask\: %4.1lf  ",
        "GPRINT:m2:MAX:Max bask\: %4.1lf  \\r",
        "LINE2:m3#00FF00:ambient",
        "GPRINT:m3:LAST:Cur ambi\: %4.1lf  ",
        "GPRINT:m3:AVERAGE:Avg ambi\: %4.1lf  ",
        "GPRINT:m3:MIN:Min ambi\: %4.1lf  ",
        "GPRINT:m3:MAX:Max ambi\: %4.1lf  \\r",
        "LINE2:m1#0000FF:in hide",
        "GPRINT:m1:LAST:Cur hide\: %4.1lf  ",
        "GPRINT:m1:AVERAGE:Avg hide\: %4.1lf  ",
        "GPRINT:m1:MIN:Min hide\: %4.1lf  ",
        "GPRINT:m1:MAX:Max hide\: %4.1lf  \\r",
    )
