import json
import sys
from viapi.fileutils import FileUtils
from typing import List
from Tea.core import TeaCore

from alibabacloud_imageseg20191230.client import Client as imageseg20191230Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_imageseg20191230 import models as imageseg_20191230_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient
import os
from urllib.request import urlretrieve
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def portrait_generator():
    dict_of_img = {}  # this if for store all of the image data
    directory_name = 'imageJPG'
    # this function is for read image,the input is directory name
        # this loop is for read each image in this foder,directory_name is the foder name with images.
    for filename in os.listdir(r"./" + directory_name):
        # print(filename) #just for test
        # img is used to store the image data
        img = cv2.imread(directory_name + "/" + filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dict_of_img[filename[0:-4]] = img
        # print(img)
    print(dict_of_img.keys())

    img_shape = dict_of_img['skin'].shape
    merge_img = np.zeros([img_shape[0], img_shape[1]])
    # merge_img = dict_of_img['skin'].copy()
    print(len(dict_of_img))
    print(img_shape)
    # plt.show()
    for key, value in dict_of_img.items():
        # sobelX = cv2.Sobel(element, cv2.CV_64F, 1, 0)  # x方向的梯度
        # sobelY = cv2.Sobel(element, cv2.CV_64F, 0, 1)  # y方向的梯度
        # element = cv2.bitwise_or(sobelX, sobelY)  #
        # ret, thresh = cv2.threshold(value, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        if key == 'l_eye' or key == 'r_eye' or key == 'l_brow' or key == 'r_brow':
            # Horizontal = cv2.Sobel(value, 0, 1, 0, cv2.CV_64F)
            #
            # # 门槛就像
            # # (variable,0,<x axis>,<y axis>,cv2.CV_64F)
            # Vertical = cv2.Sobel(value, 0, 0, 1, cv2.CV_64F)
            #
            # # 做按位运算
            # value = cv2.bitwise_or(Horizontal, Vertical)  # 显示边缘图像

            value = cv2.Laplacian(value, cv2.CV_8U, ksize=3, scale = 3, delta = 10)
        else:
            # value = cv2.Canny(value, 10, 200)
            value = cv2.Laplacian(value, cv2.CV_8U, ksize=3, scale=5, delta=10)
        # # 寻找二值化图中的轮廓
        # contours, hierarchy = cv2.findContours(
        #     thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #
        # cv2.drawContours(value, contours, -1, (0, 0, 0), 2)
        merge_img += value
        # cv2.add(merge_img, value)

    print(merge_img)
    plt.imshow(merge_img, cmap='binary')
    plt.show()
        # merge_img = cv2.add(merge_img, element)

    # cv2.imshow('merge_img', merge_img)


    pass


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> imageseg20191230Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'imageseg.cn-shanghai.aliyuncs.com'
        return imageseg20191230Client(config)

    @staticmethod
    def main(
        args: List[str],
            oss_url
    ) -> None:
        client = Sample.create_client('LTAI5t5iAHQptb1hF7Ene2Nn', 'Aavb3sy7buip8WGmOm9c9D1LaAn4Wb')
        parse_face_request = imageseg_20191230_models.ParseFaceRequest(
            image_url=oss_url
        )
        resp = client.parse_face(parse_face_request)
        result = json.loads(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

        os.makedirs('./image/', exist_ok=True)
        for element in result['body']['Data']['Elements']:
            urlretrieve(element['ImageURL'], './image/'+ element['Name'] + '.png')
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
        portrait_generator()


    @staticmethod
    async def main_async(
        args: List[str],
        oss_url
    ) -> None:
        client = Sample.create_client('LTAI5t5iAHQptb1hF7Ene2Nn', 'Aavb3sy7buip8WGmOm9c9D1LaAn4Wb')
        parse_face_request = imageseg_20191230_models.ParseFaceRequest(
            image_url=oss_url
        )
        resp = await client.parse_face_async(parse_face_request)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    # file_utils = FileUtils("LTAI5t5iAHQptb1hF7Ene2Nn", "Aavb3sy7buip8WGmOm9c9D1LaAn4Wb")
    # original_url = "https://www.thestatesman.com/wp-content/uploads/2017/08/1493458748-beauty-face-517.jpg"
    # oss_url = file_utils.get_oss_url(
    #     original_url, "jpg", False)
    #
    # Sample.main(sys.argv[1:], oss_url)
    portrait_generator()