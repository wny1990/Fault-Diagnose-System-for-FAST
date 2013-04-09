#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('/home/wny/fd_sys/mysite/')

os.environ['DJANGO_SETTINGS_MODULE'] ='mysite.settings'

from django.core.management import setup_environ

from mysite import settings



from fault_data.models import FaultMode


#python managey.py syncdb

#我是万能的分割线

p=FaultMode(FaultModeID="1",FaultMode="命令无法发送",FaultDescription="test",HighLevelFaultModeID=0,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()

p=FaultMode(FaultModeID="2",FaultMode="执行器连接异常",FaultDescription="test",HighLevelFaultModeID=1,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="3",FaultMode="子系统代理连接异常",FaultDescription="test",HighLevelFaultModeID=1,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="4",FaultMode="执行器网络异常",FaultDescription="test",HighLevelFaultModeID=2,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="5",FaultMode="执行器未启动",FaultDescription="test",HighLevelFaultModeID=2,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="6",FaultMode="ARSA连接异常",FaultDescription="test",HighLevelFaultModeID=3,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="7",FaultMode="CSSA连接异常",FaultDescription="test",HighLevelFaultModeID=3,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="8",FaultMode="ARS子系统连接异常",FaultDescription="test",HighLevelFaultModeID=3,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="9",FaultMode="CSS子系统连接异常",FaultDescription="test",HighLevelFaultModeID=3,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="10",FaultMode="ARS网络异常",FaultDescription="test",HighLevelFaultModeID=6,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="11",FaultMode="ARSA未启动",FaultDescription="test",HighLevelFaultModeID=6,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="12",FaultMode="CSSA网络异常",FaultDescription="test",HighLevelFaultModeID=8,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
p=FaultMode(FaultModeID="13",FaultMode="CSSA未启动",FaultDescription="test",HighLevelFaultModeID=8,DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)

p.save()
