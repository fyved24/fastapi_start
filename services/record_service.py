# app/services/record_service.py

from sqlmodel import Session
from fastapi import  Depends
from common import usercontext_util
from dal.record_dal import RecordDAL
from schemas.common.base_response_schema import Page
from schemas.req.record import RecordQuery
from schemas.resp.record import RecordResp
from core.dependencies import get_db


class RecordService:
    def __init__(self,  session: Session = Depends(get_db)):
        self.record_dal = RecordDAL(session)

    def fetch_data(self, query_params: RecordQuery):
        user = usercontext_util.get_current_user()
        print(user)
        records = self.record_dal.list_records(query_params)
        total_records = self.record_dal.count_records(query_params)
        page = Page()
        page.pageSize = query_params.page.pageSize
        page.currentPage = query_params.page.currentPage
        page.total = total_records
        resp = RecordResp(items=records, page=page)
        return resp