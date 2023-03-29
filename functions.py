from sqlalchemy.orm import Session
import models

def get_branch_detail(db: Session, branch_name:str):
    result = None
    try:
        result = db.query(models.Branches).filter(models.Branches.branch == branch_name).first()
    except Exception as e:
        return f"Error : {e}"
    return result


def get_list_banks(db: Session, branch_name:str):
    try:
        result = db.query(models.Branches).filter(models.Branches.branch == branch_name).all()
        return result
    except Exception as e:
       return e
    

def get_bank_name(db: Session, bank_id:int):
    try:
        result = db.query(models.Banks).filter(models.Banks.id == bank_id).first()
        print(result)
        return result.name
    except Exception as e:
        return e