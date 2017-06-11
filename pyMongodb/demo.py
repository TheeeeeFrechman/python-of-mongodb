#!/usr/bin/python
# -*- coding: utf-8 -*-  

'''
本demo以QQ上下线为例，说明pyDAStorage系列接口使用方法。
'''

import time, ctypes, sys
#加载python端入库模块路径
sys.path.append('/CySec_H008/pylib')

#from pyDAStorage import storage, opcode
import pyDAStorage
import storage, opcode

if __name__ == '__main__':

    # 11:22:33:44:55为数据包中mac地址, 时间以32为整型存储
    data = {'USERNAME': '99999999', 'TERMINAL_TYPE': '02', 'ACTION': '02', 'EQUIPMENT_ID': 'asdf23e32wf21212s', 'SRC_IP': 12312312,
            'DST_IP': 342423212, 'MAC': '11:22:33:44:55', 'CAPTURE_TIME': ctypes.c_int32(int(time.time())).value,
            'SRC_PORT': 23232, 'DST_PORT': 8000, 'COLLECT_PLACE': '111'}

    #获取认证账号
    tag, auth_type, auth, mac = storage.DA_IP2Auth(data['SRC_IP'], data['SRC_PORT'], data['MAC'])
    data['MAC'] = mac
    data['AUTH_TYPE'] = auth_type
    data['AUTH_ACCOUNT'] = auth

    #采集数据中不含有地理信息时，使用以下代码：
    #获取地理信息
    tag, x, y, street, gis_capture_time = storage.DA_Auth2GIS(auth);
    if tag == opcode.DO_SUCCESS:
        if x != 0:
            data['LONGITUDE'] = x
        if y != 0:
            data['LATITUDE'] = y
        if street is not None:
            data['DETAIL_ADDRESS'] = street
        if gis_capture_time != 0:
            data['GIS_CAPTURE_TIME'] = gis_capture_time

    #如果采集数据含中有地理信息，使用以下代码
    #更新地理信
    #tag = storage.DA_UpdateGIS(auth, x, y, street, gis_capture_time);
    print storage.DAInsert('TQQIndividual', data, storage.DEVICE_TYPE.DEVICE_SYS)
    
    DAQuery('TAccountTrace', {'NOTIFY': True}, None, {'APPTYPE': 1, 'APPNAME': 1, 'ACCOUNT': 1, 'TOOLS': 1, 'ADDRESS': 1}, 0, 0, DEVICE_TYPE.DEVICE_SYS)
