install.packages("RMySQL")
library(RMySQL)

mydb = dbConnect(MySQL(), user='root', password='', dbname='student', host='localhost')
mydb
dbListTables(mydb)
dbListFields(mydb, 'ddl_student')
rs = dbSendQuery(mydb, "select * from ddl_student")
rs
data = fetch(rs, n=-1)
data