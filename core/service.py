from multiprocessing import Process
from utils import utils
from core import handlers
from utils import logger


def excute_task():
    process_list = []
    urls, file_paths = utils.get_urls_and_files()
    for url, file_path in zip(urls, file_paths):
        p = Process(target=handlers.task_process, args=(url, file_path))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()

    logger.logger.debug("全部爬取完成！")
