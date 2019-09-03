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
    def setParameters(self, *params,**parmss):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param sex:
        :param telephone:
        :param nickname:
        :param birthday:
        :param country_id:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = params[0]
        self.method =params[1]

    def __init__(self,case_name):
        self.case_name = case_name
        self._testMethodName = self.testOne.__name__
        self._cleanups = ''
        self._testMethodDoc = self.testOne.__doc__
    def setUp(self):
        """
        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
    # def __init__(self,*args):
    #     unittest.TestCase.__init__(self,*args)
    def testOne(self):
        """
        testOne
        :return:
        """
        self.logger.info(self.case_name)
        self.assertTrue(True)
        print(self.case_name)