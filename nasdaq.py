# coding: utf8

#for 胡大仙，中美合拍，菊逼两开花

#todo: win10/python3.6调试跑过， 如是linux，errorStr需要对应调整，可以放在crontab跑，循环要改一下，延时超过60ms没做判断，请自行修改

import time,os,re

def pingComputer(host, statusFile):
	status1 = 'ping success'
	status2 = 'ping faild'
	errorStr = '请求超时'
	# for ipAdd in host:
	ipAdd = host
	for i in range(1440):
		print ("get: " +ipAdd + "  status")
		nowTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		p = os.popen("ping -n 1 " + ipAdd)
		line = p.read()

		_pattern = re.compile(r'(?<=\s时间=)\d*(?=ms\s)')
		m = _pattern.findall(line)

		print(m)

		statusString = status1 + " time=" + m[0] + "ms"

		if errorStr in line:
			# pass
			writeToText(nowTime, ipAdd, status2, statusFile)
		elif int(m[0]) > 100:
			writeToText(nowTime, ipAdd, statusString, statusFile)
		else:
			pass
			# writeToText(nowTime, ipAdd, status1, statusFile)

		time.sleep(0.5)
		
def writeToText(nowTime, ipAdd, status, statusFile):
	s_text = 'TIME:' + nowTime + '\t' + 'IP:' + ipAdd + '\t' + 'STATUS:' + status + '\r\n'
	if '0' == judgeFile(statusFile):
		with open(statusFile, 'a') as f:
			f.write(s_text)
			f.close()
	if '1' == judgeFile(statusFile):
		with open(statusFile, 'w') as f:
			f.write(s_text)
			f.close()
		
def judgeFile(statusFile):
	if os.path.exists(statusFile):
		return '0'
	else:
		return '1'
    
# if __name__ == "__main__":
# 	IpFirst = '192.168.201.'
# 	host = []
# 	for j in range(1,255):
#  		host.append(IpFirst + str(j))

# 	statusFile = 'e:/Status.txt'
# 	pingComputer(host, statusFile)

statusFile = 'e:/Status.txt'
pingComputer('steamcommunity.com', statusFile)