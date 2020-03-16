# coding:utf-8

from defines import *
import time

class CBTNode(object):

    def __init__(self,oPrecondition=None):
        self.m_DataBase=None#共享数据

        self.m_LastCheckTime=0#上次检查时间
        self.m_Interval=0#冷却

        self.m_Actived=False

        self.m_Precondition=oPrecondition#前置条件
        self.m_Child=[]#子节点

    def AddChild(self,node):
        self.m_Child.append(node)

    def RemoveChild(self,node):
        if node in self.m_Child:
            self.m_Child.remove(node)

    #配置共享数据
    def Activate(self,oData):
        if self.m_Actived:
            return
        self.m_DataBase=oData

        if self.m_Precondition:
            self.m_Precondition.Activate(oData)
        if self.m_Child:
            for oNode in self.m_Child:
                oNode.Activate(oData)
        self.m_Actived=True

    def InitNode(self,oData):
        self.m_DataBase=oData

    def Evaluate(self):
        if not self.m_Actived:
            return False
        if not self.CheckTimer():
            return False
        if not (not self.m_Precondition or self.m_Precondition.Check()):
            return False
        if not self.DoEvaluate():
            return False
        return True

    def DoEvaluate(self):
        return True

    def Tick(self):
        return RESULTSTATE_ENDED

    def Clear(self):
        pass

    def CheckTimer(self):
        iTime=time.time()
        if iTime-self.m_LastCheckTime>self.m_Interval:
            self.m_LastCheckTime=iTime
            return True
        return False








