# coding:utf-8

class CDataBase(object):

    def __init__(self):
        self.m_DataLst=[]
        self.m_NameLst=[]

    def GetDataByName(self,sDataName):
        iDataId=self.IndexOfDataId(sDataName)
        if iDataId!=-1:
            return self.m_DataLst[iDataId]
        else:
            print "DataBase: data %s not exist"%sDataName

    def GetDataById(self,iDataId):
        return self.m_DataLst[iDataId]

    def SetDataByName(self,sDataName,data):
        iDataId=self.IndexOfDataId(sDataName)
        self.m_DataLst[iDataId]=data

    def SetDataById(self,iDataId,data):
        self.m_DataLst[iDataId]=data

    def GetDataId(self,sDataName):
        iDataId=self.IndexOfDataId(sDataName)
        if iDataId==-1:
            self.m_NameLst.append(sDataName)
            self.m_DataLst.append(None)
            iDataId=len(self.m_NameLst)-1
        return iDataId
    
    def IndexOfDataId(self,sDataName):
        for i in range(len(self.m_NameLst)):
            if self.m_NameLst[i]==sDataName:
                return i
        return -1