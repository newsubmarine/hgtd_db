from re import S
from sqlalchemy.sql.expression import update
from sqlalchemy import  Column, Integer, String, FLOAT, JSON, CHAR, DATETIME, ForeignKey
from Utils import IsVilid
from database import Base
import logging

logger = logging.getLogger(__name__)


class Model(Base):
    __abstract__ = True

class HGTDModel(Model):
    __abstract__ = True
    # Common member : Serial Numbers
    # definition style
    # 20 U xx yy nnnnnnn: (nnnnnnn = "0123456")
    # SN = Column(String,primary_key = True )

    @classmethod
    def get_by_id(cls, serial_numbers):
        if IsVilid(serial_numbers):
            return cls.query.get(serial_numbers)
        else:
            logger.error("> Serial Numbers are not vilid !")

        
class Hybrid(HGTDModel):
    __tablename__ = "Hybrid"
    HybridId      = Column(CHAR, primary_key=True)
    CreateTime = Column(DATETIME)
    UpdateTime = Column(DATETIME)
    Vendor = Column(CHAR)
    Batch = Column(CHAR)
    MetroX = Column(FLOAT)
    MetroY = Column(FLOAT)
    MetroZ = Column(FLOAT)
    IV = Column(JSON)
    CV = Column(JSON)
    Temperature = Column(CHAR)
    Humidity = Column(CHAR)

    def __repr__(self) -> str:
        return "<Hybrid(HybridId = '%s')>" % (self.HybridId)

class Sensor(HGTDModel):
	__tablename__ = "Sensor"
	SensorId      = Column(CHAR, primary_key= True)
	CreateTime    = Column(DATETIME)
	UpdateTime    = Column(DATETIME)
	Vendor        = Column(CHAR)
	Batch         = Column(CHAR)
	MetroX        = Column(FLOAT)
	MetroY        = Column(FLOAT)
	MetroZ        = Column(FLOAT)
	IV            = Column(JSON)
	CV            = Column(JSON)
	Temperature   = Column(CHAR)
	Humidity      = Column(CHAR)

	def __repr__(self) -> str:
	    return "<Sensor(SensorId = '%s')>" % (self.SensorId)
