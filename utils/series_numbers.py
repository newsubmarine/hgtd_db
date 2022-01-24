import logging
import random
logger = logging.getLogger("Serial Numbers")

_BEGIN_ = ["20U"] # 20: Code for ATLAS detector; U: Phase-2 ATLAS UPGRADE
_xx_    = ["HA","HC","HG"] # HGTD endcap A; HGTD encap C; HGTD general

_yy_      = ["SE","AS","HY","MF","FT","MO","SU","DU","GL","TG"]
_yy_type_ = ["Sensor","ASIC","Hybrid","ModuleFlex","FlexTail","Module","SupportUnit","DetectorUnit","Glue","ThermalGrease"]

_vendor_  = list(range(10))
_batch_   = list(range(10))
_site_    = list(range(10))
_numbering_= list(range(100000))
_date_    = [chr(i) for i in range(97,130)] # A to Z
_position_ = list(range(6))
_phi_     = list(range(1,6))
_quadrants_ = list(range(8))



def IsVilid(type):
	return True


def get_sn(type):
	nnnnnn = []
	xx = random.choice(_xx_)
	yy = _yy_[_yy_type_.index(type)]
	d = generate_info(type)
	if type not in _yy_type_: logger.error(f"type {type} is not valid !")
	if type in _yy_type_[:5]:
		nnnnnn.append([d["vendor"],d["batch"],d["numbering"]])
	elif type == _yy_type_[5]:
		nnnnnn.append([d["site"],d["batch"],d["numbering"]])
	elif type in _yy_type_[6:8]:
		nnnnnn.append([d["site"],d["batch"],d["position"],d["phi"],d["quadrants"],0,0])
	elif type in _yy_type_[9:10]:
		nnnnnn.append([d["vendor"],d['site'],d['batch'],0,0,0,0])	
	sn = "".join([ _BEGIN_[0], xx, yy, "".join([str(i) for i in nnnnnn[0]])])
	#  20U + xx + yy + nnnnnnn
	logger.info(f"> Get Serial numbers: {sn}")
	return sn

def generate_info(type):
	d = dict()
	if type in _yy_type_[:5]:
		d["vendor"] = random.choice(_vendor_)
		d["batch"] = random.choice(_batch_)
		d["numbering"] = f"{random.choice(_numbering_):05}"

	elif type == _yy_type_[5]:
		d["site"] = random.choice(_site_)
		d["batch"] = random.choice(_batch_)
		d["numbering"] = f"{random.choice(_numbering_):05}"

	elif type == _yy_type_[6]:
		d["site"] = random.choice(_vendor_)
		d["batch"] = random.choice(_batch_)
		d["position"] = random.choice(_position_)
		d["phi"] = random.choice(_phi_)
		d["quadrants"] = random.choice(_quadrants_)

	elif type == _yy_type_[7]:
		d["site"] = random.choice(_vendor_)
		d["batch"] = random.choice(_batch_)
		d["position"] = random.choice(_position_)
		d["phi"] = random.choice(_phi_)
		d["quadrants"] = random.choice(_quadrants_)

	elif type in _yy_type_[-2:]:
		d["vendor"] = random.choice(_vendor_)
		d["site"]  = random.choice(_site_)
		d["batch"] = random.choice(_batch_)
	return d