from common.common import *
from common.excel_helper import ExcelHepler

province = "安徽"
provinceAreaId = "034"
yamlFilePath = os.path.join(rootPath, "yamlFile", "ah_interface.yaml")
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


# 接口请求出清总电价
def getClearingPriceData(session1 : requests.Session, requestInfo, startDate, endDate):

    url = requestInfo['clearingPriceUrl']
    method = requestInfo['method']
    requestsData = {
        "startDate" : startDate,
        "endDate" : endDate,
        "provinceAreaId" : provinceAreaId,
        "dataType" : "clearingPrice",
    }
    res = session1.request(method=method,url = url,params=requestsData)
    resData = res.json()['data']


    eleList = []
    priceList = []

    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    deviation = (ed - sd).days

    for i in range(0, deviation + 1):

        ele = {}
        price = {}

        for item in resData:
            date = item['date'][:10]
            resD = datetime.datetime.strptime(date, "%Y-%m-%d")
            if resD == sd:

                if item['dataType'] == 'ele':
                    ele['dayAheadData'] = item['dayAheadData']
                    ele['rtData'] = item['rtData']
                elif item['dataType'] == 'price':
                    price['dayAheadData'] = item['dayAheadData']
                    price['rtData'] = item['rtData']

        eleList.append(ele)
        priceList.append(price)

        sd += datetime.timedelta(days=1)


    return {
        "ele": eleList,
        "price": priceList,
            }

# 接口请求机组容量信息
def getStandbyData(session1 : requests.Session, requestInfo, startDate, endDate):

    url = requestInfo['standbyUrl']
    method = requestInfo['method']
    requestsData = {
        "startDate" : startDate,
        "endDate" : endDate,
        "provinceAreaId" : provinceAreaId,
        "dataType" : "standby",
    }
    res = session1.request(method=method,url = url,params=requestsData)
    resData = res.json()['data']

    positiveStandbyList = []
    negativeStandbyList = []

    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    deviation = (ed - sd).days

    for i in range(0, deviation + 1):

        positiveStandby = {}
        negativeStandby = {}

        for item in resData:
            date = item['date'][:10]
            resD = datetime.datetime.strptime(date, "%Y-%m-%d")
            if resD == sd:

                if item['dataType'] == 'positiveStandby':
                    positiveStandby['dayAheadData'] = trun24(item['dayAheadData'])
                    positiveStandby['rtData'] = item['rtData']
                elif item['dataType'] == 'negativeStandby':
                    negativeStandby['dayAheadData'] = trun24(item['dayAheadData'])
                    negativeStandby['rtData'] = item['rtData']

        positiveStandbyList.append(positiveStandby)
        negativeStandbyList.append(negativeStandby)

        sd += datetime.timedelta(days=1)


    return {
        "positiveStandby": positiveStandbyList,
        "negativeStandby": negativeStandbyList,
            }




# 接口请求设备检修信息
def getOverhaulData(session1 : requests.Session, requestInfo, startDate, endDate):

    url = requestInfo['overhaulUrl']
    method = requestInfo['method']


    sd = datetime.datetime.strptime(startDate,"%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate,"%Y-%m-%d")
    deviation = (ed-sd).days

    overhaulList = []

    for i in range(0, deviation + 1):


        deviceName = []
        startTime = []
        endTime = []

        requestsData = {
            "date": sd.strftime("%Y-%m-%d"),
        }
        res = session1.request(method=method, url=url, params=requestsData)
        resData = res.json()['data']

        typeName = {
            "No": [],
            "deviceName": [],  # 设备调度名
            "startTime": [],  # 申请开始时间
            "endTime": [],  # 申请结束时间
        }

        j = 1

        for item in resData:

            typeName['No'].append(j)

            for key in typeName.keys():
                if key == 'No':
                    continue
                typeName[key].append(item[key])

            j += 1

        sd += datetime.timedelta(days=1)

        overhaulList.append(typeName)

    return {"overhaulList":overhaulList}



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

        dateStr1 = datetime.datetime.strftime(sd,"%Y-%m-%d")
        dateStr2 = datetime.datetime.strftime(sd,"%Y%m%d")
        print(dateStr1)

        # d = []
        # for node in templateInfo['node']:
        #     d = data['da']

        saveFileName = templateInfo['saveFileName'] + "-" + dateStr2 + ".xlsx"
        saveFilePath = mkDir(rootSavePath, *templateInfo['savePath'], dateStr1)

        path = os.path.join(saveFilePath, saveFileName)
        # print(saveFileName)
        print(path)


        for info in templateInfo['typeInfo']:
            # print(info)
            d = data
            # print(d)
            if info['board'] is not None:
                for board in info['board']:
                    # print(board)
                    d = d[board]

            d = d[i]

            for node in info['node']:
                d = d[node]


            # if templateInfo['saveFileName'] == "机组检修计划":
            #     e.writeColData(sheetName="Sheet1", colList=templateInfo['colList'],
            #                    beginRowList=templateInfo['beginRowList'], dataList=dataList,
            #                    savePath=path)
            # else:
            isRowPriority = False
            if templateInfo['saveFileName'] == "机组检修计划":
                isRowPriority = True

            e.writeSpecifiedData(dataList=d,savePath=path,
                       beginRow = info['cellInfo']['beginRow'],
                       beginCol = info['cellInfo']['beginCol'],
                       maxCol = info['cellInfo']['maxCol'],
                       rowInterval = info['cellInfo']['rowInterval'],
                       isRowPriority=isRowPriority)


        sd += datetime.timedelta(days=1)



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

    privateDataItemEnums = ["DAY_AHEAD_CLEARING_POWER","DAY_AHEAD_CLEARING_PRICE","REAL_TIME_CLEARING_POWER","REAL_TIME_CLEARING_PRICE"]

    url = requestInfo['clearingUrl']
    method = "GET"
    for unit in unitData:
        requestsData = {
            "startTime" : startDate,
            "endTime" : endDate,
            "unitIds" : unit['unitId'],
            "privateDataItemEnums" : privateDataItemEnums,
        }
        res = session1.request(method=method,url = url,params=requestsData)
        print(res.json())
        resData = res.json()['data'][0]



        def getALL(dataList):

            resData = []
            count = int(len(dataList)/96)
            # print(count)
            for  i in range(0,count):
                resData.append(
                    dataList[ (96*i): (96*(i+1))  ]
                )

            return resData

        dl = []

        daClearEle = getALL(resData['daClearEle'])
        daClearPrice = getALL(resData['daClearPrice'])
        rtClearEle = getALL(resData['rtClearEle'])
        rtClearPrice = getALL(resData['rtClearPrice'])

        for i in range(0,len(daClearEle)):
            dl.append({
                "daClearEle" : daClearEle[i]  ,
                "daClearPrice" : daClearPrice[i] ,
                "rtClearEle" : rtClearEle[i] ,
                "rtClearPrice" : rtClearPrice[i]  ,
            })

        allDataList.append([ unit['unitName'],dl, unit['ownerName']])


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

            dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")
            dateStr2 = datetime.datetime.strftime(sd, "%Y%m%d")
            print(dateStr1)

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

            saveFileName = unitName + "-"+ templateInfo['saveFileName']  + dateStr2 + ".xlsx"
            savePath = mkDir(rootSavePath, *templateInfo['savePath'],ownerName, dateStr1)

            path = os.path.join(savePath, saveFileName)

            sd += datetime.timedelta(days=1)
            print(saveFileName)
            print(path)

            e.writeSpecifiedData(dataList=d, savePath=path,
                                 beginRow=info['cellInfo']['beginRow'],
                                 beginCol=info['cellInfo']['beginCol'],
                                 maxCol=info['cellInfo']['maxCol'],
                                 rowInterval=info['cellInfo']['rowInterval'],
                                 isRowPriority=False)
    e.close()


def execPublic(session, yamlPublicData, startDate, endDate):

    data = {}

    requestInfo = yamlPublicData

    data.update(getMarketData(session, requestInfo, startDate, endDate))
    data.update(getClearingPriceData(session, requestInfo, startDate, endDate))
    data.update(getStandbyData(session, requestInfo, startDate, endDate))
    data.update(getOverhaulData(session, requestInfo, startDate, endDate))

    for item in publicConfig:

        outPublicData(data,startDate,endDate,item)

    print(data)


def execPrivate(session, yamlPrivateData, startDate, endDate):

    unitInfo = getUnitId(session, yamlPrivateData)

    unitData = getPrivateData(session, yamlPrivateData, startDate, endDate ,unitInfo)

    print(unitData)

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
    #
    # session = requests.Session()
    yamlData = readYaml(yamlFilePath)
    # login(session,yamlData['login'])

    startDate = '2023-01-01'
    endDate = '2023-01-02'
    #
    # startTime = datetime.datetime.now()
    # print(startDate,endDate,type)

    beginCrawl(startDate,endDate,2)


    # d = getMarketData(session, yamlData['publicData'], startDate, endDate)
    # outPublicData(d, startDate, endDate, publicConfig[0])

