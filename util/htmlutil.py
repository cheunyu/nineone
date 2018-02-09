from bs4 import BeautifulSoup
import httputil


class Parse(object):
    """docstring for Parse"""

    def __init__(self):
        super(Parse, self).__init__()
        self.http_util = httputil.HttpUtil()

    def get_all_video_info(self):
        url = 'http://91.91p26.space/v.php?next=watch&page='
        video_info = []
        for each in range(1, 2):
            html = self.http_util.request_page(url + str(each))
            soup = BeautifulSoup(html, 'lxml')
            listchannel = soup.select('[class=listchannel]')
            for each in listchannel:
                info = {}
                info['url'] = each.a['href']
                info['title'] = each.a.img.attrs['title']
                html_info = ''.join(each.text.split())
                info['runtime'] = html_info[
                    html_info.index('时长:') + 3:html_info.index('添加')]
                info['views'] = html_info[html_info.index(
                    '查看:') + 3:html_info.index('收藏')]
                info['favorites'] = html_info[
                    html_info.index('收藏:') + 3:html_info.index('留言')]
                info['comments'] = html_info[
                    html_info.index('留言:') + 3:html_info.index('积分')]

                html_rate = each.select('[width=11]')
                nice = 'full'
                nice_rate = 0
                if len(html_rate) != 0:
                    for i in html_rate:
                        if nice in i['src']:
                            nice_rate += 1
                info['rate'] = nice_rate
                video_info.append(info)
        return video_info

    def get_video_url(self):
        parse = Parse()
        video_info = parse.get_all_video_info()
        for each in video_info:
            html = self.http_util.request_page(each['url'])
            soup = BeautifulSoup(html, 'lxml')
            guest_flag = '作为游客'
            if guest_flag in html:
                print('无权限')
            # print(html)
            # mp4_url = soup.select('source')[0].attrs['src']
            # print(mp4_url)

if __name__ == '__main__':
    parse = Parse()
    parse.get_video_url()
