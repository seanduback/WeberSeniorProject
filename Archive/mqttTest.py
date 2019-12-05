

# =============================================================================
# def on_log(client, userdata, level, buf):
#     print("log: "+buf)
# 
# def on_connect(client, userdata, flags, rc):
#     if rc==0:
#         print("connected OK")
#     else:
#         print("bad connection returned code=",rc)
# 
# 
 broker= "test.mosquitto.org"
# 
 client = mqtt.Client("computer")
# 
# client.on_connect=on_connect
# client.on_log=on_log
# print("connecting to broker",broker)
 client.connect(broker)
# f=0
# l=0
# b=0
# r=0
# cycle=0
# 
# while True:
#     if cycle==1:
#         f=1
#         l=0
#         b=0
#         r=0
#     elif cycle==2:
#         f=0
#         l=1
#         b=0
#         r=0
#     elif cycle==3:
#         f=0
#         l=0
#         b=1
#         r=0
#     elif cycle==4:
#         f=0
#         l=0
#         b=0
#         r=1
#         cycle=0
# =============================================================================
    
    #msg = ("{0},{1},{2},{3}".format(f,l,b,r))
    msg = ("{0},{1}".format(Direction, Range))
    client.publish("motors",msg)
    #cycle += 1
    time.sleep(.001)
client.loop_forever()
