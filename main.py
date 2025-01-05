import requests

def get_data():
    """To get all sessions in September 2023, use:
        https://api.openf1.org/v1/sessions?date_start>=2023-09-01&date_end<=2023-09-30
    """
    september_data = requests.get("https://api.openf1.org/v1/sessions?date_start>=2023-09-01&date_end<=2023-09-30")

    # Check if the request was successful. google the different status codes if u want
    if september_data.status_code == 200:
        return september_data.json()
    else:
        #return status code
        return september_data.status_code


def main():

    print(get_data())

main()