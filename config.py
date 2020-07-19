import logging
from logging import handlers
class Log():
    # 格式化
    ftl = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(message)s"
    # 创建格式器
    format = logging.Formatter(ftl)
    # 创建处理器
    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler("./logs/11.log", when="D", backupCount=7, encoding="utf-8")
    # 把格式器加入到处理器
    sh.setFormatter(format)
    fh.setFormatter(format)
    # 创建日志器
    logger = logging.getLogger()
    # 把处理器加入到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.setLevel(logging.INFO)

