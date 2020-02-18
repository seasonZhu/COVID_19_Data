import pygal
import matplotlib.pyplot as plt

class Draw:
    @staticmethod
    def draw(dates, addConfirms):
        my_config = pygal.Config()
        my_config.x_label_rotation = 45
        my_config.show_legend = False

        #以下三句设置字体的语句有问题
        my_config.title_font_size = 24
        my_config.label_font_size = 14
        my_config.major_label_font_size = 18

        my_config.truncate_label = 15 # 将标签截断为15个字符
                                    # 如果将鼠标指向被截断的标签，将显示完整标签
        my_config.show_y_guides = True # 隐藏图表中的水平线（y guide lines）
        my_config.width = 1000 # 图标宽度，默认800

        hist = pygal.Bar(my_config)
        hist.title = "每日确诊数量 今日更新至{}".format(dates[-1]) 
        hist.x_labels = dates
        hist.x_title = "日期"
        hist.y_title = "确诊"
        hist.add('当日确诊数', addConfirms)
        lastDate = dates[-1].replace("/", "-")
        fileName = "Confirm of Day {}.svg".format(lastDate)
        hist.render_to_file(fileName)