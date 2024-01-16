import urllib.request as urllib

def main(url):
    print("Checking connectivity")
    
    response = urllib.urlopen(url)
    print("Connected to", url, "successfullly")
    print("The response code was:", response.getcode()) 

    response_code = response.getcode()
    if response_code == 200:
        print("The site is running okay")
    elif response_code == 400:
        print("Bad Request")
    else:
        print("Failed to connect :")      

print("Site connectivity checker")
input_url = input("Type in the url to check its connectivity : ")
main(input_url)



