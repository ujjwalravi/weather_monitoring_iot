from app.db.mongodb_handler import MongoHandler
from datetime import datetime

db_obj = MongoHandler("test")

def execute():
	data = {
		"name": "name",
		"email": "ravi.ujjwal@boltiot.com",
		"offers": [
			{
				"company": "Adobe Inc",
				"ctc": 15,
				"date": datetime.utcnow()
			}
		]
	}
	db_obj.insert_one(data)
	print("EECUETD")