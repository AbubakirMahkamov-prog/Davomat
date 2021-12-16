import mysql.connector,datetime
db_name='davomat'
class DBHelper:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="inshaallah",
        database=db_name)
    def seeTables(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("show tables")
        print('Tables    👇')
        i=1
        for x in mycursor:
            print(i,' - ',x[0].title())
            i+=1
    def addGruops(self,G_name):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"INSERT INTO Groupss (G_name) VALUES ('{G_name}');")
        self.mydb.commit()
        self.mydb.close()
    def seeGroups(self):
        self.mydb._open_connection()
        mycursor=self.mydb.cursor()
        mycursor.execute('select G_name from Groupss')
        print('Groups    👇')
        j=1
        for i in mycursor:
            print(j,' - ',i[0].title())
            j+=1
        self.mydb.close()
    def addStudents(self):
        self.seeGroups()
        self.mydb._open_connection()
        print('\nchoose one of Group and enter its name')
        grp=input('enter name : ')
        mycursor=self.mydb.cursor()
        mycursor.execute(f"select G_id  from Groupss where G_name LIKE'{grp}'")
        for i in mycursor:
            id=i[0]
        amount=int(input('nechta student qo\'shasiz : '))
        for i in range(amount):
            print(i+1,' - student please enter information  👇')
            ism=input('enter firstname  :')
            familya=input('enter lastname  :')
            mycursor.execute(f"insert into students (firstname,lastname,G_id) values ('{ism}','{familya}',{id})")
            self.mydb.commit()
        self.mydb.close()
        print('entered successfully ')
    def seeStudents(self):
        self.seeGroups()
        self.mydb._open_connection()
        print('\nchoose one of Group and enter its name')
        grp=input('enter name : ')
        mycursor=self.mydb.cursor()
        mycursor.execute(f"select G_id  from Groupss where G_name LIKE'{grp}'")
        for i in mycursor:
            id=i[0]
        mycursor.execute(f"select firstname,lastname from students where G_id={id}")
        J=1
        print('\tFirstname   Lastname')
        for i in mycursor: 
            print(J,'  -  ',i[0],'  ',i[1])
            J+=1
        self.mydb.close()
    def getDavomat(self):
        self.seeGroups()
        print('\nchoose one of Group and enter its name')
        grp=input('enter name : ')
        self.mydb._open_connection()
        mycursor=self.mydb.cursor()
        talabalar=[]
        mycursor.execute(f"select G_id  from Groupss where G_name LIKE'{grp}'")
        for i in mycursor:
            G_id=i[0]
        mycursor.execute(f"select *from students where G_id ={G_id}")
        for i in mycursor:
            talaba={'ism':i[1],'fam':i[2]}
            talaba['ism']=talaba['ism'].replace("\'","")
            talaba['fam']=talaba['fam'].replace("\'","")
            talabalar.append(talaba)
        sana=input('sanani kiriting  ex(kun/oy/yil): ')
        sana.replace('/','')
        datetime_obj = datetime.datetime.strptime(sana.replace('/',''), '%d%m%Y')
        for i in range(len(talabalar)):
            by=input(f"Talaba {talabalar[i]['ism']}  {talabalar[i]['fam']}   (+/-)")
            talabalar[i]['byy']=by
        for i in talabalar:
            mycursor.execute(f"insert into Davomatlar (firstname,lastname,G_id,Dates,byy) values ('{i['ism']}','{i['fam']}',{G_id},'{datetime_obj}','{i['byy']}')")
            self.mydb.commit()
        self.mydb.close()
    def seeDavomat(self):
        self.seeGroups()
        print('\nchoose one of Group and enter its name')
        grp=input('enter name : ')
        self.mydb._open_connection()
        mycursor=self.mydb.cursor()
        mycursor.execute(f"select G_id  from Groupss where G_name LIKE'{grp}'")
        for i in mycursor:
            G_id=i[0]
        sana=input('sanani kiriting  ex(kun/oy/yil): ')
        sana.replace('/','')
        datetime_obj = datetime.datetime.strptime(sana.replace('/',''), '%d%m%Y')
        mycursor.execute(f"select firstname,lastname,byy from Davomatlar where G_id={G_id} and Dates LIKE '{datetime_obj}'")
        for  i in mycursor:
            print(i)
    def DeleteGroups(self):
        self.seeGroups()
        print('\nchoose one of Group and enter its name')
        grp=input('enter name : ')
        self.mydb._open_connection()
        mycursor=self.mydb.cursor()
        mycursor.execute(f"select G_id from Groupss where G_name LIKE '{grp}'")
        for i in mycursor:
            id=i[0]
        mycursor.execute(f"delete from students where G_id={id}")
        mycursor.execute(f"delete from Groupss where G_id={id}")
        print('successfully')
dbd=DBHelper()
# dbd.seeGroups()
# dbd.addGruops('655-20')
# dbd.seeStudents()
# dbd.addStudents()
# dbd.seeStudents()
# dbd.getDavomat()
# dbd.seeDavomat()
# dbd.seeDavomat()
# dbd.DeleteGroups()