# coding:utf-8

from BTNode import CBTNode
from defines import *

class CBTPrecondition(CBTNode):

    def __init__(self):
        super(CBTPrecondition, self).__init__()

    def Check(self):
        return True

    def Tick(self):
        iRlt=self.Check()
        if iRlt:
            return RESULTSTATE_ENDED
        else:
            return RESULTSTATE_RUNNING

class CBTPreconditionUseDB(CBTPrecondition):

    def __init__(self,sData):
        super(CBTPreconditionUseDB, self).__init__()
        self.m_DataStr=sData
        self.m_DataStrID=0

    def Activate(self,oData):
        super(CBTPreconditionUseDB, self).Activate(oData)
        self.m_DataStrID=oData.GetDataId(self.m_DataStr)

# LESS_THAN=0
# BIG_THAN=1
# EQUAL_TO=2
#
# class CBTPreconditionFloat(CBTPreconditionUseDB):
#
#     def __init__(self,sData,iRhs,iCompare):
#         super(CBTPreconditionFloat,self).__init__(sData)
#         self.m_Rhs=iRhs
#         self.m_Size=iCompare
#
#     def Check(self):
#         iLhs=self.m_DataBase.GetDataByName(self.m_DataStr)
#         if self.m_Size==LESS_THAN:
#             return iLhs<self.m_Rhs
#         elif self.m_Size==BIG_THAN:
#             return iLhs>self.m_Rhs
#         elif self.m_Size==EQUAL_TO:
#             return iLhs==self.m_Rhs
#         return False