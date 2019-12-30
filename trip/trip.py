import uuid
from nameko.rpc import rpc
from pymongo import MongoClient

client = MongoClient('mongodb', 27017)
db = client.test_database

trips = db.trips


class TripsService:
    name = "trips_service"

    # redis = Redis('development')

    @rpc
    def get(self, trip_id):
        for item in trips.find({'trip_id': trip_id}):
            trip = item['trip']
        # trip = self.redis.get(trip_id)
        return trip

    @rpc
    def create(self, airport_from_id, airport_to_id):
        trip_id = uuid.uuid4().hex
        trips.insert_one({'trip_id': trip_id,
                          'trip'   : {'from': airport_from_id,
                                      'to'  : airport_to_id}})
        # self.redis.set(trip_id, {
        #     "from": airport_from_id,
        #     "to": airport_to_id
        # })
        return trip_id
