# coding:utf-8

from BTNode import CBTNode
from defines import *

class CBTPrioritySelector(CBTNode):

    def __init__(self,oPrecondition):
        super(CBTPrioritySelector, self).__init__()
        self.m_ActiveChild=None

    def DoEvaluate(self):
        for node in self.m_Child:
            if node.Evaluate():
                if self.m_ActiveChild and self.m_ActiveChild!=node:
                    self.m_ActiveChild.Clear()
                self.m_ActiveChild=node
                return True
        if not self.m_ActiveChild:
            self.m_ActiveChild.Clear()
            self.m_ActiveChild=None
        return False

    def Tick(self):
        if not self.m_ActiveChild:
            return RESULTSTATE_ENDED
        iRlt=self.m_ActiveChild.Tick()
        if iRlt!=RESULTSTATE_RUNNING:#子节点结束后，将活跃子节点清除掉，这一步是运行后的处理
            self.m_ActiveChild.Clear()
            self.m_ActiveChild=None
        return iRlt

    def Clear(self):
        if self.m_ActiveChild:
            self.m_ActiveChild.Clear()
            self.m_ActiveChild=None