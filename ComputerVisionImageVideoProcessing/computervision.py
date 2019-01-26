import cv2

img = cv2.imread("galaxy.jpg",0)
# 1.. . image as it is
# 0. . . black and white image
# -1. .  . color img with alpha channel with transparency capabilities

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_image)
# cv2.imshow("Galaxy",img)

cv2.imwrite("Galaxy_resized.jpg",resized_image)
# cv2.waitKey(0) . . .  image will close as soon as the user presses a key
cv2.waitKey(2000)
# after 2000 millisecs
cv2.destroyAllWindows()
