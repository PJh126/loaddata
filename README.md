# loaddata
load data from local file(.csv) to mysql, make upload big file possible


Sometimes we need to quickly import large amounts of data to local mysql servers (localhost) and cloud servers. If the local csv file is too large, uploading
data in mysql command line or loading data in python program will not be executed and uploading cannot be completed.

For a 560,000 lines csv file, this project can quickly complete the data upload work, here is the program running result

![image](https://github.com/PJh126/loaddata/blob/master/images/finishtime.JPG)

When you want to run, just modify the initialization data at the beginning of the program.

```python
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
```

