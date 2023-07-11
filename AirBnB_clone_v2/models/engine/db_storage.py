from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.state import Base, State
from os import getenv
from models.city import City


class DBStorage:
    """Class created for sql storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Instance of the class DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        url = "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database)
        self.__engine = create_engine(url, pool_pre_ping=True)
        #self.__engine.connect()

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Session creation"""
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        my_dict = {}
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if cls is None:
            for attributes in classes:
                get = self.__session.query(attributes).all()
                for i in get:
                    key = i.__class__.__name__ + '.' + i.id
                    my_dict[key] = i
            return my_dict
        else:
            get = self.__session.query(cls).all()
            for i in get:
                key = i.__class__.__name__ + '.' + i.id
                my_dict[key] = i
            return my_dict

    def new(self, obj):
        """add object passed to database"""
        self.__session.add(obj)

    def save(self):
        """Save the object to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object passed"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Sessions = sessionmaker(bind=self.__engine)
        session = scoped_session(Sessions, expire_on_commit=False)
        self.__session = session()
