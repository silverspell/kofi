# -*- coding: utf-8 -*-

import numpy as np
import cv2
import argparse
import math
import requests
#import Image
import uuid

output = None
image = None
processed = None


def load_img_and_gray(path):
    """�maj y�kler, siyah beyaza �evirri"""
    global output
    global image
    image = cv2.imread(path)
    output = image.copy()
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def find_circles(img):
    """T�m yuvarlaklar� buluyor"""
    global output
    circles = cv2.HoughCircles(img, 3, 5, 200)
    return circles

def find_optimal_circle(circles):
    """En muhtemelen yuvarla�� buluyor"""
    global image
    global output

    w, h = image.shape[:2]
    print w, h
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        #imaj�n d���na ta�an yuvarlaklar� filtele
        candidates = [(x,y,r) for(x,y,r) in circles if  (r, r) < (w / 2, h / 2) and (r + x <= w and r + x <= h) and ((x - r > 0) and (y - r > 0))]
        return max (candidates, key = lambda i : math.pi * 2 * i[2])


def draw_circles(circles):
    """M�himsiz"""
    global output

    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


def crop(circle):
    """Bulunan en b�y�k circlea g�re crop yap�yor"""
    global processed
    x,y,r = circle
    rectX = (x - r)
    rectY = (y - r)
    print x, y, r, rectX, rectY
    return processed[rectY:(y+2*r), rectX:(x+2*r)]


def transform(rectangle):
    """fincan� 4 e b�l�yor"""
    w,h = rectangle.shape[:2]
    return rectangle[0:h//2, 0:w//2], rectangle[0:h//2, w//2:w], rectangle[h//2:h, 0:w//2], rectangle[h//2:h, w//2:w]

def merge(t1, t2, t3, t4):
    """4 par�ay� yan yana d���yor"""
    h1, w1 = t1.shape[:2]
    h2, w2 = t2.shape[:2]
    h3, w3 = t3.shape[:2]
    h4, w4 = t4.shape[:2]
    vis = np.zeros((max(h1,h2,h3,h4), w1+w2+w3+w4), np.uint8)
    vis[:h1, :w1] = t1
    vis[:h2, w1:w1+w2] = t2
    vis[:h3, w1+w2:w1+w2+w3] = np.flipud(t3)
    vis[:h4, w1+w2+w3:w1+w2+w3+w4] = np.flipud(t4)
    return vis

def smudge(merged):
    """Birle�tirip beyaz alanlar� yok ediyor"""
    ret2,th = cv2.threshold(merged, 127, 255, cv2.THRESH_OTSU)
    h, w = th.shape[:2]
    m = merged.copy()
    whites = (th == 255)
    copied = np.where(th < np.average(th))
    m[whites] = copied[0][-1]

    return m


def cognitiveRequest(fname):
    """imaj� mikropsofta atar"""
    url = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Categories,tags,description&language=en"
    header = {"Ocp-Apim-Subscription-Key" : "c0b391a74ee84081bf1ec525ddb68bcb", "Content-Type": "application/octet-stream"}

    imF = open(fname, "rb")
    f = imF.read()
    data = bytearray(f)

    response = requests.post(url, data=data, headers=header)
    return response.json()



def main(args):
    """main"""
    global processed
    kernel = np.ones((1, 1), np.uint8)
    gausBlurKernel = (9, 9)

    gray = load_img_and_gray(args["image"])
    processed = gray.copy()
    ret, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_OTSU)

    #gray = cv2.GaussianBlur(gray, gausBlurKernel, 0)
    gray = cv2.erode(gray, kernel)
    gray = cv2.dilate(gray, kernel)
    gray = cv2.GaussianBlur(gray, gausBlurKernel, 0)
    gray = cv2.erode(gray, kernel)


    circles = find_circles(gray)

    the_circle = find_optimal_circle(circles)

    cv2.circle(output, (the_circle[0], the_circle[1]), the_circle[2], (0, 0, 255), 6)

    cropped = crop(the_circle)
    t1, t2, t3, t4 = transform(cropped)
    transformed = merge(t1, t2, t3, t4)
    smudged = smudge(transformed)

    fname = str(uuid.uuid4()) + ".jpg"
    cv2.imwrite(fname, smudged)
    response = cognitiveRequest(fname)
    if args["log"] == "Y":
        with open("report.txt", "a") as report:
            print>>report, args["image"]
            print>>report, fname
            print>>report, cognitiveRequest(fname)
            print>>report, "-" * 150
    if args["show"] == "Y":
        cv2.imshow("circle", cropped)
        cv2.imshow("output", np.hstack([output, image]))
        cv2.imshow("temp", gray)
        cv2.imshow("transformed", transformed)
        cv2.imshow("smudged", smudged)
        cv2.waitKey(0)
    if args["return"] == "Y":
        return response, fname



if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help = "Path to image")
    ap.add_argument("-s", "--show", required=True, help="Show Opencv?")
    ap.add_argument("-l", "--log", required=True, help="Log?")
    ap.add_argument("-r", "--return", required=True, help="Return?")
    args = vars(ap.parse_args())
    main(args)
