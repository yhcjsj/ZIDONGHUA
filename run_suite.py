import unittest
from toos import HTMLTestRunner
from api.login import Login
suit = unittest.TestSuite()
suit.addTests(unittest.makeSuite(Login))
# runner = unittest.TextTestRunner

file_name = "../report/report.html"
with open(file_name, 'wb') as f:
  runner = HTMLTestRunner(stream=f, title="接口自动化测试报告", description="宇泽购物流程")
  runner.run(suit)