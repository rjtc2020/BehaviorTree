# coding:utf-8

class CDataBase(object):

    def __init__(self):
        self.m_Data={}

    def ConfigData(self,data):
        self.m_Data=data

    def Set(self,k,v):
        self.m_Data[k]=v

    def Query(self,k,default=None):
        return self.m_Data.get(k,default)

    def Delete(self,k):
        return self.m_Data.pop(k,None)