import requests

def get_data():
    """ 
    
    
    """
    #september_data = requests.get("https://api.openf1.org/v1/sessions?date_start>=2023-09-01&date_end<=2023-09-30")

    jp_data= requests.get("https://api.openf1.org/v1/sessions")

    
    # Check if the request was successful. google the different status codes if u want
    if jp_data.status_code == 200:
        data = jp_data.json()
        list = []
        for item in data:
            if item["location"] == "Suzuka" and item["session_name"] == "Race":
                list.append(item)
        
        return list_of_sesh
        
    else:
        #return status code
        return jp_data.status_code


def main():

    print(get_data())

main()