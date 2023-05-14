import requests
%matplotlib inline
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO

subscritption_key = "c64fdbde401549f5be57235b8d80f7d8"
analyze_url = "https://detection-project.cognitiveservices.azure.com//vision/v3.1/analyze"
image_url = input("Enter your Image URL - ")
headers = {'Ocp-Apim-Subscription-Key': subscritption_key}
params = {'visualFeatures':'Categories,Description,Faces,Objects'}
data = {'url': image_url}

try:
    response = requests.post(analyze_url, headers=headers, params = params, json=data)
    response.raise_for_status()
    analysis = response.json()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
#Displaying the Image
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
plt.show()
print(analysis)