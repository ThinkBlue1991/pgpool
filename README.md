# pgpool

## Install
```
pip3 install pypostgrestool==0.1
```

## Usage
```
from pg_client import PostgresDB
db = PostgresDB(host="127.0.0.1", port=5432, user='postgres',
                     password='123456', db_name=my-db', min_conn=10,
                     max_conn=100)
# search 
sql = "select * from my-tab"
print(db1.query_all(sql=sql))
```
## Singleton
```
db1 = PostgresDB(host="127.0.0.1", port=5432, user='postgres',
                     password='123456', db_name=my-db', min_conn=10,
                     max_conn=100)
db2 = PostgresDB(host="127.0.0.1", port=5432, user='postgres',
                     password='123456', db_name=my-db', min_conn=10,
                     max_conn=100)
print(db1)
print(db2)
print(db1.pool)
print(db2.pool)
```
