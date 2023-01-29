

privateFileConfig = [

    #    日前出清结果
    {
        'templatePath': ['私有数据'],
        'templateName': '日前出清结果',
        'savePath': ['私有数据'],
        'saveFileName': '日前出清结果',
        'colList': [2, 3, 6, 7, 8, 11, 12],
        'beginRowList': [2, 2, 2, 2, 2, 2, 2],
        'typeInfo': [
            {"board": None, "node": ['daMltPowerSum']},  # 中长期电力合约（MWh）
            {"board": None, "node": ['daStandardResolve']},  # 日前标准分解（MWh）
            {"board": None, "node": ['daMltEle']},  # 合计电量(折算机端电力)（MW）
            {"board": None, "node": ['daClearPower']},  # 日前出清电力（MW）
            {"board": None, "node": ['daUnitPrice']},  # 机组报价（元/MWh）
            {"board": None, "node": ['daSystemMarginJnDistrictPrice']},  # 系统边际江南分区价格（元/MWh）
            {"board": None, "node": ['daSystemMarginJbDistrictPrice']},  # 系统边际江北分区价格（元/MWh）
        ],

    },

    #    实时出清结果
    {
        'templatePath': ['私有数据'],
        'templateName': '实时出清结果统合',
        'savePath': ['私有数据'],
        'saveFileName': '实时出清结果统合',
        'colList': [2, 3, 6, 7, 8, 9],
        'beginRowList': [2, 2, 2, 2, 2, 2],
        'typeInfo': [
            {"board": None, "node": ['rtMltPowerSum']},  # 中长期电力合约（MWh）
            {"board": None, "node": ['rtStandardResolve']},  # 实时标准分解（MWh）
            {"board": None, "node": ['rtClearPower']},  # 实时出清电力（MW）
            {"board": None, "node": ['rtUnitPrice']},  # 机组报价（元/MWh）
            {"board": None, "node": ['rtSystemMarginJnDistrictPrice']},  # 系统边际江南分区价格（元/MWh）
            {"board": None, "node": ['rtSystemMarginJbDistrictPrice']},  # 系统边际江北分区价格（元/MWh）
        ],

    },

]




publicConfig = [

    {   # 系统负荷 -预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '短期系统负荷预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '短期系统负荷预测' ,
        'colList':  [6],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['loadList'] ,"node": ['dayAheadLoad'] },
                     ] ,
    },
    {   # 系统负荷 - 实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '实际系统负荷' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '实际系统负荷' ,
        'colList':  [5],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['loadList'] ,"node": ['rtLoad'] },
                     ] ,
    },

    {   # 燃机固定出力总值信息披露 - 预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '燃机固定出力总值信息披露' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '燃机固定出力总值信息披露' ,
        'colList':  [6],
        'beginRowList': [4] ,
        'typeInfo': [{"board":['unitPower'] ,"node": ['daData'] },
                     ] ,
    },
    {   # 燃机固定出力总值信息披露 - 实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '实际燃机固定出力总值信息' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '实际燃机固定出力总值信息' ,
        'colList':  [5],
        'beginRowList': [4] ,
        'typeInfo': [{"board":['unitPower'] ,"node": ['rtData'] },
                     ] ,
    },

    {   # 受电计划-华东 - 预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '受电计划-华东' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '受电计划-华东' ,
        'colList':  [6],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerPlan'] ,"node": ['daPowerPlanHuangDong'] },
                     ] ,
    },
    {   # 实际受电情况-华东 - 实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '实际受电情况-华东' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '实际受电情况-华东' ,
        'colList':  [5],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerPlan'] ,"node": ['rtPowerPlanHuangDong'] },
                     ] ,
    },

    {   # 受电计划-阳城 - 预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '受电计划-阳城' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '受电计划-阳城' ,
        'colList':  [6],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerPlan'] ,"node": ['daPowerPlanYangCheng'] },
                     ] ,
    },
    {   # 实际受电情况-阳城 - 实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '实际受电情况-阳城' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '实际受电情况-阳城' ,
        'colList':  [5],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerPlan'] ,"node": ['rtPowerPlanYangCheng'] },
                     ] ,
    },

    {   # 统调风光功率预测-风力-汇总 - 预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '统调风光功率预测-风力-汇总' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '统调风光功率预测-风力-汇总' ,
        'colList':  [6],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerWindSun'] ,"node": ['daPowerLoadWind'] },
                     ] ,
    },
    {   # 实际统调风光情况-风力-汇总 - 实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '实际统调风光情况-风力-汇总' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '实际统调风光情况-风力-汇总' ,
        'colList':  [5],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerWindSun'] ,"node": ['rtPowerLoadWind'] },
                     ] ,
    },

    {   # 统调风光功率预测-光伏-汇总 - 预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '统调风光功率预测-光伏-汇总' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '统调风光功率预测-光伏-汇总' ,
        'colList':  [6],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerWindSun'] ,"node": ['daPowerLoadSun'] },
                     ] ,
    },
    {   # 实际统调风光情况-光伏-汇总 - 实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '实际统调风光情况-光伏-汇总' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '实际统调风光情况-光伏-汇总' ,
        'colList':  [5],
        'beginRowList': [5] ,
        'typeInfo': [{"board":['powerWindSun'] ,"node": ['rtPowerLoadSun'] },
                     ] ,
    },

    {  # 现货正负备用空间信息披露 - 预测
        'templatePath': ['公有数据', '预测'],
        'templateName': '现货正负备用空间信息披露',
        'savePath': ['公有数据', '预测'],
        'saveFileName': '现货正负备用空间信息披露',
        'colList': [5,6],
        'beginRowList': [8,8],
        'typeInfo': [
            {"board": ['spareList'], "node": ['negativeSpare']},
            {"board": ['spareList'], "node": ['positiveSpare']},
                     ],
    },

    {  # 重大设备检修计划 - 预测
        'templatePath': ['公有数据', '预测'],
        'templateName': '重大设备检修计划',
        'savePath': ['公有数据', '预测'],
        'saveFileName': '重大设备检修计划',
        'colList': [2,3,4],
        'beginRowList': [4,4,4],
        'typeInfo': [
            {"board": ['overhaulList'], "node": ['deviceName']},
            {"board": ['overhaulList'], "node": ['startTime']},
            {"board": ['overhaulList'], "node": ['endTime']},
                     ],
    },

    {  # 稳定限额 - 预测
        'templatePath': ['公有数据', '预测'],
        'templateName': '稳定限额',
        'savePath': ['公有数据', '预测'],
        'saveFileName': '稳定限额',
        'colList': [1,2],
        'beginRowList': [4,4],
        'typeInfo': [
            {"board": ['limitList'], "node": ['deviceName']},
            {"board": ['limitList'], "node": ['stableLimit']},
                     ],
    },


    {   # 日前边际分区价格
        'templatePath': ['公有数据','价格'] ,
        'templateName': '日前边际分区价格' ,
        'savePath':  ['公有数据','价格'],
        'saveFileName': '日前边际分区价格' ,
        'colList':  [2,3],
        'beginRowList': [2,2] ,
        'typeInfo': [
            {"board":['areaPrice'] ,"node": ['daAreaSouthPrice'] },
            {"board":['areaPrice'] ,"node": ['daAreaNorthPrie'] },
                     ] ,
    },
    {   # 实时边际分区价格
        'templatePath': ['公有数据','价格'] ,
        'templateName': '实时边际分区价格' ,
        'savePath':  ['公有数据','价格'],
        'saveFileName': '实时边际分区价格' ,
        'colList':  [2,3],
        'beginRowList': [2,2] ,
        'typeInfo': [
            {"board":['areaPrice'] ,"node": ['rtAreaSouthPrice'] },
            {"board":['areaPrice'] ,"node": ['rtAreaNorthPrice'] },
                     ] ,
    },


]