import requests
from django.core.management.base import BaseCommand, CommandError

from Yaocai.models import Yaocai
import requests
from bs4 import BeautifulSoup
import chardet
from loguru import logger
from Yaocai.models import Yaocai, CategoryType


# from polls.models import Poll  自己的

class Command(BaseCommand):
    help = '用来爬取中药材相关信息'

    def handle(self, *args, **options):
        res = requests.get('http://www.cnzyao.com/yaocai/')
        encoding = chardet.detect(res.content)['encoding']
        result = res.content.decode(encoding)

        # 假设整个HTML页面内容保存在变量html中
        # 创建BeautifulSoup对象
        soup = BeautifulSoup(result, 'html.parser')

        # 使用CSS选择器选取所有class为order_xingtai的h2元素
        elements = soup.select('h2.order_xingtai')

        # href_list = []
        item_list = []
        # 遍历每个元素
        for element in elements:
            # 获取a标签
            a_tag = element.find('a')
            # 如果a标签存在
            if a_tag:
                # 获取href链接
                href = a_tag.get('href')
                # 获取文本
                title = a_tag.get_text()
                item = {"href": href, "title": title}
                item_list.append(item)
                # text_list.append(text)

        # 生成CategoryType类对象
        for i in range(len(item_list)):
            # 从数据库中获取，看是否存在,不存在就添加
            title = item_list[i]['title']
            if CategoryType.objects.filter(title=title).exists():
                pass
            else:
                categoryType = CategoryType()
                categoryType.title = title
                categoryType.save()

        # 依次遍历每个分类下的药材
        for item in item_list:
            # 获取item['title']对应的CategoryType
            categoryType = CategoryType.objects.get(title=item['title'])

            # 获取分类下药材清单
            yaocai_list = []
            res = requests.get(item['href'])
            encoding = chardet.detect(res.content)['encoding']
            result = res.content.decode(encoding)
            # 获取
            soup = BeautifulSoup(result, 'html.parser')
            yaocaibox2 = soup.find('div', {'class': 'yaocaibox2'})
            for link in yaocaibox2.find_all('a'):
                yaocai_list.append({'href': "http://www.cnzyao.com" + link.get('href'), 'yaocai_name': link.text})

            # 遍历药材生成药材对象
            for obj in yaocai_list:
                res = requests.get(obj['href'])
                encoding = chardet.detect(res.content)['encoding']
                result = res.content.decode(encoding)
                soup = BeautifulSoup(result, 'html.parser')
                # 提取 class="arcbody" 的 div 元素
                arcbody = soup.find('div', {'class': 'arcbody'})
                # print(arcbody)
                # 遍历 dl 元素
                feature_content = None
                img_url = None
                # 找到 class 为 "picview" 的 span 元素
                try:
                    picview_span = soup.find('span', {'class': 'picview'})
                    img = picview_span.find('img')
                    img_url = "http://www.cnzyao.com" + img.get('src')
                    for dl in arcbody.find_all('dl'):
                        dt = dl.find('dt')
                        if dt and dt.text.strip() == '【用法用量】：':
                            dd = dl.find('dd')
                            if dd:
                                feature_content = dd.text.strip()
                                break
                except Exception as e:
                    logger.info(obj['href'])
                    pass

                if feature_content:
                    # 生成对应的药材
                    Yaocai.objects.create(name=obj['yaocai_name'], description=feature_content,
                                          categoryType=categoryType, image=img_url)
        self.stdout.write('爬取完毕')
