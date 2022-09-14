from itertools import permutations
import re

def ip_to_bits(x):
  binary = ""
  x = x.split(".")
  for i in x:
    binary+=str(reportbin(int(i)))
  return binary


def bits_to_ip(x):
    if len(x) != 32:
        x = x+"0"*(32-len(x))
        ip = ".".join(list(map(get_dec, re.findall("[0-1]{1,8}", x))))
        return ip   
    else:
        ip = ".".join(list(map(get_dec, re.findall("[0-1]{1,8}", x))))
        return ip   


def reportbin(d):
  integar = str(bin(int(d))).replace("0b", "")
  if len(integar) < 8:
    add= (8-len(integar))*"0"
    add+= integar
    return add
  return integar


def get_dec(x):
    # conevrts to decimal
    return str(int("0b"+str(int(x)), 2))



def ipcal(d):
    # covert the decimal into binary
    x = d.split("/")
    if re.fullmatch("([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})", x[0]):
        c = list(map(reportbin, list(map(int, x[0].split(".")))))
        binarybits = ["0"*(8-len(str(i)))+str(i) for i in c]
        bit_line = "".join(binarybits)
        # dicovering the net id from CIDR notation
        net_id = bit_line[:int(x[1])]
        broadcast_ip = net_id+"1"*(32-len(net_id))
        iprange_first = net_id+"0"*(32-int(x[1])-1)+"1"
        iprange_last = net_id+"1"*(32-int(x[1])-1)+"0"
        cidr = "1"*int(x[1])+"0"*(32-int(x[1]))
        cidr_mask = ".".join(re.findall("[0-1]{1,8}", cidr))
        if len(net_id) < 32:
            net_idd = net_id+"0"*(32-len(net_id))

        net_id_dec = list(map(get_dec, re.findall("[0-1]{1,8}", net_idd)))
        broadcast_ip_dec = list(map(get_dec, re.findall("[0-1]{1,8}", broadcast_ip)))
        iprange_first_dec = list(map(get_dec, re.findall("[0-1]{1,8}", iprange_first)))
        iprange_last_dec = list(map(get_dec, re.findall("[0-1]{1,8}", iprange_last)))
        subnet_mask = ".".join(list(map(get_dec, re.findall("[0-1]{1,8}", cidr))))
        info1 = "\nNetwork ID: "+".".join(net_id_dec)+"\nBroadcast IPv4 address: "+".".join(broadcast_ip_dec)
        info2 = "\nIP Host range: "+".".join(iprange_first_dec)+" - "+".".join(iprange_last_dec)
        info3 = "\nCIDR Notation in Binary: "+cidr_mask+"\nSubnet Mask: "+subnet_mask
        info4 = "\nValid Hosts: "+str((2**(32-int(x[1])))-2)
        info = info1+info2+info3+info4
        return info

def subnett(string):
    # subnetting
    network_id , new_cidr = string.split("/")
    network_id = ip_to_bits(network_id)
    all = []
    all_sub_net = []
    subnets = {}
    j = 0
    network_bits =network_id[0:32-abs(len(network_id)-int(new_cidr))]
    print(network_bits)
    counter = 0
    for num in network_bits:
      if num == "0":
        counter+=1
      elif num == "1":
        counter = 0
    print(counter)
    ip_subnet_range = network_bits[:int(new_cidr)-counter]

    ip = list("0"*counter)
  
    for i in range(len(ip)+1):
        x = sorted(set(list(permutations(ip))))
        all += [ip_subnet_range+"".join(i) for i in x]
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


