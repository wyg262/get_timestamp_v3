#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-f', "--file", help='日志文件')
parser.add_argument('-i', "--knightid", help='骑手账号')
args = parser.parse_args()

knightId = args.knightid
logFile = args.file
serverTime = ''

def stamp_to_local_time(timeStamp):
    timeArray = time.localtime(int(timeStamp)/1000)
    localTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
    return localTime

def get_properties_time(log):
    with open(log) as f:
        result = {}
        enumPropertiestime = {}
        floatPropertiestime = {}
        longPropertiestime = {}
        textPropertiestime = {}
        for line in f.readlines():
            if 'deviceName' in line and knightId in line:
                serverTime = line.split('.')[0]
                result['serverTime'] = serverTime
                content = json.loads(line.split('product=')[1])
                #enumPropertiestime
                enumPropertieslist = ['elevator_predict_status', 'IODetector_status']
                for item in enumPropertieslist:
                    if content['data']['enumProperties'].get(item) != None:
                        enumPropertiestime[item] = stamp_to_local_time(content['data']['enumProperties'][item]['startTime'])
                    else:
                        enumPropertiestime[item] = '                   '
                result['enumPropertiestime'] = enumPropertiestime
                #floatPropertiestime
                floatPropertieslist = ['accel_x', 'accel_y', 'accel_z', 'mag_x', 'mag_y', 'mag_z', 'orien_roll', 'orien_yaw', 'gyro_x', 'gyro_y', 'gyro_z', 'gps_bearing',
                                       'gps_lat', 'gps_lon', 'gps_speed', 'gps_hori_accuracy', 'gps_altitude', 'grav_x', 'grav_y', 'grav_z',
                                       'user_accel_x', 'user_accel_y', 'user_accel_z', 'step_number', 'screen_lightNum', 'light_value', 'proximity', 'orien_pitch']
                for item in floatPropertieslist:
                    if content['data']['floatProperties'].get(item) != None:
                        floatPropertiestime[item] = stamp_to_local_time(content['data']['floatProperties'][item]['startTime'])
                    else:
                        floatPropertiestime[item] = '                   '
                result['floatPropertiestime'] = floatPropertiestime
                #longPropertiestime
                longPropertieslist = ['gps_isOpen', 'gps_time', 'light_time', 'mag_time', 'grav_time', 'gyro_time', 'light_time', 'step_time', 'satellite_count'
                                      'accel_time', 'orien_time', 'nfc_isOpen', 'screen_isLight', 'proximity_time', 'user_accel_time', 'screen_isLock', ]
                for item in longPropertieslist:
                    if content['data']['longProperties'].get(item) != None:
                        longPropertiestime[item] = stamp_to_local_time(content['data']['longProperties'][item]['startTime'])
                    else:
                        longPropertiestime[item] = '                   '
                result['longPropertiestime'] = longPropertiestime
                #textPropertiestime
                textPropertieslist = ['satellite_snr_list', 'satellite_prn_list', 'satellite_azimuth_list', 'satellite_elevation_list', 'wifi_list']
                for item in textPropertieslist:
                    if content['data']['textProperties'].get(item) != None:
                        textPropertiestime[item] = stamp_to_local_time(content['data']['textProperties'][item]['startTime'])
                    else:
                        textPropertiestime = '                   '
                result['textPropertiestime'] = textPropertiestime
                for k, v in result.items():
                    print ('{}: {}\n'.format(k, v))
                print ('===================================================')

if __name__ == '__main__':
    get_properties_time(logFile)





