import logging
import os
from config import logging_settings


logger = logging.getLogger(logging_settings.LOGGER_NAME)
logger.setLevel(level=logging.DEBUG)

if not os.path.exists(logging_settings.LOGGER_DIR_PATH):
    os.mkdir(logging_settings.LOGGER_DIR_PATH)

# 创建处理器 输出到文件中+控制台
file_handler = logging.FileHandler(filename=logging_settings.LOGGER_FILE_PATH, mode='a',
                                   encoding='utf-8')
console_handler = logging.StreamHandler()

# 将输出的文件写入到log文件夹中
# 创建日志格式
formatter = '%(asctime)s-%(levelname)s-%(name)s : %(message)s'
file_handler.setFormatter(logging.Formatter(formatter))
console_handler.setFormatter(logging.Formatter(formatter))
# 将处理器添加到logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
