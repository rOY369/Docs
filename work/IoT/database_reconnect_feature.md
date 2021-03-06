
## Current solution

```
class reconnect:
    def __init__(self, delay=10, numOfRetries=5):
        self.delay = delay
        self.numOfRetries = numOfRetries

    def __call__(self, function, *args, **kwargs):
        def wrapper(*args, **kwargs):
            numOfRetries = self.numOfRetries
            result = False
            while (numOfRetries > 0):
                try:
                    if args[0].CONNECTION_STATUS:
                        result = function(*args, **kwargs)
                        break
                    else:
                        raise Exception
                except Exception:
                    args[0].connect_db()
                    time.sleep(self.delay)
                    numOfRetries -= 1
            return result
        return wrapper


class DATABASE():

    # xx-----------------INIT FUNCTION----------------------------xx
    # Initailses database class.....accepts database credentials
    # Requires:
    # Databse IP : eg:"localhost"
    # Port Number : 8888
    # User Name : "SomeUser"
    # Database Name: "testdb"
    # Database Password:"abcdef"
    def __init__(self, DATABASE_IP, DATABASE_PORT, DATABASE_USER,
                 DATABASE_NAME, DATABASE_PASSWORD):
        self.DATABASE_IP = DATABASE_IP
        self.DATABASE_PORT = DATABASE_PORT
        self.DATABASE_USER = DATABASE_USER
        self.DATABASE_NAME = DATABASE_NAME
        self.DATABASE_PASSWORD = DATABASE_PASSWORD
        self.GET_DEVICEID_LIST = []
        self.GET_ALL_DEVICEID_LIST_OF_MY_NS1 = []
        self.UNUPLODED_DATA = []
        self.connect_db()

    def connect_db(self):
        try:
            self.CONNECTION_DATABASE = psycopg2.connect(
                host=self.DATABASE_IP,
                database=self.DATABASE_NAME,
                user=self.DATABASE_USER,
                password=self.DATABASE_PASSWORD,
                port=self.DATABASE_PORT)
            self.CURSOR = self.CONNECTION_DATABASE.cursor()
            print("opened database successfully")
            return True
        except Exception as error:
            return False

    @reconnect
    def mqtt_to_database_worker(self, DEVICEID, TOPIC, DATA, TS, STATUS):
        try:
            self.CURSOR.execute(
                "INSERT INTO LOGDATA(deviceid,topic,data,ts,datauploaded) VALUES(%s,%s,%s,%s,%s)",
                [DEVICEID, TOPIC, DATA, TS, STATUS])
            self.CONNECTION_DATABASE.commit()
        except Exception as error:
            print("WRONG QUERY..ROLLING BACK", error)
            self.CONNECTION_DATABASE.rollback()
	
	@reconnect
    def set_command_status_worker(self, status, epochtime):
        try:
            self.CURSOR.execute(
                'UPDATE COMMAND SET "status"=\'{}\' where ("commandArrived"={})'
                .format(status, epochtime))
            self.CONNECTION_DATABASE.commit()
        except Exception as error:
            print("WRONG QUERY..ROLLING BACK", error)
            self.CONNECTION_DATABASE.rollback()

```

## Problems/Edge cases/Concerns if we use the above design  

### Calling of Database functions in different threads

Considering that the software running inside applicationcontainer calls the database object in multiple threads.
Suppose the usage of the database object in the following way - 

```
# dbObject can be global object (remote_obj/local_obj/proxy_obj)
# dbObject can be same or different in both thread target functions.

def thread_target_func_1():
	dbObject.execute(<query>)
	or 
	dbObject.mqtt_to_database_worker(args)

def thread_target_func_2():
	dbObject.execute(<qos_related_query>)
	or 
	dbObject.get_unuploaded_data_from_database(args)
```

- Different queries like - 
	- inserting devices data in the `logdata` table
	- Running qos queries like `get_unuploaded_data_from_database`
- Suppose the local db crashes 
	- In cases where same object is used in both threads, reconnect could take place through the same object from 2 different occurrences at the same time. 
	- The same job with the same outcome could run twice or multiple times in a parallel fashion. This is some extra redundant processing. 
- Also even if the database connection is stable, the same task of whether there is a need to reconnect happens every time a database function is called. 	It would make more sense if the reconnection procedure is a property of the database object and not each database function. 

### Increase in Database functions execution time

- In the current software architecture of applicationcontainer, the execution time of database functions depends on the time it takes for the local database/nas database to execute the respective query. 
- We already know if there is a lag from the database side(local or nas), the applicationcontainer  suffers in data, commands and recipe reliability. 
- If we go with the above approach, we would strictly have to put delay and retries as minimum as possible. 
- But considering the current health of applicationcontainer, even if we keep the above settings minimum, it will add some lag in the return of the database functions especially when database is crashed. Also this approach is not giving us any other advantage so this is not a good trade-off. 

### Unnecessary Reconnect

- If we don't catch specific database errors, the reconnect procedure will be called even if there is any other exception which did not require the reconnect in the first place. 
- For example
	- Some error with the computation/logic of query inside the database function
	- Query syntax error

## Opportunity to improve software quality 

***Considering the above problems and concerns, I see this as an opportunity to reduce some of the coupling in the applicationcontainer software. We have to take a look at how database is being accessed right now and how can we improve the design of database interface  keeping in mind the problems we have faced in the past and the problems we have at hand and those that we can anticipate.***

- Have to bring in Database reconnect functionality 
- The database functions are exactly the same while accessing the nas database/local database. So they should be reusable i.e. it should have a single source. But right now we have 2 different sources. We have to make the same change in 2 places which is a redundant effort and also increases scope of error.
- In case of local database, the database object is not thread safe.
- Local Database is accessed through 3 different db objects that are a part of  `remote_obj`, `proxy_obj` and `local_obj` in applicationcontainer. Is there a way to isolate the channel of accessing the database ?
	- Are there any advantages of using one channel entirely in a software piece like applicationcontainer to access the database ?
	- Will it save some ram/processing ? Will it be a Better architectural design decision ?
- Can be integrated with current application with least amount of effort and change. 
- Increase efficiency 
- Improve overall software design

## Better Alternative

The connection manager which uses a database connections pool to execute queries can be a single channel of database access. 
- Instantiate the connection manager inside applicationMain during init. 
- Hook up the same connection manager object to `remote_obj`, `local_obj` and `proxy_obj` during init using the below interface.
```
class Application():

	def setup_database(connectionManager):
		self.dbConnectionManager = connectionManager
```

Use to access the database in the following manner : 
```
remote_obj.dbConnectionManager.executor(funcName, tableName, *args, **kwargs)
local_obj.dbConnectionManager.executor(funcName, tableName, *args, **kwargs)
```

**Note** : It would be even better even if we can do all database access using only `proxy_obj`. 



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg4NjQyMzQ2OCwtMTU0MTU4MjIwNCw5MD
E3NzI5ODYsLTExMTIzMjQ2NzYsMTg4MjYzNDkzMl19
-->