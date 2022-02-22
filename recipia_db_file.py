import sqlite3
from sqlite3 import Error
import os

dirname = os.path.dirname(__file__)
dbpath = os.path.join(dirname, "database")
imge_path = os.path.join(dirname,"images")
print(dbpath)

#this func creates a connection with our database
def create_connection(db_file):
    conn = None
    try:
        #Creates a connection 
        conn = sqlite3.connect(db_file)
        print("Connection successs")
    
    except Error as e:
        print(e)
    
    return conn

    # finally:
    #     if conn:
    #         #clse the connection
    #         conn.close()

#Func to create ouur tables
def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
        print("table created")
    except Error as e:
        print(e)


#FUnc to insert data into Categpry table
def create_Town(conn, town):
    sql = '''
            INSERT INTO Town(name, image)
            VALUES(?, ?)
            '''
    cur = conn.cursor()
    cur.execute(sql, town)
    conn.commit()
    #return cur.lastrowid    #To get the generated id


#Funct to insrt data into the recipe table
def create_SchoolData(conn, schooldata):
    sql = '''
            INSERT INTO SchoolData(name, fees, image, language, certificate, specialty, website, info, w_rating, i_rating, searches, location)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''

    cur = conn.cursor()
    cur.execute(sql, schooldata)
    conn.commit()
    # return cur.lastrowid

#The main func that performs all the task tgether
def main():

    database = f"{dbpath}/GReccommendData.db"

    #Write down syntax for the creation of our table
    sql_create_Town_table = """ CREATE TABLE IF NOT EXISTS Town (
                                    id integer PRIMARY KEY,
                                    name text UNIQUE NOT NULL,
                                    image text
                                ); """

    sql_create_SchoolData_table = """ CREATE TABLE IF NOT EXISTS SchoolData (
                                    id integer PRIMARY KEY,
                                    name text UNIQUE NOT NULL,
                                    logo text,
                                    fees text,
                                    image text,
                                    language text,
                                    certificate text,
                                    specialty text,
                                    website text,
                                    info text,
                                    w_rating integer,
                                    i_rating integer,
                                    searches integer,
                                    location text,
                                    FOREIGN KEY(location) REFERENCES Town(name)
                                ); """


    #connect to our database
    conn = create_connection(database)

    #create the table
    if conn is not None:
        #create the category table
        create_table(conn, sql_create_Town_table)
        
        #create the recipes table
        create_table(conn, sql_create_SchoolData_table)


    else:
        print(" Error connecting to the database")



    with conn:
        
    #Create Category var and store in the Category table
        town_1 = ('Yaounde', f'{imge_path}/Category Images/yde.jpg')
        town_2 = ('Douala', f'{imge_path}/Category Images/dla.jpg')
        town_3 = ('Buea', f'{imge_path}/Category Images/buea.jpg')
        town_4 = ('Bamenda', f'{imge_path}/Category Images/bda.jpg')
        town_5 = ('Dschang', f'{imge_path}/Category Images/dsc.jpg')
        town_6 = ('Bertoua', f'{imge_path}/Category Images/bert.jpg')
        town_7 = ('Maroua', f'{imge_path}/Category Images/mar.jpg')
        town_8 = ('Garoua', f'{imge_path}/Category Images/gar.jpg')
        town_9 = ('Adamawa', f'{imge_path}/Category Images/ada.jpg')
        town_10 = ('Ngaoundere', f'{imge_path}/Category Images/ngo.jpg')

        #Now add the Towns to the database
        create_Town(conn, town_1)
        create_Town(conn, town_2)
        create_Town(conn, town_3)
        create_Town(conn, town_4)
        create_Town(conn, town_5)
        create_Town(conn, town_6)
        create_Town(conn, town_7)
        create_Town(conn, town_8)
        create_Town(conn, town_9)
        create_Town(conn, town_10)

        #Now for school Data

        
        #First lets start with yaounde
        sc_1 = ('University of Yaounde', '250,000 XFA', f'{imge_path}/University of Yaounde img.jpg','bilingual', 'Bachelors,Masters,PHD','Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business', 'www.uy1.uninet.cm','The University of Yaoundé 1 is a public university offering degree programs in both French and English. The university was formed in 1993 when a decision was made to split Cameroon’s oldest university into two separate institutions: University of Yaoundé 1 and University of Yaoundé 2.', 3447, 12540, 9000, 'Yaounde')
        
        sc_2 = ('Higher Institute Public Finance Of Cameroun', '750,000 XFA', f'{imge_path}/Higher Institute Public Finance Of Cameroun img.jpg', 'French', 'Masters', 'Finance & Banking,Business,Management,Accounting', 'www.pfinancespubliques.org', 'We are an Institute in Yaounde Specialised in the training of Students in the field of business and finance', 10678, 9349, 2500, 'Yaounde')
        
        sc_3 = ('Catholic University of Central Africa', '700,000 XFA', f'{imge_path}/Catholic University of Central Africa img.jpg', 'bilingual', 'Bachelors,Masters,PHD', 'Nursing,Philosophy,Computer Science,Medicine,Law,Telecom,Networking', 'www.ucac-icy.net', 'CUAC was founded in 1989 by the Association of the Episcopal Conference of the Central African Region. It opened in 1991 with 111 students. The university has three campuses around Yaoundé, two in the center of town with the main campus outside of the city', 9681, 11423, 3500, 'Yaounde')
        
        #Now Dla
        
        sc_4 = ('UNIVERSITY INSTITUTE GULF OF GUINEA', '450,000 XFA', f'{imge_path}/iug img.jpg', 'bilingual', 'HND,Bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA', 'www.univ-iug.com', 'IUG is a group of three higher education institutions based in the same campus in Bassa-Douala. Specialized in fields as varied as Commerce and Management, Communication and Information, Industry and New Technologies, and Paramedic Training', 3883, 15879, 11800, 'Douala')
        
        sc_5 = ('University Institute Of Technology', '400,000 XFA', f'{imge_path}/iut img.jpg', 'bilingual', 'HND,Bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business, Nursing,ICA', 'www.iut-dla.cm', 'IUT is a State Institute that trains students in a variety of fields like techhnology, commerce and medicine',3783, 15579, 12000, 'Douala')
        
        sc_6 = ('university of douala', '350, 000 XFA', f'{imge_path}/university of douala img.jpg', 'French', 'HND,Bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA', 'www.univ-douala.cm', 'We are a state University located in Douala. we provide training in economics and commerce, technical training, industrial engineering, medicine and pharmaceutics, arts, fisheries science, humanities, law and politics, sciences, economic sciences and management', 5415 ,21608, 12900, 'Douala')
        
        #Now Buea
        
        sc_7 = ('University Of Buea', '50, 000 XFA', f'{imge_path}/ub img.jpg', 'English', 'bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA,MEdicine,Health Science', 'www.ubuea.cm', 'We are one of the state Universities located in buea and we are divided into various faculties', 4525,25321,1425, 'Buea')
        
        sc_8 = ('HIBMAT', '150, 000 XFA',f'{imge_path}/hibmat img.jpg', "English", 'HND,Bachelors', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA','www.hibmat.com', 'We are a proffesional university located in buea that ensures efficient training of students', 345,3563,245, 'Buea')
        
        sc_9 = ('Higher Institute of Management Studies', '250, 000 XFA',f'{imge_path}/hims img.jpg', 'English', 'Bachelors', 'Finance & Banking,Business,Management,Accounting', 'www.himsbuea.org', 'We are a proffesional university located in buea that ensures efficient training of students to obtain the Bachelors Certificate', 345, 3521, 1452, 'Buea')
        
        #bda
        
        sc_10 = ('University Of Bamenda', '50, 000 XFA', f'{imge_path}/uba img.jpg', "English", 'Bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA,MEdicine,Health Science','www.uniba.cm', 'We are one of the state Universities located in bamenda and we are divided into various faculties', 63723, 1278, 16378, 'Bamenda')
        
        sc_11 = ('International Uniersity Of Bamenda', '350, 000 XFA',  f'{imge_path}/iub img.jpg', "English", 'HND,Bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA','www.iubamenda.org', 'We are a proffesional university located in bamenda that ensures efficient training of students', 345,3563,245, 'Bamenda')
        
        sc_12 = ('Bamenda University Of science and Tech', '400, 000 XFA', f'{imge_path}/bust img.jpg', "English", 'HND,Bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA','www.bamendauniversity.com', 'We are one of the pioneer proffesional universities located in bamenda that ensures efficient training of students', 63723, 1278, 16378, 'Bamenda')
        
        #Dchang
        sc_13 = ('University Of Dschang', '100, 000 XFA', f'{imge_path}/udschang img.jpg', "French", 'HND,Bachelors,Masters,PHD', 'Accounting,Management,Software Engineering,Telecom,Netorking,Finance & Banking,Business,Nursing,ICA', 'www.univ-dschang.org','We are one of the state Universities located in Dschang in the West Region and we are divided into various faculties', 63723, 1278, 16378, 'Dschang')
        
        create_SchoolData(conn, sc_1)
        create_SchoolData(conn, sc_2)
        create_SchoolData(conn, sc_3)
        create_SchoolData(conn, sc_4)
        create_SchoolData(conn, sc_5)
        create_SchoolData(conn, sc_6)
        create_SchoolData(conn, sc_7)
        create_SchoolData(conn, sc_8)
        create_SchoolData(conn, sc_9)
        create_SchoolData(conn, sc_10)
        create_SchoolData(conn, sc_11)
        create_SchoolData(conn, sc_12)
        create_SchoolData(conn, sc_13)
            




#Call the main() funct
if __name__ == '__main__':
    main()