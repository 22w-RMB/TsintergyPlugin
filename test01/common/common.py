
import base64

import numpy
import yaml
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import requests
import os
import datetime



# RSA 加密
def encrpt(s , key):
    public_key = "-----BEGIN PUBLIC KEY-----\n" + key + "\n-----END PUBLIC KEY-----"
    rsakey = RSA.importKey(public_key)
    cipher = PKCS1_v1_5.new(rsakey)
    # 因为encryptor.encrypt方法其内部就实现了加密再次Base64加密的过程，所以这里实际是通过下面的1和2完成了JSEncrypt的加密方法
    encrpt_text = cipher.encrypt(s.encode())  # 1.对账号密码组成的字符串加密
    base64_text = base64.b64encode(encrpt_text)  # 2.对加密后的字符串base64加密

    return base64_text.decode()


# 读取yaml文件
def readYaml(yamlFilePath):

    data : dict
    with open(yamlFilePath,'r',encoding="utf-8") as f:
        data =  yaml.safe_load(f)

    return data

def mkDir(root, *args,isGetStr=False):

    for i in args:
        root = os.path.join(root, i)
        if isGetStr == False:
            if not os.path.exists(root):
                os.mkdir(root)

    return root

def mkDateDir(path, startDate,endDate ):

    sd = datetime.datetime.strptime(startDate,"%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate,"%Y-%m-%d")


    while sd <= ed:

        d = datetime.datetime.strftime(sd,"%Y-%m-%d")
        mkDir(path, d)

        sd += datetime.timedelta(days=1)


def mkPublicDir(publicSavePath,startDate, endDate):

    mkDateDir(publicSavePath, startDate, endDate)


def mkPrivateDir(privateSavePath,unitData,startDate, endDate):

    for unit in unitData:

        ownerPath = mkDir(privateSavePath,unit['ownerName'])

        mkDateDir(ownerPath,startDate, endDate)

def trun24(dataList, turnLen=24):

    if len(dataList) != 96:
        print("数据长度不为96")
        return
    list24 = []

    for i in range(0,turnLen):

        if dataList[i*4] is None:
            list24.append(None)
            continue
        #
        # print(dataList[(i * 4):(i * 4 + 4)])

        list24.append(

            numpy.mean( dataList[ (i*3):(i*3+4) ] )
        )

    return list24

# def saveFile(openFilePath, colList, dataList, saveFilePath ):
#     e = ExcelHepler(openFilePath)
#     e.writeColData(sheetName="Sheet1",colList=colList,dataList=dataList)
#     e.saveFile(saveFilePath)
#     e.close()
#


def login(session1 : requests.Session, loginInfo):


    password = loginInfo['password']
    if loginInfo['publicKeyUrl'] is not None:
        key = session1.request(method="GET",url=loginInfo['publicKeyUrl']).json()['data']
        password = encrpt(loginInfo['password'],key)

    loginData = {
        "username":  loginInfo['username'] ,
        "loginMode":  loginInfo['loginMode'] ,
        "password":  password
    }

    print(password)

    r1 = session1.request(method="POST",url=loginInfo['loginUrl'],params=loginData)
    print(r1.json())

    switchTenantData = {
        "tenantId" :  loginInfo['tenantId']
    }
    r2 = session1.request(method="GET",url=loginInfo['switchTenantUrl'],params=switchTenantData)
    print(r2.json())




rootPath = os.path.dirname(os.path.dirname(__file__))


if __name__ == '__main__':


    print(rootPath)

    print(trun24([1, 2, 3, 4, 5, 6, 7, 8,None,5,8,9], turnLen=3))
    pass