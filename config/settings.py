import os

URL_POSITION = "https://www.zyctd.com/jiage/1-0-0-{}.html"

DATE_PATH = os.path.join(os.getcwd() + '\\data', '药材数据_{}.{}')


class PageConfig:
    START = 0
    STOP = 122
    STEP = 32


class FileType:
    EXCEL = 1
    CSV = 0
