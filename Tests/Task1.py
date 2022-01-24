import sys

import requests

# One
response = requests.post('https://careers-api.fixably.com/token', data={"Code": '69432457'})
json_response = response.json()
print(json_response['token'])
token = json_response['token']


# Two
pageNumber = 1
orders = []
order_stats = {
    "Assigned": 0,
    "Unpaid": 0,
    "Open": 0,
    "Closed": 0,
    }
while  True:
    try:
        response = requests.get(
            "https://careers-api.fixably.com/orders?page=%s" % pageNumber,
            headers = {'X-Fixably-Token':token, 'Content-Type':'multipart/form-data'},
            )
        print("We are on page %s" %pageNumber, end="\r")
        pageNumber += 1
        orders += response.json()['results']
    except KeyError:
        break
    except:
        print("Problem accessing the endpoint")
        break
print("\nOut of %s orders: " % len(orders))
for order in orders:
    if order['status'] ==1:
        order_stats['Open'] += 1
    elif order['status'] ==2:
        order_stats['Closed'] += 1
    elif order['status'] == 3:
        order_stats['Assigned'] += 1
    elif order['status'] == 4:
        order_stats['Unpaid'] += 1
for i in order_stats.keys():
    print("%s orders are %s" %(order_stats[i], i))


# Three
iPhoneDeviceTech = []
for order in orders:
    if order["deviceBrand"].startswith('iPhone') and order['status'] ==2:
        iPhoneDeviceTech.append(order)
    #print(iPhoneDeviceTech)

sys.stdout = open("Task3.txt", "w")
#sys.stdout = open("Task3.xls", "w")
print(iPhoneDeviceTech)
sys.stdout.close()
