# 						COMP9331 LAB 01 

#### 																												YUAN GAO Z5239220

++++

#### Exercise 1: nslookup

>1. Which is the IP address of the website www.koala.com.au? In your opinion, what is the reason of having several IP addresses as an output?
>
>   >```powershell
>   >wagner % nslookup www.koala.com.au
>   >Server:		129.94.242.2
>   >Address:	129.94.242.2#53
>   >
>   >Non-authoritative answer:
>   >Name:	www.koala.com.au
>   >Address: 104.18.61.21
>   >Name:	www.koala.com.au
>   >Address: 172.67.219.46
>   >Name:	www.koala.com.au
>   >Address: 104.18.60.21
>   >```
>   >
>   >+ According to `nslookup` command, the IP address of website www.koala.com.au are "104.18.61.21", "172.67.219.46" and "104.18.60.21"
>   >+ In order to achive load balancing, company provides several accessible IP addresses and each address corresponds to a web server. Client can connects any one of them. DNS will pick an IP address that is geographically closest to the client which can improve access speed.
>
>2. Find out the name of the IP address 127.0.0.1. What is special about this IP address?
>
>   >```powershell
>   >wagner % nslookup 127.0.0.1
>   >Server:		129.94.242.2
>   >Address:	129.94.242.2#53
>   >
>   >1.0.0.127.in-addr.arpa	name = localhost.
>   >```
>   >
>   >+ The name is "localhost"
>   >+ 127.0.0.1 is Loopback Address. The local loopback mechanism may be used to run a network service on a host without requiring a physical network interface, or without making the service accessible from the networks the computer may be connected to. (From wikipedia)
>
#### Exercise 2: Use ping to test host reachability 

>+ **Reachable web:** [`www.unsw.edu.au`](http://www.unsw.edu.au/), www.mit.edu, [www.intel.com.au](http://www.intel.com.au/), www.tpg.com.au, [www.amazon.com](http://www.amazon.com/), [www.tsinghua.edu.cn](http://www.tsinghua.edu.cn/),  8.8.8.8
>
>  **Unreachable web:** [www.getfittest.com.au](http://www.getfittest.com.au/), [www.hola.hp](http://www.hola.hp/), [www.kremlin.ru](http://www.kremlin.ru/) and [www.hola.hp](http://www.hola.hp/) does not exist. We cannot open them.
>
>+ We can open [www.kremlin.ru](http://www.kremlin.ru/), but there is no ping. Perhaps for some security reasons, some web cannot access from replying to ICMP request packets by `ping` command.
#### Exercise 3: Use traceroute to understand network topology

>1. Run `traceroute` on machine to [www.columbia.edu](http://www.columbia.edu/)
>
>   ><img src="/Users/yuan/Desktop/截屏2020-09-22 下午2.19.36.png" alt="截屏2020-09-22 下午2.19.36" style="zoom: 200%;" />
>   >
>   >+ According to `traceroute` command, there are 22 hops. 
>   >
>   >  Therefore,  there are 21 routers between my workstation and www.columbia.edu. 
>   >
>   >+ There are 5 routers are part of the UNSW network.
>   >
>   >+ From the graph:
>   >
>   >  ```powershell
>   >   7  et-1-3-0.pe1.sxt.bkvl.nsw.aarnet.net.au (113.197.15.149)  1.988 ms  1.887 ms  1.933 ms
>   >   8  et-0-0-0.pe1.a.hnl.aarnet.net.au (113.197.15.99)  95.326 ms  95.451 ms  95.372 ms
>   >   9  et-2-1-0.bdr1.a.sea.aarnet.net.au (113.197.15.201)  146.901 ms  146.802 ms  146.861 ms
>   >  ```
>   >
>   >  The 7, 8 and 9 hops have huge trip time. Therefore, we can infer that (7-8 and 8-9 between 113.197.15.149 and 113.197.15.201) there are two routers cross the Pacific Ocean.
>
>2. Run `traceroute` from machine to the following destinations
>
>   >(i) [www.ucla.edu ](http://www.ucla.edu/)
>   >
>   >><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午2.33.24.png" alt="截屏2020-09-22 下午2.33.24" style="zoom:200%;" />
>   >
>   >(ii) [www.u-tokyo.ac.jp ](http://www.u-tokyo.ac.jp/)
>   >
>   >> <img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午2.34.36.png" alt="截屏2020-09-22 下午2.34.36" style="zoom:200%;" />
>   >
>   >(iii) [www.lancaster.ac.uk](http://www.lancaster.ac.uk/)
>   >
>   >><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午2.36.39.png" alt="截屏2020-09-22 下午2.36.39" style="zoom:200%;" />
>   >
>   >+ According to three pictures, we can see that 1-6 hops are same, started from 7th hops, the IP addresses are different. Hence, path diverging occurs from 6th router. The IP is 138.44.5.0.
>   >
>   >  The details of this IP:
>   >
>   >  ```powershell
>   >  wagner % whois 138.44.5.0
>   >  
>   >  #
>   >  # ARIN WHOIS data and services are subject to the Terms of Use
>   >  # available at: https://www.arin.net/resources/registry/whois/tou/
>   >  #
>   >  # If you see inaccuracies in the results, please report at
>   >  # https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
>   >  #
>   >  # Copyright 1997-2020, American Registry for Internet Numbers, Ltd.
>   >  #
>   >  
>   >  
>   >  NetRange:       138.44.0.0 - 138.44.255.255
>   >  CIDR:           138.44.0.0/16
>   >  NetName:        APNIC-ERX-138-44-0-0
>   >  NetHandle:      NET-138-44-0-0-1
>   >  Parent:         NET138 (NET-138-0-0-0-0)
>   >  NetType:        Early Registrations, Transferred to APNIC
>   >  OriginAS:
>   >  Organization:   Asia Pacific Network Information Centre (APNIC)
>   >  RegDate:        2003-12-11
>   >  Updated:        2009-10-08
>   >  Comment:        This IP address range is not registered in the ARIN database.
>   >  Comment:        This range was transferred to the APNIC Whois Database as
>   >  Comment:        part of the ERX (Early Registration Transfer) project.
>   >  Comment:        For details, refer to the APNIC Whois Database via
>   >  Comment:        WHOIS.APNIC.NET or http://wq.apnic.net/apnic-bin/whois.pl
>   >  Comment:
>   >  Comment:        ** IMPORTANT NOTE: APNIC is the Regional Internet Registry
>   >  Comment:        for the Asia Pacific region.  APNIC does not operate networks
>   >  Comment:        using this IP address range and is not able to investigate
>   >  Comment:        spam or abuse reports relating to these addresses.  For more
>   >  Comment:        help, refer to http://www.apnic.net/apnic-info/whois_search2/abuse-and-spamming
>   >  Ref:            https://rdap.arin.net/registry/ip/138.44.0.0
>   >  
>   >  ResourceLink:  http://wq.apnic.net/whois-search/static/search.html
>   >  ResourceLink:  whois.apnic.net
>   >  
>   >  
>   >  OrgName:        Asia Pacific Network Information Centre
>   >  OrgId:          APNIC
>   >  Address:        PO Box 3646
>   >  City:           South Brisbane
>   >  StateProv:      QLD
>   >  PostalCode:     4101
>   >  Country:        AU
>   >  RegDate:
>   >  Updated:        2012-01-24
>   >  Ref:            https://rdap.arin.net/registry/entity/APNIC
>   >  
>   >  ReferralServer:  whois://whois.apnic.net
>   >  ResourceLink:  http://wq.apnic.net/whois-search/static/search.html
>   >  
>   >  OrgTechHandle: AWC12-ARIN
>   >  OrgTechName:   APNIC Whois Contact
>   >  OrgTechPhone:  +61 7 3858 3188
>   >  OrgTechEmail:  search-apnic-not-arin@apnic.net
>   >  OrgTechRef:    https://rdap.arin.net/registry/entity/AWC12-ARIN
>   >  
>   >  OrgAbuseHandle: AWC12-ARIN
>   >  OrgAbuseName:   APNIC Whois Contact
>   >  OrgAbusePhone:  +61 7 3858 3188
>   >  OrgAbuseEmail:  search-apnic-not-arin@apnic.net
>   >  OrgAbuseRef:    https://rdap.arin.net/registry/entity/AWC12-ARIN
>   >  
>   >  
>   >  #
>   >  # ARIN WHOIS data and services are subject to the Terms of Use
>   >  # available at: https://www.arin.net/resources/registry/whois/tou/
>   >  #
>   >  # If you see inaccuracies in the results, please report at
>   >  # https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
>   >  #
>   >  # Copyright 1997-2020, American Registry for Internet Numbers, Ltd.
>   >  #
>   >  
>   >  
>   >  
>   >  Found a referral to whois.apnic.net.
>   >  
>   >  % [whois.apnic.net]
>   >  % Whois data copyright terms    http://www.apnic.net/db/dbcopyright.html
>   >  
>   >  % Information related to '138.44.0.0 - 138.44.255.255'
>   >  
>   >  % Abuse contact for '138.44.0.0 - 138.44.255.255' is 'abuse@aarnet.edu.au'
>   >  
>   >  inetnum:        138.44.0.0 - 138.44.255.255
>   >  netname:        AARNET
>   >  descr:          Australian Academic and Research Network
>   >  descr:          Building 9
>   >  descr:          Banks Street
>   >  country:        AU
>   >  org:            ORG-AAAR1-AP
>   >  admin-c:        SM6-AP
>   >  tech-c:         ANOC-AP
>   >  abuse-c:        AA1638-AP
>   >  status:         ALLOCATED PORTABLE
>   >  remarks:        -+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+
>   >  remarks:        This object can only be updated by APNIC hostmasters.
>   >  remarks:        To update this object, please contact APNIC
>   >  remarks:        hostmasters and include your organisation's account
>   >  remarks:        name in the subject line.
>   >  remarks:        -+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+
>   >  notify:         irrcontact@aarnet.edu.au
>   >  mnt-by:         APNIC-HM
>   >  mnt-lower:      MAINT-AARNET-AP
>   >  mnt-routes:     MAINT-AARNET-AP
>   >  mnt-irt:        IRT-AARNET-AU
>   >  last-modified:  2020-06-22T05:22:11Z
>   >  source:         APNIC
>   >  
>   >  irt:            IRT-AARNET-AU
>   >  address:        AARNet Pty Ltd
>   >  address:        26 Dick Perry Avenue
>   >  address:        Kensington, Western Australia
>   >  address:        Australia
>   >  e-mail:         abuse@aarnet.edu.au
>   >  abuse-mailbox:  abuse@aarnet.edu.au
>   >  admin-c:        SM6-AP
>   >  tech-c:         ANOC-AP
>   >  auth:           # Filtered
>   >  remarks:        abuse@aarnet.edu.au was validated on 2020-06-22
>   >  mnt-by:         MAINT-AARNET-AP
>   >  last-modified:  2020-06-22T05:21:20Z
>   >  source:         APNIC
>   >  
>   >  organisation:   ORG-AAAR1-AP
>   >  org-name:       Australian Academic and Research Network
>   >  country:        AU
>   >  address:        Building 9
>   >  address:        Banks Street
>   >  phone:          +61-2-6222-3530
>   >  fax-no:         +61-2-6222-3535
>   >  e-mail:         irrcontact@aarnet.edu.au
>   >  mnt-ref:        APNIC-HM
>   >  mnt-by:         APNIC-HM
>   >  last-modified:  2017-10-09T12:56:36Z
>   >  source:         APNIC
>   >  
>   >  role:           ABUSE AARNETAU
>   >  address:        AARNet Pty Ltd
>   >  address:        26 Dick Perry Avenue
>   >  address:        Kensington, Western Australia
>   >  address:        Australia
>   >  country:        ZZ
>   >  phone:          +000000000
>   >  e-mail:         abuse@aarnet.edu.au
>   >  admin-c:        SM6-AP
>   >  tech-c:         ANOC-AP
>   >  nic-hdl:        AA1638-AP
>   >  remarks:        Generated from irt object IRT-AARNET-AU
>   >  abuse-mailbox:  abuse@aarnet.edu.au
>   >  mnt-by:         APNIC-ABUSE
>   >  last-modified:  2020-06-22T05:22:10Z
>   >  source:         APNIC
>   >  
>   >  role:           AARNet Network Operations Centre
>   >  remarks:
>   >  address:        AARNet Pty Ltd
>   >  address:        GPO Box 1559
>   >  address:        Canberra
>   >  address:        ACT  2601
>   >  country:        AU
>   >  phone:          +61 1300 275 662
>   >  phone:          +61 2 6222 3555
>   >  remarks:
>   >  e-mail:         noc@aarnet.edu.au
>   >  remarks:
>   >  remarks:        Send abuse reports to abuse@aarnet.edu.au
>   >  remarks:        Please include timestamps and offset to UTC in logs
>   >  remarks:        Peering requests to peering@aarnet.edu.au
>   >  remarks:
>   >  admin-c:        SM6-AP
>   >  tech-c:         BM-AP
>   >  nic-hdl:        ANOC-AP
>   >  mnt-by:         MAINT-AARNET-AP
>   >  last-modified:  2010-06-30T13:16:48Z
>   >  source:         APNIC
>   >  
>   >  person:         Steve Maddocks
>   >  remarks:        Director Operations
>   >  address:        AARNet Pty Ltd
>   >  address:        26 Dick Perry Avenue
>   >  address:        Kensington
>   >  address:        Perth
>   >  address:        WA  6151
>   >  country:        AU
>   >  phone:          +61-8-9289-2210
>   >  fax-no:         +61-2-6222-7509
>   >  e-mail:         steve.maddocks@aarnet.edu.au
>   >  nic-hdl:        SM6-AP
>   >  mnt-by:         MAINT-AARNET-AP
>   >  last-modified:  2011-02-01T08:37:06Z
>   >  source:         APNIC
>   >  
>   >  % Information related to '138.44.5.0/24AS7575'
>   >  
>   >  route:          138.44.5.0/24
>   >  origin:         AS7575
>   >  descr:          Australian Academic and Research Network
>   >                  Building 9
>   >                  Banks Street
>   >  mnt-by:         MAINT-AARNET-AP
>   >  last-modified:  2019-04-03T03:55:51Z
>   >  source:         APNIC
>   >  
>   >  % This query was served by the APNIC Whois Service version 1.88.15-SNAPSHOT (WHOIS-NODE4)
>   >  ```
>   >
>   >  
>   >
>   >+ No,
>   >
>   >  The distance between AU and UK is 15,195
>   >
>   >  The distance between AU and JP is 6,848
>   >
>   >  *(Source from google)*
>   >
>   >  Access [www.u-tokyo.ac.jp ](http://www.u-tokyo.ac.jp/) experienced 15 hops, but access [www.lancaster.ac.uk](http://www.lancaster.ac.uk/) experienced 14 hops.
>
>3. Several servers distributed around the world
>
>   >```powershell
>   >wagner % nslookup www.speedtest.com.sg
>   >Server:		129.94.242.2
>   >Address:	129.94.242.2#53
>   >
>   >Non-authoritative answer:
>   >Name:	www.speedtest.com.sg
>   >Address: 202.150.221.170
>   >```
>   >
>   >```powershell
>   >wagner % nslookup www.telstra.net
>   >Server:		129.94.242.2
>   >Address:	129.94.242.2#53
>   >
>   >Non-authoritative answer:
>   >Name:	www.telstra.net
>   >Address: 203.50.5.178
>   >```
>   >
>   >+ www.speedtest.com.sg IP addresses is 202.150.221.170
>   >
>   >  www.telstra.net IP addresses is 203.50.5.178
>   >
>   >+ Through `/sbin/ifconfig`, I can check my IP address is 129.94.242.19![截屏2020-09-22 下午3.27.49](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午3.27.49.png)
>   >
>   >  (1). Check forward path
>   >
>   >  www.speedtest.com.sg:
>   >
>   >  >![截屏2020-09-22 下午3.32.18](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午3.32.18.png)
>   >
>   >  www.telstra.net
>   >
>   >  >![截屏2020-09-22 下午3.33.09](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午3.33.09.png)
>   >
>   >  (2). Check reverse path
>   >
>   >  www.speedtest.com.sg:
>   >
>   >  > ![截屏2020-09-22 下午3.28.27](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午3.28.27.png)
>   >
>   >  www.telstra.net
>   >
>   >  >![截屏2020-09-22 下午3.30.35](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午3.30.35.png)
>   >
>   >  According to **forward path** and **reverse path**, we can find that they do not choose the same routers. In order to avoid traffic porblem, DNS will pick different path following load balancing.

#### Exercise 4: Use ping to gain insights into network performance 

>1. Through google map:
>
>   > The distance between UNSW and Brisbane is $738.81km$
>   >
>   > The distance between UNSW and Serdang is $6,606.01km$
>   >
>   > The distace between UNSW and Berlin is $16,099.98km$
>   >
>   > Hence, the time of delay is:
>   >
>   > $T_{Brisbane}= (738.81 \times 10^3) \div (3 \times 10^8) \approx 2.46 ms$
>   >
>   > $T_{Serdang}= (6606.01 \times 10^3) \div (3 \times 10^8) \approx 22.02 ms$
>   >
>   > $T_{Berlin}= (16099.98 \times 10^3) \div (3 \times 10^8) \approx 53.67 ms$
>   >
>   > According to the file of `runping.sh`, the minimum RTT Ping program are:
>   >
>   > $minRTT_{Brisbane} = 16.880 ms$
>   >
>   > $minRTT_{Serdang} = 98.806 ms$
>   >
>   > $minRTT_{Berlin} = 274.700 ms$
>   >
>   > Therefore, the ratio are:
>   >
>   > $R_{Brisbane} = 6.86$
>   >
>   > $R_{Serdang} = 4.48$
>   >
>   > $R_{Berlin} = 5.12$
>   >
>   > <img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午9.55.23.png" alt="截屏2020-09-22 下午9.55.23" style="zoom: 50%;" />
>   >
>   > + The reasons of the y-axis values that the plot are greater than 2:
>   >
>   >   a) The speed of packet moves has loss in physical media (not vacuum)
>   >
>   >   b) The physical cables are not laid in a straight line
>   >
>   >   c) Total nodal delay contains nodal processing delay, queeing delay, transmission delay and propagation delay. It does not be considered.
>
>2.  The delay to the destinations is vary over time. 
>
>   >The graphs show that:
>   >
>   >(i) www.uq.edu.au
>   >
>   ><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午10.10.36.png" alt="截屏2020-09-22 下午10.10.36" style="zoom:67%;" />![截屏2020-09-22 下午10.17.22](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午10.17.22.png)
>   >
>   >(ii) www.upm.edu.my
>   >
>   ><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午10.11.22.png" alt="截屏2020-09-22 下午10.11.22" style="zoom:67%;" />
>   >
>   >![截屏2020-09-22 下午10.19.47](/Users/yuan/Desktop/截屏2020-09-22 下午10.19.47.png)
>   >
>   >(iii) www.tu-berlin.de
>   >
>   ><img src="/Users/yuan/Desktop/截屏2020-09-22 下午10.11.44.png" alt="截屏2020-09-22 下午10.11.44" style="zoom:67%;" />
>   >
>   >![截屏2020-09-22 下午10.20.37](/Users/yuan/Desktop/截屏2020-09-22 下午10.20.37.png)
>   >
>   >+ Through curve graph, these show that the delay to the destinations randomly varies over time. This is mainly due to changing processing delay and queuing delay
>   >+ Through Scatter plot graph, the size of packets may not have correlation with time delay. The delay could couased by lower bandwidth in some channels.
>
>3. [www.epfl.ch](http://www.epfl.ch/)
>
>   >```powershell
>   >wagner % nslookup www.epfl.ch
>   >Server:		2001:8003:2475:7600::1
>   >Address:	2001:8003:2475:7600::1#53
>   >
>   >Non-authoritative answer:
>   >www.epfl.ch	canonical name = www.epfl.ch.cdn.cloudflare.net.
>   >Name:	www.epfl.ch.cdn.cloudflare.net
>   >Address: 104.20.228.42
>   >Name:	www.epfl.ch.cdn.cloudflare.net
>   >Address: 172.67.2.106
>   >Name:	www.epfl.ch.cdn.cloudflare.net
>   >Address: 104.20.229.42
>   >```
>   >
>   >According to the IP addresses, 
>   >
>   ><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-22 下午10.44.44.png" alt="截屏2020-09-22 下午10.44.44" style="zoom:50%;" />
>   >
>   >The IP addresses of  [www.epfl.ch](http://www.epfl.ch/) are located in Unitide States, not in Switzerland.
>
>4. **Propagation delay** depends on the length of channel. It does not depend on packet size.
>
>   **Transmission delay** depends on the length of data frames. It relates on packet size.
>
>   **Processing delay** need to process packets, so it  depend on packet size.
>
>   **Queuing delay** is time the packet spends in routing queues. It relates on packet size.
>
>   Hence,
>
>   Depend on the packet size: Transmission delay, Processing delay and Queuing delay
>
>   Not depend on the packet size: Propagation delay

