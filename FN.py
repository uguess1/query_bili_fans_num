import sys


from PyQt5.QtCore import QFileInfo, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMessageBox

from spider import *
from UI_choose import *
from UI_help import *
from UI_main import *
from UI_visual import *
from visual_function.line_chart import Line_Chart


@logger.catch()
def init_file():
    """
    文件初始化
    """
    # 日志
    logger.add(LOG)
    # 数据
    if not os.path.exists(DATAPATH):
        initdict = DEFAULT_JSON
        with open(DATAPATH, "w+") as f:
            f.write(json.dumps(initdict))
    # 可视化
    if not os.path.exists(VISUALDATAPATH):
        initdict = DEFAULT_VISUAL_JSON
        with open(VISUALDATAPATH, "w+") as f:
            f.write(json.dumps(initdict))


# 主页面
class Mainpage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, spider):
        super(Mainpage, self).__init__()
        self.setupUi(self)
        # 爬虫
        self.spider = spider
        self._bind_contrl()

    def _bind_contrl(self):
        """
        按钮绑定
        """
        self.refresh_Button.clicked.connect(self._clicked_refresh_button)
        self.help_Button.clicked.connect(self._clicked_help_button)

    # 刷新
    def _clicked_refresh_button(self):
        try:
            gets = self.query_line_edit.text()
            if gets == "":
                self.__query_and_set()
            # 启动菜单
            elif gets == "#1":
                choose_page.show()
            elif gets.isdigit():
                self.spider.set_vmid(gets)
                self.__query_and_set()
            else:
                QMessageBox.critical(self, "错误", "输入错误！")
        except Exception as e:
            logger.error("刷新功能函数出错:{}".format(e.args))

    # 查询主函数
    @logger.catch()
    def __query_and_set(self):
        """
        完成查询粉丝数，显示各项数据，并存储的功能
        """
        if self.spider.get_vmid() == "":
            QMessageBox.critical(self, "错误", "未选择查询用户！")
        else:
            res_code = self.spider.get_fans()
            if res_code == 0:
                self.label_fansnum.setText(str(self.spider.get_fans_num()))
                rem_data = get_data(DATAPATH, DEFAULT_JSON)
                ever_fans_num = (
                    -1
                    if self.spider.get_vmid() not in rem_data["fans_num"]
                    else rem_data["fans_num"][self.spider.get_vmid()][1]
                )
                if ever_fans_num != -1:
                    self.label_change.setText(
                        "距离上次刷新变化:  {}".format(
                            self.spider.get_fans_num() - ever_fans_num
                        )
                    )
                else:
                    self.label_change.setText("距离上次刷新变化:  0")
                set_rem_fans_num(
                    DATAPATH,
                    rem_data,
                    self.spider.get_vmid(),
                    self.spider.get_username(),
                    self.spider.get_fans_num(),
                )
                set_rem_visual_num(
                    VISUALDATAPATH, self.spider.get_vmid(), self.spider.get_fans_num()
                )
            else:
                QMessageBox.critical(self, "错误", "请输入正确的uid！")

    def _clicked_help_button(self):
        help_page.show()

    @logger.catch()
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        重写关闭函数，实现关闭主页面同时关闭所有打开页面
        """
        # reply = QMessageBox.question(self, '提示',
        #                              "是否要关闭所有窗口?",
        #                              QMessageBox.Yes | QMessageBox.No,
        #                              QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     event.accept()
        #     sys.exit(0)  # 退出程序
        # else:
        #     event.ignore()
        event.accept()
        sys.exit(0)  # 退出程序

    @logger.catch()
    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.label_fansnum.setText(str(self.spider.get_fans_num()))
        self.label_change.setText(self.spider.get_change())
        self.show()


# 选择页面
class Choosepage(QtWidgets.QMainWindow, Ui_ChooseWindow):
    def __init__(self, spider):
        super(Choosepage, self).__init__()
        self.setupUi(self)
        self.spider = spider
        self.visual_path_list = set()
        self.data_clean_dict = {
            "15分钟": 15 * 60,
            "30分钟": 30 * 60,
            "1小时": 3600,
            "2小时": 2 * 3600,
            "6小时": 6 * 3600,
            "12小时": 12 * 3600,
            "1天": 24 * 3600,
            "2天": 48 * 3600,
            "3天": 72 * 3600,
            "15天": 15 * 86400,
            "1月": 30 * 86400,
        }
        self.data_clean_choose.addItems(list(self.data_clean_dict.keys()))
        self._bind_contrl()

    def _bind_contrl(self):
        self.add_button.clicked.connect(self._add)
        self.delete_button.clicked.connect(self._delete)
        self.visual_smooth_line_button.clicked.connect(self._generate_smooth_line_chart)
        self.data_clean_button.clicked.connect(self._data_clean)

    def _add(self):
        try:
            gets = self.add_line_edit.text().strip()
            res_code = self.spider.get_fans(gets)
            if gets != "" and res_code == 0:
                if gets not in self.items_set:
                    index = my_bisect(self.items_list, gets)
                    self.listWidget.insertItem(
                        index,
                        # \u3000全角空格，\t要与汉字对齐需要全角空格
                        "{0:\u3000<10}\t({1})".format(self.spider.get_username(), gets),
                    )
                    self.items_list.insert(index, gets)
                    self.items_set.add(gets)
                    set_rem_fans_num(
                        DATAPATH,
                        get_data(DATAPATH, DEFAULT_JSON),
                        gets,
                        self.spider.get_username(),
                        self.spider.get_fans_num(),
                    )
                    set_rem_visual_num(
                        VISUALDATAPATH, gets, self.spider.get_fans_num(),
                    )
                else:
                    QMessageBox.warning(self, "消息", "该uid已存在,请勿重复添加！")
            else:
                QMessageBox.warning(self, "错误", "不存在该uid用户！")
        except Exception as e:
            logger.error(
                "添加功能函数出错:{0},输入为:{1}".format(e.args, self.add_line_edit.text())
            )

    def _delete(self):
        try:
            if self.listWidget.count() == 0:
                QMessageBox.warning(self, "错误", "列表为空！")
                return
            delItem = self.listWidget.currentItem()
            curr_rows = self.listWidget.row(delItem)

            # 有选中的项目
            if curr_rows >= 0:
                self.listWidget.takeItem(curr_rows)

                # 删除用户存储
                content = get_data(DATAPATH, DEFAULT_JSON)
                del content["fans_num"][self.items_list[curr_rows]]
                set_data(DATAPATH, content)

                # 删除可视化数据
                try:
                    content_visual = get_data(VISUALDATAPATH, DEFAULT_VISUAL_JSON)
                    del content_visual[self.items_list[curr_rows]]
                    set_data(VISUALDATAPATH, content_visual)
                except:
                    logger.error('删除可视化数据时出错！')

                self.items_set.remove(self.items_list[curr_rows])
                del self.items_list[curr_rows]
                if self.listWidget.count() > 0:
                    self.listWidget.setCurrentRow(
                        min(curr_rows, self.listWidget.count() - 1)
                    )
            else:
                QMessageBox.warning(self, "错误", "未选择删除对象！")
        except Exception as e:
            logger.error(
                "删除功能函数出错:{0},列表为:{1},选择的为:{2}".format(
                    e.args, self.items_list, self.listWidget.currentItem().text()
                )
            )

    def _generate_smooth_line_chart(self):
        currItem = self.listWidget.currentItem()
        currRow = self.listWidget.row(currItem)
        if currRow >= 0:
            mid = self.items_list[currRow]
            content = get_data(DATAPATH, DEFAULT_JSON)
            name = content["fans_num"][mid][0]
            smooth = True
            Line_Chart(mid, name, VISUALDATAPATH, smooth)
            # print("生成用户 " + name + " 的平滑折线图成功！")
            visual_page.set_show_item(name + "_line_chart.html")
            visual_page.show()
            self.visual_path_list.add(name + "_line_chart.html")
        else:
            QMessageBox.warning(self, "错误", "未选择要生成粉丝数平滑折线图的对象！")

    def _data_clean(self):
        reply = QMessageBox.warning(
            self,
            "警告",
            "警告！该选项会导致选中用户存储的可视化数据被调整为上诉选择栏所选择的时间间隔，该操作不可逆！\n是否继续？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            currItem = self.listWidget.currentItem()
            curr_rows = self.listWidget.row(currItem)

            # 得到选项
            interval_choose = self.data_clean_choose.currentText()
            interval_time = self.data_clean_dict[interval_choose]

            # 有选中的项目
            if curr_rows >= 0:
                content_visual = get_data(VISUALDATAPATH, DEFAULT_VISUAL_JSON)
                tmpdict = collections.OrderedDict()
                visualdict = content_visual[self.items_list[curr_rows]]
                f = visualdict.popitem()
                ftime = time.mktime(time.strptime(f[0], FORMAT_TIME))
                while visualdict:
                    tmp = visualdict.popitem()
                    tmptime = time.mktime(time.strptime(tmp[0], FORMAT_TIME))
                    if ftime - tmptime > interval_time:
                        tmpdict[f[0]] = f[1]
                        f = tmp
                        ftime = time.mktime(time.strptime(f[0], FORMAT_TIME))
                tmpdict[f[0]] = f[1]
                content_visual[self.items_list[curr_rows]] = collections.OrderedDict(
                    reversed(tmpdict.items())
                )
                set_data(VISUALDATAPATH, content_visual)
                QMessageBox.information(self, "提示", "间隔更新完毕！")
            else:
                QMessageBox.warning(self, "错误", "未选择对象！")

    @logger.catch()
    def __get_all_items(self):
        data = get_data(DATAPATH, DEFAULT_JSON)
        item_list = data["remvid"]
        item_show = [
            "{0:\u3000<10}\t({1})".format(data["fans_num"][i][0], i) for i in item_list
        ]
        return item_list, item_show

    @logger.catch()
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        event.accept()
        content = get_data(DATAPATH, DEFAULT_JSON)
        content["remvid"] = self.items_list
        tmp_curr_choose = self.listWidget.currentItem()
        content["currchoose"] = (
            self.items_list[self.listWidget.row(tmp_curr_choose)]
            if tmp_curr_choose
            else ""
        )
        self.spider.set_vmid(content["currchoose"])
        with open(DATAPATH, "w+") as f:
            content = json.dumps(content)
            f.write(content)
        main_page.query_line_edit.setText("")

        # 删除生成的可视化文件
        for p in self.visual_path_list:
            os.remove(p)
        self.close()

    @logger.catch()
    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.items_list, tmp_items_show = self.__get_all_items()
        self.items_set = set(self.items_list)
        self.listWidget.clear()
        self.listWidget.addItems(tmp_items_show)
        self.show()


class Helppage(QtWidgets.QMainWindow, Ui_HelpWindow):
    def __init__(self):
        super(Helppage, self).__init__()
        self.setupUi(self)
        self.helpBrowser.setText(HELPTEXT)


class Visualpage(QtWidgets.QMainWindow, Ui_Visual):
    def __init__(self):
        super(Visualpage, self).__init__()
        self.setupUi(self)
        self.browser = QWebEngineView()

    def set_show_item(self, file_path):
        self.browser.load(QUrl(QFileInfo(file_path).absoluteFilePath()))
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    try:
        init_file()

        spider = Crawler()

        # 自适应高分辨率
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

        # 实例化一个对象
        app = QtWidgets.QApplication(sys.argv)

        # 主页面
        main_page = Mainpage(spider)

        # 禁止窗口缩放
        main_page.setFixedSize(main_page.width(), main_page.height())

        # 查询页面声明
        choose_page = Choosepage(spider)

        # 禁止窗口缩放
        choose_page.setFixedSize(choose_page.width(), choose_page.height())

        # 帮助页面声明
        help_page = Helppage()

        # 禁止窗口缩放
        help_page.setFixedSize(help_page.width(), help_page.height())

        # 可视化页面声明
        visual_page = Visualpage()

        # # 禁止窗口缩放
        visual_page.setFixedSize(visual_page.width(), visual_page.height())

        # 主页面显示
        main_page.show()

        # 确保主循环安全退出
        sys.exit(app.exec_())
    except Exception as e:
        logger.error("主函数出错:{}".format(e.args))
