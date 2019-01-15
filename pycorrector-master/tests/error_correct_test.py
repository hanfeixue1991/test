# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief:
import pycorrector

# pycorrector.set_language_model_path(path='/Users/xuming06/Documents/Data/normal_train_lm.klm')

error_sentences = [
    '橄榄的和这款哪个比较好用？味道都是一样的么？',
    '这个跟 原木纯品 那个啥区别？不是原木纸浆做的？',
    '能充几次呢？',
    '这是酸奶还是像饮料一样的奶？',
    '现在银色的K2P是MTK还是博通啊？',
    '是浓稠的还是稀薄的？',
    '这个到底有多辣？',
    'U盘有送挂绳吗',
    '果子酸吗？有烂的吗？',
    '刚下单买了一箱，需要明天到货，先问下味道如何',
    '2周岁22斤宝宝用多大的啊？',
    '请问这茶是一条装的吗',
    '有坏的果吗',
    '生产日期怎么样 新嘛',
    '插上去的时候是驱蚊液放下面的吗？',

    '服装店里的衣服各试各样',
    '这纸厚度如何？质量怎么样',
    '一但工作效率提升，需要时间在工作上也减少',
    "第一章图表示全球产龄妇女人口同计每五年增加的产龄妇女人口一值往上升。",
    "一但工作效率提升，需要时间在工作上也减少，足以照顾老人。",
    "早婚，有可能行成了「少子化」现象",
    "这样一个家庭的费用会因为工作有限而减少，所以婴而生育的数量才会减少。",
    "相反的，生太多孩子的社会要有政府多鼓励少生孩子。",
    "一年又一年的过去，产龄妇女跟着变多，但婴儿的个数却是在慢慢的下降。",
    "由图可见到产龄妇女的人数是慢慢的加倍，而婴儿的数字已然是逐渐减少。",
    '双十一下单到现在还没发货的，',

    '汽车新式在这条路上',
    '中国人工只能布局很不错',
    '想不想在来一次比赛',
    '你不觉的高兴吗',
    '权利的游戏第八季',
    '美食美事皆不可辜负，这场盛会你一定期待已久',
    '点击咨询痣疮是什么原因?咨询医师痣疮原因',
    '附睾焱的症状?要引起注意!',
    '外阴尖锐涅疣怎样治疗?-济群解析',
    '洛阳大华雅思 30天突破雅思7分',
    '男人不育少靖子症如何治疗?专业男科,烟台京城医院',
    '疝気医院那好 疝気专科百科问答',
    '成都医院治扁平苔鲜贵吗_国家2甲医院',
    '少先队员因该为老人让坐',
    '一只小鱼船浮在平净的河面上',
    '我的家乡是有明的渔米之乡',
    ' _ ,',
    '我对于宠物出租得事非常认同，因为其实很多人喜欢宠物',  # 出租的事
    '有了宠物出租地方另一方面还可以题高人类对动物的了解，因为那些专业人氏可以指导我们对于动物的习惯。',  # 题高 => 提高 专业人氏 => 专业人士
    '三个凑皮匠胜过一个诸葛亮也有道理。',  # 凑
    '还有广告业是只要桌子前面坐者工作未必产生出来好的成果。',
]
for line in error_sentences:
    print(pycorrector.corrector.detect(line))
    correct_sent = pycorrector.corrector.correct(line)
    print("original sentence:{} => correct sentence:{}".format(line, correct_sent))