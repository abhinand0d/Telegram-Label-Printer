import pyodbc
import requests as rq

DBQ = 'D:\BESPOKE TSR\MData.mdb' #DB Location
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DBQ+';')

def item_search(item,rate):
    cursor = conn.cursor()
    cursor.execute(f"SELECT citcode,citname,nigst FROM item WHERE citname LIKE '%{item}%';")
    result = []
    for i in cursor.fetchall():
        cursor.execute(f"SELECT nsalerate,nprrate FROM itembatch WHERE citbatcode='{i[0]}' and nsalerate={rate}")
        for g in cursor.fetchall():
            if int(g[0]) <= int(rate):
                result.append([i[1],i[0],i[2],int(g[0]),int(g[1])])
    return result

def item_load():
    item_code = []
    item_name = []
    item_gst = []
    item_selling_rate = []
    item_purchase_rate = []
    cursor = conn.cursor()
    cursor.execute("SELECT citcode,citname,nigst FROM item;")
    for i in cursor.fetchall():
        item_code.append(i[0])
        item_name.append(i[1])
        item_gst.append(i[2])
        cursor.execute(f"SELECT nsalerate,nprrate FROM itembatch WHERE citbatcode='{i[0]}'")
        for g in cursor.fetchall():
            item_selling_rate.append(int(g[0]))
            item_purchase_rate.append(int(g[1]))

    return {"Item Name":item_name,"Item Code":item_code,"Item GST":item_gst,"Item Purchase Rate":item_purchase_rate,"Item Selling Rate":item_selling_rate}

def expense_load():
    Date=[]
    Amount=[]
    cursor = conn.cursor()
    cursor.execute("SELECT djsdate,njsamt FROM daybook WHERE ndrslno=5015 and ncrslno=1000;")
    for i in cursor.fetchall():
        Date.append(i[0])
        Amount.append(i[1])
    
    return {"Expense":{"Date":Date,"Amount":Amount}}

def home():
    print("Welcome to abhi list")
