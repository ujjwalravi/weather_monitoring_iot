"""DB operations for Mongo """
import json

from bson.json_util import dumps
from app.db import db_conf
from pymongo import MongoClient


class MongoHandler():
    """Handles all the MongoDB operations"""

    __ip_addr = db_conf.MONGO_DB["IP_ADDRESS"]
    __port_num = db_conf.MONGO_DB["PORT_NUMBER"]
    __db_name = db_conf.MONGO_DB["DB_NAME"]
    __coll_name = None

    def __enter__(self):
        """Create a connection to Mongo Server. For with invocation"""
        try:
            self.__db_conn = MongoClient(
                self.__ip_addr + ":" + self.__port_num)
        except Exception as e:
            print("Unable to connect to Mongo")
            pass
        else:
            return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Disconnect the connection from DB"""
        self.close_conn()

    def __init__(self, collection_name):
        """Connect to collection inside DB."""
        self.__coll_name = collection_name
        try:
            self.__db_conn = MongoClient(
                self.__ip_addr + ":" + self.__port_num)
            self.__db_obj = self.__db_conn[self.__db_name][self.__coll_name]
        except Exception as e:
            print("ERROR: DB connection Failed.")
            pass

    def close_conn(self):
        """Closes the connection to MongoDB"""
        try:
            self.__db_conn.close()
        except Exception as e:
            print("Unable to close DB connection")
            pass

    def find(self, params=dict(), limit=None, skip=None, sort=[]):
        """Executes find() operation on the DB

        :params dict params: The parameters to find
        """
        try:
            resp = self.__db_obj.find(params)
            if skip:
                resp = resp.skip(skip)
            if limit:
                resp = resp.limit(limit)
            if sort:
                resp = resp.sort(sort)
        except Exception as e:
            print("Unable to perform find operation.")
            return {"status": False, "message": "Unable to execute find()", "Error": str(e.message)}

        else:
            data = json.loads(dumps(resp))
            return {"status": True, "message": "Executed find()", "data": data}

    def find_one(self, params=dict()):
        """Executes find() operation on the DB

        :params dict params: The parameters to find
        """
        try:
            resp = self.__db_obj.find_one(params)
        except Exception as e:
            print("Unable to perform find_one operation")
            return {"status": False, "message": "Unable to execute find_one()", "Error": str(e.message)}
        else:
            if not resp:
                return {"status": False, "data": resp}

            return {"status": True, "data": resp}

    def update(self, find=dict(), update=dict(), upsert=False):
        """Executes update() operation on the DB

        :params dict find: The parameters to match the document.
        :params dict update: What to update in the matched document.
        :params bool upsert: Upsert flag.
        """
        try:
            resp = self.__db_obj.update(find, update, upsert)
        except Exception as e:
            print("Unable to perform update operation.")
            return {"status": False, "message": "Unable to execute update()", "Error": str(e.message)}
        else:
            #data = json.loads(dumps(resp))
            return {"status": True, "message": "Executed update()", "data": data}

    def update_many(self, find=dict(), update=dict(), upsert=False):
        """Executes update_many() operation on the DB

        :params dict find: The parameters to match the document.
        :params dict update: What to update in the matched document.
        :params bool upsert: Upsert flag.
        """
        try:
            resp = self.__db_obj.update_many(find, update, upsert)
        except Exception as e:
            print("Unable to perform update operation")
            return {"status": False, "message": "Unable to execute update()", "Error": str(e.message)}
        else:
            return {"status": True, "message": "Executed update()", "data": resp}

    def insert(self, data=dict()):
        """Executes insert() operation on the DB

        :params dict data: The data to insert into the collection.
        """
        print(data)
        try:
            resp = self.__db_obj.insert_many(json.loads(data))
        except Exception as e:
            print("Unable to perform insert operation"+str(e))
            return {"status": False, "message": "Unable to execute insert()", "Error": str(e)}
        else:
            #data = json.loads(dumps(resp))
            return {"status": True, "message": "Executed insert()", "data": data}

    def insert_one(self, data=dict()):
        """Executes insert() operation on the DB

        :params dict data: The data to insert into the collection.
        """
        try:
            resp = self.__db_obj.insert_one(data)
        except Exception as e:
            print("Unable to perform insert_one operation")
            return {"status": False, "message": "Unable to execute insert_one()", "Error": str(e.message)}
        else:
            #data = json.loads(dumps(resp))
            return {"status": True, "message": "Executed insert_one()", "data": data}

    def delete(self, key=dict()):
        """Executes delete() operation on document in DB
        :params dict key: The unique key of the document to be deleted.
        """
        try:
            resp = self.__db_obj.delete_many(key)
        except Exception as e:
            print("Unable to perform delete operation")
            return {"status": False, "message": "Unable to execute delete() ", "Error": str(e.message)}
        else:
            return {"status": True, "message": "Executed delete()", "data": resp}