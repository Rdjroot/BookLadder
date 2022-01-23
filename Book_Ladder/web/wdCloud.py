# -*- coding = utf-8 -*-
# @Time:2021/3/1915:58
# @Author:Linyu
# @Software:PyCharm
from web.models import Modle
import jieba
import cv2
from matplotlib import colors
from wordcloud import WordCloud


def infoCloud(title):
    title = "'"+title+"'"
    sql = 'select intro,comment1,comment2,comment3 from corebook where title = %s'%(title)
    data = Modle().query(sql)
    text = ""
    for item in data:
        for it in item:
            text= text+ it
    #分词
    cut = jieba.lcut(text)
    # print(cut)
    strings = ' '.join(cut)

    color_list=['#CD853F','#DC143C','#00FF7F','#FF6347','#8B008B','#00FFFF','#0000FF','#8B0000','#FF8C00',
                '#1E90FF','#00FF00','#FFD700','#008080','#008B8B','#8A2BE2','#228B22','#FA8072','#808080']
    colormap=colors.ListedColormap(color_list)
    #设置图片属性
    img_mask = cv2.imread('web/static/icon/book.png')
    # img_array = np.array(img)
    wc = WordCloud(
        background_color='white',
        colormap = colormap,
        scale=20,
        mask=img_mask,
        font_path="STXINWEI.TTF",
        width = 400,
        height = 300,
    )
    wcCloud = wc.generate(strings)


    #添加新的存储图片
    sqlNum = 'select id_num from corebook where title = %s'%(title)
    id_num = Modle().query(sqlNum)
    num = str(id_num[0][0])
    id_str = 'web/static/icon/'+ num +'.png'

    wcCloud.to_file(id_str)
    #

    #绘制图片
    # fig = plt.figure(1)
    # plt.imshow(wc)
    # plt.axis('off')

    # plt.show()


