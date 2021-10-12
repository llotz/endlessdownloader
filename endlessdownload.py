import requests
import datetime
import sys
i = 0

#url = 'https://releases.ubuntu.com/20.04.2.0/ubuntu-20.04.2.0-desktop-amd64.iso'
url = 'http://ipv4.download.thinkbroadband.com/100MB.zip'
while True:
    try:
        start = datetime.datetime.now()
        data = requests.get(url)
        size = round(sys.getsizeof(data.content)/1024/1024, 2)
        data = None
        i = i+1
        gb = i/(1000/size)
        currentDT = datetime.datetime.now()
        diff = (currentDT-start).total_seconds()
        mbps = size/diff
        print(currentDT.strftime("%H:%M:%S: ") + str(gb) +
              " GB at "+str("{:.2f}".format(mbps))+" mbps")
    except KeyboardInterrupt:
        print("---kthxbye---")
        exit()
    except:
        print("Ooops:", sys.exc_info()[0], " occured")
        f = open("errorlog.txt", "a")
        message = currentDT.strftime(
            "%Y-%m-%d %H:%M:%S: ")+str(sys.exc_info()[0])
        f.write(message)
        f.close()
