import cv2

img = cv2.imread('images/cellphone.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 2.)
_, cnts, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

def deskew(image, width):
    (h, w) = image.shape[:2]
    moments = cv2.moments(image)

    skew = moments["mu11"] / moments["mu02"]
    M = np.float32([
        [1, skew, -0.5 * w * skew],
        [0, 1, 0]
    ])
    image = cv2.warpAffine(image, M, (w, h), flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    image = imutils.resize(image, width = width)
    return image 

def center_extent(image, size):
    (eW, eH) = size 

    if image.shape[1] > image.shape[0]:
        image = imutils.resize(image, width=eW)

    else:
        image = imutils.resize(image, height=eH)

    extent = np.zeros((eH, eW), dtype="uint8")
    offsetX = (eW - image.shape[1]) // 2
    offsetY = (eH - image.shape[0]) // 2
    extent[offsetY:offsetY + image.shape[0], offsetX:offsetX + image.shape[1]] = image
    CM = mahotas.center_of_mass(extent)
    (cY, cX) = np.round(CM).astype("int32")
    (dX, dY) = ((size[0] // 2) - cX, (size[1] // 2) - cY)
    M = np.float32([
        [1, 0, dX],
        [0, 1, dY]
    ])
    extent = cv2.warpAffine(extent, M, size)
    return extent


# cv2.imshow('gambar', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print(cnts)