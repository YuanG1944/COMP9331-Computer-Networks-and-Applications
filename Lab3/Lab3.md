# 						COMP9331 LAB 03 

#### 																												YUAN GAO Z5239220

### **Exercise 3: Digging into DNS **

>```powershell
>weber % dig www.eecs.berkeley.edu A
>
>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> www.eecs.berkeley.edu A
>;; global options: +cmd
>;; Got answer:
>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50319
>;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 4, ADDITIONAL: 6
>
>;; OPT PSEUDOSECTION:
>; EDNS: version: 0, flags:; udp: 4096
>;; QUESTION SECTION:
>;www.eecs.berkeley.edu.		IN	A
>
>;; ANSWER SECTION:
>www.eecs.berkeley.edu.	72217	IN	CNAME	live-eecs.pantheonsite.io.
>live-eecs.pantheonsite.io. 600	IN	CNAME	fe1.edge.pantheon.io.
>fe1.edge.pantheon.io.	27	IN	A	23.185.0.1
>
>;; AUTHORITY SECTION:
>pantheon.io.		8037	IN	NS	ns-1096.awsdns-09.org.
>pantheon.io.		8037	IN	NS	ns-924.awsdns-51.net.
>pantheon.io.		8037	IN	NS	ns-1857.awsdns-40.co.uk.
>pantheon.io.		8037	IN	NS	ns-148.awsdns-18.com.
>
>;; ADDITIONAL SECTION:
>ns-148.awsdns-18.com.	97716	IN	A	205.251.192.148
>ns-924.awsdns-51.net.	159800	IN	A	205.251.195.156
>ns-924.awsdns-51.net.	74987	IN	AAAA	2600:9000:5303:9c00::1
>ns-1096.awsdns-09.org.	158128	IN	A	205.251.196.72
>ns-1857.awsdns-40.co.uk. 163762	IN	A	205.251.199.65
>
>;; Query time: 24 msec
>;; SERVER: 129.94.242.2#53(129.94.242.2)
>;; WHEN: Tue Oct 06 15:49:49 AEDT 2020
>;; MSG SIZE  rcvd: 369
>```
>
>According to the above code:
>
>**Question 1**
>
>>+ The IP address is `23.185.0.1`
>>
>>+ The type of DNS query is `A`.
>
>**Question 2**
>
>>+ The canonical name for the eecs.berkeley web server is `live-eecs.pantheonsite.io.`
>>
>>+ Using alias because they are easier to remember by clinets.
>
>**Question 3**
>
>>According to ` AUTHORITY SECTION` and  `ADDITIONAL SECTION:` `
>>
>>+ `NS` records domain name.
>>+ `A` records IPv4 addresses.
>>+ `AAAA` records IPv6 addresses.
>
>**Question 4**
>
>>+ The local nameserver for cse is `129.94.242.2`
>
>**Question 5**
>
>>```powershell
>>weber % dig eecs.berkeley.edu NS
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> eecs.berkeley.edu NS
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 22447
>>;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 9
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;eecs.berkeley.edu.		IN	NS
>>
>>;; ANSWER SECTION:
>>eecs.berkeley.edu.	9535	IN	NS	adns3.berkeley.edu.
>>eecs.berkeley.edu.	9535	IN	NS	ns.CS.berkeley.edu.
>>eecs.berkeley.edu.	9535	IN	NS	adns1.berkeley.edu.
>>eecs.berkeley.edu.	9535	IN	NS	ns.eecs.berkeley.edu.
>>eecs.berkeley.edu.	9535	IN	NS	adns2.berkeley.edu.
>>
>>;; ADDITIONAL SECTION:
>>ns.CS.berkeley.edu.	28593	IN	A	169.229.60.61
>>ns.eecs.berkeley.edu.	28593	IN	A	169.229.60.153
>>adns1.berkeley.edu.	5070	IN	A	128.32.136.3
>>adns1.berkeley.edu.	5070	IN	AAAA	2607:f140:ffff:fffe::3
>>adns2.berkeley.edu.	5070	IN	A	128.32.136.14
>>adns2.berkeley.edu.	5070	IN	AAAA	2607:f140:ffff:fffe::e
>>adns3.berkeley.edu.	5239	IN	A	192.107.102.142
>>adns3.berkeley.edu.	5240	IN	AAAA	2607:f140:a000:d::abc
>>
>>;; Query time: 0 msec
>>;; SERVER: 129.94.242.2#53(129.94.242.2)
>>;; WHEN: Tue Oct 06 16:30:44 AEDT 2020
>>;; MSG SIZE  rcvd: 307
>>```
>>
>>+ The DNS nameserver are:
>>
>>  >`adns3.berkeley.edu.`
>>  >`ns.CS.berkeley.edu.`
>>  >`adns1.berkeley.edu.`
>>  >`ns.eecs.berkeley.edu.`
>>  >`adns2.berkeley.edu.`
>>
>>+ The IP address of these server are:
>>
>>  >`169.229.60.61`  (IPv4)
>>  >`169.229.60.153`  (IPv4)
>>  >`128.32.136.3`  (IPv4)
>>  >`2607:f140:ffff:fffe::3`  (IPv6)
>>  >`128.32.136.14`  (IPv4)
>>  >`2607:f140:ffff:fffe::e`  (IPv6)
>>  >`192.107.102.142`  (IPv4)
>>  >`2607:f140:a000:d::abc`  (IPv6)
>
>**Question 6**
>
>>```powershell
>>weber % dig -x 111.68.101.54
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> -x 111.68.101.54
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50127
>>;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 2, ADDITIONAL: 3
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;54.101.68.111.in-addr.arpa.	IN	PTR
>>
>>;; ANSWER SECTION:
>>54.101.68.111.in-addr.arpa. 2274 IN	PTR	webserver.seecs.nust.edu.pk.
>>
>>;; AUTHORITY SECTION:
>>101.68.111.in-addr.arpa. 22917	IN	NS	ns2.hec.gov.pk.
>>101.68.111.in-addr.arpa. 22917	IN	NS	ns1.hec.gov.pk.
>>
>>;; ADDITIONAL SECTION:
>>ns1.hec.gov.pk.		2274	IN	A	103.4.93.5
>>ns2.hec.gov.pk.		2274	IN	A	103.4.93.6
>>
>>;; Query time: 0 msec
>>;; SERVER: 129.94.242.2#53(129.94.242.2)
>>;; WHEN: Tue Oct 06 16:45:05 AEDT 2020
>>;; MSG SIZE  rcvd: 172
>>```
>>
>>+ The DNS name associated with the IP address 111.68.101.54 is `webserver.seecs.nust.edu.pk.`
>>+ Run ` dig -x 111.68.101.54`, the information is above of code.
>
>**Question 7**
>
>>```powershell
>>weber % dig @129.94.242.33 yahoo.com MX
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @129.94.242.33 yahoo.com MX
>>; (1 server found)
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43686
>>;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 10
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;yahoo.com.			IN	MX
>>
>>;; ANSWER SECTION:
>>yahoo.com.		1011	IN	MX	1 mta7.am0.yahoodns.net.
>>yahoo.com.		1011	IN	MX	1 mta5.am0.yahoodns.net.
>>yahoo.com.		1011	IN	MX	1 mta6.am0.yahoodns.net.
>>
>>;; AUTHORITY SECTION:
>>yahoo.com.		66085	IN	NS	ns4.yahoo.com.
>>yahoo.com.		66085	IN	NS	ns2.yahoo.com.
>>yahoo.com.		66085	IN	NS	ns1.yahoo.com.
>>yahoo.com.		66085	IN	NS	ns5.yahoo.com.
>>yahoo.com.		66085	IN	NS	ns3.yahoo.com.
>>
>>;; ADDITIONAL SECTION:
>>ns1.yahoo.com.		578933	IN	A	68.180.131.16
>>ns1.yahoo.com.		658	IN	AAAA	2001:4998:130::1001
>>ns2.yahoo.com.		596360	IN	A	68.142.255.16
>>ns2.yahoo.com.		94710	IN	AAAA	2001:4998:140::1002
>>ns3.yahoo.com.		1106	IN	A	27.123.42.42
>>ns3.yahoo.com.		1106	IN	AAAA	2406:8600:f03f:1f8::1003
>>ns4.yahoo.com.		105322	IN	A	98.138.11.157
>>ns5.yahoo.com.		23405	IN	A	202.165.97.53
>>ns5.yahoo.com.		23405	IN	AAAA	2406:2000:ff60::53
>>
>>;; Query time: 0 msec
>>;; SERVER: 129.94.242.33#53(129.94.242.33)
>>;; WHEN: Tue Oct 06 17:01:41 AEDT 2020
>>;; MSG SIZE  rcvd: 399
>>```
>>
>>+ No, the information of above code dose not have authoritative answer.
>>+ This is because this IP address only has CSE domain, but does not have Yahoo domain
>
>**Question 8**
>
>>```powershell
>>weber % dig @adns3.berkeley.edu yahoo.com MX
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @adns3.berkeley.edu yahoo.com MX
>>; (2 servers found)
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: REFUSED, id: 62994
>>;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
>>;; WARNING: recursion requested but not available
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;yahoo.com.			IN	MX
>>
>>;; Query time: 167 msec
>>;; SERVER: 192.107.102.142#53(192.107.102.142)
>>;; WHEN: Tue Oct 06 17:12:19 AEDT 2020
>>;; MSG SIZE  rcvd: 38
>>```
>>
>>+ They are not available
>
>**Question 9**
>
>>+ Run `dig yahoo.com NS`, we can get the one of IP address is `68.180.131.16`
>>
>>+ Run `dig @68.180.131.16 yahoo.com MX`
>>
>>  >```powershell
>>  >weber % dig @68.180.131.16 yahoo.com MX
>>  >
>>  >; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @68.180.131.16 yahoo.com MX
>>  >; (1 server found)
>>  >;; global options: +cmd
>>  >;; Got answer:
>>  >;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 40271
>>  >;; flags: qr aa rd; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 10
>>  >;; WARNING: recursion requested but not available
>>  >
>>  >;; OPT PSEUDOSECTION:
>>  >; EDNS: version: 0, flags:; udp: 1272
>>  >;; QUESTION SECTION:
>>  >;yahoo.com.			IN	MX
>>  >
>>  >;; ANSWER SECTION:
>>  >yahoo.com.		1800	IN	MX	1 mta5.am0.yahoodns.net.
>>  >yahoo.com.		1800	IN	MX	1 mta6.am0.yahoodns.net.
>>  >yahoo.com.		1800	IN	MX	1 mta7.am0.yahoodns.net.
>>  >
>>  >;; AUTHORITY SECTION:
>>  >yahoo.com.		172800	IN	NS	ns3.yahoo.com.
>>  >yahoo.com.		172800	IN	NS	ns2.yahoo.com.
>>  >yahoo.com.		172800	IN	NS	ns4.yahoo.com.
>>  >yahoo.com.		172800	IN	NS	ns1.yahoo.com.
>>  >yahoo.com.		172800	IN	NS	ns5.yahoo.com.
>>  >
>>  >;; ADDITIONAL SECTION:
>>  >ns1.yahoo.com.		1209600	IN	A	68.180.131.16
>>  >ns2.yahoo.com.		1209600	IN	A	68.142.255.16
>>  >ns3.yahoo.com.		1800	IN	A	27.123.42.42
>>  >ns4.yahoo.com.		1209600	IN	A	98.138.11.157
>>  >ns5.yahoo.com.		86400	IN	A	202.165.97.53
>>  >ns1.yahoo.com.		86400	IN	AAAA	2001:4998:130::1001
>>  >ns2.yahoo.com.		86400	IN	AAAA	2001:4998:140::1002
>>  >ns3.yahoo.com.		1800	IN	AAAA	2406:8600:f03f:1f8::1003
>>  >ns5.yahoo.com.		86400	IN	AAAA	2406:2000:ff60::53
>>  >
>>  >;; Query time: 145 msec
>>  >;; SERVER: 68.180.131.16#53(68.180.131.16)
>>  >;; WHEN: Tue Oct 06 17:20:09 AEDT 2020
>>  >;; MSG SIZE  rcvd: 399
>>  >```
>>
>>+ The type of DNS is `MX`
>
>**Question 10**
>
>>The following steps are:
>>
>>```powershell
>>weber % dig . NS
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> . NS
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 35305
>>;; flags: qr rd ra; QUERY: 1, ANSWER: 13, AUTHORITY: 0, ADDITIONAL: 27
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;.				IN	NS
>>
>>;; ANSWER SECTION:
>>.			317667	IN	NS	i.root-servers.net.
>>.			317667	IN	NS	e.root-servers.net.
>>.			317667	IN	NS	k.root-servers.net.
>>.			317667	IN	NS	h.root-servers.net.
>>.			317667	IN	NS	c.root-servers.net.
>>.			317667	IN	NS	g.root-servers.net.
>>.			317667	IN	NS	l.root-servers.net.
>>.			317667	IN	NS	f.root-servers.net.
>>.			317667	IN	NS	j.root-servers.net.
>>.			317667	IN	NS	a.root-servers.net.
>>.			317667	IN	NS	d.root-servers.net.
>>.			317667	IN	NS	b.root-servers.net.
>>.			317667	IN	NS	m.root-servers.net.
>>
>>;; ADDITIONAL SECTION:
>>a.root-servers.net.	83589	IN	A	198.41.0.4
>>a.root-servers.net.	83589	IN	AAAA	2001:503:ba3e::2:30
>>b.root-servers.net.	11594	IN	A	199.9.14.201
>>b.root-servers.net.	421655	IN	AAAA	2001:500:200::b
>>c.root-servers.net.	536195	IN	A	192.33.4.12
>>c.root-servers.net.	536195	IN	AAAA	2001:500:2::c
>>d.root-servers.net.	536195	IN	A	199.7.91.13
>>d.root-servers.net.	536195	IN	AAAA	2001:500:2d::d
>>e.root-servers.net.	3438	IN	A	192.203.230.10
>>e.root-servers.net.	43178	IN	AAAA	2001:500:a8::e
>>f.root-servers.net.	7063	IN	A	192.5.5.241
>>f.root-servers.net.	421655	IN	AAAA	2001:500:2f::f
>>g.root-servers.net.	13765	IN	A	192.112.36.4
>>g.root-servers.net.	421655	IN	AAAA	2001:500:12::d0d
>>h.root-servers.net.	188897	IN	A	198.97.190.53
>>h.root-servers.net.	421654	IN	AAAA	2001:500:1::53
>>i.root-servers.net.	601833	IN	A	192.36.148.17
>>i.root-servers.net.	601833	IN	AAAA	2001:7fe::53
>>j.root-servers.net.	164470	IN	A	192.58.128.30
>>j.root-servers.net.	93302	IN	AAAA	2001:503:c27::2:30
>>k.root-servers.net.	170229	IN	A	193.0.14.129
>>k.root-servers.net.	93302	IN	AAAA	2001:7fd::1
>>l.root-servers.net.	11594	IN	A	199.7.83.42
>>l.root-servers.net.	421654	IN	AAAA	2001:500:9f::42
>>m.root-servers.net.	183241	IN	A	202.12.27.33
>>m.root-servers.net.	421654	IN	AAAA	2001:dc3::35
>>
>>;; Query time: 0 msec
>>;; SERVER: 129.94.242.2#53(129.94.242.2)
>>;; WHEN: Tue Oct 06 17:25:36 AEDT 2020
>>;; MSG SIZE  rcvd: 811
>>```
>>
>>
>>
>>```powershell
>>weber % dig @198.41.0.4 lyre00.cse.unsw.edu.au
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @198.41.0.4 lyre00.cse.unsw.edu.au
>>; (1 server found)
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 65502
>>;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 9, ADDITIONAL: 19
>>;; WARNING: recursion requested but not available
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;lyre00.cse.unsw.edu.au.		IN	A
>>
>>;; AUTHORITY SECTION:
>>au.			172800	IN	NS	m.au.
>>au.			172800	IN	NS	d.au.
>>au.			172800	IN	NS	q.au.
>>au.			172800	IN	NS	t.au.
>>au.			172800	IN	NS	s.au.
>>au.			172800	IN	NS	r.au.
>>au.			172800	IN	NS	n.au.
>>au.			172800	IN	NS	a.au.
>>au.			172800	IN	NS	c.au.
>>
>>;; ADDITIONAL SECTION:
>>m.au.			172800	IN	A	156.154.100.24
>>m.au.			172800	IN	AAAA	2001:502:2eda::24
>>d.au.			172800	IN	A	162.159.25.38
>>d.au.			172800	IN	AAAA	2400:cb00:2049:1::a29f:1926
>>q.au.			172800	IN	A	65.22.196.1
>>q.au.			172800	IN	AAAA	2a01:8840:be::1
>>t.au.			172800	IN	A	65.22.199.1
>>t.au.			172800	IN	AAAA	2a01:8840:c1::1
>>s.au.			172800	IN	A	65.22.198.1
>>s.au.			172800	IN	AAAA	2a01:8840:c0::1
>>r.au.			172800	IN	A	65.22.197.1
>>r.au.			172800	IN	AAAA	2a01:8840:bf::1
>>n.au.			172800	IN	A	156.154.101.24
>>n.au.			172800	IN	AAAA	2001:502:ad09::24
>>a.au.			172800	IN	A	58.65.254.73
>>a.au.			172800	IN	AAAA	2407:6e00:254:306::73
>>c.au.			172800	IN	A	162.159.24.179
>>c.au.			172800	IN	AAAA	2400:cb00:2049:1::a29f:18b3
>>
>>;; Query time: 118 msec
>>;; SERVER: 198.41.0.4#53(198.41.0.4)
>>;; WHEN: Tue Oct 06 17:29:53 AEDT 2020
>>;; MSG SIZE  rcvd: 591
>>```
>>
>>
>>
>>```powershell
>>weber % dig @156.154.100.24 lyre00.cse.unsw.edu.au
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @156.154.100.24 lyre00.cse.unsw.edu.au
>>; (1 server found)
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29021
>>;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 4, ADDITIONAL: 9
>>;; WARNING: recursion requested but not available
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;lyre00.cse.unsw.edu.au.		IN	A
>>
>>;; AUTHORITY SECTION:
>>edu.au.			86400	IN	NS	s.au.
>>edu.au.			86400	IN	NS	q.au.
>>edu.au.			86400	IN	NS	r.au.
>>edu.au.			86400	IN	NS	t.au.
>>
>>;; ADDITIONAL SECTION:
>>q.au.			86400	IN	A	65.22.196.1
>>r.au.			86400	IN	A	65.22.197.1
>>s.au.			86400	IN	A	65.22.198.1
>>t.au.			86400	IN	A	65.22.199.1
>>q.au.			86400	IN	AAAA	2a01:8840:be::1
>>r.au.			86400	IN	AAAA	2a01:8840:bf::1
>>s.au.			86400	IN	AAAA	2a01:8840:c0::1
>>t.au.			86400	IN	AAAA	2a01:8840:c1::1
>>
>>;; Query time: 14 msec
>>;; SERVER: 156.154.100.24#53(156.154.100.24)
>>;; WHEN: Tue Oct 06 17:31:37 AEDT 2020
>>;; MSG SIZE  rcvd: 291
>>```
>>
>>
>>
>>```powershell
>>weber % dig @65.22.196.1 lyre00.cse.unsw.edu.au
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @65.22.196.1 lyre00.cse.unsw.edu.au
>>; (1 server found)
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63906
>>;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 3, ADDITIONAL: 6
>>;; WARNING: recursion requested but not available
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;lyre00.cse.unsw.edu.au.		IN	A
>>
>>;; AUTHORITY SECTION:
>>unsw.edu.au.		900	IN	NS	ns2.unsw.edu.au.
>>unsw.edu.au.		900	IN	NS	ns1.unsw.edu.au.
>>unsw.edu.au.		900	IN	NS	ns3.unsw.edu.au.
>>
>>;; ADDITIONAL SECTION:
>>ns1.unsw.edu.au.	900	IN	A	129.94.0.192
>>ns2.unsw.edu.au.	900	IN	A	129.94.0.193
>>ns3.unsw.edu.au.	900	IN	A	192.155.82.178
>>ns1.unsw.edu.au.	900	IN	AAAA	2001:388:c:35::1
>>ns2.unsw.edu.au.	900	IN	AAAA	2001:388:c:35::2
>>
>>;; Query time: 24 msec
>>;; SERVER: 65.22.196.1#53(65.22.196.1)
>>;; WHEN: Tue Oct 06 17:32:44 AEDT 2020
>>;; MSG SIZE  rcvd: 209
>>```
>>
>>
>>
>>```powershell
>>weber % dig @129.94.0.192 lyre00.cse.unsw.edu.au
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @129.94.0.192 lyre00.cse.unsw.edu.au
>>; (1 server found)
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49739
>>;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 2, ADDITIONAL: 5
>>;; WARNING: recursion requested but not available
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;lyre00.cse.unsw.edu.au.		IN	A
>>
>>;; AUTHORITY SECTION:
>>cse.unsw.edu.au.	10800	IN	NS	beethoven.orchestra.cse.unsw.edu.au.
>>cse.unsw.edu.au.	10800	IN	NS	maestro.orchestra.cse.unsw.edu.au.
>>
>>;; ADDITIONAL SECTION:
>>beethoven.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.242.2
>>beethoven.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.172.11
>>beethoven.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.208.3
>>maestro.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.242.33
>>
>>;; Query time: 3 msec
>>;; SERVER: 129.94.0.192#53(129.94.0.192)
>>;; WHEN: Tue Oct 06 17:34:27 AEDT 2020
>>;; MSG SIZE  rcvd: 171
>>```
>>
>>
>>
>>```powershell
>>weber % dig @129.94.242.2 lyre00.cse.unsw.edu.au
>>
>>; <<>> DiG 9.9.5-9+deb8u19-Debian <<>> @129.94.242.2 lyre00.cse.unsw.edu.au
>>; (1 server found)
>>;; global options: +cmd
>>;; Got answer:
>>;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12396
>>;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 2, ADDITIONAL: 3
>>
>>;; OPT PSEUDOSECTION:
>>; EDNS: version: 0, flags:; udp: 4096
>>;; QUESTION SECTION:
>>;lyre00.cse.unsw.edu.au.		IN	A
>>
>>;; ANSWER SECTION:
>>lyre00.cse.unsw.edu.au.	3600	IN	A	129.94.210.20
>>
>>;; AUTHORITY SECTION:
>>cse.unsw.edu.au.	3600	IN	NS	beethoven.orchestra.cse.unsw.edu.au.
>>cse.unsw.edu.au.	3600	IN	NS	maestro.orchestra.cse.unsw.edu.au.
>>
>>;; ADDITIONAL SECTION:
>>maestro.orchestra.cse.unsw.edu.au. 3600	IN A	129.94.242.33
>>beethoven.orchestra.cse.unsw.edu.au. 3600 IN A	129.94.242.2
>>
>>;; Query time: 0 msec
>>;; SERVER: 129.94.242.2#53(129.94.242.2)
>>;; WHEN: Tue Oct 06 17:35:31 AEDT 2020
>>;; MSG SIZE  rcvd: 155
>>```
>
>**Question 11**
>
>>Yes, a physical machine could have several network interfaces.

### **Exercise 4: A Simple Web Server**

>+ http://127.0.0.1:5001/index.html
>
>  ><img src="/Users/yuan/Desktop/截屏2020-10-07 下午5.10.55.png" alt="截屏2020-10-07 下午5.10.55" style="zoom:50%;" />
>  >
>  ><img src="/Users/yuan/Desktop/截屏2020-10-07 下午5.11.20.png" alt="截屏2020-10-07 下午5.11.20" style="zoom:50%;" />
>
>+ http://127.0.0.1:5001/myimage.png
>
>  ><img src="/Users/yuan/Desktop/截屏2020-10-07 下午5.12.22.png" alt="截屏2020-10-07 下午5.12.22" style="zoom:50%;" />
>  >
>  ><img src="/Users/yuan/Desktop/截屏2020-10-07 下午5.13.33.png" alt="截屏2020-10-07 下午5.13.33" style="zoom:50%;" />
>
>+ http://127.0.0.1:5001/bio.html
>
>  >![截屏2020-10-07 下午5.12.56](/Users/yuan/Desktop/截屏2020-10-07 下午5.12.56.png)
>  >
>  ><img src="/Users/yuan/Desktop/截屏2020-10-07 下午5.13.50.png" alt="截屏2020-10-07 下午5.13.50" style="zoom:50%;" />

