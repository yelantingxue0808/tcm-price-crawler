import asyncio
import aiohttp
from lxml import etree
from config import http_settings
from utils import logger
from utils import utils
from save_data import dao


async def fetch_page(url):
    """
    异步请求 + 解析数据
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=http_settings.HEADERS, timeout=10) as resp:
            html = await resp.text()
            await asyncio.sleep(0.1)
            tree = etree.HTML(html)
            tr_list = tree.xpath('//div[@class="price-list"]/table/tbody/tr')
            result = []

            for tr in tr_list:
                item = {}
                tds = tr.xpath('./td')[:8]
                item["品名"] = tds[0].xpath('.//a/text()')[0]
                item["规格"] = tds[1].xpath('.//a/text()')[0]
                item["市场"] = tds[2].xpath('.//text()')[0].strip()
                item["价格"] = tds[3].xpath('.//text()')[0].strip()
                item["趋势"] = tds[4].xpath('.//text()')[0].strip()
                item["周涨跌"] = tds[5].xpath('.//text()')[0].strip()
                item["月涨跌"] = tds[6].xpath('.//text()')[0].strip()
                item["年涨跌"] = tds[7].xpath('.//text()')[0].strip()
                result.append(item)

            logger.logger.debug(f'完成{url}的数据抓取')
            return result


def task_process(url_group, filename):
    """
    每个进程执行的任务
    """
    data = asyncio.run(utils.batch_fetch(url_group))
    dao.save_to_excel(data, filename)
