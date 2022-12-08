import cv2
import pytesseract
from PIL import Image

print("1. Use Camera")
print("2. Use Uploaded Image (Recommended)")
print("3. Exit")
choice = int(input("Enter Choice: "))
outputText = ""
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

#Turn on Camera and Capture Image
if(choice == 1):
    
    camera_port = 0

    camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)

    while True:
        retval, image = camera.read()
        cv2.imshow("Test", image)

        if not retval:
            break

        k = cv2.waitKey(1)

        # Press Spacebar to capture Image pip 
        if k%256==32:
            file = "test_image.png"
            cv2.imwrite(file, image)
            break
        
    del camera
    cv2.destroyAllWindows()


    img=cv2.imread("test_image.png")
    outputText = pytesseract.image_to_string(img)
    outputText = outputText.strip().replace(" ", "")

elif(choice == 2):

    print("Uploaded Car Image")
    imageName = input("Enter name of Image (including extension): ")
    img=cv2.imread(imageName)
     
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    flter=cv2.bilateralFilter(gray,11,15,15)
    edge=cv2.Canny(flter,170,200)
    contor,herf=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    ctn=sorted(contor,key=cv2.contourArea,reverse=True)
     
    for c in ctn:
        peri=cv2.arcLength(c,True)
        epsilon=0.018*peri
        approx=cv2.approxPolyDP(c,epsilon,True)
        if len(approx)==4:
            x,y,w,h=cv2.boundingRect(approx)
            img2=img[y:y+h,x:x+w]
            configr = ('-l eng --oem 1 --psm 3')

            outputText=pytesseract.image_to_string(img2,config=configr)
            final=cv2.drawContours(img,[approx],-1,(255,0,0),3)
            break
        
    cv2.imshow("Image",img)
    cv2.waitKey(0)

    outputText = outputText.strip().replace(" ", "")

elif choice == 3: 
    exit()

else:
    print("Wrong Choice Entered")
    exit()




