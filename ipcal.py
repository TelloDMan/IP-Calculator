import re


def reportbin(d):
    return int(str(bin(d)).replace("0b", ""))


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