# /env/bin/python
# -*- coding:utf-8 -*-
# auther: d3ckx1
# time: 2021/03/01

import nmap
import time
import threading

banner = '''


                   _      _            _   _             
                  | |    | |          | | (_)            
  _ ____      ____| | ___| |_ ___  ___| |_ _  ___  _ __  
 | '_ \ \ /\ / / _` |/ _ \ __/ _ \/ __| __| |/ _ \| '_ \ 
 | | | \ V  V / (_| |  __/ ||  __/ (__| |_| | (_) | | | |
 |_| |_|\_/\_/ \__,_|\___|\__\___|\___|\__|_|\___/|_| |_|
                                                         
                                                         
                    code by d3ckx1
            Usage : python nwdetection.py
            
'''
print banner

localnet = {'192.168.0.1/16','172.16.0.1/16', '10.0.0.1/16','10.1.0.1/16','10.2.0.1/16','10.3.0.1/16','10.4.0.1/16','10.5.0.1/16','10.6.0.1/16','10.8.0.1/16','10.10.0.1/16',}  #如果不知道网段，就使用这些相对常见的网段，
#localnet = {'192.168.0.1/24','172.16.24.1/24', '192.168.1.1/24',}   #如果大概知道什么网段，可以修改使用这个，速度比较快

def nmap_ping_scan(nets):
    nm = nmap.PortScanner()
    ping_scan_raw = nm.scan(hosts = nets,arguments='-sn') #hosts可以是单个IP地址也可以是一整个网段。 arguments就是运用什么方式扫描，-sn就是ping扫描。

    host_list_ip = []
    for result in ping_scan_raw['scan'].values():  #将scan下面的数值赋值给result，并开始遍历。

        if result['status']['state'] == 'up':  #如果是up则表明对方主机是存活的。
            #print result
            host_list_ip.append(result['addresses']['ipv4'])  #在addresses层下的ipv4，也就是IP地址添加到result字典中。

    isfind = open('localip.txt', 'a+')
    isfind.write(str(host_list_ip))
    isfind.write('\r\n')
    isfind.close()


if __name__ == '__main__':
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print "The scanning time is: ", localtime
    print '-----------------------------------------------------------'

    for nets in localnet:
        print "Start Scaner Local Network: %s\n" % nets
        t1 = threading.Thread(target=nmap_ping_scan(nets), args=(100, 110))
        t1.setDaemon(True)
        t1.start()

    print '-----------------------------------------------------------'
    print "Scanner is Over!"






