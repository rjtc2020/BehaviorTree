# coding:utf-8

from BTNode import CBTNode
from defines import *

class CBTParallelFlexible(CBTNode):

    def __init__(self,oPrecondition):
        super(CBTParallelFlexible, self).__init__()
        self.m_Precondition=oPrecondition
        self.m_ActiveLst=[]

    def DoEvaluate(self):
        iActiveChild=0
        for i in range(len(self.m_Child)):
            oNode=self.m_Child[i]
            if oNode.Evaluate():
                self.m_ActiveLst[i]=True
                iActiveChild+=1
            else:
                self.m_ActiveLst[i]=False
        if iActiveChild==0:#子节点全部不能进
            return False
        return True

    def Tick(self):
        iRunningChildCount=0
        for i in range(len(self.m_Child)):#对可以进的子节点进行是否在运行判断，在运行数量+1
            iActive=self.m_ActiveLst[i]
            if iActive:
                iRlt=self.m_Child[i].Tick()
                if iRlt==RESULTSTATE_RUNNING:
                    iRunningChildCount+=1
        if iRunningChildCount==0:
            return RESULTSTATE_ENDED
        return RESULTSTATE_RUNNING

    def AddChild(self,node):
        super(CBTParallelFlexible,self).AddChild(node)
        self.m_ActiveLst.append(RESULTSTATE_RUNNING)

    def RemoveChild(self,node):
        iIndex=self.m_Child.index(node)
        self.m_ActiveLst.remove(iIndex)
        super(CBTParallelFlexible,self).RemoveChild(node)

    def Clear(self):
        super(CBTParallelFlexible,self).Clear()
        for node in self.m_Child:
            node.Clear()