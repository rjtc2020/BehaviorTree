# coding:utf-8

from BTNode import CBTNode
from defines import *

class CBTSequence(CBTNode):

    def __init__(self,oPrecondition):
        super(CBTSequence, self).__init__()
        self.m_ActiveChild=None
        self.m_ActiveIndex=-1

    def DoEvaluate(self):
        if not self.m_ActiveChild:
            iRlt=self.m_ActiveChild.Evaluate()
            if not iRlt:
                self.m_ActiveChild.Clear()
                self.m_ActiveChild=None
                self.m_ActiveIndex=-1
            return iRlt
        else:
            return self.m_Child[0].Evaluate()

    def Tick(self):
        if not self.m_ActiveChild:
            self.m_ActiveChild=self.m_Child[0]
            self.m_ActiveIndex=0
        iRlt=self.m_ActiveChild.Tick()
        if iRlt==RESULTSTATE_ENDED:
            self.m_ActiveIndex+=1
            if self.m_ActiveIndex>=len(self.m_Child):
                self.m_ActiveChild.Clear()
                self.m_ActiveChild=None
                self.m_ActiveIndex=-1
            else:
                self.m_ActiveChild.Clear()
                self.m_ActiveChild=self.m_Child[self.m_ActiveIndex]
                iRlt=RESULTSTATE_RUNNING
        return iRlt

    def Clear(self):
        if self.m_ActiveChild:
            self.m_ActiveChild=None
            self.m_ActiveIndex=-1
        for node in self.m_Child:
            node.Clear()