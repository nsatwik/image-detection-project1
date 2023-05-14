import numpy as np
import cv2

def generate_bounding_box(image_url, boundRect):
    image = Image.open(BytesIO(requests.get(image_url).content))
    np_img = np.array(image)
    drawing = np_img
    for i in range(len(boundRect)):
        color =(225,0,0)
        cv2.rectangle(drawing, int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3]),color , 2)
        
        
        #showing the image
        plt.figure(figsize=(14,8))
        plt.imshow(drawing)
        plt.axis("off")
        plt.show()
        
generate_bounding_box(image_url,faces)