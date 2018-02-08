import urllib.request

class HttpUtil(object):
	"""http工具包"""
	def __init__(self, url):
		super(HttpUtil, self).__init__()
		self.url = url
	
	def login(self):
		headers = {
			'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
			'Referer':'https://www.google.com.hk/',
			'Connection':'keep-alive',
			'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
		}
		req = urllib.request.Request(self.url, headers=headers)
		urllib.request.urlopen(req)

if __name__ == '__main__':
	http_util = HttpUtil('http://www.baidu.com')
	http_util.login()