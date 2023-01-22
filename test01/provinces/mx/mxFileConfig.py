

privateFileConfig = [

    #    日前出清结果
    {
        'templatePath': ['私有数据'],
        'templateName': '省内现货出清结果',
        'savePath': ['私有数据'],
        'saveFileName': '省内现货出清结果',
        'colList': [3,4,5,6,7,8],
        'beginRowList': [2, 2, 2, 2, 2, 2],
        'typeInfo': [
            {"board": None, "node": ['fittingPower']},  # 拟合电力
            {"board": None, "node": ['fittingPrice']},  # 拟合电价
            {"board": None, "node": ['dayAheadClearingPower']},  # 日前出清电力
            {"board": None, "node": ['realTimeClearingPower']},  # 实时出清电力
            {"board": None, "node": ['realTimeClearingPrice']},  # 实时出清电价
            {"board": None, "node": ['actualMeasuredPower']},  # 实际计量电力
        ],

    },


]




publicConfig = [

    {   # 统调负荷预测及实测
        'templatePath': ['公有数据'] ,
        'templateName': '统调负荷预测及实测' ,
        'savePath':  ['公有数据'],
        'saveFileName': '统调负荷预测及实测' ,
        'colList':  [3,4,5,6],
        'beginRowList': [2,2,2,2] ,
        'typeInfo': [
            {"board":['loadList'] ,"whitchDay": 0, "node": ['dayAheadLoad'] },
            {"board":['loadList'] ,"whitchDay": 1, "node": ['dayAheadLoad'] },
            {"board":['loadList'] ,"whitchDay": 2, "node": ['dayAheadLoad'] },
            {"board":['loadList'] ,"whitchDay": 0, "node": ['rtLoad'] },
                     ] ,
    },

    {  # 新能源出力预测及实测 全网风电
        'templatePath': ['公有数据'],
        'templateName': '新能源出力预测及实测 全网风电',
        'savePath': ['公有数据'],
        'saveFileName': '新能源出力预测及实测 全网风电',
        'colList': [3, 4, 5, 6],
        'beginRowList': [2, 2, 2, 2],
        'typeInfo': [
            {"board": ['newEnergyWind'], "whitchDay": 0, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergyWind'], "whitchDay": 1, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergyWind'], "whitchDay": 2, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergyWind'], "whitchDay": 0, "node": ['rtNewEnergyLoad']},
        ],
    },

    {  # 新能源出力预测及实测 全网光伏
        'templatePath': ['公有数据'],
        'templateName': '新能源出力预测及实测 全网光伏',
        'savePath': ['公有数据'],
        'saveFileName': '新能源出力预测及实测 全网光伏',
        'colList': [3, 4, 5, 6],
        'beginRowList': [2, 2, 2, 2],
        'typeInfo': [
            {"board": ['newEnergySun'], "whitchDay": 0, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergySun'], "whitchDay": 1, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergySun'], "whitchDay": 2, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergySun'], "whitchDay": 0, "node": ['rtNewEnergyLoad']},
        ],
    },

    {  # 新能源出力预测及实测 全网新能源
        'templatePath': ['公有数据'],
        'templateName': '新能源出力预测及实测 全网新能源',
        'savePath': ['公有数据'],
        'saveFileName': '新能源出力预测及实测 全网新能源',
        'colList': [3, 4, 5, 6],
        'beginRowList': [2, 2, 2, 2],
        'typeInfo': [
            {"board": ['newEnergySun'], "whitchDay": 0, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergySun'], "whitchDay": 1, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergySun'], "whitchDay": 2, "node": ['dayAheadNewEnergyLoad']},
            {"board": ['newEnergySun'], "whitchDay": 0, "node": ['rtNewEnergyLoad']},
        ],
    },

    {  # 非市场出力计划及实测
        'templatePath': ['公有数据'],
        'templateName': '非市场出力计划及实测',
        'savePath': ['公有数据'],
        'saveFileName': '非市场出力计划及实测',
        'colList': [3, 4, 5, 6],
        'beginRowList': [2, 2, 2, 2],
        'typeInfo': [
            {"board": ['noMarketPlan'], "whitchDay": 0, "node": ['nonMarketPlanForecast']},
            {"board": ['noMarketPlan'], "whitchDay": 1, "node": ['nonMarketPlanForecast']},
            {"board": ['noMarketPlan'], "whitchDay": 2, "node": ['nonMarketPlanForecast']},
            {"board": ['noMarketPlan'], "whitchDay": 0, "node": ['nonMarketPlanReal']},
        ],
    },

    {  # 东送计划预测及实际
        'templatePath': ['公有数据'],
        'templateName': '东送计划预测及实际',
        'savePath': ['公有数据'],
        'saveFileName': '东送计划预测及实际',
        'colList': [3, 4, 5, 6],
        'beginRowList': [2, 2, 2, 2],
        'typeInfo': [
            {"board": ['eastTransPlan'], "whitchDay": 0, "node": ['eastTransForecast']},
            {"board": ['eastTransPlan'], "whitchDay": 1, "node": ['eastTransForecast']},
            {"board": ['eastTransPlan'], "whitchDay": 2, "node": ['eastTransForecast']},
            {"board": ['eastTransPlan'], "whitchDay": 0, "node": ['eastTransReal']},
        ],
    },


    {  # 检修信息
        'templatePath': ['公有数据'],
        'templateName': '检修信息',
        'savePath': ['公有数据'],
        'saveFileName': '检修信息',
        'colList': [1,2,3,4,5,6,7,8,9,10,11],
        'beginRowList': [2, 2, 2, 2,2,2,2,2,2,2,2],
        'typeInfo': [
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['No']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['factoryName']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['deviceName']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['unitCapacity']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['overhaulNo']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['deviceType']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['deviceStatus']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['statusType']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['changeReason']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['startTime']},
            {"board": ['overhaulList'], "whitchDay": 0, "node": ['endTime']},
        ],
    },

    {  # 日分解及出清结果数据
        'templatePath': ['公有数据'],
        'templateName': '日分解及出清结果数据',
        'savePath': ['公有数据'],
        'saveFileName': '日分解及出清结果数据',
        'colList': [9, 10, 11],
        'beginRowList': [2, 2, 2],
        'typeInfo': [
            {"board": ['clearingPrice'], "whitchDay": 0, "node": ['netUnifiedPrice']},
            {"board": ['clearingPrice'], "whitchDay": 0, "node": ['hbdUnifiedPrice']},
            {"board": ['clearingPrice'], "whitchDay": 0, "node": ['hbxUnifiedPrice']},
        ],
    },

]