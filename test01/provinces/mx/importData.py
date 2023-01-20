import json

from test01.common.common import *
import requests



def predictImport(session,predictInfo,startDate, endDate):

    url =predictInfo['predictDataUrl']
    print(url)

    dataTypeList = ["统调负荷预测", "东送计划预测", "非市场出力计划", "新能源出力预测（全网新能源）",
                     "新能源出力预测（全网风电）", "新能源出力预测（全网光伏）", "正负备用容量", "检修信息"]

    fileNamesList = []

    for i in dataTypeList:

        if i == "正负备用容量" or i == "检修信息":
            continue

        fileNamesList.append(("fileNames", (None, i + ".xlsx")))

    # fileNamesList = [
    #     ("fileNames", (None, "统调负荷预测.xlsx")),
    #     ("fileNames", (None, "东送计划预测.xlsx")),
    #     ("fileNames", (None, "非市场出力计划.xlsx")),
    #     ("fileNames", (None, "新能源出力预测（全网新能源）.xlsx")),
    #     ("fileNames", (None, "新能源出力预测（全网风电）.xlsx")),
    #     ("fileNames", (None, "新能源出力预测（全网光伏）.xlsx")),
    # ]

    dataFileName = ["统调负荷预测及实测.xlsx",
                    "东送计划预测及实际.xlsx",
                    "非市场出力计划及实测.xlsx",
                    "新能源出力预测及实测 全网新能源.xlsx",
                    "新能源出力预测及实测 全网风电.xlsx",
                    "新能源出力预测及实测 全网光伏.xlsx",

                    ]


    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")
        dateStr2 = datetime.datetime.strftime(sd, "%Y%m%d")

        print(dateStr1)

        filePathList = []

        for i in dataFileName:
            filePathList.append(
                ("files", (dateStr2 + i,
                       open(os.path.join(publicPath, dateStr1, dateStr2 + i), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, "015")),
            ("templateNameList", (None, json.dumps(dataTypeList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "SPOT_BEFORE")),
            ("descr", (None, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"导入")),
        ]

        importDatas.extend(fileNamesList)
        importDatas.extend(filePathList)

        importRes = session.request(method="post", url=url, files=importDatas)

        print(importDatas)
        print(importRes.json())

        sd += datetime.timedelta(days=1)


def realImport(session, realInfo, startDate, endDate):
    url = realInfo['realDataUrl']
    print(url)

    dataTypeList = ["统调负荷实测", "东送计划实测", "非市场出力实测", "新能源出力实测（全网新能源）",
                     "新能源出力实测（全网风电）", "新能源出力实测（全网光伏）", ]

    dataFileName = ["统调负荷预测及实测.xlsx",
                    "东送计划预测及实际.xlsx",
                    "非市场出力计划及实测.xlsx",
                    "新能源出力预测及实测 全网新能源.xlsx",
                    "新能源出力预测及实测 全网风电.xlsx",
                    "新能源出力预测及实测 全网光伏.xlsx",

                    ]

    fileNamesList = []

    for i in dataTypeList:
        fileNamesList.append( ("fileNames", (None, i+ ".xlsx"))  )


    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:
        dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")
        dateStr2 = datetime.datetime.strftime(sd, "%Y%m%d")



        filePathList = []

        for i in dataFileName:
            filePathList.append(
                ("files", (dateStr2 + i,
                       open(os.path.join(publicPath, dateStr1, dateStr2 + i), "rb")
                           )
                 )
            )


        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, "015")),
            ("templateNameList", (None, json.dumps(dataTypeList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "SPOT_AFTER")),
        ]

        importDatas.extend(fileNamesList)
        importDatas.extend(filePathList)

        importRes = session.request(method="post", url=url, files=importDatas)

        print(importDatas)
        print(importRes.json())

        sd += datetime.timedelta(days=1)



def priceImport(session, priceInfo, startDate, endDate):
    url = priceInfo['priceDataUrl']
    print(url)


    fileNamesList = ["全网统一出清电价","呼包东统一出清电价","呼包西统一出清电价"]



    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:
        dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")

        filename = dateStr1 + '日分解及出清结果数据.xlsx'

        importDatas = [
            ("fileNames",(None,filename )),
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, "015")),
            ("templateNameList", (None, json.dumps(fileNamesList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "PRICE_DATA")),
            ("files", (filename,
                       open(os.path.join(publicPath, dateStr1, filename), "rb")
                           )
             )
        ]


        importRes = session.request(method="post", url=url, files=importDatas)

        print(importDatas)
        print(importRes.json())

        sd += datetime.timedelta(days=1)


def beginImport(startDate,endDate):

    s = requests.Session()
    yamlData = readYaml()

    login(s, loginInfo=yamlData['importInfo']['login'])
    predictImport(s,yamlData['importInfo'],startDate,endDate)
    realImport(s,yamlData['importInfo'],startDate,endDate)
    priceImport(s,yamlData['importInfo'],startDate,endDate)



if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    beginImport('2022-12-01','2022-12-02')