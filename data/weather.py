import datetime
import mongoengine

class Weather(mongoengine.Document):
    temperature = mongoengine.IntField(min_value=-90)
    precipitation = mongoengine.IntField()
    humidity = mongoengine.IntField()
    wind = mongoengine.IntField()
    time = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db-alias': 'core',
        'collection': 'weather',
        'indexes': [
            'temperature',
            'precipitation',
            'humidity',
            'wind',
            'time',
        ]
    }

    @classmethod
    def countReport(cls):
        return Weather.objects().count()

    
