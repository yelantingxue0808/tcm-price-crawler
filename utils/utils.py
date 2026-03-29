import asyncio
from core import handlers
from config import settings
import os


async def batch_fetch(url_list):
    """
    协程批量执行
    """
    tasks = [handlers.fetch_page(url) for url in url_list]
    data_list = await asyncio.gather(*tasks)
    all_data = []
    for data in data_list:
        all_data.extend(data)
    return all_data


def get_all_urls():
    """
    生成 1~122 页 URL
    """
    urls = []
    for page in range(settings.PageConfig.START + 1, settings.PageConfig.STOP + 1):
        url = settings.URL_POSITION.format(page)
        urls.append(url)
    return urls


def split_urls():
    """
    把URL分成4组，给多进程使用
    """
    urls = get_all_urls()
    # 将总页数分片，分成四组
    return [urls[index:index + settings.PageConfig.STEP] for index in
            range(settings.PageConfig.START, settings.PageConfig.STOP, settings.PageConfig.STEP)]


def get_urls_and_files():
    urls_groups = split_urls()
    file_paths = []
    if not os.path.exists('./data'):
        os.mkdir('./data')
    for num in range(len(urls_groups)):
        file_path = settings.DATE_PATH.format(num+1, 'xlsx' if settings.FileType.CSV else 'csv')
        file_paths.append(file_path)
    return urls_groups, file_paths
