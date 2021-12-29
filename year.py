# -*- coding: utf-8 -*-

import time
from random import randint

for i in range(1,45):
    print('')

s = ''

for i in range(1,1000):
    count = randint(1,100)
    while (count > 0):
        s += ' '
        count -= 1

    if (i % 10 ==0):
        print(s + 'اليوم نهاية عام وغدًا بداية لعام')
	print(s + '     كل عام وانتم بخير 2022    ')
    else:
        print(s + '*-*')

    s = ''
    time.sleep(0.3)
