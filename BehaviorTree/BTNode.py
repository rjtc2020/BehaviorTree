# coding:utf-8

from BTResult import CBTResult
import time

class CBTNode(object):

    def __init__(self):
        self.m_DataBase=None#共享数据

        self.m_LastCheckTime=0
        self.m_Interval=0#冷却

        self.m_Actived=True
        self.m_Result=CBTResult()

        self.m_Parent=None
        self.m_Child=[]

    def SetParent(self,oParent):
        self.m_Parent=oParent

    def Parent(self):
        return self.m_Parent

    def AddChild(self,node):
        self.m_Child.append(node)

    def RemoveChild(self,node):
        self.m_Child.remove(node)

    #配置共享数据
    def Activate(self,oData):
        if self.m_Actived:
            return
        self.m_DataBase=oData

        if self.Parent():
            self.m_Parent.Activate(oData)
        if self.m_Child:
            for oNode in self.m_Child:
                oNode.Activate(oData)

    def InitNode(self,oData):
        self.m_DataBase=oData

    def Evaluate(self):
        if not self.m_Actived:
            return False
        if not self.CheckTimer():
            return False

    def DoEvaluate(self):
        return True

    def Tick(self):
        pass

    def Clear(self):
        pass

    def CheckTimer(self):
        iTime=time.time()
        if iTime-self.m_LastCheckTime>self.m_Interval:
            self.m_LastCheckTime=iTime
            return True
        return False








