from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel):
    id:int
    content:str

memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return '메모 추가에 성공했습니다'

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    print(req_memo.id)
    for memo in memos: 
        print(memo.id)
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return '성공했습니다.'
    return '그런 메모는 없습니다'

# @app.put("/memos/{memo_id}")
# def put_memo(req_memo:Memo):
#     print(req_memo.id)
#     print(req_memo.content)
#     print(type(req_memo.id))
#     for memo in memos:
#         print(type(memo.id))
#         if memo.id==req_memo.id:
#             memo.content=req_memo.content
#             return '성공했습니다'
#         return '그런 메모는 없습니다'
    
@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    print(memo_id)
    for index, memo in enumerate (memos):
        if str(memo.id)==str(memo_id):
            memos.pop(index)
            return '성공했습니다'
    return '그런 메모는 없습니다'

app.mount("/", StaticFiles(directory="static",html=True), name="static")