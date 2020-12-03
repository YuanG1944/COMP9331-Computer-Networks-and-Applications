# 						COMP9331 LAB 04

#### 																												YUAN GAO Z5239220

### **Exercise 1: Understanding TCP using Wireshark**

>#### ***Question 1***
>
>><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-10-30 上午8.19.46.png" alt="截屏2020-10-30 上午8.19.46" style="zoom:50%;" />
>>
>>+ The IP address of [<u>gaia.cs.umass.edu</u>]() is `128.119.245.12`
>>+ The port number of [gaia.cs.umass.edu]() is ` 80`
>>+ The client computer IP address is `192.168.1.102`
>>+ The client computer IP port number is  `1161`
>
>#### *Question 2*
>
>><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-10-30 上午8.24.35.png" alt="截屏2020-10-30 上午8.24.35" style="zoom:50%;" />
>>
>>+ The sequence number of the TCP segment containing the HTTP POST command is `232129013`
>
>#### *Question 3*
>
>>| Sequence Number | Send Time | ACK      | RTT      | EstimatedRtt |
>>| --------------- | --------- | -------- | -------- | ------------ |
>>| 232129013       | 0.026477  | 0.053937 | 0.027460 | 0.027460     |
>>| 232129578       | 0.041737  | 0.077294 | 0.035557 | 0.028472     |
>>| 232131038       | 0.054026  | 0.124085 | 0.070059 | 0.033670     |
>>| 232132498       | 0.054690  | 0.169118 | 0.114428 | 0.043765     |
>>| 232133958       | 0.077405  | 0.217299 | 0.139894 | 0.055781     |
>>| 232135418       | 0.078157  | 0.267802 | 0.189645 | 0.072514     |
>
>#### *Question 4*
>
>>| Sequence Number | Length |
>>| --------------- | ------ |
>>| 232129013       | 565    |
>>| 232129578       | 1460   |
>>| 232131038       | 1460   |
>>| 232132498       | 1460   |
>>| 232133958       | 1460   |
>>| 232135418       | 1460   |
>
>#### *Question 5*
>
>>![截屏2020-10-30 上午8.39.33](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-10-30 上午8.39.33.png)
>>
>>+ The minimum amount of available buffer space is 5840 bytes.
>>+ No, there is not flow control. The window size always more than 1460 bytes.
>
>#### *Question 6*
>
>><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-10-30 上午8.52.35.png" alt="截屏2020-10-30 上午8.52.35" style="zoom:50%;" />
>>
>>+ There is increasing line. Therefore, there is not any retransmitted segments in the trace file.
>>+ I check the TCP stream graph  ->  Time sequence (tcptrace)
>
>#### *Question 7*
>
>><img src="/Users/yuan/Library/Application Support/typora-user-images/截屏2020-10-30 上午9.10.57.png" alt="截屏2020-10-30 上午9.10.57" style="zoom:50%;" />
>>
>>+ The receiver typically acknowledge in an ACK is 1460
>>
>>| No.  | acknowledged sequence number | acknowledged data |
>>| ---- | ---------------------------- | ----------------- |
>>| 18   | 232138025                    | 1460              |
>>| 19   | 232139485                    | 1460              |
>>| 20   | 232140945                    | 1460              |
>>| 21   | 232142405                    | 1460              |
>>| 22   | 232143865                    | 1460              |
>
>#### *Question 8*
>
>>$$
>>Throughput = \frac{totalData}{time} = \frac{ (lastACK – firstSeq)}{time} = \frac{ (232293103 – 232129013)}{5.455803 – 0.026477} = 30222.904 byte/s
>>$$

### Exercise 2: TCP Connection Management

>#### *Question 1*
>
>>The sequence number is `2818463618`
>
>#### *Question 2*
>
>>+ The sequence number of the SYNACK segment is `2818463619`
>>+ The value of the Acknowledgement field in the SYNACK segment is `1247095790`
>>+ Server will send $ackNum = seqNum + 1$ to determine it have received the data.
>
>#### *Question 3*
>
>>+ The sequence number is 2818463619
>>+ The value of the acknowledgement field is the ACK number 1247095791.
>>+  There is no data contains.
>
>#### *Question 4*
>
>>+ Both client and server done the active close.
>>+ No.304 Seq == No.305 ACK
>>+ Simultaneous close
>
>#### Question 5
>
>>+ Client -> Server: $Data = lastAck - firstSeq - (SYN + FIN) = 33 \ bytes $
>>+ Server -> Client: $Data = lastAck - firstSeq - (SYN + FIN) = 40 \ bytes $
>>+ Relationship is:  $Data = lastAck - firstSeq - (SYN + FIN)$

