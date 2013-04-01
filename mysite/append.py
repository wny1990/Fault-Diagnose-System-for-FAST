#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('/home/wny/fd_sys/mysite/')

os.environ['DJANGO_SETTINGS_MODULE'] ='mysite.settings'

from django.core.management import setup_environ

from mysite import settings



from fault_data.models import FaultMode

p=FaultMode(FaultModeID="1",FaultMode="总控和馈源连接异常",FaultDescription="test",HighLevelFaultModeID="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()

p=FaultMode(FaultModeID="2",FaultMode="节点未上传信息",FaultDescription="test",HighLevelFaultModeID="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()

p=FaultMode(FaultModeID="3",FaultMode="电机过载",FaultDescription="test",HighLevelFaultModeID="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()

p=FaultMode(FaultModeID="4",FaultMode="抛物面成型失败",FaultDescription="test",HighLevelFaultModeID="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()