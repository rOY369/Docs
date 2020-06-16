
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
	- inserting devices date in the `logdata` table
	- Running qos queries like `get_unuploaded_data_from_database`
- Suppose the local db crashes 
	- In cases where same object is used in both threads, reconnect could take place through the same object from 2 different occurrences at the same time. 
	- The same job with the same outcome could run twice or multiple times in a parallel fashion. This is some extra redundant processing. 
- Also even if the database connection is stable, the same task of whether there is a need to reconnect happens every time a database function is called. This seems like a minute unnecessary processing/ram we could save by exploring other alternatives/design to tackle the problem. 

### Increase in Database functions execution time

- In the current software architecture of applicationcontainer, the execution time of database functions depends on the time it takes for the local database/nas database to execute the respective query. 
- We already know if there is a lag from the database side(local or nas), the applicationcontainer  suffers in data, commands and recipe reliability. 
- If we go with the above approach, we can not afford putting delay and retries as minimum as possible. 
- But considering the current health of applicationcontainer, even if we keep the above settings minimum, it will ad
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYwNzA5NjQzMywxODgyNjM0OTMyXX0=
-->