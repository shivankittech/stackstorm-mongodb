import eventlet
from st2reactor.sensor.base import Sensor

import pymongo
from bson.json_util import dumps

class CollectionSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(CollectionSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._mongoclient = None
        self.change_stream = None
        self._trigger = None

    def setup(self):
        # self._mongoclient = pymongo.MongoClient("mongodb+srv://sansi:$anskar@cluster0.z9jhd.mongodb.net/stackstorm?retryWrites=true&w=majority")
        # self.change_stream = self._mongoclient["stackstorm"]["sensorData"].watch()
        pass

    def run(self):
        # for change in self.change_stream:
        #     self.on_mongo_data_event(change)
        pass

    def cleanup(self):
        pass

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        self._trigger = trigger.get("ref", None)

        uri = trigger["parameters"].get("uri", None)
        collection = trigger["parameters"].get("collection", None)
 
        database = uri.split('/')[3].split('?')[0]

        self._mongoclient = pymongo.MongoClient(uri)
        self.change_stream = self._mongoclient[database][collection].watch()
        self.observe_change()
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def observe_change(self):
        for change in self.change_stream:
            self.on_mongo_data_event(change)

    def on_mongo_data_event(self, data):
        self.sensor_service.dispatch(trigger=self._trigger, payload=data)




import eventlet
from st2reactor.sensor.base import Sensor

import pymongo
from bson.json_util import dumps

import threading

def listen_to_events(new_conn_info, logger):
    mongoclient = pymongo.MongoClient(new_conn_info[connectionString])
    change_stream = mongoclient[new_conn_info[database]][new_conn_info[collection]].watch()
    for change in change_stream:
        logger.debug('[CollectionSensor Thread]: Got ' + str(change)))
        # self.on_mongo_data_event(change)

class CollectionSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(CollectionSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._mongoclient = None
        self.change_stream = None
        self._trigger = None

    def setup(self):
        pass

    def run(self):
        for index, thread in enumerate(threads):
            logging.info("Main    : before joining thread %d.", index)
            thread.join()
            logging.info("Main    : thread %d done", index)

    def cleanup(self):
        pass

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        self._trigger = trigger.get("ref", None)
        
        uri = trigger['parameters'].get("uri", None)
        database = uri.split("/")[3].split['?'][0]
        collection = trigger['parameters'].get("collection", None)

        new_conn_info = {}
        new_conn_info[connectionString] = uri
        new_conn_info[collection] = colelction
        new_conn_info[database] = database

        
        x = threading.Thread(target=listen_to_events, args=(new_conn_info, self._logger,))
        threads.append(x)
        x.start()
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def on_mongo_data_event(self, data):
        self.sensor_service.dispatch(trigger=self._trigger, payload=data) 