
import io
from google.cloud import vision, storage
from google.cloud.vision import types
from config import Config

def cloudAPI(file_image):
    #vision_client = vision.ImageAnnotatorClient()
    vision_client = storage.Client.from_service_account_json(Config.GOOGLE_APPLICATIONS_CREDENTIALS)

    #file_name = file_image

    with io.open(file_image,'rb') as image_file:
        content = image_file.read()
        image = types.Image(content=content)
        #sending image to Vision API

        response = vision_client.text_detection(image=image) #getting text from imaged passed

        texts = response.text_annotations #placing response from Vision API in to an array


        return texts

'''for text in texts:
    print(text.description)

tCount = 0
for text in texts:
    if tCount == 0:
     parsey = text.description
     print(parsey)
    #print("texts 2", countcounter)
    tCount = tCount + 1
countcounter = 0
while counter != len(parsey):
 print(newlineCounter)
 if newlineCounter == 3:
  while parsey[counter] != '\n':
   LicensePlateActual[countcounter] = parsey[counter]
 #print(LicensePlateActual)
 if parsey[counter] == '\n':
  newlineCounter = newlineCounter + 1
 counter = counter + 1
'''
