from test01.common.common import *

province = "蒙西"
publictemplatePath = os.path.join(rootPath, "template", province, "公有数据")
privatetemplatePath = os.path.join(rootPath, "template", province, "私有数据")
savePath = mkDir(rootPath, "save")
publicSavePath = mkDir(savePath, province, "公有数据")
privateSavePath = mkDir(savePath, province, "私有数据")

# 接口请求所有的公有数据
def getPublicData(session1 : requests.Session, requestInfo, startDate, endDate, provinceAreaId="015",dataLen="LEN_96"):
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    ed += datetime.timedelta(days=2)
    date = datetime.datetime.strftime(ed, "%Y-%m-%d")

    url = requestInfo['url']
    method = requestInfo['method']
    requestsData = {
        "startDate" : startDate,
        "endDate" : date,
        "provinceAreaId" : provinceAreaId,
        "dataLen" : dataLen,
    }
    res = session1.request(method=method,url = url,params=requestsData)
    print(res.json())

    return res.json()['data']


# 获取其他公有数据
def outPublicData(data, startDate, endDate, boardName, dayAheadName, realName, templateName,colList, isPrice):

    board = data[boardName]

    openFilePath :str
    if isPrice:
        openFilePath = os.path.join(publictemplatePath,"预测",templateName)
    else:
        openFilePath = os.path.join(publictemplatePath,"价格",templateName)

    sd = datetime.datetime.strptime(startDate,"%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate,"%Y-%m-%d")
    deviation = (ed-sd).days

    e = ExcelHepler(openFilePath)
    for i in range(0,deviation+1):


        dataList = []

        date = datetime.datetime.strftime(sd,"%Y-%m-%d")
        dd = datetime.datetime.strftime(sd,"%Y%m%d")
        print(date)
        saveFileName = ""



        if isPrice:
            # 全网统一出清
            dataList.append(board[i]['netUnifiedPrice'])
            # 呼包东出清
            dataList.append(board[i]['hbdUnifiedPrice'])
            # 呼包西出清
            dataList.append(board[i]['hbxUnifiedPrice'])

            # 文件名
            saveFileName = date + templateName
        else:
            # D日
            dataList.append(board[i][dayAheadName])
            # D+1日
            dataList.append(board[i + 1][dayAheadName])
            # D+2日
            dataList.append(board[i + 2][dayAheadName])
            # 实时
            dataList.append(board[i][realName])

            #文件名
            saveFileName = dd + templateName

        sd += datetime.timedelta(days=1)
        print(saveFileName)
        saveFilePath = os.path.join(publicSavePath, date, saveFileName)


        e.writeColData(sheetName="Sheet1", colList=colList, dataList=dataList)
        e.saveFile(saveFilePath)
    e.close()

        # saveFile(openFilePath,colList,dataList,saveFilePath)


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
            "businessType" : unit['businessType']
        }
        res = session1.request(method=method,url = url,params=requestsData)

        allDataList.append([ unit['unitName'],res.json()['data'], unit['ownerName']])


    return allDataList

# 输出所有的私有数据
def outPrivateData(data, startDate, endDate):


    openFilePath = os.path.join(privatetemplatePath,"省内现货出清结果.xlsx")

    colList = [3,4,5,6,7,8]

    sd = datetime.datetime.strptime(startDate,"%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate,"%Y-%m-%d")
    deviation = (ed-sd).days


    e = ExcelHepler(openFilePath)



    for item in data:
        unitName = item[0]
        ownerName = item[2]
        unitData = item[1]
        sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")

        for i in range(0,deviation+1):


            dataList = []

            date = datetime.datetime.strftime(sd,"%Y-%m-%d")
            dd = datetime.datetime.strftime(sd,"%Y%m%d")
            # print(date)
            saveFileName = unitName + "-" + "省内现货出清结果" + "-"  + dd +".xlsx"

            print(ownerName,"： " +saveFileName)


            saveFilePath = os.path.join(privateSavePath, ownerName,date,saveFileName)

            # 中长期合同电力
            dataList.append(unitData[i]["fittingPower"])
            # 中长期合同电价
            dataList.append(unitData[i]["fittingPrice"])
            # 日前出清电力
            dataList.append(unitData[i]["dayAheadClearingPower"])
            # 实时出清电力
            dataList.append(unitData[i]["realTimeClearingPower"])
            # 实时出清电价
            dataList.append(unitData[i]["realTimeClearingPrice"])
            # 实际计量电力
            dataList.append(unitData[i]["actualMeasuredPower"])

            sd += datetime.timedelta(days=1)

            e.writeColData(sheetName="Sheet1", colList=colList, dataList=dataList)
            e.saveFile(saveFilePath)

            # saveFile(openFilePath,colList,dataList,saveFilePath)
    e.close()


def execPublic(session, yamlData, startDate, endDate):

    mkPublicDir(startDate, endDate)

    responseData = getPublicData(session, yamlData['publicData'], startDate, endDate)

    a = [
        ['clearingPrice', None, None, '日分解及出清结果数据.xlsx', [9, 10, 11], True],
        ['loadList', 'dayAheadLoad', 'rtLoad', '统调负荷预测及实测.xlsx', [3, 4, 5, 6], False],
        ['newEnergyAll', 'dayAheadNewEnergyLoad', 'rtNewEnergyLoad', '新能源出力预测及实测 全网新能源.xlsx', [3, 4, 5, 6], False],
        ['newEnergySun', 'dayAheadNewEnergyLoad', 'rtNewEnergyLoad', '新能源出力预测及实测 全网光伏.xlsx', [3, 4, 5, 6], False],
        ['newEnergyWind', 'dayAheadNewEnergyLoad', 'rtNewEnergyLoad', '新能源出力预测及实测 全网风电.xlsx', [3, 4, 5, 6], False],
        ['eastTransPlan', 'eastTransForecast', 'eastTransReal', '东送计划预测及实际.xlsx', [3, 4, 5, 6], False],
        ['noMarketPlan', 'nonMarketPlanForecast', 'nonMarketPlanReal', '非市场出力计划及实测.xlsx', [3, 4, 5, 6], False]
    ]

    for i in a:
        outPublicData(responseData, startDate, endDate, i[0], i[1], i[2], i[3], i[4], i[5])


def execPrivate(session, yamlData, startDate, endDate):
    unitInfo = getUnitId(session, yamlData['privateData'])

    # 创建文件夹
    mkPrivateDir(unitInfo,startDate, endDate)

    unitData = getPrivateData(session, yamlData['privateData'], startDate, endDate ,unitInfo)
    outPrivateData(unitData,startDate,endDate)

def beginCrawl(startDate,endDate,type):

    session = requests.Session()
    yamlData = readYaml()
    login(session,yamlData['login'])


    startTime = datetime.datetime.now()
    print(startDate,endDate,type)



    # 公有和私有
    if type ==  0:
        execPublic(session, yamlData, startDate, endDate)
        execPrivate(session, yamlData, startDate, endDate)
    # 公有
    elif type ==  1:
        execPublic(session, yamlData, startDate, endDate)
    # 私有
    elif type == 2:
        execPrivate(session, yamlData, startDate, endDate)

    endTime = datetime.datetime.now()

    # print(startTime)
    # print(endTime)
    return (endTime-startTime).seconds


if __name__ == '__main__':
    beginCrawl('2022-12-01','2022-12-02',2)