class BaseRepository:
    def __init__(self, session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get_all(self, entity):
        return self.session.query(entity).all()

    def get_by_id(self, entity, id):
        return self.session.query(entity).filter(entity.id == id).first()

    def update(self):
        self.session.commit()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()
