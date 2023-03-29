from typing import Union
import models
import database
import functions
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/bank-list/{branch_name}")
def get_banks(branch_name: str, db: Session = Depends(get_db)):

    branch_detail = functions.get_branch_detail(db =db, branch_name= branch_name)

    if branch_detail is None:
        raise HTTPException(status_code=400, detail="Branch name doesn't exist.")
    if isinstance(branch_detail, dict):
        raise HTTPException(status_code=500, detail="Internal server error")
    
    results = functions.get_list_banks(db= db, branch_name= branch_name)
    result_dicts = {"ifsc": branch_detail.ifsc,
                    "branch": branch_detail.branch,
                    "address": branch_detail.address,
                    "city": branch_detail.city,
                    "district": branch_detail.district,
                    "state": branch_detail.state,
                    "banks": []}
    for result in results:
        print(functions.get_bank_name(db=db, bank_id=result.bank_id))
        result_dicts["banks"].append({"name": functions.get_bank_name(db=db, bank_id=result.bank_id)})
    return result_dicts



