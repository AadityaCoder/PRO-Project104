import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )

cv2.putText(img,
            "Mercury",
             (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )

cv2.putText(img,
            "Venus",
             (190,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )

cv2.putText(img,
            "Earth",
             (300,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )
cv2.putText(img,
            "Mars",
             (400,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )
cv2.putText(img,
            "Jupiter",
             (500,90),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )            
            
cv2.putText(img,
            "Saturn",
             (720,110),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             ) 

cv2.putText(img,
            "Uranus",
             (950,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )

cv2.putText(img,
            "Neptune",
             (1080,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,
             color=(127,255,127)
             )

cv2.imshow("Solar System",img)
cv2.waitKey(0)             