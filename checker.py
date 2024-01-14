import urllib.request as urllib

def main(url):
    print("Checking connectivity")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfullly")
    print("The response code was:", response.getcode())

print("Site connectivity checker")
input_url = input("Type in the url to check its connectivity : ")
main(input_url)



