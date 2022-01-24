from re import S
import site
from sqlalchemy.sql.expression import update
from sqlalchemy import  Column, Integer, String, FLOAT, JSON, CHAR, DATETIME, ForeignKey, INT, BLOB
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


class ASIC(HGTDModel):
	__tablename__ = "ASIC"
	id            = Column(INT, primary_key = True)
	vendor        = Column(CHAR)
	batch = Column(CHAR)
	metrox = Column(FLOAT)
	metroy = Column(FLOAT)
	metroz = Column(FLOAT)
	dacsetting = Column(CHAR)
	#pass = Column(CHAR)
	defect = Column(CHAR)
	shearofbump = Column(CHAR)
	hybridid = Column(CHAR)

class Detectorunit(HGTDModel):
	__tablename__ = "detectorunit"
	id            = Column(INT, primary_key = True)
	site        = Column(CHAR)
	date = Column(DATETIME)
	metrox = Column(FLOAT)
	metroy = Column(FLOAT)
	metroz = Column(FLOAT)
	flatness = Column(FLOAT)
	gluethickness = Column(FLOAT)
	#pass = Column(CHAR)
	picture = Column(BLOB)
	
class Hybrid(HGTDModel):
	__tablename__ = "hybrid"
	id = Column(INT, primary_key=True)
	vendor = Column(CHAR)
	batch = Column(CHAR)
	metrox = Column(FLOAT)
	metroy = Column(FLOAT)
	metroz = Column(FLOAT)
	disconectdbumps = Column(CHAR)
	#pass = Column(CHAR)
	picture = Column(BLOB)
	scratche = Column(CHAR)
	damage = Column(CHAR)
	moduleid = Column(CHAR)
	def __repr__(self) -> str:
		return "<Hybrid(HybridId = '%s')>" % (self.HybridId)

class Sensor(HGTDModel):
	__tablename__ = "sensor"
	id            = Column(INT, primary_key= True)
	sensorname    = Column(DATETIME)
	vendor        = Column(DATETIME)
	batch         = Column(CHAR)
	metrox        = Column(CHAR)
	metroy        = Column(FLOAT)
	metroz        = Column(FLOAT)
	hybridid      = Column(INT)
	SN            = Column(CHAR)

	def __repr__(self) -> str:
	    return "<Sensor(id = '%s')>" % (self.id)