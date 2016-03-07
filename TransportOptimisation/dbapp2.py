#coding: utf-8 
import sqlite3

"""
データベースに履歴をキャッシュとして残す、また各価値ランキングの表示を行う
"""

con = sqlite3.connect("./app.db")
cur = con.cursor()

#履歴を取得する
def getContent():
	ret = cur.execute("select * from cache")
	return ret.fetchall()

#キャッシュを取得する	
def setContent(start,end,amount,weight,price,cost,time,envload,mode):
	cur.execute("insert into cache values (?,?,?,?,?,?,?,?,?)",(start,end,amount,weight,price,cost,time,envload,mode))
	con.commit()

#運賃ランキングの作成	
def getFee(start,end):
	ret = cur.execute("select mode from app where start=? and end=? order by fee asc",(start,end))
	return ret.fetchall()
	
#時間ランキングの作成	
def getTime(start,end):
	ret = cur.execute("select mode from app where start=? and end=? order by time asc",(start,end))
	return ret.fetchall()

#環境負荷ランキングの作成	
def getEload(start,end):
	ret = cur.execute("select mode from app where start=? and end=? order by eload asc",(start,end))
	return ret.fetchall()
		
if __name__=="__main__":
	pass