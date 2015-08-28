from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Boolean,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'PiUrl'
    uuid = Column(Text, primary_key=True)
    url = Column(Text)
    landscape = Column(Boolean)
    description = Column(Text)
