#-*-coding:utf-8-*-
import os
import pdb
import urllib2

import config
from models import Student,Subject,Score,db
import requests
from bs4 import BeautifulSoup
from lxml import etree
from PIL import Image
from ZFCheckCode import recognizer, trainner

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer': 'http://jwgl1.hbnu.edu.cn/(S(nxuiogv1kq4coqvvhltax145))/default2.aspx?'
}

baseurl = 'http://jwgl1.hbnu.edu.cn'
s=requests.Session()
html = s.get(baseurl, headers=headers, allow_redirects=False )
loc = html.headers['location']
loginurl = baseurl + loc
codeu = loginurl[0:54]
codeurl = codeu + '/CheckCode.aspx?'

# 获取验证码并自动识别
def checkcode():
    img=s.get(codeurl, stream=True, headers=headers)
    with open('checkcode.gif','wb') as f:
        f.write(img.content)
    trainner.update_model() 
    code = recognizer.recognize_checkcode('checkcode.gif')
    #print(code)
    return code



def spider_login(id, passwd):
    #构造表单字典
    payload={'__VIEWSTATE':'',
        'txtUserName':'',
        'Textbox1':'',
        'TextBox2':'',
        'txtSecretCode':'',
        'RadioButtonList1':'',
        'Button1':'',
        'lbLanguage':'',
        'hidPdrs':'',
        'hidsc':'',
        '__EVENTVALIDATION':'',
        }
    
    #获取表单字典数据
    index = s.get(loginurl, headers=headers)
    soup = BeautifulSoup(index.content,'lxml')
    value1=soup.find('input',id='__VIEWSTATE')['value']
    value2=soup.find('input',id='__EVENTVALIDATION')['value']
    payload['txtUserName']=id
    payload['TextBox2']=passwd
    code = checkcode()
    payload['txtSecretCode']= code
    payload['RadioButtonList1']=u"学生".encode('gb2312','replace')
    payload['__VIEWSTATE']=value1       
    payload['__EVENTVALIDATION']=value2 
    payload['RadioButtonList1']= '%D1%A7%C9%FA' 

    loginresponse = s.post(loginurl, data=payload, headers=headers)
    content = loginresponse.content.decode('gb2312')
    soup = BeautifulSoup(content, 'lxml')
    uname=soup.find('span', id='xhxm')
    xsxm =  uname.text

    # 返回学生姓名
    return xsxm




def getgrades(id, name):

    payload1={'__VIEWSTATE':'',
          'ddlXN':'', 
          'ddlXQ':'' ,
          'Button1':'',
          '__EVENTVALIDATION':'',

}
    #url2 = spider_login(id, passwd)
    name = name[0:9]
    cname = urllib2.quote(name.encode('gb2312'))
    xingming = urllib2.quote(cname) 

    req_url = codeu + '/xscj_gc.aspx?xh=' + str(id) + '&xm=' + xingming + '&gnmkdm=N121603'
    req2 = s.get(req_url, headers=headers)

    soup = BeautifulSoup(req2.content,'lxml')
    value3=soup.find('input',id='__VIEWSTATE')['value']
    value4=soup.find('input',id='__EVENTVALIDATION')['value']
    payload1['__VIEWSTATE']=value3
    payload1['__EVENTVALIDATION']=value4
    pos = s.post(req_url, data=payload1, headers=headers)
    grades = pos.content.decode('gbk')
    
    return grades


def getxskbcx(id,name):
    
    payload2={'__EVENTTARGET':'xqd',
              '__EVENTARGUMENT':'',
              '__LASTFOCUS':'',
              '__VIEWSTATE':'',
              'xnd':'',
              'xqd':'',
              '__EVENTVALIDATION':''
}
    name = name[0:9]
    cname = urllib2.quote(name.encode('gb2312'))
    xingming = urllib2.quote(cname) 

    kbcx_url = codeu + '/xskbcx.aspx?xh='+str(id)+'&xm='+xingming+'&gnmkdm=N121603' 
    kbcx = s.get(kbcx_url,headers = headers)

    soup_kb = BeautifulSoup(kbcx.content,'lxml')
    value5 = soup_kb.find('input',id='__VIEWSTATE')['value']
    value6 = soup_kb.find('input',id='__EVENTVALIDATION')['value']

    payload2['__VIEWSTATE'] = value5
    payload2['xnd'] = '2017-2018'
    payload2['xqd'] = '1'
    payload2['__EVENTVALIDATION'] = value6

    kbcx_response = s.post(kbcx_url,data = payload2,headers = headers)
    html2 = kbcx_response.content.decode('gbk')
    
    return html2


def parser(id, grades):
    
    # 根据HTML网页字符串创建BeautifulSoup
    soup = BeautifulSoup(
        grades,  # HTML文档字符串
        'html.parser',  # HTML解析器
    )

    tables = soup.findAll('table')
    #filename = '/home/cris/system/flask/templates/score/'+ str(id) +'.html'
    #filename = '/home/fty/new-system/templates/score/'+ id +'.html'
    #with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    tab = tables[0]
        #list = [6, 10, 14, 16]
      
    for tr in tab.findAll('tr'):            
        for td in tr.findAll('td'):
        
 


def parsers(id,html2):

    soup_kbcx =BeautifulSoup(html2,'html.parser')
    html_data2 = soup_kbcx.find_all('table',class_='blacktab')
    filenames = '/home/cris/system/flask/templates/xskb/'+str(id)+'.html'
    with open(filenames,'w') as f:
        for tab in html_data2:
            f.write("{% extends 'student.html' %}")
 	    f.write('\n')
            f.write("{% block page_name %}课表{% endblock %}")
            f.write('\n')
            f.write('{% block body_part2 %}')
            f.write('\n')
	    f.write('<table class="blacktab" border="0" style="border-color:Black;width:100%;">')
	    for tr in tab.find_all('tr'):
		f.write('<tr>')
                f.write('&ensp;')
                f.write('&ensp;')
		for td in tr.find_all('td'):
		    f.write('<td>')
		    f.write(td.get_text().encode('utf-8'))
		    f.write('</td>')
		f.write('</tr>')
		f.write('\n')
	    f.write('</table>')
            f.write('\n')
            f.write('{% endblock %}')




'''a = raw_input('学号：')
b = raw_input('密码：')
name = '付同永同学'
'''
# 将unicode编码编码成utf8
#getname = spider_login(a, b).encode('utf8')
# 将utf8解码成unicode
#name = name.decode('utf8')
