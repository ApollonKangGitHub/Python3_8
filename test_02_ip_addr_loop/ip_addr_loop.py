#-----------------------------------------------------------------------
#    Time           :2020年5月27日22:20:28
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :python初体验，查找资料学习简单语法，写个循环逻辑
#    FileName       :ip_addr_loop.py
#-----------------------------------------------------------------------

#导出time库
import time

ip_addr_1_max = 255
ip_addr_2_max = 255
ip_addr_3_max = 255
ip_addr_4_max = 255

ip_addr_1 = 1
ip_addr_2 = 1
ip_addr_3 = 1
ip_addr_4 = 1

count = 0

#IP address 循环打印
while (ip_addr_1 <= ip_addr_1_max):
	ip_addr_2 = 1
	while (ip_addr_2 <= ip_addr_2_max):
		ip_addr_3 = 1
		while (ip_addr_3 <= ip_addr_3_max):
			ip_addr_4 = 1
			while (ip_addr_4 <= ip_addr_4_max):
				
				count += 1
				#使用str内置函数，以及字符串的相加拼接方式
				ip_addr = "ipaddr[" + str(count) + "] : " 
				ip_addr += str(ip_addr_1) + "." 
				ip_addr += str(ip_addr_2) + "." 
				ip_addr += str(ip_addr_3) + "." 
				ip_addr += str(ip_addr_4)
				
				print(ip_addr)
				time.sleep(0.00001)
				ip_addr_4 += 1
				
			ip_addr_3 += 1
		ip_addr_2 += 1
	ip_addr_1 += 1

