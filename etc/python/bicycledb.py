import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta.bikes

def print_and_insert():
        r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')
        rjson = r.json()

        rentBikeStatus = rjson['rentBikeStatus']
        rows = rentBikeStatus['row']

        for row in rows:
                station = row['stationName'].split('. ')[1]
                parked = row['parkingBikeTotCnt']
                total = row['rackTotCnt']

                print('{} ( {}/{} )'.format(station, parked, total))
                db.insert_one({'station': station, 'parked': parked, 'total': total})

def find_and_print():
        all_bikes = list(db.find())
        for bike in all_bikes:
                print('{} ( {}/{} )'.format(bike['station'], bike['parked'], bike['total']))

find_and_print()