import pymongo
def MongoConnect(mongolist):
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Database1"]
        mycol = mydb['InternInfo']
        list=[]
        list.append(mongolist)
        result=mycol.insert_many(list)


        return True
    except Exception as e:
        print(e)
        print("Check your Internet Connection !!")
        return False
def MongoData() :
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Database1"]
    mycol = mydb['InternInfo']

    Newlist=[]
    for i in mycol.find() :
        list = []
        for key, value in i.items():
            list.append(str(value))
        Newlist.append(list)
    return Newlist

