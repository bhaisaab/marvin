# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
'''
Initializes the marvin and does required prerequisites
for starting it.
   1. Parses the configuration file passed to marvin and creates a
   parsed config
   2. Initializes the logging required for marvin.All logs are
   now made available under a single timestamped folder.
   3. Deploys the Data Center based upon input

'''

from marvin.configGenerator import getSetupConfig
from marvin.marvinLog import MarvinLog
from marvin.deployDataCenter import DeployDataCenters
from marvin.cloudstackTestClient import CSTestClient
from marvin.cloudstackException import GetDetailExceptionInfo
from marvin.codes import(
    PASS,
    YES,
    NO,
    SUCCESS,
    FAILED
    )
import sys
import time
import os
import logging
import string
import random
from sys import exit
from marvin.codegenerator import CodeGenerator


class MarvinInit:
    def __init__(self, config_file,
                 load_api_flag=None,
                 deploy_dc_flag=None,
                 test_module_name=None,
                 zone=None):
        self.__configFile = config_file
        self.__deployFlag = deploy_dc_flag
        self.__loadApiFlag = load_api_flag
        self.__parsedConfig = None
        self.__logFolderPath = None
        self.__tcRunLogger = None
        self.__testClient = None
        self.__tcResultFile = None
        self.__testModuleName = test_module_name
        self.__testDataFilePath = None
        self.__zoneForTests = None

    def __parseConfig(self):
        '''
        @Name: __parseConfig 
        @Desc : Parses the configuration file passed and assigns
        the parsed configuration
        @Output : SUCCESS or FAILED
        '''
        try:
            self.__parsedConfig = getSetupConfig(self.__configFile)

            return SUCCESS
        except Exception, e:
            print "\nException Occurred Under __parseConfig : " \
                  "%s" % GetDetailExceptionInfo(e)
            return FAILED

    def getParsedConfig(self):
        return self.__parsedConfig

    def getLogFolderPath(self):
        return self.__logFolderPath

    def getTestClient(self):
        return self.__testClient

    def getLogger(self):
        return self.__tcRunLogger

    def getDebugFile(self):
        '''
        @Name : getDebugFile
        @Desc : Returns the Result file to be used for writing 
                test outputs
        '''
        if self.__logFolderPath is not None:
            self.__tcResultFile = open(self.__logFolderPath +
                                       "/results.txt", "w")
            return self.__tcResultFile

    def init(self):
        '''
        @Name : init
        @Desc :Initializes the marvin by
               1. Parsing the configuration and creating a parsed config
                  structure
               2. Creates a timestamped log folder and provides all logs
                  to be dumped there
               3. Creates the DataCenter based upon configuration provided
        @Output : SUCCESS or FAILED
        '''
        try:
            if ((self.__parseConfig() != FAILED) and
               (self.__setTestDataPath() != FAILED) and
               (self.__initLogging() != FAILED) and
               (self.__createTestClient() != FAILED) and
               (self.__deployDC() != FAILED) and
               (self.__loadNewApiFromXml() != FAILED)):
                return SUCCESS
            else:
                return FAILED
        except Exception, e:
            print "\n Exception Occurred Under init " \
                  "%s" % GetDetailExceptionInfo(e)
            return FAILED

    def __initLogging(self):
        '''
        @Name : __initLogging
        @Desc : 1. Initializes the logging for marvin and so provides
                    various log features for automation run.
                    2. Initializes all logs to be available under
                    given Folder Path,where all test run logs
                    are available for a given run.
                    3. All logging like exception log,results, run info etc
                     for a given test run are available under a given
                     timestamped folder
        @Output : SUCCESS or FAILED
        '''
        try:
            log_obj = MarvinLog("CSLog")
            if log_obj is None:
                return FAILED
            else:
                ret = log_obj.\
                    createLogs(self.__testModuleName,
                            self.__parsedConfig.logger)
                if ret != FAILED:
                    self.__logFolderPath = log_obj.getLogFolderPath()
                    self.__tcRunLogger = log_obj.getLogger()
                    return SUCCESS
            return FAILED
        except Exception, e:
            print "\n Exception Occurred Under __initLogging " \
                  ":%s" % GetDetailExceptionInfo(e)
            return FAILED

    def __createTestClient(self):
        '''
        @Name : __createTestClient
        @Desc : Creates the TestClient during init
                based upon the parameters provided
        @Output: Returns SUCCESS or FAILED
        '''
        try:
            mgt_details = self.__parsedConfig.mgtSvr[0]
            dbsvr_details = self.__parsedConfig.dbSvr
            self.__testClient = CSTestClient(mgt_details, dbsvr_details,
                                             logger=self.__tcRunLogger,
                                             test_data_filepath=
                                             self.__testDataFilePath,
                                             zone=self.__zoneForTests)
            if self.__testClient is not None:
                return self.__testClient.createTestClient()
            else:
                return FAILED
        except Exception, e:
            print "\n Exception Occurred Under __createTestClient : %s" % \
                  GetDetailExceptionInfo(e)
            return FAILED

    def __loadNewApiFromXml(self):
        '''
        @Desc: Kept for future usage
               Will enhance later.
        '''
        try:
            return SUCCESS
            if self.__loadApiFlag:
                apiLoadCfg = self.__parsedConfig.apiLoadCfg
                api_dst_dir = apiLoadCfg.ParsedApiDestFolder + "/cloudstackAPI"
                api_spec_file = apiLoadCfg.ApiSpecFile

                if not os.path.exists(api_dst_dir):
                    try:
                        os.mkdir(api_dst_dir)
                    except Exception, e:
                        print "Failed to create folder %s, " \
                              "due to %s" % (api_dst_dir,
                                             GetDetailExceptionInfo(e))
                        return FAILED
                mgt_details = self.__parsedConfig.mgtSvr[0]
                cg = CodeGenerator(api_dst_dir)
                if os.path.exists(api_spec_file):
                    cg.generateCodeFromXML(api_spec_file)
                elif mgt_details is not None:
                    endpoint_url = 'http://%s:8096/client/api?' \
                                   'command=listApis&response=json' \
                                   % mgt_details.mgtSvrIp
                    cg.generateCodeFromJSON(endpoint_url)
            return SUCCESS
        except Exception, e:
            print "\n Exception Occurred Under __loadNewApiFromXml : %s" \
                  % GetDetailExceptionInfo(e)
            return FAILED

    def __setTestDataPath(self):
        '''
        @Name : __setTestDataPath
        @Desc: Sets the TestData Path for tests to run
        @Output: Returns SUCCESS or FAILED
        '''
        try:
            if ((self.__parsedConfig.TestData is not None) and
                    (self.__parsedConfig.TestData.Path is not None)):
                self.__testDataFilePath = self.__parsedConfig.TestData.Path
            return SUCCESS
        except Exception, e:
            print "\nException Occurred Under __setTestDataPath : %s" % \
                  GetDetailExceptionInfo(e)
            return FAILED

    def __deployDC(self):
        '''
        @Name : __deployDC
        @Desc : Deploy the DataCenter and returns accordingly.
        @Output : SUCCESS or FAILED
        '''
        try:
            ret = SUCCESS
            if self.__deployFlag:
                deploy_obj = DeployDataCenters(self.__testClient,
                                           self.__parsedConfig,
                                           self.__tcRunLogger)
                ret = deploy_obj.deploy()
            if ret == SUCCESS:
                print "Deploy DC Successful"
            else:
                print "Deploy DC Failed"
            return ret
        except Exception, e:
            print "\n Exception Occurred Under __deployDC : %s" % \
                  GetDetailExceptionInfo(e)
            return FAILED
