# nwdetection

在内网渗透中，大家平时除了看目标所属网段外，其他未知网段怎么办呐？运行netdiscover流量太大容易造成断网？

那就试试这个吧

优点：流量小、使用方便、依赖模块少

缺点：探测速度较慢、内网的ip地址库可能还不全

使用方法：
命令： python nwdetection.py
![Image text](https://github.com/d3ckx1/nwdetection/blob/main/WechatIMG515.jpeg)

跑完后，存活的IP都存储到同目录下 “localip.txt” 中

![Image text](https://github.com/d3ckx1/nwdetection/blob/main/WechatIMG516.jpeg)
