import android
import time
import datetime

droid = android.Android()

today=datetime.datetime.now().strftime("%Y%m%d-%M%H")
droid.startLocating()
#sometimes takes a long time for the phone to pickup the signal
time.sleep(20)
for x in range(120):
    data=""
    data=droid.readLocation().result
    output={}
    try:
        data=data["gps"]
        output["type"]="GPS"
    except:
        data=data["network"]
        output["type"]="Cell Network"
    output["x"]=data["latitude"]
    output["y"]=data["longitude"]
    output["t"]=datetime.datetime.fromtimestamp(int(data["time"])/1000)
    file="/sdcard/docs/gpslog/"+today+".log"
    outfile=open(file, "a")
    outfile.write(str(output)+"\n,")
    outfile.close()
    print str(output)
    time.sleep(20)
droid.stopLocating()
