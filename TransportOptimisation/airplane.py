# -*- coding: utf-8 -*-

import dbapp

"""
航空機モードの計算を行う
"""

__author__ = "第1班"
__status__ = "debug"
__version__= "0.1"
__date__   = "2015/7/10"

class Airplane:

    """
   航空機モードクラス
    """

    # 各種変数が未設定として定義する
    def __init__(self,app):
        self.app = app
	self.mode = None
	self.start = None
	self.end = None

    # データフレームをセットする
    def setDataFrame(df):
	self.dataframes = df

    # 現在の輸送モードを設定する
    def setMode(self,mode):
	self.mode = mode

    # 重量を設定する
    def setWeight(self,kg):
	self.weight = kg
	
    # データベースからデータを取得する
    def getData(self,mode,start,end):
	data = dbapp.getContent(mode,start,end)
	return data
     	
    # 地点間の距離を計算する
    def calcDistance(self,mode,start,end):
    	try:
    		self.mode = mode
    		self.start = start
    		self.end = end
		distance = self.getData(mode,start,end)[0][0]	
        	return distance
        except:
       		return 0
       		
    # 出発地と終着地を指定して距離を算出する
    def setStartEnd(self,start,end):
	self.start = start
	self.end = end
	self.distance = self.calcDistance("airplane",start,end)


    # 一般化費用
    def calcGeneralCost(self,a,b,c,start,end,price,totalweight):
    	try:
    		result = a*self.calcFee("airplane",start,end,totalweight)*self.traffic(totalweight) + b*self.calcTime("airplane",start,end)*self.calcTimeValue(price) + c*self.calcELoad("airplane",start,end,totalweight)*self.calcDistance("airplane",start,end)*self.UnitCost("airplane",start,end)*self.traffic(totalweight)
		if result == 0:
			return 0
		else:
			return result
	except:
		return 0
	    
    # 運賃を計算する(円/kg)*kg
    def calcFee(self,mode,start,end,totalweight):
   	try:
   		self.mode = mode
    		self.start = start
    		self.end = end
    		fee = self.getData(mode,start,end)[0][1]*totalweight
    		return fee
	except:
		return 0

    # 出発地から終着地までの時間（待ち時間を含む）
    def calcTime(self,mode,start,end):
	# start , end
	try:
		self.mode = mode
    		self.start = start
    		self.end = end
		time = self.getData(mode,start,end)[0][2]+24/self.getData(mode,start,end)[0][3]
		return time
	except:
		return 0

    # 時間価値
    def calcTimeValue(self,price):
	# start , end
	try:
		timevalue=price*(1.3*(1/365)*24)
    		return timevalue
    	except:
		return 0

    # 環境負荷
    def calcELoad(self,mode,start,end,totalweight):
    	try:
    		self.mode = mode
    		self.start = start
    		self.end = end
    		eload = self.getData(mode,start,end)[0][4]*totalweight
    		return eload
	except:
		return 0

    # 単位価格
    def UnitCost(self,mode,start,end):
    	try:
    		self.mode = mode
    		self.start = start
    		self.end = end
    		cost = self.getData(mode,start,end)[0][5]
		return cost
    	except:
		return 0
	
    #輸送可能量
    def traffic(self,totalweight):
    	tra = 106
    	fic = totalweight/tra
    	if fic <= 1:
    		return 1
    	else :
    		return int(fic)