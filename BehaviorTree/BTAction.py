# coding:utf-8

from BTNode import CBTNode
from defines import *

ACTIONSTATUS_READY=0
ACTIONSTATUS_RUNNING=1

class CBTAction(CBTNode):

    def __init__(self):
        super(CBTAction,self).__init__()
        self.m_ActionStatus=ACTIONSTATUS_READY

    def ActionStatus(self):
        return self.m_ActionStatus

    def SetActionStatus(self,iStatus):
        self.m_ActionStatus=iStatus

    def Enter(self):
        print "Enter"

    def Exit(self):
        print "Exit"

    def Execute(self):
        return RESULTSTATE_RUNNING

    def Clear(self):
        if self.m_ActionStatus!=ACTIONSTATUS_READY:
            self.SetActionStatus(ACTIONSTATUS_READY)
            self.Exit()

    def Tick(self):
        iRlt=RESULTSTATE_ENDED
        if self.ActionStatus()==ACTIONSTATUS_READY:
            self.SetActionStatus(ACTIONSTATUS_RUNNING)
            self.Enter()
        if self.ActionStatus()==ACTIONSTATUS_RUNNING:
            iRlt=self.Execute()
            if iRlt!=RESULTSTATE_RUNNING:
                self.SetActionStatus(ACTIONSTATUS_READY)
                self.Exit()
        return iRlt

    #action不可以添加子节点
    def AddChild(self,node):
        print "CBTAction : cannot addchild"

    def RemoveChild(self,node):
        print "CBTAction : cannot removechild"