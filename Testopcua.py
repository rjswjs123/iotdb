from time import sleep
from datetime import datetime
import time
import random
from opcua import Server
import numpy as np
server=Server()
server.set_endpoint("opc.tcp://127.0.0.1:12345")
server.register_namespace("Room1")
objects=server.get_objects_node()
tempsens=objects.add_object('ns=2;s="TS"',"Temperature Sensor")


temp1=tempsens.add_variable('ns=2;s="TS1_Temperature"',"TS1 Temperature",20)
temp2=tempsens.add_variable('ns=2;s="TS2_Temperature"',"TS2 Temperature",20)
temp3=tempsens.add_variable('ns=2;s="TS3_Temperature"',"TS3 Temperature",20)
temp4=tempsens.add_variable('ns=2;s="TS4_Temperature"',"TS4 Temperature",20)
temp5=tempsens.add_variable('ns=2;s="TS5_Temperature"',"TS5 Temperature",20)
temp6=tempsens.add_variable('ns=2;s="TS6_Temperature"',"TS6 Temperature",20)
temp7=tempsens.add_variable('ns=2;s="TS7_Temperature"',"TS7 Temperature",20)
temp8=tempsens.add_variable('ns=2;s="TS8_Temperature"',"TS8 Temperature",20)
temp9=tempsens.add_variable('ns=2;s="TS9_Temperature"',"TS9 Temperature",20)
temp10=tempsens.add_variable('ns=2;s="TS10_Temperature"',"TS10 Temperature",20)
temp11=tempsens.add_variable('ns=2;s="TS11_Temperature"',"TS11 Temperature",20)
temp12=tempsens.add_variable('ns=2;s="TS12_Temperature"',"TS12 Temperature",20)
temp13=tempsens.add_variable('ns=2;s="TS13_Temperature"',"TS13 Temperature",20)
temp14=tempsens.add_variable('ns=2;s="TS14_Temperature"',"TS14 Temperature",20)
temp15=tempsens.add_variable('ns=2;s="TS15_Temperature"',"TS15 Temperature",20)
temp16=tempsens.add_variable('ns=2;s="TS16_Temperature"',"TS16 Temperature",20)
temp17=tempsens.add_variable('ns=2;s="TS17_Temperature"',"TS17 Temperature",20)
temp18=tempsens.add_variable('ns=2;s="TS18_Temperature"',"TS18 Temperature",20)
temp19=tempsens.add_variable('ns=2;s="TS19_Temperature"',"TS19 Temperature",20)
temp20=tempsens.add_variable('ns=2;s="TS20_Temperature"',"TS20 Temperature",20)



sensor_number=5
time=0
try:
    print("start server")
    server.start()
    print("Server online")

    while True:
        temperature = 20.0
        print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
        time+=1
        for i in tempsens.get_children():
            temperature += random.uniform(-1, 1)
            i.set_value(np.around(temperature,4))

        # print("New Temperature1: " + str(temp1.get_value())+","+str(temp2.get_value())+","+str(temp3.get_value())+","+str(temp4.get_value())+","+str(temp5.get_value())
        #       +str(temp6.get_value())+","+str(temp7.get_value())+","+str(temp8.get_value())+","+str(temp9.get_value())+","+str(temp10.get_value())
        #       +str(temp11.get_value())+","+str(temp12.get_value())+","+str(temp13.get_value())+","+str(temp14.get_value())+","+str(temp15.get_value())
        #       +str(temp16.get_value())+","+str(temp17.get_value())+","+str(temp18.get_value())+","+str(temp19.get_value())+","+str(temp20.get_value()))
        print("total: " + str(time))
finally:
    server.stop()
    print("server offline")







