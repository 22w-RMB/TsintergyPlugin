import json

import requests
from provinces.ah.public_private_date import *


def predictImport(session,info,startDate, endDate):

    url =info['predictDataUrl']
    print(url)

    # 接口参数 templateNameList  的数据
    templateNameList = [  "负荷信息-预测","发电总出力-预测","水电含抽蓄发电出力-预测","外来（外送）电交易计划-预测","非市场机组总出力-预测",
                          "新能源总出力-预测","风电总出力-预测","光伏总出力-预测","正备用信息-预测","负备用信息-预测","机组检修计划"
                    ]


    # 要导入的文件名称
    importFileName = [
            "光伏总出力-预测",
            "发电总出力-预测",
            "外来（外送）电交易计划-预测",
            "新能源总出力-预测",
            "机组检修计划",
            "正备用信息-预测",
            "水电含抽蓄发电出力-预测",
            "负备用信息-预测",
            "负荷信息-预测",
            "非市场机组总出力-预测",
            "风电总出力-预测",

    ]

    # 将 开始日期和结束日期转换成 datetime 格式
    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr1 = datetime.datetime.strftime(sd, "%Y-%m-%d")
        dateStr2 = datetime.datetime.strftime(sd, "%Y%m%d")

        print(dateStr2)

        fileList = []
        fileNameList = []

        for i in importFileName:

            fileName = i + "-" + dateStr2 + ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames",(None,fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                       open(os.path.join(rootSavePath, "公有数据","预测", dateStr1,  fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, provinceAreaId)),
            ("templateNameList", (None, json.dumps(templateNameList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "SPOT_BEFORE")),
            ("descr", (None, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "上传")),
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
    templateNameList = ["负荷信息-实际","发电总出力-实际","水电含抽蓄发电出力-实际","非市场机组总出力-实际",
                        "新能源总出力-实际","风电总出力-实际","光伏总出力-实际","正备用信息-实际","负备用信息-实际"
                        ]

    # 要导入的文件名称
    importFileName = ["光伏总出力-实际",
                    "发电总出力-实际",
                    "新能源总出力-实际",
                    "正备用信息-实际",
                    "水电含抽蓄发电出力-实际",
                    "负备用信息-实际",
                    "负荷信息-实际",
                    "非市场机组总出力-实际",
                    "风电总出力-实际",

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
            fileName = i + "-" + dateStr2 + ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames", (None, fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                           open(os.path.join(rootSavePath, "公有数据", "实际", dateStr1,  fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, provinceAreaId)),
            ("templateNameList", (None, json.dumps(templateNameList))),
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
                        "日前实时出清总电量",
                        "日前实时出清加权均价"
                        ]

    # 要导入的文件名称
    importFileName = [
                      "日前实时出清总电量",
                      "日前实时出清加权均价"

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
            fileName = i + "-" + dateStr2 + ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames", (None, fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                           open(os.path.join(rootSavePath, "公有数据", "价格", dateStr1, fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr1)),
            ("provinceAreaId", (None, provinceAreaId)),
            ("templateNameList", (None, json.dumps(templateNameList))),
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
    beginImport('2022-12-01','2022-12-01')