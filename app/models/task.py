from sqlalchemy import Column, String, Boolean
from sqlalchemy.sql.sqltypes import Integer
from app.db.base_class import Base

class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
