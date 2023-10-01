from models import Dog

def create_table(base,engine):
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).first()

def find_by_id(session, id):
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()