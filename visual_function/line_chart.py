import pyecharts.options as opts
from pyecharts.charts import Line

from function import *


class Line_Chart:
    def __init__(self, mid, name, data_path, smooth=False):
        self._mid = str(mid)
        self._name = str(name)
        self._data_path = data_path
        self._smooth = smooth
        self._drawing_picture()

    def _drawing_picture(self):
        content = get_data(self._data_path, collections.OrderedDict())
        c = (
            Line(
                init_opts=opts.InitOpts(width="880px", height="500px", theme="vintage")
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="粉丝数变化"),
                yaxis_opts=opts.AxisOpts(
                    name="粉丝数", max_="dataMax", min_="dataMin", type_="log"
                ),
                xaxis_opts=opts.AxisOpts(name="时间", type_="time", is_scale=True),
                datazoom_opts=[
                    opts.DataZoomOpts(type_="inside"),
                    opts.DataZoomOpts(type_="slider"),
                ],
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
            )
            .add_xaxis(list(content[self._mid].keys()))
            .add_yaxis(
                self._name, list(content[self._mid].values()), is_smooth=self._smooth
            )
        )
        c.render(self._name + "_line_chart.html")
