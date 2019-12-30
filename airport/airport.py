import uuid
from nameko.rpc import rpc
from pymongo import MongoClient

client = MongoClient('mongodb', 27017)
db = client.test_database

airports = db.airports


class AirportsService:
    name = "airports_service"

    # redis = Redis('development')

    @rpc
    def get(self, airport_id):
        for item in airports.find({'airport_id': airport_id}):
            airport = item['airport']
        # airport = self.redis.get(airport_id)
        return airport

    @rpc
    def create(self, airport):
        airport_id = uuid.uuid4().hex
        airports.insert_one({'airport_id': airport_id,
                             'airport'   : airport})
        # self.redis.set(airport_id, airport)
        return airport_id
