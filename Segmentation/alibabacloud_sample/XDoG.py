#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


def XDoG_filter(image,
                kernel_size=0,
                sigma=1.4,
                k_sigma=1.6,
                epsilon=0,
                phi=10,
                gamma=0.98):
    epsilon /= 255
    dog = DoG_filter(image, kernel_size, sigma, k_sigma, gamma)
    dog /= dog.max()
    e = 1 + np.tanh(phi * (dog - epsilon))
    e[e >= 1] = 1
    return e.astype('uint8') * 255


def DoG_filter(image, kernel_size=0, sigma=1.4, k_sigma=1.6, gamma=1):

    g1 = cv.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    g2 = cv.GaussianBlur(image, (kernel_size, kernel_size), sigma * k_sigma)
    return g1 - gamma * g2


if __name__ == '__main__':
    sample_image = cv.imread('./imageJPG/skin.jpg')
    gray_image = cv.cvtColor(sample_image, cv.COLOR_BGR2GRAY)

    result_image = XDoG_filter(gray_image)
    print(result_image)
    # cv.imshow('Before', sample_image)
    cv.imshow('After', result_image)
    cv.waitKey(-1)
