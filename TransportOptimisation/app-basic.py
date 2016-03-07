# -*- coding: utf-8 -*-
"""
最適輸送モード計算ソフトウェア
"""

__author__ = "第1班"
__status__ = "debug"
__version__= "0.1"
__date__   = "2015/7/10"

# 輸送モードのリスト
modeStr = [ u'船舶', u'航空', u'鉄道', u'トラック' ]
# 使用する都道府県名のリスト
pref = [u'選択してください',u'北海道',u'福島',u'東京',u'山梨',u'滋賀',u'鳥取',u'香川',u'熊本']
# 輸送モードにおける運賃、時間、環境負荷ランキング
rank = [u'選択してください',u'運賃',u'時間',u'環境負荷']
# 出発地の番号(0は未選択)
start = 0
# 到着地の番号(0は未選択)
end = 0
# ランキングの番号
ranking = 0



import appui
import ship
import airplane
import train
import track
import dbapp
import dbapp2

# UIから、重みパラメータを取得する
def getVariables():
  cost = appl.getNumber('cost')
  time = appl.getNumber('time')
  envload = appl.getNumber('envload')
  return [cost,time,envload]

# UIの重みパラメータを設定する
def setVariablescost(val):
	cost = appl.setText('cost',str(val))	
def setVariablestime(val):
	time = appl.setText('time',str(val))
def setVariablesenvload(val):
	envload = appl.setText('envload',str(val))

# 最適モードを計算する
def doCalc():
    if start==end:
        appl.log(u'出発地と到着地が同じ場所の時は計算できません')
        return
    appl.log(u'最適モード計算中')
    newmode = getOptimalMode( getVariables() )
    setMode(newmode)

# 履歴を表示する
def doCache():
	cache = dbapp2.getContent()
	try:
		appl.log(u'出発地:'+cache[-1][0]+u'到着地:'+cache[-1][1]+u'のとき')
		appl.log(u'個数:'+str(cache[-1][2])+u'重量:'+str(cache[-1][3])+u'単価:'+str(cache[-1][4]))
		appl.log(u'コスト:'+str(cache[-1][5])+u'時間:'+str(cache[-1][6])+u'環境負荷:'+str(cache[-1][7])+u'で')
		appl.log(u'輸送モードは,'+modeStr[int(cache[-1][8])]+u'です')
	except:
		appl.log(u'履歴はありません')
		

# コスト、時間、環境負荷を引数として最適モードを計算する
def getOptimalMode(variables):
    a,b,c = variables
    modes = {}  # 空の辞書型を用意
    dict = {}
    for mode in range(4):
        T = trans[mode]		    # 輸送モードのクラスをTに設定する
        T.setStartEnd(start,end)     # 出発地・終着地を設定
        T.setWeight(appl.getNumber('weight'))         # 重量を設定
        price = appl.getNumber('price')
        totalweight = appl.getNumber('weight')*appl.getNumber('amount')
        w = appl.getNumber('weight')
        am = appl.getNumber('amount')
        t = T.calcGeneralCost(a,b,c,start,end,price,totalweight)
        if t == 0:
        	pass
        else:
        	dict[t] = [am,w,price]
        	modes[t] = mode  # 注：同じコストの時は上書き
    dbapp2.setContent(start,end,dict[t][0],dict[t][1],dict[t][2],a,b,c,modes[min(modes)])
    return modes[min(modes)]	# 最小の輸送モードの値を返す
    
# ランキングを変更する
def setRanking(num):
	global ranking
	ranking = num
	
# ランキングを表示する
def doRanking():
    if ranking==1:
    	r = dbapp2.getFee(start,end)
    	try:
    		appl.log(u'輸送モードの運賃ランキングは')
    		appl.log(u'一位:'+r[0][0])
    		appl.log(u'二位:'+r[1][0])
    		appl.log(u'三位:'+r[2][0])
    		appl.log(u'四位:'+r[3][0])
    		return
    	except:
    		pass
    if ranking==2:
    	r = dbapp2.getTime(start,end)
    	try:
    		appl.log(u'輸送モードの時間ランキングは')
    		appl.log(u'一位:'+r[0][0])
    		appl.log(u'二位:'+r[1][0])
    		appl.log(u'三位:'+r[2][0])
    		appl.log(u'四位:'+r[3][0])
    	except:
    		pass
    if ranking==3:
    	r = dbapp2.getEload(start,end)
    	try:
    		appl.log(u'輸送モードの環境負荷ランキングは')
    		appl.log(u'一位:'+r[0][0])
    		appl.log(u'二位:'+r[1][0])
    		appl.log(u'三位:'+r[2][0])
    		appl.log(u'四位:'+r[3][0])
    	except:
    		pass
        
    
# 最適輸送モードを表示する
def setMode(mode):
  appl.setText('optmode', modeStr[mode] )

# 重量と個数から、合計重量を計算し表示する
def calcTotalWeight():
    w = appl.getNumber('weight')
    a = appl.getNumber('amount')
    appl.setText('totalweight', str(w*a) )

# 単価と合計重量から合計金額を表示する
def calcTotalPrice():
    p = appl.getNumber('price')
    w = appl.getNumber('totalweight')
    appl.setText('totalprice', str(p*w) )

# startのコンボボックスが変更されたときに呼び出される
def setStart(num):
    global start,end
    appl.log(u'出発地:'+pref[num])
    start = pref[num]
    if start==end:
        appl.log(u'出発地と到着を同じ場所に設定できません')

# endのコンボボックスが変更されたときに呼び出される
def setEnd(num):
    global start,end
    appl.log(u'到着地:'+pref[num])
    end = pref[num]
    if start==end:
        appl.log(u'出発地と到着を同じ場所に設定できません')

if __name__=='__main__':


    # UI関係モジュールをクラスとして生成し、applに入れる
    appl = appui.AppUI(pref,rank)
 
    # 輸送クラスの初期化した配列
    trans = [ ship.Ship(appl), airplane.Airplane(appl), train.Train(appl), track.Track(appl) ]
    
    # sliderがスライドされた時に呼び出す関数を設定
    appl.valueChanged('horizontalSlider',setVariablescost)
    appl.valueChanged('horizontalSlider_2',setVariablestime)
    appl.valueChanged('horizontalSlider_3',setVariablesenvload)
    # pushButtonが押されたときにdoCalc関数を呼び出すように設定
    appl.setClickFunction('pushButton',doCalc)
    # pushButtonが押されたときにdoCache関数を呼び出すように設定
    appl.setClickFunction('pushButton_3',doCache)
    # pushButtonが押されたときにdoRanking関数を呼び出すように設定
    appl.setClickFunction('pushButton_2',doRanking)
    # テキストインプットに文字が入力された時に呼び出す関数を設定
    appl.setEditingFinishFunction('weight',calcTotalWeight)
    appl.setEditingFinishFunction('amount',calcTotalWeight)
    appl.setEditingFinishFunction('price',calcTotalPrice)
    # コンボボックスが変更されたときに呼び出す関数を設定
    appl.setIndexChangedFunction('start',setStart)
    appl.setIndexChangedFunction('end',  setEnd)
    appl.setIndexChangedFunction('comboBox',  setRanking)
    # Quitメニューが選ばれた時の処理関数を設定
    appl.setActionFunction('actionQuit',quit)  
    # UIを動作させる
    appl.run()