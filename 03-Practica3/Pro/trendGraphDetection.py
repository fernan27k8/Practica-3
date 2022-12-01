import sys
import rrdtool
import time
import datetime
from Notify import send_alert_attached
import time
rrdpath = '/home/fernan/PycharmProjects/Introduccion_SNMP/03-Practica3/RRD/'
imgpath = '/home/fernan/PycharmProjects/Introduccion_SNMP/03-Practica3/IMG/'

def generarGrafica(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv(imgpath + "deteccionCPU.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=CPU load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales\nchristian.fernan.reyes@gmail.com",
                    "DEF:cargaCPU="+rrdpath+"trend.rrd:CPULoad:AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                     "CDEF:umbral38=cargaCPU,38,LT,0,cargaCPU,IF",
                     "CDEF:umbral60=cargaCPU,60,LT,0,cargaCPU,IF",
                     "CDEF:umbral76=cargaCPU,76,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral38#FF9F00:Carga CPU mayor de 38",
                     "AREA:umbral60#FF91AF:Carga CPU mayor de 60",
                     "AREA:umbral76#00E1FF:Carga CPU mayor de 76",
                     "HRULE:38#FF0000:Umbral 1 38%",
                     "HRULE:60#FFCF00:Umbral 2 60%",
                     "HRULE:76#B100FF:Umbral 3 76%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
    print(ret)
    ret = rrdtool.graphv(imgpath + "deteccionRam.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Ram load",
                         '--lower-limit', '0',
                         '--upper-limit', '100000',
                         "--title=Carga de memoria ram del agente Usando SNMP y RRDtools \n Detección de umbrales\nchristian.fernan.reyes@gmail.com",
                         "DEF:CargaRam="+rrdpath+"trend.rrd:MemoryRam:AVERAGE",
                         "VDEF:cargaMAX=CargaRam,MAXIMUM",
                         "VDEF:cargaMIN=CargaRam,MINIMUM",
                         "VDEF:cargaSTDEV=CargaRam,STDEV",
                         "VDEF:cargaLAST=CargaRam,LAST",
                         "CDEF:umbral80000=CargaRam,80000,LT,0,CargaRam,IF",
                         "CDEF:umbral90000=CargaRam,90000,LT,0,CargaRam,IF",
                         "CDEF:umbral99000=CargaRam,99000,LT,0,CargaRam,IF",
                         "AREA:CargaRam#00FF00:Carga de la Memoria",
                         "AREA:umbral80000#FF9F00:Carga Memoria Ram mayor de 80000",
                         "AREA:umbral90000#FF91AF:Carga Memoria Ram mayor de 90000",
                         "AREA:umbral99000#00E1FF:Carga Memoria Ram mayor de 99000",
                         "HRULE:80000#FF0000:Umbral 1 80000",
                         "HRULE:90000#FFCF00:Umbral 2 90000",
                         "HRULE:99000#B100FF:Umbral 3 99000",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST")
    print(ret)
    ret = rrdtool.graphv(imgpath + "deteccionTrafico.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Traffic load",
                         '--lower-limit', '0',
                         '--upper-limit', '1000000',
                         "--title=Trafico de Red del agente Usando SNMP y RRDtools \n Detección de umbrales\nchristian.fernan.reyes@gmail.com",
                         "DEF:Trafico="+rrdpath+"trend.rrd:Traffic:AVERAGE",
                         "VDEF:cargaMAX=Trafico,MAXIMUM",
                         "VDEF:cargaMIN=Trafico,MINIMUM",
                         "VDEF:cargaSTDEV=Trafico,STDEV",
                         "VDEF:cargaLAST=Trafico,LAST",
                         "CDEF:umbral800000=Trafico,800000,LT,0,Trafico,IF",
                         "CDEF:umbral900000=Trafico,900000,LT,0,Trafico,IF",
                         "CDEF:umbral990000=Trafico,990000,LT,0,Trafico,IF",
                         "AREA:Trafico#00FF00:Trafico de Red",
                         "AREA:umbral800000#FF9F00:Carga de trafico de red mayor de 800000",
                         "AREA:umbral900000#FF91AF:Carga de trafico de red mayor de 900000",
                         "AREA:umbral990000#00E1FF:Carga de trafico de red mayor de 990000",
                         "HRULE:800000#FF0000:Umbral 800000",
                         "HRULE:900000#FFCF00:Umbral 900000",
                         "HRULE:990000#B100FF:Umbral 990000",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST")
    print(ret)

while (1):
    ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trend.rrd")
    timestamp=ultima_actualizacion['date'].timestamp()
    dato1 = ultima_actualizacion['ds']["CPULoad"]
    dato2 = ultima_actualizacion['ds']["MemoryRam"]
    dato3 = ultima_actualizacion['ds']["Traffic"]
    print("CPU: ",dato1)
    print("RAM: ",dato2)
    print("Red: ",dato3)
    if dato1> 76:
        generarGrafica(int(timestamp))
        send_alert_attached("CPU Sobrepasa el umbral 3","deteccionCPU.png")
        print("CPU sobrepasa el umbral 3")
    elif dato1> 60:
        generarGrafica(int(timestamp))
        send_alert_attached("CPU Sobrepasa el umbral 2","deteccionCPU.png")
        print("CPU sobrepasa el umbral 2")
    elif dato1> 38:
        generarGrafica(int(timestamp))
        send_alert_attached("CPU obrepasa el umbral 1","deteccionCPU.png")
        print("CPU sobrepasa el umbral 1")

    if dato2 > 990000:
        generarGrafica(int(timestamp))
        send_alert_attached("RAM Sobrepasa el umbral 3", "deteccionRam.png")
        print("RAM sobrepasa el umbral 3")
    elif dato2 > 900000:
        generarGrafica(int(timestamp))
        send_alert_attached("RAM Sobrepasa el umbral 2", "deteccionRam.png")
        print("RAM sobrepasa el umbral 2")
    elif dato2 > 800000:
        generarGrafica(int(timestamp))
        send_alert_attached("RAM Sobrepasa el umbral 1", "deteccionRam.png")
        print("RAM sobrepasa el umbral 1")

    if dato3 > 990000:
        generarGrafica(int(timestamp))
        send_alert_attached("RED Sobrepasa el umbral 3", "deteccionTrafico.png")
        print("RED sobrepasa el umbral 3")
    elif dato3 > 900000:
        generarGrafica(int(timestamp))
        send_alert_attached("RED Sobrepasa el umbral 2", "deteccionTrafico.png")
        print("RED sobrepasa el umbral 2")
    elif dato3 > 800000:
        generarGrafica(int(timestamp))
        send_alert_attached("RED Sobrepasa el umbral 1", "deteccionTrafico.png")
        print("RED sobrepasa el umbral 1")
    time.sleep(20)