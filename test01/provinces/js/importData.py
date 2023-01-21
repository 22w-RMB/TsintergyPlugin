import json

from test01.provinces.js.public_private_date import *
import requests



def predictImport(session,info,startDate, endDate):

    url =info['predictDataUrl']
    print(url)

    # 接口参数 templateNameList  的数据
    templateNameList = ["短期系统负荷预测", "受电计划-华东","受电计划-阳城","统调风光功率预测-风力",
                    "统调风光功率预测-光伏","重大设备检修计划","稳定限额","燃机固定出力总值信息披露","现货正负备用空间信息披露"
                    ]


    # 要导入的文件名称
    importFileName = ["短期系统负荷预测",
                    "燃机固定出力总值信息披露",
                    "受电计划-华东",
                    "受电计划-阳城",
                    "统调风光功率预测-风力-汇总",
                    "统调风光功率预测-光伏-汇总",
                    "稳定限额",
                    "现货正负备用空间信息披露",
                    "重大设备检修计划",
                    ]

    # 将 开始日期和结束日期转换成 datetime 格式
    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr = datetime.datetime.strftime(sd, "%Y-%m-%d")

        print(dateStr)

        fileList = []
        fileNameList = []

        for i in importFileName:

            fileName = i + "-" + dateStr + ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames",(None,fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                       open(os.path.join(rootSavePath, "公有数据","预测", dateStr,  fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr)),
            ("provinceAreaId", (None, provinceAreaId)),
            ("templateNameList", (None, json.dumps(templateNameList ))),
            ("type", (None, "PUBLIC")),
            ("dataType", (None, "SPOT_BEFORE")),
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
    importFileName = ["实际系统负荷",
                      "实际统调风光情况-光伏-汇总",
                      "实际统调风光情况-风力-汇总",
                      "实际受电情况-阳城",
                      "实际受电情况-华东",
                      "实际燃机固定出力总值信息",

                      ]

    # 将 开始日期和结束日期转换成 datetime 格式
    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr = datetime.datetime.strftime(sd, "%Y-%m-%d")

        print(dateStr)

        fileList = []
        fileNameList = []

        for i in importFileName:
            fileName = i + "-" + dateStr + ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames", (None, fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                           open(os.path.join(rootSavePath, "公有数据", "实际", dateStr,  fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr)),
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
                        "日前边际分区价格（江南、江北）",
                        "实时边际分区价格（江南、江北）",
                        ]

    # 要导入的文件名称
    importFileName = [
                      "日前边际分区价格",
                      "实时边际分区价格",

                      ]

    # 将 开始日期和结束日期转换成 datetime 格式
    sd = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")

    while sd <= ed:

        dateStr = datetime.datetime.strftime(sd, "%Y-%m-%d")

        print(dateStr)

        fileList = []
        fileNameList = []

        for i in importFileName:
            fileName = i + "-" + dateStr + ".xlsx"

            #  设置 fileNames  参数
            fileNameList.append(
                ("fileNames", (None, fileName))
            )

            # 设置 files  参数
            fileList.append(
                ("files", (fileName,
                           open(os.path.join(rootSavePath, "公有数据", "价格", dateStr, fileName), "rb"))
                 )
            )

        importDatas = [
            ("date", (None, dateStr)),
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
    beginImport('2022-11-15','2022-11-15')