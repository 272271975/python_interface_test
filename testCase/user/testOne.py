#! /opt/conda/bin/python 
# -*- coding: utf-8 -*- 
import unittest
import paramunittest
import common.readConfig as readConfig
from common import common
from common import Log as Log
from common.Log import MyLog

localReadConfig = readConfig.ReadConfig()
localLogin_xls = common.get_xls("userCase.xlsx", "login")

@paramunittest.parametrized(*localLogin_xls)
class testOne(unittest.TestCase):
    """
    testOne
    :return:
    """
    def setParameters(self,case_name,data,url,method,result,code,case_method_name,msg):
        """
        set params
        :params case_name
        :params data
        :params url
        :params method
        :params result
        :params code
        :params msg
        """
        self.case_name = case_name
        self.data = data
        self.case_method_name = case_method_name
        self._testMethodName = case_method_name

    def __init__(self,case_name):
        self._testMethodName = self.testOne.__name__
        self._cleanups = ''
        self._testMethodDoc = self.testOne.__doc__
    def setUp(self):
        """
        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def tearDown(self):
        """
            tearDown
            reutrn
        """
        print('tear down test case ran')

    def test_login1(self):
        """
        test_One
        :return:
        """
        self.assertTrue(False)
        self.assertFalse('LOO'.isupper(), self.case_method_name)
        print('test_login1-333')

    def testOne(self):
        """
        testOne
        :return:
        """
        print('call 文件指定的方法 完成测试'+self.case_method_name)
        if not self.case_method_name:
            pass
        else:
            getattr(self,self.case_method_name)()
        
        
        