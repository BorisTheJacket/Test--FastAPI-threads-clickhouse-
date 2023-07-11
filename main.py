from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import EtgbDeclaration
from db import session
from api import Api
import concurrent.futures
from repository import RepositoryDB


app=FastAPI()


db=session()



@app.post('/downloadETGB')
def apiGetETGB(client_id: str, api_key: str, days_range:int):
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        threads = [executor.submit(Api().api_post_etgb, [client_id, api_key,i]) for i in range(days_range)]
        db_conn = RepositoryDB(db)

        for declaration in concurrent.futures.as_completed(threads):    
            
            etgb_decl = EtgbDeclaration(
                    posting_number = declaration.result()['posting_number'],
                    number = declaration.result()['etgb']['number'],
                    date = declaration.result()['etgb']['date'],
                    url = declaration.result()['etgb']['url']
                )
            if db_conn.decl_dont_exists(etgb_decl):            
                db_conn.create_etgb(etgb_decl)
            
        
    
    return JSONResponse(content={'Количество загруженных деклораций': db_conn.db.query().execute('''
                                                                                                SELECT COUNT(*)
                                                                                                FROM etgb_table''')})