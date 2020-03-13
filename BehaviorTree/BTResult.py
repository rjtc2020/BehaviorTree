# coding:utf-8

from defines import *

class CBTResult(object):
    def __init__(self):
        self.m_Result=RESULTSTATE_ENDED

    def SetResult(self,iResult):
        self.m_Result=iResult

    def Result(self):
        return self.m_Result

    def Reset(self):
        self.m_Result=RESULTSTATE_ENDED