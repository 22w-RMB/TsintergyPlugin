from test01.common.common import *
from test01.common.excel_helper import ExcelHepler
from jsFileConfig import *

province = "江苏"
provinceAreaId = "032"
yamlFilePath = os.path.join(rootPath, "yamlFile", "js_interface.yaml")
rootTemplatePath = os.path.join(rootPath, "template", province)
savePath = mkDir(rootPath, "save")
rootSavePath = mkDir(savePath, province)



# 接口请求市场行情看板的公有数据
def getMarketData(session1 : requests.Session, requestInfo, startDate, endDate, dataLen="LEN_96"):

    url = requestInfo['marketurl']
    method = requestInfo['method']
    requestsData = {
        "startDate" : startDate,
        "endDate" : endDate,
        "provinceAreaId" : provinceAreaId,
        "dataLen" : dataLen,
    }
    res = session1.request(method=method,url = url,params=requestsData)
    print(res.json())

    return res.json()['data']

# 接口请求机组容量信息
def getSpareData(session1 : requests.Session, requestInfo, startDate, endDate):

    url = requestInfo['spareUrl']
    method = requestInfo['method']
    requestsData = {
        "startDate" : startDate,
        "endDate" : endDate,
        "provinceAreaId" : provinceAreaId,
    }
    res = session1.request(method=method,url = url,params=requestsData)
    print(res.json())

    return {"spareList":res.json()['data']}

# 接口请求设备检修信息
def getOverhaulData(session1 : requests.Session, requestInfo, startDate, endDate):

    url = requestInfo['overhaulUrl']
    method = requestInfo['method']
    requestsData = {
        "startDate" : startDate,
        "endDate" : endDate,
        "provinceAreaId" : provinceAreaId,
    }
    res = session1.request(method=method,url = url,params=requestsData)
    resData = res.json()['data']

    sd = datetime.datetime.strptime(startDate,"%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate,"%Y-%m-%d")
    deviation = (ed-sd).days

    overhaulList = []

    for i in range(0, deviation + 1):

        deviceName = []
        startTime = []
        endTime = []

        for item in resData:
            date = item['date'][:10]
            resD = datetime.datetime.strptime(date, "%Y-%m-%d")
            if resD == sd:
                deviceName.append(item['deviceName'])
                startTime.append(item['startTime'])
                endTime.append(item['endTime'])

        sd += datetime.timedelta(days=1)

        overhaulList.append({
            "deviceName" : deviceName,
            "startTime" : startTime,
            "endTime" : endTime,
        })

    return {"overhaulList":overhaulList}

# 接口请求断面约束
def getLimitUrlData(session1 : requests.Session, requestInfo, startDate, endDate):

    url = requestInfo['limitUrl']
    method = requestInfo['method']
    requestsData = {
        "startDate" : startDate,
        "endDate" : endDate,
        "provinceAreaId" : provinceAreaId,
    }
    res = session1.request(method=method,url = url,params=requestsData)
    resData = res.json()['data']

    sd = datetime.datetime.strptime(startDate,"%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate,"%Y-%m-%d")
    deviation = (ed-sd).days

    limitList = []

    for i in range(0, deviation + 1):

        deviceName = []
        stableLimit = []

        for item in resData:
            date = item['date'][:10]
            resD = datetime.datetime.strptime(date, "%Y-%m-%d")
            if resD == sd:
                deviceName.append(item['deviceName'])
                stableLimit.append(item['stableLimit'])

        sd += datetime.timedelta(days=1)

        limitList.append({
            "deviceName" : deviceName,
            "stableLimit" : stableLimit,
        })

    return {"limitList":limitList}

# 输出公有数据
def outPublicData(data, startDate, endDate,  templateInfo):

    templatePath = os.path.join(mkDir(rootTemplatePath,*templateInfo['templatePath'],isGetStr=True),
                                templateInfo['templateName']+".xlsx")


    e = ExcelHepler(templatePath)


    sd = datetime.datetime.strptime(startDate,"%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate,"%Y-%m-%d")
    deviation = (ed-sd).days



    for i in range(0,deviation+1):
        dataList = []

        date = datetime.datetime.strftime(sd,"%Y-%m-%d")
        print(date)

        # d = []
        # for node in templateInfo['node']:
        #     d = data['da']

        for info in templateInfo['typeInfo']:

            d = data
            print(d)
            if info['board'] is not None:
                for board in info['board']:
                    print(board)
                    d = d[board]

            d = d[i]

            for node in info['node']:
                d = d[node]

            dataList.append(d)


        saveFileName = templateInfo['saveFileName'] + "-" + date + ".xlsx"
        savePath = mkDir(rootSavePath, *templateInfo['savePath'],date)

        path = os.path.join(savePath,saveFileName)

        sd += datetime.timedelta(days=1)
        print(saveFileName)
        print(path)


        e.writeColData(sheetName="Sheet1", colList=templateInfo['colList'],
                       beginRowList=templateInfo['beginRowList'],dataList=dataList,
                       savePath=path)

    e.close()



# 请求所有的机组
def getUnitId(session1,privateData):

    url = privateData['unitIdUrl']

    r1 = session1.request(method="GET",url=url)
    # print(r1.json())

    data = r1.json()['data']


    unitList = []

    for item in data:
        for unit in item['children']:

            unitList.append(
                {"unitId": unit['unitId'],
                 "unitName": unit['unitName'],
                 "businessType": unit['businessType'],
                 "ownerName" : item['ownerName']
                 }
            )

    return unitList


# 接口请求所有的私有数据
def getPrivateData(session1 : requests.Session, requestInfo, startDate, endDate ,unitData):


    allDataList = []

    url = requestInfo['clearingUrl']
    method = "GET"
    for unit in unitData:
        requestsData = {
            "startDate" : startDate,
            "endDate" : endDate,
            "deviceId" : unit['unitId'],
        }
        res = session1.request(method=method,url = url,params=requestsData)

        allDataList.append([ unit['unitName'],res.json()['data'], unit['ownerName']])


    return allDataList

# 输出所有的私有数据
def outPrivateData(data, startDate, endDate,  templateInfo):


    templatePath = os.path.join(mkDir(rootTemplatePath,*templateInfo['templatePath'],isGetStr=True),
                                templateInfo['templateName']+".xlsx")


    e = ExcelHepler(templatePath)


    for item in data:
        unitName = item[0]
        ownerName = item[2]
        unitData = item[1]

        sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")
        deviation = (ed - sd).days

        for i in range(0, deviation + 1):
            dataList = []

            date = datetime.datetime.strftime(sd, "%Y-%m-%d")
            print(date)

            # d = []
            # for node in templateInfo['node']:
            #     d = data['da']

            for info in templateInfo['typeInfo']:

                d = unitData
                # print(d)
                if info['board'] is not None:
                    for board in info['board']:
                        print(board)
                        d = d[board]

                d = d[i]

                for node in info['node']:
                    d = d[node]

                dataList.append(d)

            saveFileName = unitName + "-"+ templateInfo['saveFileName']  + date + ".xlsx"
            savePath = mkDir(rootSavePath, *templateInfo['savePath'],ownerName, date)

            path = os.path.join(savePath, saveFileName)

            sd += datetime.timedelta(days=1)
            print(saveFileName)
            print(path)

            e.writeColData(sheetName="Sheet1", colList=templateInfo['colList'],
                           beginRowList=templateInfo['beginRowList'], dataList=dataList,
                           savePath=path)
    e.close()


def execPublic(session, yamlPublicData, startDate, endDate):

    data = {}

    requestInfo = yamlPublicData

    data.update(getMarketData(session, requestInfo, startDate, endDate))
    data.update(getSpareData(session, requestInfo, startDate, endDate))
    data.update(getOverhaulData(session, requestInfo, startDate, endDate))
    data.update(getLimitUrlData(session, requestInfo, startDate, endDate))

    for item in publicConfig:

        outPublicData(data,startDate,endDate,item)

    # print(data)


def execPrivate(session, yamlPrivateData, startDate, endDate):

    unitInfo = getUnitId(session, yamlPrivateData)

    unitData = getPrivateData(session, yamlPrivateData, startDate, endDate ,unitInfo)

    # print(unitData)
    for item in privateFileConfig:

        outPrivateData(unitData,startDate,endDate,item)

def beginCrawl(startDate,endDate,type):
    session = requests.Session()
    yamlData = readYaml(yamlFilePath)
    login(session, yamlData['login'])


    startTime = datetime.datetime.now()
    print(startDate, endDate, type)



    # 公有和私有
    if type ==  0:
        execPublic(session, yamlData['publicData'], startDate, endDate)
        execPrivate(session, yamlData['privateData'], startDate, endDate)
    # 公有
    elif type ==  1:
        execPublic(session, yamlData['publicData'], startDate, endDate)
    # 私有
    elif type == 2:
        execPrivate(session, yamlData['privateData'], startDate, endDate)

    endTime = datetime.datetime.now()

    # print(startTime)
    # print(endTime)
    return (endTime-startTime).seconds


if __name__ == '__main__':
    # beginCrawl('2022-12-01','2022-12-01',1)

    # 哪个模板
    # 哪些数据项  ，用list存储
    # 在数据哪个层级 ，用list存储
    # 保存在第几列，第几行
    # 哪个保存名

    # session = requests.Session()
    # yamlData = readYaml(yamlFilePath)
    # login(session,yamlData['login'])

    startDate = '2022-11-15'
    endDate = '2022-11-15'
    #
    # startTime = datetime.datetime.now()
    # print(startDate,endDate,type)

    beginCrawl(startDate,endDate,1)

