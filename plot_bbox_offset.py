import cv2

im_path = 'buildings.png'
img = cv2.imread(im_path)

bboxes = [[559., 607.,  80.,  97.],
        [606, 510, 72, 68],
        [776, 526, 106, 48],
        [720., 654., 118.,  68.],
        [888, 436, 74, 86],
        [766, 506, 134, 78],
        [852, 700, 60, 136],
        [644, 386, 80, 84],
        
        ]
offsetes = [[-1.5281978*6, -3.429912*6 ],
            [-1.7888961*6, -1.7642419*6],
            [-3.210652*6,6*   -0.90059865],
            [6*-3.1665087, -2.587991*6 ],
            [-1.2137605*6, -2.5592842*6],
            [-3.8895855*6, -1.8631905*6],
            [-2.632319*6,  -3.9743512*6],
            [-1.7618666 *6, 6*-1.2724816 ]]

for bbox, offset in zip(bboxes, offsetes):
    start = (int(bbox[0]+bbox[2]/2), int(bbox[1]+bbox[3]/2))
    endpoint = (int(start[0]+offset[0]),int(start[1]+offset[1]))
    cv2.arrowedLine(img,endpoint, start, (0,0,255),2,0,0,0.2)
    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (0,255,0), 2)
cv2.imwrite('buildings_bbox_offset.png', img)
cv2.imshow('image', img)
cv2.waitKey(0)