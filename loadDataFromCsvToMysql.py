import pymysql
import io
import os
import datetime

#the parent directory of you csv file
csvfiledir = ''
#your csv file name(excluding .csv)
csvfilename = ''
#your database name
databasesname = ''
#your table name in your database
databasetablename = ''

#mysql connection configuration 
config = {'host':'localhost',
          'port':3306,
          'user':'root',
          'passwd':'',
          'charset':'utf8mb4',
          'local_infile':1
          }
 
def split_file(filename, table_name, database):
    csv_reader = open(filename, 'r',encoding='utf-8')
    line1 = csv_reader.readline()
    csv_path = csvfiledir + 'source.csv'
    i=j=0
    for row in csv_reader:
        if i%5000==0:
            print(u"Now making the %s th 5000 lines uploading ! " % j)
            csv_file = open(csv_path, 'a+', encoding='utf-8')
            j+=1
    
        if i==0:
            create_table(line1, table_name, database)
        
        csv_file.writelines(row)

        if i%5000==4999:
            load_csv(csv_path, table_name)
            csv_file.close()
            os.remove(csv_path)
        i+=1


def create_table(columns, table_name, database):
    b = columns.split(',')
    colum = ''
    Idin = False
    for a in b:
        if a == 'Id':
            Idin = True
            colum = colum + a + ' INT UNSIGNED AUTO_INCREMENT,'
        else:
            colum = colum + a + ' varchar(255),'
    colum = colum[:-1]
    if Idin == True:
        colum = colum + ', PRIMARY KEY ( Id )'
        
    create_sql = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'

    cur.execute('use %s' % database)
    
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    
#    cur.execute('drop table if exists %s' % table_name)
    cur.execute(create_sql)
    
    


def load_csv(csv_file_path,table_name,database='myweb'):
    
    file = io.open(csv_file_path, 'r', encoding='utf-8')
    
    reader = file.readline()
    print(reader)
    
    data_sql = "LOAD DATA LOCAL INFILE '%s' IGNORE INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES" % (csv_file_path,table_name)

    cur.execute('use %s' % database)
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    
    cur.execute(data_sql)
    conn.commit()
    
    
if __name__ == '__main__':
    start = datetime.datetime.now()
    conn = pymysql.connect(**config)    
    cur = conn.cursor()
    filename = csvfiledir + csvfilename + '.csv'
    
    split_file(filename, csvfilename, databasesname)
    conn.close()
    cur.close()
    end = datetime.datetime.now()
    print("Total program run time" + str(end - start))