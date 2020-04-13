import pingparsing
import json
from textwrap import dedent
import operator



def pingAverage(host):
    ping = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.count = 4
    transmitter.destination = str(host)
    hasil = transmitter.ping() 
    result = (ping.parse(hasil).as_dict())
    return result

def allHost():
    hosts = open("hostlist.txt","r")
    averages = {}
    downServer = {}
    c = 0
    print("**************** Mohon Menunggu **************** ")
    for x in hosts:
        c = c+1
        avg = pingAverage(x)['rtt_avg']
        hostname = str(x[:-1])
        
        if avg != None:
            if(hostname not in averages):
                averages[hostname] = avg

            else:
                averages[hostname].append(avg)

            print("Server : {} \t \t Average : {} ms".format(x[:-1].ljust(40, ' '),str(avg)))
        else:
            if(hostname not in downServer):
                downServer[hostname] = "Down"

            else:
                downServer[hostname].append("Down / Tidak dapat dijangkau")
            
            print("Server : {} Average : {} ms".format(x[:-1].ljust(40, ' '),"Down / Tidak dapat dijangkau"))

    print("**************** Selesai **************** \n")
    print("\n\nTotal Server yang dicek : {} Server \n".format(str(c)))   

    return averages,downServer




def intro():
    print("====================================================\n")
    print("Latency Video Confrence Server Tester")
    print("list didapat dari Telegram Group OpisBoy Zaman Now")
    print("versi 0.1.2")
    print("@arsyifha")
    print("@si_faisal - reza@jagonetwork.id")
    print("@WillyRL - willyrobertus@gmail.com")
    print("====================================================\n")
    

def main():
    intro()
    averages,downserver = allHost()
    serverSorted = sorted(averages.items(), key=operator.itemgetter(1))

    
    print("=================== Server Terbaik =============================================================\n")
    c = 0
    
    for x in serverSorted[0:5] :
        c = c+1
        print(str(c)+". Server : {} \t \t Average : {} ms".format(x[0].ljust(40, ' '),x[1]))

    print("\n\n=================== Server Down / Tidak Terjangkau ==============================================\n")

    for x in downserver :
        print(x)

    


if __name__ == "__main__":
    main()