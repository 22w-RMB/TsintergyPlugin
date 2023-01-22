dataTypeList = ["统调负荷实测", "东送计划实测", "非市场出力实测", "新能源出力实测（全网新能源）",
                "新能源出力实测（全网风电）", "新能源出力实测（全网光伏）", ]

dataTypeList = ["统调负荷预测", "东送计划预测", "非市场出力计划", "新能源出力预测（全网新能源）",
                "新能源出力预测（全网风电）", "新能源出力预测（全网光伏）", "正负备用容量", "检修信息"]

fileNamesList = ["全网统一出清电价", "呼包东统一出清电价", "呼包西统一出清电价"]


def writeSpecifiedData(self, dataList, beginRow, beginCol, savePath,
                       maxRow=None, maxCol=None,
                       rowInterval=1, colInterval=1,
                       isRowPriority=True,
                       sheetName="Sheet1"):
    ws = self.wb.sheets[sheetName]

    row = beginRow
    col = beginCol

    for item in dataList:
        ws.range(row, col).value = item

        if isRowPriority:
            row += rowInterval

            if maxRow is None:
                continue

            if row > maxRow:
                row = beginRow
                col += colInterval

            if col > maxCol:
                break

        else:
            col += colInterval

            if maxCol is None:
                continue

            if col > maxCol:
                row += rowInterval
                col += beginCol

            if row > maxRow:
                break

    for i in range(0, len(colList)):

        row = beginRowList[i]
        col = colList[i]
        if len(dataList[i]) == 0:
            continue
        for data in dataList[i]:
            ws.range(row, col).value = data
            row += 1