import requests
import concurrent.futures
from datetime import datetime, date


class Api():
    OZON = 'https://api-seller.ozon.ru/'    
    api_etgb = 'v1/posting/global/etgb'
    today = date.today()
    

    def api_post_etgb(self, client_id, api_key, range):
        
        params = {
            'date':{
                'from': datetime.fromordinal(self.today.replace(day=self.today.day-range).toordinal()),
                'to' : datetime.fromordinal(self.today.replace(day=self.today.day-(range+1)).toordinal())
            }}
        
        headers = {
            'Client-Id':client_id,
            'Api-Key':api_key,
            'Content-Type': 'application/json'
        }

        return requests.post(self.OZON+self.api_etgb, headers=headers, params=params).json()