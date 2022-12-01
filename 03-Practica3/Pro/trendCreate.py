import rrdtool
ret = rrdtool.create("/home/fernan/PycharmProjects/Introduccion_SNMP/03-Practica3/RRD/trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPULoad:GAUGE:60:0:100",
                     "DS:MemoryRam:GAUGE:60:0:100000",
                     "DS:Traffic:GAUGE:60:0:2000000",
                     "RRA:AVERAGE:0.5:1:24")
if ret:
    print (rrdtool.error())