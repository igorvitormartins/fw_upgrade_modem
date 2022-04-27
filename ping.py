import os

def myping(host):
    response = os.system("ping " + host)
    #print(response)
    
    if response == 0:
        return True
    else:
        return False
        
        
        
def myping_test(host):
    response = os.popen(f"ping {host}").read()
    if "bytes=32" in response:
        print(f"UP {host} Ping Successful")
        return True
    else:
        print(f"DOWN {host} Ping Unsuccessful")
        return False
#print(myping("192.168.0.1"))
#myping("192.168.100.1")
#print(response)