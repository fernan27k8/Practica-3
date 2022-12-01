import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/fernan/PycharmProjects/Introduccion_SNMP/03-Practica3/RRD/'
carga_CPU = 0
memoryRam = 0
traffic = 0
while 1:
    carga_CPU = int(consultaSNMP('comunidadASR', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196608'))
    memoryRam = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.4.1.2021.4.6.0'))
    traffic = int(consultaSNMP('comunidadASR', 'localhost', '1.3.6.1.2.1..2.2.1.16.2'))
    valor = "N:" + str(carga_CPU)+":"+str(memoryRam)+":"+str(traffic)
    print (valor)
    rrdtool.update(rrdpath+'trend.rrd', valor)
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
