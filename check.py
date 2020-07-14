import requests


RESULTS_FILE_NAME = "results.txt"
DOMAINS_FILE_NAME = "domains.txt"
NOT_MATCHING_LIST = ["not found", "404"]


# clear results file
open(RESULTS_FILE_NAME, "w").close()

urlsFile = open(DOMAINS_FILE_NAME, "r")
urls = urlsFile.readlines()

for url in urls:

    # remove line breaks from url
    url = url.replace('\n', '')

    # add http if missing
    if "http://" not in url: 
        url = "http://"+url

    print ("Processing URL: " + url)

    # get request on url
    r = requests.get(url)

    # if nothing is present from NOT_MATCHING_LIST
    # print the url in console
    for not_matching in NOT_MATCHING_LIST:
        if not_matching not in r.text:
            file_object = open(RESULTS_FILE_NAME, "a")
            file_object.write(url+"\n")
            file_object.close()
            

    
