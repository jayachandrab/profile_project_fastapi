from typing import Any, AnyStr
from sqlalchemy.ext.declarative import as_declarative,declared_attr

@as_declarative()
class Base:
    id:Any
    __name__:str
    def __tablename__(cls)->str:
        # it will return class name as table name for all the classes which inherites Base class
        return cls.__name__.lower()
