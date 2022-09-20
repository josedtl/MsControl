from datetime import datetime


class PersonaNaturalEntity:
    PERID: int
    TIP_DOCID: int
    DOC_PER: str
    NOM_PER: str
    APE_PAT: str
    APE_MAT: str
    FEC_NAC: datetime
    FEC_VEC: datetime
    TIP_SEXID: int
    TIP_CIVID: int
    DIR: str
    DIR_REF: str
    UBIID: int
    FEC_REG: datetime
    USU_REG: str
    EST_REG: bool

    def Cargar(_json: any):
        c = PersonaNaturalEntity()
        c.PERID = _json['PERID']
        c.TIP_DOCID = _json['TIP_DOCID']
        c.DOC_PER = _json['TDOC_PER']
        c.NOM_PER = _json['TNOM_PER']
        c.APE_PAT = _json['TAPE_PAT']
        c.APE_MAT = _json['TAPE_MAT']
        c.FEC_NAC = _json['TFEC_NAC']
        c.FEC_VEC = _json['TFEC_VEC']
        c.TIP_SEXID = _json['TTIP_SEXID']
        c.TIP_CIVID = _json['TTIP_CIVID']
        c.DIR = _json['TDIR']
        c.DIR_REF = _json['TDIR_REF']
        c.UBIID = _json['TUBIID']
        c.FEC_REG = _json['TFEC_REG']
        c.USU_REG = _json['TUSU_REG']
        c.EST_REG = _json['TEST_REG']
        return c
