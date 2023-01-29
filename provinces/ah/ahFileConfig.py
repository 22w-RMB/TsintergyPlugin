

privateFileConfig = [

    {   # 日前出清电量
        'templatePath': ['私有数据'] ,
        'templateName': '日前出清电量' ,
        'savePath':  ['私有数据'],
        'saveFileName': '日前出清电量' ,
        'typeInfo': [
            {"board": None, "node": ['daClearEle'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 日前出清电价
        'templatePath': ['私有数据'] ,
        'templateName': '日前出清电价' ,
        'savePath':  ['私有数据'],
        'saveFileName': '日前出清电价' ,
        'typeInfo': [
            {"board": None, "node": ['daClearPrice'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 实时出清电量
        'templatePath': ['私有数据'] ,
        'templateName': '实时出清电量' ,
        'savePath':  ['私有数据'],
        'saveFileName': '实时出清电量' ,
        'typeInfo': [
            {"board": None, "node": ['rtClearEle'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 实时出清电价
        'templatePath': ['私有数据'] ,
        'templateName': '实时出清电价' ,
        'savePath':  ['私有数据'],
        'saveFileName': '实时出清电价' ,
        'typeInfo': [
            {"board": None, "node": ['rtClearPrice'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },





]




publicPredictConfig = [

    {   # 负荷信息-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '负荷信息-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '负荷信息-预测' ,
        'typeInfo': [
            {"board": ['loadList'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 发电总出力-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '发电总出力-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '发电总出力-预测' ,
        'typeInfo': [
            {"board": ['powerGeneration'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 非市场机组总出力-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '非市场机组总出力-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '非市场机组总出力-预测' ,
        'typeInfo': [
            {"board": ['noMarketPlan'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 风电总出力-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '风电总出力-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '风电总出力-预测' ,
        'typeInfo': [
            {"board": ['newEnergyWind'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 光伏总出力-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '光伏总出力-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '光伏总出力-预测' ,
        'typeInfo': [
            {"board": ['newEnergySun'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 新能源总出力-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '新能源总出力-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '新能源总出力-预测' ,
        'typeInfo': [
            {"board": ['newEnergyAll'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 水电含抽蓄发电出力-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '水电含抽蓄发电出力-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '水电含抽蓄发电出力-预测' ,
        'typeInfo': [
            {"board": ['pumpingPower'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 外来（外送）电交易计划-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '外来（外送）电交易计划-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '外来（外送）电交易计划-预测' ,
        'typeInfo': [
            {"board": ['tradePower'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 正备用信息-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '正备用信息-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '正备用信息-预测' ,
        'typeInfo': [
            {"board": ['positiveStandby'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 负备用信息-预测
        'templatePath': ['公有数据','预测'] ,
        'templateName': '负备用信息-预测' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '负备用信息-预测' ,
        'typeInfo': [
            {"board": ['negativeStandby'], "node": ['dayAheadData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 机组检修计划
        'templatePath': ['公有数据','预测'] ,
        'templateName': '机组检修计划' ,
        'savePath':  ['公有数据','预测'],
        'saveFileName': '机组检修计划' ,
        'typeInfo': [
            {"board": ['overhaulList'],  "node": ['No'] , "cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": None, "rowInterval": 1} },
            {"board": ['overhaulList'],  "node": ['deviceName'], "cellInfo": {'beginRow': 2, "beginCol": 2, "maxCol": None, "rowInterval": 1} },
            {"board": ['overhaulList'],  "node": ['startTime'], "cellInfo": {'beginRow': 2, "beginCol": 3, "maxCol": None, "rowInterval": 1} },
            {"board": ['overhaulList'],  "node": ['endTime'], "cellInfo": {'beginRow': 2, "beginCol": 4, "maxCol": None, "rowInterval": 1} }, ] ,
    },


]

publicRealConfig = [

    {   # 负荷信息-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '负荷信息-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '负荷信息-实际' ,
        'typeInfo': [
            {"board": ['loadList'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 发电总出力-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '发电总出力-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '发电总出力-实际' ,
        'typeInfo': [
            {"board": ['powerGeneration'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 非市场机组总出力-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '非市场机组总出力-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '非市场机组总出力-实际' ,
        'typeInfo': [
            {"board": ['noMarketPlan'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 风电总出力-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '风电总出力-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '风电总出力-实际' ,
        'typeInfo': [
            {"board": ['newEnergyWind'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 光伏总出力-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '光伏总出力-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '光伏总出力-实际' ,
        'typeInfo': [
            {"board": ['newEnergySun'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 新能源总出力-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '新能源总出力-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '新能源总出力-实际' ,
        'typeInfo': [
            {"board": ['newEnergyAll'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 水电含抽蓄发电出力-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '水电含抽蓄发电出力-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '水电含抽蓄发电出力-实际' ,
        'typeInfo': [
            {"board": ['pumpingPower'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },



    {   # 正备用信息-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '正备用信息-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '正备用信息-实际' ,
        'typeInfo': [
            {"board": ['positiveStandby'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

    {   # 负备用信息-实际
        'templatePath': ['公有数据','实际'] ,
        'templateName': '负备用信息-实际' ,
        'savePath':  ['公有数据','实际'],
        'saveFileName': '负备用信息-实际' ,
        'typeInfo': [
            {"board": ['negativeStandby'], "node": ['rtData'],"cellInfo": {'beginRow': 2, "beginCol": 1, "maxCol": 16, "rowInterval": 2}   },
                     ] ,
    },

]


publicPriceConfig = [
    {  # 日前实时出清总电量
        'templatePath': ['公有数据', '价格'],
        'templateName': '日前实时出清总电量',
        'savePath': ['公有数据', '价格'],
        'saveFileName': '日前实时出清总电量',
        'typeInfo': [
            {"board": ['ele'], "node": ['dayAheadData'],
             "cellInfo": {'beginRow': 2, "beginCol": 2, "maxCol": 17, "rowInterval": 3}},

            {"board": ['ele'], "node": ['rtData'],
             "cellInfo": {'beginRow': 3, "beginCol": 2, "maxCol": 17, "rowInterval": 3}},
        ],
    },

    {  # 日前实时出清加权均价
        'templatePath': ['公有数据', '价格'],
        'templateName': '日前实时出清加权均价',
        'savePath': ['公有数据', '价格'],
        'saveFileName': '日前实时出清加权均价',
        'typeInfo': [
            {"board": ['price'], "node": ['dayAheadData'],
             "cellInfo": {'beginRow': 2, "beginCol": 2, "maxCol": 17, "rowInterval": 3}},

            {"board": ['price'], "node": ['rtData'],
             "cellInfo": {'beginRow': 3, "beginCol": 2, "maxCol": 17, "rowInterval": 3}},
        ],
    },

]

publicConfig = []
publicConfig.extend(publicPredictConfig)
publicConfig.extend(publicRealConfig)
publicConfig.extend(publicPriceConfig)
