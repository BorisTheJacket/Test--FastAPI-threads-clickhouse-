from sqlalchemy.orm import Session
from models import EtgbDeclaration


class RepositoryDB():
    
    def __init__(self, db:Session):
        self.db = db


    def create_etgb(self, declaration: EtgbDeclaration):
        self.db.add(declaration)
        self.db.commit()
        self.db.refresh(declaration)
        return declaration
    

    def decl_dont_exists(self, declaration: EtgbDeclaration):
        return self.db.query(EtgbDeclaration).get(declaration.url) != None 