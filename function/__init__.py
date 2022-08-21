import bisect
import json
import time

from loguru import logger

from config import *


@logger.catch()
def get_data(datapath, DEFAULTDATE):
    with open(datapath, "r+") as f:
        content = f.read()
        if not content:
            content = DEFAULTDATE
            content = json.dumps(content)
            f.write(content)
    content = json.loads(content)
    return content


@logger.catch()
def set_data(datapath, content):
    with open(datapath, "w+") as f:
        json.dump(content, f)


# 设置数据库内存储的粉丝数
@logger.catch()
def set_rem_fans_num(datapath, content, vmid, username, fansnum):
    vmid = str(vmid)
    fansnum = int(fansnum)
    if vmid not in content["fans_num"]:
        index = my_bisect(content["remvid"], vmid)
        content["remvid"].insert(index, vmid)
    content["fans_num"][vmid] = [username, fansnum]
    set_data(datapath, content)


# 向可视化数据库添加信息
@logger.catch()
def set_rem_visual_num(datapath, vmid, fansnum):
    vmid = str(vmid)
    fansnum = int(fansnum)
    now_time = time.strftime(FORMAT_TIME, time.localtime())
    content = get_data(datapath, DEFAULT_VISUAL_JSON)
    if vmid not in content:
        content[vmid] = collections.OrderedDict()
    if content[vmid]:
        tmp_time, tmp_data = content[vmid].popitem()
        if tmp_data != fansnum:
            content[vmid][tmp_time] = tmp_data
    content[vmid][now_time] = fansnum
    set_data(datapath, content)


# 求插入的位置
@logger.catch()
def my_bisect(lists, num):
    listlen = len(lists)
    numlen = len(num)
    l, r = 0, listlen
    # 求左边界
    while l < r:
        mid = r + ((l - r) >> 1)
        if len(lists[mid]) >= numlen:
            r = mid
        elif len(lists[mid]) < numlen:
            l = mid + 1
    limit_l = l
    l, r = 0, listlen
    # 求右边界
    while l < r:
        mid = r + ((l - r) >> 1)
        if len(lists[mid]) > numlen:
            r = mid
        elif len(lists[mid]) <= numlen:
            l = mid + 1
    limit_r = l
    return bisect.bisect_right(lists[limit_l:limit_r], num) + limit_l
