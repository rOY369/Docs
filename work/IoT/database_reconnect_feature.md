
The current solution is the following : 

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

    @reconnect()
    def mqtt_to_database_worker(self, DEVICEID, TOPIC, DATA, TS, STATUS):
        try:
            self.CURSOR.execute(
                "INSERT INTO LOGDATA(deviceid,topic,data,ts,datauploaded) VALUES(%s,%s,%s,%s,%s)",
                [DEVICEID, TOPIC, DATA, TS, STATUS])
            self.CONNECTION_DATABASE.commit()
        except Exception as error:
            print("WRONG QUERY..ROLLING BACK", error)
            self.CONNECTION_DATABASE.rollback()
	@reconnect()
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNTUyMjQyMl19
-->