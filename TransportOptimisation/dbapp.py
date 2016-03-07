# coding: utf-8
"""
データベースから値を取り出すモジュール
"""
import sqlite3

con = sqlite3.connect("./app.db")
cur = con.cursor()

def getContent(mode,start,end):
	ret = cur.execute("select distance,fee,time,waitingtime,eload,cost from app where mode=? and start=? and end=?",(mode,start,end))
	return ret.fetchall()
	
if __name__=="__main__":
	pass