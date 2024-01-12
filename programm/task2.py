#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def circle(radius):
    return math.pi * radius ** 2


def cylinder():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    print("Рассчитать только площадь боковой поверхности? (да/нет): ")
    surface_only = input().lower() == 'да'

    lateral_surface_area = 2 * math.pi * radius * height

    if surface_only:
        print("Площадь боковой поверхности цилиндра:", lateral_surface_area)
    else:
        total_surface_area = lateral_surface_area + 2 * circle(radius)
        print("Полная площадь цилиндра:", total_surface_area)


if __name__ == "__main__":
    cylinder()
