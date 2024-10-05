from models.base import BizBaseModel

class Record(BizBaseModel, table=True):
    uuid: str
    version: str
    language: str
    region: str
