import requests

response = requests.get("https://goldilocksresearch.com/cus_dashboard.php")

print(response.text)