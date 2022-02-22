import os
import sqlite3
from sqlite3 import Error


#Getting the dir of the database
dirname = os.path.dirname(__file__)
def getParent(path, levels=1):
    common = path
    for i in range(levels+1):
        common = os.path.dirname(common)
        
    return os.path.abspath(common)

basepath = getParent(dirname)
database = f'{basepath}\database'

entries= os.listdir(database)
# print(database)


for entry in entries:
    if entry == 'recipiaData.db':
        db_path = f'{database}\{entry}'
        # print(db_path)
    else:
        db_path2 = f'{database}\{entry}'


name = []
image = []
duration = []

town_name = []   
town_image = []  
s_names = []

lan_list = []
town_list = []
cert_list= []
specialty_list = []

loop_list = []

req_list = []   #specialty_list
ar_recipe = []
steps_list = []

spec_list = []

school_name = [] 
school_image = []
school_fees = []
school_info = []
school_link = []

school_name1 = [] 
school_image1 = []
school_fees1 = []
school_info1 = []


town_school_name = []
town_school_image = []
town_school_fees = []



def open_db():
    global conn, cur
    #Create a connection with the database

    try:
        #Creates a connection
        conn = sqlite3.connect(db_path)
        # print("Connection successs")

    except Error as e:
        # print(e)
        pass
        
    #setup a cursor to manipulate the database

    cur = conn.cursor()
    
#Testing the school DB
def open_db2():
    global conn, cur
    #Create a connection with the database

    try:
        #Creates a connection
        conn = sqlite3.connect(db_path2)
        # print("Connection successs")

    except Error as e:
        # print(e)
        pass
        
    #setup a cursor to manipulate the database

    cur = conn.cursor()


def search_labelTextAR(ar_name_in_db):
    open_db()

    for row1, row2, row3, row4, row5, row6 in cur.execute(f'SELECT name,steps,image,duration,requirements,Cat_name FROM Recipes WHERE name ="{ar_name_in_db}";'):

        #Split the each obj in the tuple to a single obj on its own
        ar_recipe.clear()
        ar_recipe.append(row1)
        ar_recipe.append(row3)
        ar_recipe.append(row4)
        ar_recipe.append(row6)

        step= str(row2).split(":")
        req = str(row5).split(",")
        steps_list.clear()
        req_list.clear()
        for i in range(len(step)):
            steps_list.append(step[i])
        for i in range(len(req)):
            req_list.append(req[i])
        
    conn.close()

#Gets the recipe name,imge, and duration for a specific category

def search_labelTextCAT(town_in_db):
    open_db2()
    for row1, row2, row3 in cur.execute(f'SELECT name,image,fees FROM SchoolData WHERE location ="{town_in_db}";'):
        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        town_school_name.append(row1)
        town_school_image.append(row2)
        town_school_fees.append(row3)

    conn.close()

#Gets the recipe name,imge, and duration of all recipes
def search_school():
    open_db2()
    for row1, row2, row3 in cur.execute(f'SELECT name,image,fees FROM SchoolData;'):
        
        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        if row1 in school_name:
            school_name.remove(row1)
            school_name.append(row1)
        else:
            school_name.append(row1)

        if row2 in school_image:
            school_image.remove(row2)
            school_image.append(row2)
        else:
            school_image.append(row2)

            school_fees.append(row3)
            

        
            
#Function to get the school info for a particulater school
def search_school_v2(name):
    school_info.clear()
    for row4, row5, row6 in cur.execute(f'SELECT info, website, specialty FROM SchoolData WHERE name = "{name}";'):
        spec = str(row6).split(",")
        spec_list.clear()
        for i in range(len(spec)):
            spec_list.append(spec[i])
        return row4, row5

    conn.close()
    
def query_user_criteria(req_1, req_2, req_3, req_4, req_5):
    open_db2()
    lan_list.clear()
    town_list.clear()
    cert_list.clear()
    specialty_list.clear()
    for row1, row2, row3, row4, row5 in cur.execute(f'SELECT specialty,certificate,location,language, fees < "{req_5}" FROM SchoolData;'):
        #Split the each obj in the tuple to a single obj on its own
        # print(type(row3))
        spe= row1.split(",")
        for s in  spe:
            if s in specialty_list:
                specialty_list.remove(s)
                specialty_list.append(s)
            else:
                specialty_list.append(s)

        cer= row2.split(",")
        for c in  cer:
            if c in cert_list:
                cert_list.remove(c)
                cert_list.append(c)
            else:
                cert_list.append(c)

        town_list.append(row3)
        lan_list.append(row4)
    # print(specialty_list)
    # print(cert_list)
    # print(town_list)
    # print(lan_list)
        
    if req_1 in specialty_list:
        new_req_1 = req_1
    else:
        new_req_1 = '' 
    if req_2 in cert_list:
        new_req_2 = req_2
    else:
        new_req_2 = ''
    if req_3 in town_list:
        new_req_3 = req_3
    else:
        new_req_3 = ''
    if req_4 in lan_list:
        new_req_4 = req_4
    else:
        new_req_4 = ''
    
    # print(new_req_1)
    # print(new_req_2)
    # print(new_req_3)
    # print(new_req_4)
    # print(type(cert_list))
    # print(type(cert_list[0]))

        
    #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
    for row in cur.execute(f"SELECT name FROM SchoolData WHERE location= '{new_req_3}' AND (language= '{new_req_4}' OR language= 'bilingual');"): 
    
        # print(f"appended {row}")
        s_names.append(row)
    # print(s_names)
    
    #This part was omitted for obvious reasons
    #  specialty= '{new_req_1}' AND certificate= '{new_req_2}' AND 
        

    conn.close()
    
    
def search_school_with_condition(s_name):
    open_db2()

    for row1, row2, row3, row4 in cur.execute(f'SELECT name,image,fees, info FROM SchoolData WHERE name= "{s_name}";'):
        
        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        if row1 in school_name1:
            school_name1.remove(row1)
            school_name1.append(row1)
        else:
            school_name1.append(row1)

        if row2 in school_image1:
            school_image1.remove(row2)
            school_image1.append(row2)
        else:
            school_image1.append(row2)

        if row3 in school_fees1:
            school_fees1.remove(row3)
            school_fees1.append(row3)
        else:
            school_fees1.append(row3)
        if row4 in school_info1:
            school_info1.remove(row4)
            school_info1.append(row4)
        else:
            school_info1.append(row4)
        # print(school_name1)
        # print(school_image1)
        # print(school_fees1)
        # print(new_req_4)
    # print(school_name1)
            

    conn.close()

def search_town():  #search_town()
    open_db2()
    for row1, row2 in cur.execute(f'SELECT name, image FROM Town;'):   
        row1 = ''.join(row1)
        row2 = ''.join(row2)
        if row1 in town_name:
            town_name.remove(row1)   
            town_name.append(row1)   
        else:
            town_name.append(row1)   

        if row2 in town_image:
            town_image.remove(row2) 
            town_image.append(row2)  
        else:
            town_image.append(row2)  

    conn.close()


#Function to handle the user search options 
def user_searches(search_var):
    open_db2()
    
    for row in cur.execute(f'SELECT name FROM SchoolData;'):  
        row = ''.join(row)
        if str(search_var).lower() == row.lower():
            first_user_retrieve(search_var)
            # print("Found")
            # print(school_name)

            return True
        else:
            word_split = row.lower().split()
            if str(search_var).lower() in word_split:
                second_user_retrieve(search_var)
                print("Found2")
                return True

    conn.close()
    # print("NOt FOund")
    return False


def first_user_retrieve(db_name):
    open_db2()
    school_name.clear()
    school_image.clear()
    school_fees.clear()
    for row1, row2, row3 in cur.execute(f'SELECT name,image,fees FROM SchoolData WHERE name ="{db_name}";'):

        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        if row1 in school_name:
            school_name.remove(row1)
            school_name.append(row1)
        else:
            school_name.append(row1)

        if row2 in school_image:
            school_image.remove(row2)
            school_image.append(row2)
        else:
            school_image.append(row2)

        if row3 in school_fees:
            school_fees.remove(row3)
            school_fees.append(row3)
        else:
            school_fees.append(row3)

    conn.close()


def second_user_retrieve(db_name):
    open_db2()
    for row1, row2, row3 in cur.execute(f"SELECT name,image,fees FROM SchoolData WHERE name LIKE '%{db_name}%';"):

        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        if row1 in school_name:
            school_name.remove(row1)
            school_name.append(row1)
        else:
            school_name.append(row1)

        if row2 in school_image:
            school_image.remove(row2)
            school_image.append(row2)
        else:
            school_image.append(row2)

        if row3 in school_fees:
            school_fees.remove(row3)
            school_fees.append(row3)
        else:
            school_fees.append(row3)


    conn.close()


# search_school()
# query_user_criteria("Netorking","HND", "Douala","French")
# for s_name in s_names:
#     search_school_with_condition(s_name[0])

# user_searches("University Institute Of Technology")