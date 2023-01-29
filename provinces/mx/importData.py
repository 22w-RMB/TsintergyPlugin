import json

import requests
from provinces.mx.public_private_date import *


def predictImport(session,info,startDate, endDate):

    url =info['predictDataUrl']
    print(url)

    # 接口参数 templateNameList  的数据
    templateNameList = ["统调负荷预测", "东送计划预测", "非市场出力计划", "新能源出力预测（全网新能源）",
                "新能源出力预测（全网风电）", "新能源出力预测（全网光伏）", "正负备用容量", "检修信息"]


    # 要导入的文件名称
    importFileName = ["东送计划预测及实际",
                    "非市场出力计划及实测",
                    "检修信息",
                    "统调负荷预测及实测",
                    "新能源出力预测及实测 全网风电",
                    "新能源出力预测及实测 全网光伏",
                    "新能源出力预测及实测 全网新能源",
                    ]

    # 将 开始日期和结束日期转换成 datetime 格式
    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")
        dateStr2 = datetime.datetime.strftime(sd, "%Y%m%d")

        print(dateStr1)

        fileList = []
        fileNameList = []

        for i in importFileName:

            fileName = dateStr2 + i +  ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames",(None,fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                       open(os.path.join(rootSavePath, "公有数据", dateStr1,  fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, provinceAreaId)),
            ("templateNameList", (None, json.dumps(templateNameList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "SPOT_BEFORE")),
            ("descr", (None, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "上传" )  ),
        ]

        importDatas.extend(fileNameList)
        importDatas.extend(fileList)

        # 发起请求
        importRes = session.request(method="post", url=url, files=importDatas)

        print(importDatas)
        print(importRes.json())

        # 日期 +1
        sd += datetime.timedelta(days=1)


def realImport(session, info, startDate, endDate):

    url = info['realDataUrl']
    print(url)

    # 接口参数 templateNameList  的数据
    templateNameList = ["实际系统负荷","实际受电情况-华东","实际受电情况-阳城",
                        "实际统调风光情况-风力","实际统调风光情况-光伏","实际燃机固定出力总值信息"
                        ]

    # 要导入的文件名称
    importFileName = ["东送计划预测及实际",
                    "非市场出力计划及实测",
                    "检修信息",
                    "统调负荷预测及实测",
                    "新能源出力预测及实测 全网风电",
                    "新能源出力预测及实测 全网光伏",
                    "新能源出力预测及实测 全网新能源",
                    ]

    # 将 开始日期和结束日期转换成 datetime 格式
    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")
        dateStr2 = datetime.datetime.strftime(sd, "%Y%m%d")

        print(dateStr1)

        fileList = []
        fileNameList = []

        for i in importFileName:

            fileName = dateStr2 + i +  ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames",(None,fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                       open(os.path.join(rootSavePath, "公有数据", dateStr1,  fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, provinceAreaId)),
            ("templateNameList", (None, json.dumps(templateNameList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "SPOT_AFTER")),
        ]

        importDatas.extend(fileNameList)
        importDatas.extend(fileList)

        # 发起请求
        importRes = session.request(method="post", url=url, files=importDatas)

        print(importDatas)
        print(importRes.json())

        # 日期 +1
        sd += datetime.timedelta(days=1)



def priceImport(session, info, startDate, endDate):

    url = info['priceDataUrl']
    print(url)

    # 接口参数 templateNameList  的数据
    templateNameList = [
        "全网统一出清电价",
        "呼包东统一出清电价",
        "呼包西统一出清电价"
    ]

    # 要导入的文件名称
    importFileName = [
                      "日分解及出清结果数据",

                      ]

    # 将 开始日期和结束日期转换成 datetime 格式
    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")

        print(dateStr1)

        fileList = []
        fileNameList = []

        for i in importFileName:

            fileName = dateStr1 + i +  ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames",(None,fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                       open(os.path.join(rootSavePath, "公有数据", dateStr1,  fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, provinceAreaId)),
            ("templateNameList", (None, json.dumps(templateNameList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "PRICE_DATA")),
        ]

        importDatas.extend(fileNameList)
        importDatas.extend(fileList)

        # 发起请求
        importRes = session.request(method="post", url=url, files=importDatas)

        print(importDatas)
        print(importRes.json())

        # 日期 +1
        sd += datetime.timedelta(days=1)


def beginImport(startDate,endDate):

    s = requests.Session()
    yamlData = readYaml(yamlFilePath)

    login(s, loginInfo=yamlData['importInfo']['login'])
    predictImport(s,yamlData['importInfo'],startDate,endDate)
    realImport(s,yamlData['importInfo'],startDate,endDate)
    priceImport(s,yamlData['importInfo'],startDate,endDate)



if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    beginImport('2022-11-28','2022-11-28')