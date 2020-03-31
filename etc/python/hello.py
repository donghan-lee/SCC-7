import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')
rjson = r.json()

for row in rjson['rentBikeStatus']['row']:
        print(row["stationName"][4:] + ' ( ' + row['parkingBikeTotCnt'] + '/' + row['rackTotCnt'] + ' )')
