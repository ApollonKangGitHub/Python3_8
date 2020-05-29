#-----------------------------------------------------------------------
#    Time           :2020年5月29日22:19:29
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :对test_02_ip_addr_loop的ip地址遍历循环代码重构
#    FileName       :test_04_list_ip_addr_loop.py
#-----------------------------------------------------------------------

#导出time库
import time

count = 0
#IP address 循环打印
for ip_addr_1 in range(1,255):
	for ip_addr_2 in range(1,255):
		for ip_addr_3 in range(1,255):		
			for ip_addr_4 in range(1,255):
				count += 1
				#使用str内置函数，以及字符串的相加拼接方式
				ip_addr = "ipaddr[" + str(count) + "] : " 
				ip_addr += str(ip_addr_1) + "." 
				ip_addr += str(ip_addr_2) + "." 
				ip_addr += str(ip_addr_3) + "." 
				ip_addr += str(ip_addr_4)
				
				print(ip_addr)
				time.sleep(0.00001)

