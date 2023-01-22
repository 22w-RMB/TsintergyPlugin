import os.path

import xlwings


class ExcelHepler:


    def __init__(self , filePath):

        self.app = xlwings.App(visible=False,add_book=False)
        self.app.display_alerts = False
        self.app.screen_updating = False
        self.wb = self.app.books.open(filePath)

        pass

    def writeColData(self,colList,dataList,beginRowList,savePath,sheetName="Sheet1"):
        if len(colList) != len(dataList):
            print("输入的列数组和数据数组不一致！！！！")
            return

        ws = self.wb.sheets[sheetName]
        for i in range(0,len(colList)):

            row = beginRowList[i]
            col = colList[i]
            if len(dataList[i]) == 0:
                continue
            for data in dataList[i]:
                ws.range(row,col).value = data
                row += 1

        self.saveFile(savePath)

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

                # if col > maxCol:
                #     break

            else:
                col += colInterval

                if maxCol is None:
                    continue

                if col > maxCol:
                    row += rowInterval
                    col = beginCol

                # if row > maxRow:
                #     break
        self.saveFile(savePath)


    def saveFile(self, savePath = None):

        if savePath is None:
            savePath = self.filePath

        # 保存
        self.wb.save(savePath)


    def close(self):
        self.wb.close()
        self.app.kill()




if __name__ == '__main__':


    e = ExcelHepler(r'D:\code\pyhton\plugin\test01\common\日前实时出清总电量-20221201.xlsx')

    a = []

    b = []

    savePath = r'D:\code\pyhton\plugin\test01\common\日前实时出清总电量.xlsx'

    for i in range(0,24):
        a.append(i*3)
        b.append(i*4)




    e.writeSpecifiedData(dataList=a, beginRow=2, beginCol=1,savePath=savePath ,
                           maxRow=None, maxCol=16,
                           rowInterval=3, colInterval=1,
                           isRowPriority=False,
                           sheetName="Sheet1")

    a[5] = None

    e.writeSpecifiedData(dataList=a, beginRow=2, beginCol=1,savePath=savePath ,
                           maxRow=None, maxCol=16,
                           rowInterval=3, colInterval=1,
                           isRowPriority=False,
                           sheetName="Sheet1")

    e.close()