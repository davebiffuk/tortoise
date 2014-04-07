#!/usr/bin/python
import rrdtool

# http://supportex.net/2011/09/rrd-python/

ret = rrdtool.create("temps.rrd", "--step", "300", "--start", '0',
 "DS:white:GAUGE:2000:0:50",
 "DS:black:GAUGE:2000:0:50",
 "DS:ambient:GAUGE:2000:0:50",
 #"RRA:LAST:0.5:1:600",
 "RRA:AVERAGE:0.5:1:600",
 "RRA:AVERAGE:0.5:6:700",
 "RRA:AVERAGE:0.5:24:775",
 "RRA:AVERAGE:0.5:288:797",
 "RRA:MIN:0.5:1:600",
 "RRA:MIN:0.5:6:700",
 "RRA:MIN:0.5:24:775",
 "RRA:MIN:0.5:444:797",
 "RRA:MAX:0.5:1:600",
 "RRA:MAX:0.5:6:700",
 "RRA:MAX:0.5:24:775",
 "RRA:MAX:0.5:444:797")

