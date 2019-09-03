#! /opt/conda/bin/python 
# -*- coding: utf-8 -*- 
import os
import unittest
import traceback
import common.readConfig as readConfig
from common.Log import MyLog as Log
import common.HTMLTestRunner as HTMLTestRunner

# loadingReadConfig  = readConfig.ReadConfig()

class Test:
	def __init__(self):
		print('init...')
		global log, logger, resultPath
		log = Log.get_log()
		logger = log.get_logger()
		resultPath = log.get_report_path()
		self.caseListFile = os.path.join(readConfig.proDir, "../config/testCases.txt")
		self.caseFile = os.path.join(readConfig.proDir, "../testCase")
		self.caseList = []
		self.test_suite = []
		self.set_case_list()
		self.set_case_suite()
	
	def set_case_list(self):
		"""
		set case list
		:return :
		"""
		fd = open(self.caseListFile)
		for value in fd.readlines():
			data = str(value)
			if data != '' and not data.startswith('#'):
				self.caseList.append(data.replace("\n",""))
		fd.close()
	
	#设置suite同时返回数据
	def set_case_suite(self):
		"""
		set case suite
		:return:
		"""
		test_suite = unittest.TestSuite()
		suite_module = []
		for case in self.caseList:
			if len(case) == 0:
				break
			path_arr = case.split("/")
			case_name = path_arr[-1]
			case_path_prefix = '/'.join(path_arr[0:-1])
			test_file_path = os.path.join(self.caseFile, case_path_prefix)
			discover = unittest.defaultTestLoader.discover(test_file_path,pattern=case_name+'.py',top_level_dir=None)
			print(discover)
			suite_module.append(discover)
		if len(suite_module) > 0:
			for _discover in suite_module:
				for test_task in _discover:
					test_suite.addTest(test_task)
		else:
			return None
		self.test_suite = test_suite

	def run(self):
		"""
		run test
		"""
		fp = open(resultPath, 'wb')
		try:
			logger.info("********TEST START********")
			suit = self.test_suite
			if suit is not None:
				runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
				runner.run(suit)
			else:
				logger.info("Have no case to runner")
		except Exception as ex:
			traceback.print_exc()
		finally:
			logger.info("test end")
			fp.close()


if __name__ == "__main__":
	print("starting。。。")
	test = Test()#创建对象 测试对象
	test.run()#开始运行


