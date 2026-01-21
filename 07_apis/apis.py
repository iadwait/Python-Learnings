import requests

url = "https://dummy.restapiexample.com/api/v1/employees"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36"
}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data)
    print(f"Status = {data['status']}")
    print(f"Message = {data['message']}")
    for emp in data['data']:
        print(f"Id = {emp['id']}, Name = {emp['employee_name']}")
elif response.status_code == 429:
    print('Request Limit Exceeded !!')
else:
    print('Internal Server Error Occurred !!')