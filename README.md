# loaddata
load data from local file(.csv) to mysql, making load big file possible（LOAD DATA INFILE 导入数据， 解决大文件load data不执行问题）


快速向本地mysql服务器（localhost）和云端服务器导入大量数据。如果本地csv文件太大，直接用mysql中的load data或自己用python写的load data会不执行，无法完成上传。

当你要运行时，只需修改程序开始部分的初始化数据即可


对于一个56万行本项目能快速完成数据上传工作，程序运行情况

![image](https://github.com/PJh126/loaddata/blob/master/images/finishtime.JPG)

当你要运行时，只需修改程序开始部分的初始化数据即可

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

