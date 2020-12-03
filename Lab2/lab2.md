# 						COMP9331 LAB 02 

#### 																												YUAN GAO Z5239220

---

#### **Exercise 3: Using Wireshark to understand basic HTTP request/response messages**

>![截屏2020-09-29 下午11.31.17](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-29 下午11.31.17.png)
>
>**Question 1**
>
>>According to the graph:
>>
>>+ `Status Conde: 200`
>>
>>+ `Response Phrase: OK`
>
>**Question 2**
>
>>According to the graph:
>>
>>+ Last modified at the server:
>>
>>   `Last-Modified: Tue, 23 Sep 2003 05:29:00 GMT\r\n`
>>
>>+ Yes, the response contains a DATE header:
>>
>>   `Date: Tue, 23 Sep 2003 05:29:50 GMT\r\n`
>>
>>+ `Data:` indicates response time from server to client.
>>
>>  `Last-Modified:` indicates the last modified time of data.
>
>**Question 3**
>
>>+  The connection established between the browser and the server persistent is persistent. Because in `Connection:` line, the status is `Keep-Alive\r\n`
>
>**Question 4**
>
>>+ According to `Content-Length: 73\r\n` line,  there are 73 bytes of content are being returned to the browser
>
>**Question 5**
>
>> ![截屏2020-09-29 下午11.36.27](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-29 下午11.36.27.png)
>>
>> + Accprding to `Line-based text data: ` line, the data contained inside the HTTP response packet is `Congratulations.  You've downloaded the file lab2-1.html!`



#### **Exercise 4: Using Wireshark to understand the HTTP CONDITIONAL GET/response interaction**

>![截屏2020-09-29 下午11.46.51](/Users/yuan/Desktop/截屏2020-09-29 下午11.46.51.png)
>
>**Question 1**
>
>>+ No, because it is may the first request.
>
>**Question 2**
>
>>+ Yes, thr last modified is:
>>
>>  `Tue, 23 Sep 2003 05:35:00 GMT\r\n`
>
>**Question 3**
>
>> ![截屏2020-09-29 下午11.49.41](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-29 下午11.49.41.png)
>>
>> + Yes, according to the graph, we can see these two line.
>>
>> + The information contained in these header lines is:
>>
>>   `If-Modified-Since: Tue, 23 Sep 2003 05:35:00 GMT\r\n`
>>
>>   `If-None-Match: "1bfef-173-8f4ae900"\r\n`
>
>**Question 4**
>
>>![截屏2020-09-29 下午11.55.08](/Users/yuan/Library/Application Support/typora-user-images/截屏2020-09-29 下午11.55.08.png)
>>
>>+ According to the graph:
>>
>>  The HTTP status code `304`
>>
>>  Phrase returned from the server in response is `Not Modified`
>>
>>+ No, because the last request was not modified in server.
>
>**Question 5**
>
>>+ According to the graph, the ETag value is:
>>
>>  `ETag: "1bfef-173-8f4ae900"\r\n`
>>
>>+ This value has not changed since the $1^{st}$ response message was received.





#### **Exercise 5: Ping Client**

>**Client message: **
>
><img src="/Users/yuan/Desktop/截屏2020-10-01 上午12.49.09.png" alt="截屏2020-10-01 上午12.49.09" style="zoom:90%;" />
>
>**Server message: **
>
><img src="/Users/yuan/Desktop/截屏2020-10-01 上午12.49.18.png" alt="截屏2020-10-01 上午12.49.18" style="zoom:75%;" />

