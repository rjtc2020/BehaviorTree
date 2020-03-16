# coding:utf-8

from BTNode import CBTNode
from defines import *

ALL_NOT_RUNNING=0#当所有结果非运行，返回end
ANY_NOT_RUNNING=1#当任意结果非运行，返回end

class CBTParallel(CBTNode):

    def __init__(self,oPrecondition,iResult=ALL_NOT_RUNNING):
        super(CBTParallel, self).__init__()
        self.m_Result=iResult
        self.m_ResultLst=[]

    def DoEvaluate(self):
        for oNode in self.m_Child:
            if not oNode.Evaluate():
                return False
        return True

    def Tick(self):
        iEndingRltCount=0
        for i in range(len(self.m_Child)):
            if self.m_Result==ALL_NOT_RUNNING:#并行节点end有两种模式，第一种要求所有子节点全部为非运行
                if self.m_ResultLst[i]==RESULTSTATE_RUNNING:
                    self.m_ResultLst[i]=self.m_Child[i].Tick()
                else:
                    iEndingRltCount+=1
            else:
                if self.m_ResultLst[i]==RESULTSTATE_RUNNING:
                    self.m_ResultLst[i] = self.m_Child[i].Tick()
                else:#子节点全部非运行中状态，说明结束了
                    self.ResetResults()
                    return RESULTSTATE_ENDED
            if iEndingRltCount==len(self.m_Child):
                self.ResetResults()
                return RESULTSTATE_ENDED
            return RESULTSTATE_RUNNING

    def AddChild(self,node):
        super(CBTParallel,self).AddChild(node)
        self.m_ResultLst.append(RESULTSTATE_RUNNING)

    def RemoveChild(self,node):
        iIndex=self.m_Child.index(node)
        self.m_ResultLst.remove(iIndex)
        super(CBTParallel,self).RemoveChild(node)

    def Clear(self):
        super(CBTParallel, self).Clear()
        self.ResetResults()
        for node in self.m_Child:
            node.Clear()

    def ResetResults(self):
        for i in range(len(self.m_ResultLst)):
            self.m_ResultLst[i]=RESULTSTATE_RUNNING
