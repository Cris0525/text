# encoding: utf-8
import time
import sys
import shutil
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

from pyecharts import Line
def chart(lists):
    bar = Line("学生成绩平均绩点折线图")
    bar.add("平均绩点GPA", ["大一（上）", "大一（下）", "大二（上）", "大二（下）", "大三（上）", "大三（下）"], [lists[0], lists[1], lists[2], lists[3], lists[4],lists[5],lists[6]],is_more_utils=True)
    bar.show_config()
    bar.render()
    #shutil.move('/home/cris/system/flask/render.html','/home/cris/system/flask/templates/html')

    with open('/home/cris/system/flask/render.html','r') as f:
        hello = f.read()
        abc = hello

    with open('/home/cris/system/flask/templates/student.html','w') as f1:
        f1.write("{% extends 'base.html' %}")
    	f1.write('\n')
    	f1.write("{% block page_name %}你好,{{login_user}}{% endblock %}")
    	f1.write('\n')
    	f1.write("{% block body_part1 %}你好,{{login_user}}{% endblock %}")
    	f1.write('\n')
    	f1.write("{% block body_part2 %}")
    	f1.write('\n')
    	f1.write(abc)
    	f1.write('\n')
    	f1.write("{% endblock %}")




