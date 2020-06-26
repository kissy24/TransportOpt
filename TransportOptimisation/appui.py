# -*- coding: utf-8 -*-

"""
ユーザインタフェースの処理を記述する
"""

import sys
from PySide2 import QtGui,QtUiTools,QtWidgets

__author__ = "第1班"
__status__ = "debug"
__version__= "0.1"
__date__   = "2015/5/29"

class AppUI:
    """
    このクラスでは入力を処理する
    """

    # 初期化メソッド(引数：県名リストpref)
    def __init__(self,pref,rank):
        self.app = QtWidgets.QApplication(sys.argv)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load("app.ui")
        self.ui.start.addItems(pref)  # 出発地をリストで設定
        self.ui.end.addItems(pref)    # 到着地をリストで設定
        self.ui.comboBox.addItems(rank)
        self.ui.show()

    # ユーザインタフェースを実行する（イベントループを開始する）
    def run(self):
        sys.exit(self.app.exec_())
        
    # 実行ボタンが押されたときに呼び出す関数を設定する
    def setClickFunction(self,name,func):
        obj = getattr(self.ui,name)
        obj.clicked.connect(func)

    # テキストボックスの入力が終了したときに呼び出す関数を設定する
    def setEditingFinishFunction(self,name,func):
        obj = getattr(self.ui,name)
        obj.editingFinished.connect(func)

    # メニューが選択された時に呼び出す関数を設定する
    def setActionFunction(self,name,func):
        obj = getattr(self.ui,name)
        obj.triggered.connect(func)
        
    # sliderがスライドされた時に呼び出す関数を設定する
    def valueChanged(self,name,func):
    	obj = getattr(self.ui,name)
    	obj.valueChanged.connect(func)

    # コンボボックスの選択が変更された時に呼び出す関数を設定する
    def setIndexChangedFunction(self,name,func):
        obj = getattr(self.ui,name)
        obj.currentIndexChanged.connect(func)

    # コンボボックスの現在の選択の値を取得する
    def getCurrentIndex(self,name):
        obj = getattr(self.ui,name)
        return obj.currentIndex()

    # 下部のテキストWidgetに処理の内容を出力する
    def log(self,text):
      current = self.ui.textBrowser.toHtml()
      self.ui.textBrowser.setHtml( current+text+'<BR>' )

    # 指定した名前の部品が持つテキストを取得する
    def getText(self,name):
        obj = getattr(self.ui,name)
        return obj.text()

    # 指定した名前の部品が持つテキストを数字として取得する
    def getNumber(self,name):
        val = self.getText(name)
        ret = 0
        try:
          ret = float(val)
        except Exception:
          pass
        return ret

    # 指定した名前の部品に、指定したテキストを設定する
    def setText(self,name,text):
        obj = getattr(self.ui,name)
        obj.setText(text)
