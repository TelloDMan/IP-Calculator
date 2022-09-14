from itertools import permutations
import re


def bits_to_ip(x):
    if len(x) != 32:
        x = x+"0"*(32-len(x))
        ip = ".".join(list(map(get_dec, re.findall("[0-1]{1,8}", x))))
        return ip   
    else:
        ip = ".".join(list(map(get_dec, re.findall("[0-1]{1,8}", x))))
        return ip   


def get_dec(x):
    return str(int("0b"+str(int(x)), 2))


def subnet(string):
    # subnetting
    network_id , new_cidr = string.split("/")
    all = []
    all_sub_net = []
    subnets = {}
    j = 0
    ip = list("0"*(abs(len(network_id)-int(new_cidr))))
    for i in range(len(ip)+1):
        x = sorted(set(list(permutations(ip))))
        all += [network_id+"".join(i) for i in x]
        ip.pop()
        ip.insert(0, "1")
    print("Subnet ips:", len(all))

    for i in all:
        # convert each binary subent to an ip network id
        all_sub_net.append(bits_to_ip(i)) 

    for ip_sub in all:
        # add each subnet with its range to a dictionary
        subnets[all_sub_net[j]] = str(bits_to_ip(ip_sub+"0"*(31-len(ip_sub))+"1"))+" - "+str(bits_to_ip(ip_sub+"1"*(31-len(ip_sub))+"0"))
        j += 1

    for ipaddress in all:
        # print an output of subnetting func
        print("\n\nNetwork ID:", str(bits_to_ip(ipaddress))+"/"+new_cidr)
        print("Broadcast Address:", str(bits_to_ip(ipaddress+"1"*(32-len(ipaddress)))))
        print("IP Range:", subnets[str(bits_to_ip(ipaddress))])
        print("Host:", (2**(32-int(new_cidr)))-2)
        
    return None
