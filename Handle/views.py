from django.shortcuts import render
from django.db import connection
# Create your views here.

def Extract_context(user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM BBO_ChatHistory WHERE UserID='{user_id}'")
            rows = cursor.fetchall()
            context=[
                {
                    "quest":row[2],
                    "answer":row[3],
                    "time":row[4],
                    "lang":row[5]
                }
                for row in rows
            ]
        return context     
    except Exception as e:
        return e

def sort_dics(array):
    for i in range(len(array)):
        for j in range(i,len(array)-1):
            if array[j]> array[j+1]:
                tmp=array[j]
                array[j]=array[j+1]
                array[j+1]=tmp
    return array