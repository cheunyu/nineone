from bs4 import BeautifulSoup
import urllib.request
import sys



def spider():
	url = 'http://91.91p26.space/v.php?next=watch'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
	headers = { 'User-Agent' : user_agent}
	data = urllib.parse.urlencode({'session_language':'cn_CN'}).encode('utf-8')
	req = urllib.request.Request(url=url, headers=headers)
	response = urllib.request.urlopen(req, data)
	html = response.read().decode('utf-8','ignore')
	soup = BeautifulSoup(html, "lxml")
	listchannel = soup.select('[class=listchannel]')
	# for each in listchannel:
	# 	print(each.a['href'])
	# 	print(each.a.img.attrs['title'])
	print(listchannel[0].a['href'])

	child_url = listchannel[0].a['href']
	req = urllib.request.Request(url=child_url, headers=headers)
	response = urllib.request.urlopen(req)
	child_html = response.read().decode('utf-8','ignore')
	child_soup = BeautifulSoup(child_html, "lxml")
	# print(child_html)
	# print(child_soup.select('[class=videoplayer]'))
	mp4_url = child_soup.select('source')[0].attrs['src']
	print(mp4_url)
	urllib.request.urlretrieve(mp4_url,r'd:\\'+listchannel[0].a.img.attrs['title']+'.mp4')
	print('download done')
def main():
    spider()

if __name__ == '__main__':
    main()
