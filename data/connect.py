import mongoengine

def global_init(db_name: str):
    mongoengine.connect(db=db_name)