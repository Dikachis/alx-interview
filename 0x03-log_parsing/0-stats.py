#!/usr/bin/python3
"""Log Parser"""

from sys import stdin

status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
tot_size = 0
count = 0


def printStatistics():
    print('File size: {}'.format(tot_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in status.keys():
                status[code] += 1
            tot_size += size
            count += 1

        if count == 10:
            count = 0
            printStatistics()

except Exception as err:
    pass

finally:
    printStatistics()
