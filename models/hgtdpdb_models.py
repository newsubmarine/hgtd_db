from re import S
import site
from sqlalchemy.sql.expression import update
from sqlalchemy import  Column, TIMESTAMP, BOOLEAN,Integer, String, FLOAT, JSON, CHAR, DATETIME, ForeignKey, INT, BLOB
from utils.series_numbers import IsVilid
from Root.database import Base
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

class DetectorUnit(HGTDModel):
	__tablename__ = "detectorunit"
	SN 			  = Column(CHAR)
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
	
	def __repr__(self) -> str:
	    return "<detectorUnit(id = '%s')>" % (self.id)
	
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
		return "<Hybrid(HybridId = '%s')>" % (self.id)

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


class FlexTail(HGTDModel):
	__tablename__ = "FlexTail"
	flexTailid      = Column(INT, primary_key= True)
	Vendor        = Column(CHAR)
	batch         = Column(CHAR)
	metrox        = Column(FLOAT)
	metroy        = Column(FLOAT)
	metroz       = Column(FLOAT)
	connectivity   = Column(CHAR)
	moduleId      = Column(CHAR)

	def __repr__(self) -> str:
	    return "<FlexTail(FlexTailID = '%s')>" % (self.flexTailid)


class Glue(HGTDModel):
	__tablename__ = "Glue"
	id      = Column(INT, primary_key= True)
	site          = Column(CHAR)
	vendor        = Column(CHAR)
	batch         = Column(CHAR)
	duid 	      = Column(INT)

	def __repr__(self) -> str:
	    return "<Glue(ID = '%s')>" % (self.id)

class Module(HGTDModel):
	__tablename__ = "Module"
	id            = Column(CHAR, primary_key= True)
	site     = Column(CHAR)
	date         = Column(TIMESTAMP)
	metrox        = Column(FLOAT)
	metroy        = Column(FLOAT)
	metroz        = Column(FLOAT)
	wireWeight    = Column(FLOAT)
	flatness      = Column(FLOAT)
	glueThickness = Column(FLOAT)
	wp            = Column(CHAR)
	ThermalCycles = Column(CHAR)
	connectivity  = Column(CHAR)
	powerconsumpution= Column(CHAR)
	#detectorUnitId= Column(CHAR)
	#PASS          = Column(CHAR)
	picture       = Column(BLOB)
	pullofwires   = Column(CHAR)

	def __repr__(self) -> str:
	    return "<Module(ModuleId = '%s')>" % (self.id)

class Moduleflex(HGTDModel):
	__tablename__ = "moduleflex"
	SN 	          = Column(INT)
	id      = Column(CHAR, primary_key= True)
	vendor        = Column(CHAR)
	batch         = Column(CHAR)
	metrox        = Column(FLOAT)
	metroy        = Column(FLOAT)
	metroz        = Column(FLOAT)
	connectivity  = Column(CHAR)
	connectorUsage= Column(CHAR)
	#PASS          = Column(BOOLEAN)
	soldering     = Column(CHAR)
	#Components    = Column(CHAR)

	def __repr__(self) -> str:
	    return "<ModuleFlex(ud = '%s')>" % (self.id)

class SupportUnit(HGTDModel):
	__tablename__ = "SupportUnit"
	id			  = Column(CHAR, primary_key= True)
	vendor        = Column(CHAR)
	batch         = Column(CHAR)
	metrox        = Column(FLOAT)
	metroy        = Column(FLOAT)
	metroz        = Column(FLOAT)
	detectorunitld= Column(CHAR)
	PASS          = Column(BOOLEAN)
	picture       = Column(BLOB)

	def __repr__(self) -> str:
	    return "<SupportUnit(SupportUnitId = '%s')>" % (self.id)

class ThermalGrease(HGTDModel):
	__tablename__ = "ThermalGrease"
	id            = Column(CHAR, primary_key= True)
	site          = Column(CHAR)
	vendor        = Column(CHAR)
	batch         = Column(CHAR)
	duid          = Column(CHAR)

	def __repr__(self) -> str:
	    return "<ThermalGrease(ThermalGreaseId = '%s')>" % (self.id)