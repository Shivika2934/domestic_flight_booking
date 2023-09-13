import pymysql as pm;
conn=pm.connect(host='Localhost',user='root',passwd='Qwerty.123') #connection object
#c.execute("create database cs_project;")
c=conn.cursor()
c.execute("use cs_project ;")
conn.select_db("cs_project") 

def create_table():
    c.execute("create table account(Full_Name varchar(25),Age int,Phone_Number bigint,Email_Id varchar(35),Password varchar(20),Gender char(2)) ;")
    c.execute("desc account ;")
    print(c.fetchall())
    c.execute("create table booking(Full_Name varchar(25),Number_of_Passengers int,Time_of_travel varchar(6),Date_of_Departure date,Date_of_Arrival date,City varchar(20),Plane_code char(2),Business_or_Personal_Trip varchar(10),Single_or_Return_Way_Trip varchar(8),Mode_of_Payment varchar(15),Total_cost_of_booking int) ;")
    c.execute("desc booking;")
    print(c.fetchall())

def welcome_screen():
    print('                                                                                                         ')
    print('                              |||||||    |||||||    |||||||    |||||||    ||   ||                        ')
    print('                              ||         ||         ||         ||          || ||                         ')
    print('                              |||||||    |||||||    |||||||    |||||||      ||                           ')
    print('                              ||              ||         ||    ||          || ||                         ')
    print('                              |||||||    |||||||    |||||||    |||||||    ||   ||                        ')
    print('                                                                                                         ')
    print('                                           Essex Tours and Travels                                       ')
    print('                                           -----------------------                                       ')
    print('                             Welcome to our site ! Hope you have a great time ahead :)                   ')
    print('                                                                                                         ')
welcome_screen()

def login():
    email=input("Enter E-mail Address - ")
    passwd=input("Enter Password - ")
    c.execute("select * from account")
    r=c.fetchall()
    acc=[]
    log=[]
    for i in r:
        acc.append([i[3],i[4]])
    for j in acc:
        if email==j[0]:
            log.append(j)
        elif passwd==j[1]:
            log.append(j)
    if [email,passwd] in log:
        print("Account exists")
        print("***** Logged In Succesfully! *****")
        print(" ")
    else:
        print("Account doesn't exist. Create Account first")
        print(" ")
        account()

def account():
    name=input("Enter Full Name - ")
    age=input("Enter Age - ")
    phone=input("Enter Phone Number - ")
    email=input("Enter E-mail Address - ")
    if '@' not in email:
        print("Invalid Email")
        email=input("Re-enter E-mail Address")
    passwd=password()
    gender=input("Enter M for Male /F for female /N for not specified - ")
    query1="insert into account values(%s,%s,%s,%s,%s,%s);"
    values1=(name,age,phone,email,passwd,gender)
    c.execute(query1,values1)
    conn.commit()
    print("***** Account Created Succesfully! *****")
    print(" ")    

def password():
    while True:
        passwd=input("Enter Password - ")
        upper=0
        lower=0
        digit=0
        for i in passwd:
            if i.isupper()==True:
                upper+=1
            elif i.islower()==True:
                lower+=1
            elif i.isdigit()==True:
                digit+=1
        if len(passwd)>6 and upper>0 and lower>0 and digit>0:
            print("Valid Password")
            return passwd
            break
        else:
            print("Invalid Password") 
            print("Length of Password should be greater than 6 and should contain atleast 1 uppercase letter, 1 lowercase letter and 1 digit.")
            
def ticket(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10):
        print("Here Is Your Final Ticket:")
        print("------------------------------------------------------------------------")
        print("  Name: ",t1,"                                                           ")
        print("  Airplane: ",t2,"                                                     ")
        print("  To: ",t3,"                                                            ")
        print("  Date: ",t4,"                                                           ")
        print("  No Of Boarding pass: ",t5,"                                           ")
        print("  For Return / Single: ",t6,"                                            ") 
        print("  Mode of Payment: ",t7,"                                            ")
        print("  Final Cost: ",t8,"                                                    ")
        print("  Your Seats For Trip To ",t9,"Via Airplane ",t10," Is Booked.","      ")
        print("------------------------------------------------------------------------    ")
        print("                                                                           ")
        print("  ***** Thank you for booking with Essex Tour & Travels *****","             ")
        print("  ***** Have a safe and Relaxing Journey *****","                            ")
        print(" ")

name=dod=SR=""
psng=0

def booking():
    global name
    global dod
    global psng
    global SR
    print("Enter the Following Details for Ticket Booking:-")
    name=input("Enter Full Name - ")
    psng=int(input("Enter Number of Passengers - "))
    time=input("Enter Time of Travel (HH:MM:SS) - ")
    dod=input("Enter Date of Departure (YYYYMMDD) - ")
    doa=input("Enter Date of Arrival (YYYYMMDD) - ")
    BP=input("Enter Reason of Travel(Business/Personal) - ")     
    SR=input("Enter (Single /Return) Way - ")
    query2="insert into booking(Full_Name,Number_of_Passengers,Time_of_travel,Date_of_Departure,Date_of_Arrival,Business_or_Personal_Trip,Single_or_Return_Way_Trip) values(%s,%s,%s,%s,%s,%s,%s);"
    values2=(name,psng,time,dod,doa,BP,SR)
    c.execute(query2,values2)
    conn.commit()
    print("***** Details Entered Succesfully! *****")
    print(" ") 
    
    c_code=""
    cc={"a1":"Delhi","b2":"Mumbai","c3":"Ahmedabad","d4":"Chandigarh","e5":"Srinagar","f6":"Jaipur","g7":"Lucknow","h8":"Amritsar","i9":"Guwahati","j10":"Kolkata","k11":"Ranchi","l12":"Bhopal","m13":"Goa","n14":"Bengaluru","o15":"Chennai","p16":"Kochi"}
    c_cost={"a1":2000,"b2":2250,"c3":2500,"d4":2750,"e5":3000,"f6":3250,"g7":3500,"h8":3750,"i9":4000,"j10":4250,"k11":4500,"l12":4750,"m13":5000,"n14":5250,"o15":5500,"p16":5750}
    city=""
    
    print(" ")
    print("List of Cities with Respective Codes :-")
    print(cc)
    print(" ")
    c_code=input("Enter Code for Desired City - ")
    city=cc[c_code]
    print("Desired city: ",city)
    print(" ")
    print("loading....")
    print(" ")

    a_code=""
    plane={"x1":12,"x2":14,"x3":16,"x4":18,"x5":20,"x6":22,"x7":24,"x8":26,"x9":28,"x10":30}
    
    print("List of Airplanes with Respective Cost(per Km) :-")
    print(plane)
    print(" ")
    a_code=input("Enter Airplane Code - ")
    print("Desired Airplane: ",a_code,"with per Km rate: ",plane[a_code])
    print(" ")

    cost=psng*(int(c_cost[c_code])+int(plane[a_code]))
    if SR.lower()=="return":
        cost=cost*2
    elif SR.lower()=="single":
        cost=cost*1
    print("Total Cost: ",cost)
            
    payment=input("Enter C for cash payment / BT for bank account tranfer - ")
    if payment.upper()=="BT":
        print("Here are the bank details of Essex Tours and Travels:")
        print("Company name - Essex Tours and Travels")
        print("Account number - 123456789001")
        print("IFSC Code- SBI0001234")
        print("Kindly tranfer the necessary amount within 24 hours to confrim your booking")
    print(" ")
            
    query3="update booking set City=%s,Plane_code=%s,Mode_of_Payment=%s,Total_cost_of_booking=%s where full_name=%s;"
    values3=(city,a_code,payment,cost,name)
    c.execute(query3,values3)
    conn.commit()
    ticket(name,a_code,city,dod,psng,SR,payment,cost,city,a_code)
    end=input("Enter END To Exit or CONTINUE ")
    print(" ")
    if end.lower()=="continue":
        menu2()

def update_mem():
    name1=input("Enter Name for Which you Wish to Update Record - ")
    print("Enter 1 to Update Full Name/ 2 to Update Age/ 3 to Update Phone Number/ 4 to Update Email ID/ 5 to Update Password/ 4 to Update Gender")
    num_update=int(input("Enter Choice - "))
    choice1={1:"Full_Name",2:"Age",3:"Phone_Number",4:"Email_Id",5:"Password",6:"Gender"}
    clause1=input("Enter "+choice1[num_update]+" - ")
    query6="update account set "+choice1[num_update]+" ='"+clause1+"' where Full_name= "+"'"+name1+" ';"
    c.execute(query6)
    conn.commit()
    print(" ***** Record Updated Succesfully *****")
    end=input("Enter END To Exit or CONTINUE ")
    print(" ")
    if end.lower()=="continue":
        menu2()
    
def delete():
    name_del=input("Enter Name to Delete Record - ")
    query4="delete from account where Full_Name= '"+name_del+"' ;"
    c.execute(query4)
    conn.commit() 
    print(" ***** Record Deleted Succesfully *****")
    end=input("Enter END To Exit or CONTINUE ")
    print(" ")
    if end.lower()=="continue":
        menu2()

def search():
    print("Enter 1 to Search on Full Name/ 2 to Search on Phone Number/ 3 to Search on Email ID/ 4 to Search on Gender")
    num=int(input("Enter Choice - "))
    choice={1:"Full_Name" , 2:"Phone_Number" , 3:"Email_Id" , 4:"Gender"}
    clause=input("Enter "+choice[num]+" - ")
    query5="select * from account where "+choice[num]+" = '"+clause+"' ;"
    c.execute(query5)
    r1=c.fetchall()
    print("Selected Records are :-")
    for j in r1:
        print(j)
    end=input("Enter END To Exit or CONTINUE ")
    print(" ")
    if end.lower()=="continue":
        menu2()
    
def stats():
    print("Statistics Menu :-")
    print("Enter 1 to view Member List")
    print("Enter 2 to view City/Airplane List")
    print("Enter 3 to view Members visiting Certain city")
    print("Enter 4 to view Total Cost of Booking done this year/month")
    print("Enter 5 to view Total Tickets Booked")
    s=int(input('Enter Choice - '))
    if s==1:
        c.execute("select Full_Name from account;")
        result=c.fetchall()
        print("Member List :-")
        for i in result:
            print(i)
            
    elif s==2:
        ch=int(input("Enter 1 for City List / Enter 2 for Airplane List"))
        if ch==1:
            lst1=["Delhi","Mumbai","Ahmedabad","Chandigarh","Srinagar","Jaipur","Lucknow","Amritsar","Guwahati","Kolkata","Ranchi","Bhopal","Goa","Bengaluru","Chennai","Kochi"]
            print("List of Cities :-")      
            for i in lst1:
                print(i)
        elif ch==2:
            lst2=["x1","x2","x3","x4","x5","x6","x7","x8","x9","x10"]
            print("List of Airplanes :-")
            for j in lst2:
                print(j)    
                
    elif s==3:
        c.execute("select * from booking;")
        r=c.fetchall()
        mem_city={}
        for i in r:
            name=str(i[0])
            city=str(i[5])
            if city not in mem_city:
                mem_city[city]=[name]
            else:
                mem_city[city].append(name)
        for j in mem_city.items():
            print(j)
            
    elif s==4:
        c.execute("select sum(Total_cost_of_booking) from booking;")
        tot=str(c.fetchall()).replace("((Decimal('","").replace("'),),)","")
        print("Total Cost of Booking :- ",tot)
        
    elif s==5:
        c.execute("select sum(Number_of_Passengers) from booking;")
        pas=str(c.fetchall()).replace("((Decimal('","").replace("'),),)","")
        print("Total Number of tickets booked :- ",pas)
    end=input("Enter END To Exit or CONTINUE ")
    print(" ")
    if end.lower()=="continue":
        menu2()

def menu1():
    print("Enter 1 for Log in")
    print("Enter 2 to Create Account")
    start1=int(input("Enter your Desired Choice - "))
    print(" ")
    if start1==1:
        login()
    elif start1==2:
        account()
menu1()    

def menu2():
    print("Enter 1 for New Booking")
    print("Enter 2 to Update Member Details")
    print("Enter 3 to Delete Member")
    print("Enter 4 to Search for Member (On Name, Phone, Email Id, Gender)")
    print("Enter 5 for Statistics")
    start2=int(input("Enter your Desired Choice - "))
    print(" ")
    if start2==1:
        booking()
    elif start2==2:
        update_mem()
    elif start2==3:
        delete()
    elif start2==4:
        search()
    elif start2==5:
        stats()
menu2()   