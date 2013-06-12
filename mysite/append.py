#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('/home/wny/fd_sys/mysite/')

os.environ['DJANGO_SETTINGS_MODULE'] ='mysite.settings'

from django.core.management import setup_environ

from mysite import settings

from fault_data.models import *


#python manage.py syncdb


#故障原因 开始
p=FaultCause(FaultCauseID=1,FaultCause="运行参数错误",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="重新发送正确参数")
p.save()
p=FaultCause(FaultCauseID=2,FaultCause="节点电机故障",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=3,FaultCause="节点索长超限",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="紧急停止节点，并恢复到正常范围")
p.save()
p=FaultCause(FaultCauseID=4,FaultCause="节点温度超限",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=5,FaultCause="节点索力超限",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=6,FaultCause="节点未开启上传功能",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="开启节点上传功能")
p.save()
p=FaultCause(FaultCauseID=7,FaultCause="节点网线断开",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=8,FaultCause="区域控制器未连接节点",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="重新与节点建立socket连接")
p.save()
p=FaultCause(FaultCauseID=9,FaultCause="反射面温度过高",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=10,FaultCause="刚索断裂",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=11,FaultCause="刚索腐蚀损坏",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=12,FaultCause="线缆断裂",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=13,FaultCause="节点未上电",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="给节点上电")
p.save()
p=FaultCause(FaultCauseID=14,FaultCause="节点网线断开",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="重新插入网线或者换新网线")
p.save()
p=FaultCause(FaultCauseID=15,FaultCause="节点处于紧急停止",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="解除节点的紧急停止")
p.save()
p=FaultCause(FaultCauseID=16,FaultCause="主控机与交换机连接故障",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=17,FaultCause="电机未上电",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="给电机上电")
p.save()
p=FaultCause(FaultCauseID=18,FaultCause="滑索脱槽",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=19,FaultCause="绳索震动",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=20,FaultCause="绳索虚滑",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=21,FaultCause="电机过载",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=22,FaultCause="电机漂零",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=23,FaultCause="Stewart平台连接故障",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="重新连接")
p.save()
p=FaultCause(FaultCauseID=24,FaultCause="Stewart平台位姿不当",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="调整位姿")
p.save()
p=FaultCause(FaultCauseID=25,FaultCause="Stewart平台耦合震荡",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=26,FaultCause="AB转台连接故障",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="重新连接")
p.save()
p=FaultCause(FaultCauseID=27,FaultCause="工控机连接故障",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="重新连接")
p.save()
p=FaultCause(FaultCauseID=28,FaultCause="执行器网络异常",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=29,FaultCause="执行器未启动",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=30,FaultCause="ARSA网络异常",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=31,FaultCause="ARSA未启动",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=32,FaultCause="CSSA网络异常",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=33,FaultCause="CSSA未启动",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=34,FaultCause="MASTER网络异常",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=35,FaultCause="MASTER未启动",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=36,FaultCause="区域控制器连接异常",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=37,FaultCause="索塔网络断开",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=38,FaultCause="工控机网络异常",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=39,FaultCause="工控机程序未启动",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
p=FaultCause(FaultCauseID=40,FaultCause="馈源网络断开",FaultCauseDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0,MaintenanceSuggestions="test2")
p.save()
#故障原因 结束


# 故障模式 开始
#p=FaultMode(FaultModeID=0,FaultMode="NULL",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
#p.save()
p=FaultMode(FaultModeID=1,FaultMode="反射面故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=2,FaultMode="抛物面成型失败",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=3,FaultMode="命令执行失败",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=4,FaultMode="照明区域错误",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=5,FaultMode="节点运行超时",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=6,FaultMode="节点没有反馈",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=7,FaultMode="反射面面板故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=8,FaultMode="钢索故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=9,FaultMode="线缆故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=10,FaultMode="节点连接失败",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=11,FaultMode="节点不转动",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()


p=FaultMode(FaultModeID=12,FaultMode="馈源支撑故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=13,FaultMode="馈源舱未动",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=14,FaultMode="馈源舱未达到指定位置",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=15,FaultMode="馈源舱刚索系统故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=16,FaultMode="馈源舱测量仪器故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=17,FaultMode="一次支撑未到位",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=18,FaultMode="二次支撑未到位",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=19,FaultMode="索故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=20,FaultMode="电机故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=21,FaultMode="馈源舱故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=22,FaultMode="工控机故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=23,FaultMode="Stewart平台故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=24,FaultMode="A-B转台故障",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()

p=FaultMode(FaultModeID=25,FaultMode="命令无法发送",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=26,FaultMode="执行器连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=27,FaultMode="子系统代理连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()

p=FaultMode(FaultModeID=28,FaultMode="ARSA连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=29,FaultMode="CSSA连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=30,FaultMode="ARS子系统连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=31,FaultMode="CSS子系统连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()

p=FaultMode(FaultModeID=32,FaultMode="MASTER连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=33,FaultMode="区域控制器连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()

p=FaultMode(FaultModeID=34,FaultMode="索塔连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=35,FaultMode="工控机连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()
p=FaultMode(FaultModeID=36,FaultMode="馈源连接异常",FaultDescription="test",DetectionMethod=1,ManualDetectionMethodID="test",FunctionID="test",Priority=1,LogicalRelationship=0)
p.save()

# 故障模式 结束

#故障模式关系 开始
p=FaultModeRelation(HighLevelFaultModeID=0,FaultModeID=1,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=1,FaultModeID=2,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=1,FaultModeID=3,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=2,FaultModeID=4,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=2,FaultModeID=5,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=2,FaultModeID=6,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=2,FaultModeID=7,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=2,FaultModeID=8,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=2,FaultModeID=9,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=3,FaultModeID=10,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=3,FaultModeID=11,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=3,FaultModeID=5,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=3,FaultModeID=6,LogicalRelationship=0)
p.save()
#
p=FaultModeRelation(HighLevelFaultModeID=0,FaultModeID=12,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=12,FaultModeID=13,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=12,FaultModeID=14,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=13,FaultModeID=15,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=13,FaultModeID=16,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=14,FaultModeID=17,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=14,FaultModeID=18,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=14,FaultModeID=16,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=17,FaultModeID=19,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=17,FaultModeID=20,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=18,FaultModeID=21,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=18,FaultModeID=22,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=21,FaultModeID=23,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=21,FaultModeID=24,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=23,FaultModeID=20,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=24,FaultModeID=20,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=0,FaultModeID=25,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=25,FaultModeID=26,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=25,FaultModeID=27,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=27,FaultModeID=28,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=27,FaultModeID=29,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=27,FaultModeID=30,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=27,FaultModeID=31,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=28,FaultModeID=32,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=28,FaultModeID=33,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=33,FaultModeID=10,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=31,FaultModeID=34,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=31,FaultModeID=35,LogicalRelationship=0)
p.save()
p=FaultModeRelation(HighLevelFaultModeID=35,FaultModeID=36,LogicalRelationship=0)
p.save()
#故障模式关系 结束

#故障原因关系 开始
p=FaultCauseRelation(FaultModeID=4,FaultCauseID=1,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=5,FaultCauseID=2,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=5,FaultCauseID=3,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=5,FaultCauseID=4,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=5,FaultCauseID=5,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=6,FaultCauseID=6,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=6,FaultCauseID=7,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=6,FaultCauseID=8,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=7,FaultCauseID=9,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=8,FaultCauseID=10,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=8,FaultCauseID=11,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=9,FaultCauseID=12,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=10,FaultCauseID=13,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=10,FaultCauseID=14,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=10,FaultCauseID=8,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=11,FaultCauseID=2,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=11,FaultCauseID=3,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=11,FaultCauseID=4,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=11,FaultCauseID=5,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=11,FaultCauseID=15,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=15,FaultCauseID=16,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=15,FaultCauseID=17,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=19,FaultCauseID=18,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=19,FaultCauseID=19,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=19,FaultCauseID=20,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=20,FaultCauseID=21,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=20,FaultCauseID=22,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=22,FaultCauseID=27,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=23,FaultCauseID=23,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=23,FaultCauseID=24,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=23,FaultCauseID=25,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=24,FaultCauseID=26,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=26,FaultCauseID=28,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=26,FaultCauseID=29,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=28,FaultCauseID=30,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=28,FaultCauseID=31,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=29,FaultCauseID=32,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=29,FaultCauseID=33,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=32,FaultCauseID=34,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=32,FaultCauseID=35,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=33,FaultCauseID=36,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=34,FaultCauseID=37,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=35,FaultCauseID=38,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=35,FaultCauseID=39,LogicalRelationship=0)
p.save()
p=FaultCauseRelation(FaultModeID=36,FaultCauseID=40,LogicalRelationship=0)
p.save()
#故障原因关系 结束
