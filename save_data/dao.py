import pandas as pd
from config import settings
from utils import logger


def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False) if settings.FileType.CSV else df.to_csv(filename)
    df.to_csv(filename)
    logger.logger.debug(f"已保存{filename}")
