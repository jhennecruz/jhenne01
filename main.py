import requests, sys

# Gets the contents of an image on the Internet to be
# sent to the machine learning model for classifying
def getImageUrlData(wwwLocationOfImage):
    data = requests.get(wwwLocationOfImage).content
    if sys.version_info[0] < 3:
        # Python 2 approach to handling bytes
        return data.encode("base64")
    else:
        # Python 3 approach to handling bytes
        import base64
        return base64.b64encode(data).decode()



# This function will pass your image to the machine learning model
# and return the top result with the highest confidence
def classify(imageurl):
    key = "3814dad0-0ae9-11ea-9313-371577b835dfd6cb22e6-2aac-4b8c-88bb-ae819561fe24"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.post(url, json={ "data" : getImageUrlData(imageurl) })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to the URL of the image you want to classify

demo = classify(input("Digite a url: "))

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" %(label, confidence))