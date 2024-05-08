from core.config import settings
from sqlalchemy import Column,INTEGER,String

class CarroModel(settings.DBBaseModel):
    __tablename__ ='carros'
    
    id: int = Column(INTEGER(), primary_key=True, autoincrement=True)
    nome: str =Column(String(50))
    marca : str = Column(String(75))
    ano: str = Column(String(4))