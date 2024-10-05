
from dal import utils
from models.record import Record
from sqlmodel import Session, select, func
from fastapi import Depends
from schemas.req.record import RecordQuery


class RecordDAL:
    def __init__(self,  session: Session = Depends()):
        self.session = session

    def list_records(self, query_params: RecordQuery) -> list[Record]:
        statement = select(Record)
        statement = utils.apply_sort(Record, statement, query_params.sort_fields)
        statement = utils.apply_page(statement, query_params.page)
        results = self.session.exec(statement)
        records = results.all()
        return records

    # 获取符合条件的总记录数
    def count_records(self, query_params: RecordQuery) -> int:
        # 基于 Record 表进行查询，使用 func.count() 来计算总数
        count_statement = select(func.count(Record.id))  # 选择记录的数量
        # 执行查询并返回总记录数
        result = self.session.exec(count_statement)
        total_records = result.one()  # 获取查询结果
        return total_records