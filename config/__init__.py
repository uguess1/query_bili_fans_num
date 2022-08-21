import collections

# 数据存储路径
DATAPATH = "datarem.json"

# 日志存储路径
LOG = "log.txt"

# 默认json写入数据
DEFAULT_JSON = {
    "fans_num": {"33605910": ["啵啵小狗341", 0]},
    "currchoose": "33605910",
    "remvid": ["33605910"],
}

# 可视化数据路径
VISUALDATAPATH = "visualdata.json"

# 默认可视化写入数据
DEFAULT_VISUAL_JSON = collections.OrderedDict()

# 时间格式
FORMAT_TIME="%Y-%m-%d %H:%M"

HELPTEXT = """
<html><head/><body><p><span style=" font-family:'宋体','monospace'; font-size:12pt; font-weight:600; color:#000000;">主页面</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#067d17;"><br/></span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">UID:  </span>
<span style=" font-family:'宋体','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">输入用户</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">UID</span>
<span style=" font-family:'宋体','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">可以查询用户的粉丝数。</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; font-weight:600; color:#000000;"><br/>#1:   </span>
<span style=" font-family:'宋体','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">输入该指令会弹出存储用户页面。</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#000000;"><br/></span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">…………</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#000000;"><br/></span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#ff0000;">&lt; </span>
<span style=" font-family:'宋体','monospace'; font-size:9.8pt; color:#ff0000;">听说还有一些以</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#ff0000;">#</span>
<span style=" font-family:'宋体','monospace'; font-size:9.8pt; color:#ff0000;">开头的彩蛋指令</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#ff0000;"> &gt;</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#067d17;"><br/><br/><br/></span>
<span style=" font-family:'宋体','monospace'; font-size:12pt; font-weight:600; color:#000000;">存储用户页面</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#000000;"><br/></span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">UID:  </span>
<span style=" font-family:'宋体','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">输入用户</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">UID</span>
<span style=" font-family:'宋体','monospace'; font-size:9.8pt; font-weight:600; color:#000000;">可以存储用户。</span>
<span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; font-weight:600; color:#000000;"><br/>…………</span></p></body></html>
"""
