

from urllib import parse, request
import random
from lxml import etree
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
    ]


def getPlayedData():
    url = "http://www.dotamax.com/hero/played/?skill=vh&ladder=y"
    user_agent = random.choice(ua_list)
    headers = {
        "User-Agent": user_agent
    }
    req = request.Request(url, headers=headers)   
    resp = request.urlopen(req)
    html_data = resp.read()

    html = etree.HTML(html_data)
#    li_list_html = html.xpath('//span[@class="hero-name-list"]')
    li_list_html = html.xpath('//tr')
    data_list=[]
    columns_name=['英雄','使用次数','胜率']
    for li in li_list_html:
        hero_name = li.xpath('.//span[@class="hero-name-list"]/text()')
        if not hero_name:
            hero_name = None
        else:
            hero_name = hero_name[0]
        
        use_count=li.xpath('.//td[@style="width: 30%"]//div[@style="height: 10px"]/text()')
        if not use_count:
            use_count = None
        else:
            use_count = use_count[0]
            use_count=use_count.replace(',','')
            use_count=int(use_count)
        
        win_rate=li.xpath('.//td[@style="width: 40%"]//div[@style="height: 10px"]/text()')
        if not win_rate:
            win_rate = None
        else:
            win_rate = win_rate[0]
            win_rate=win_rate.replace('%','')
            win_rate=win_rate.replace('.','')
            win_rate=float(win_rate)/100
        
        data_list.append([hero_name,use_count,win_rate])
    array=np.array(data_list)
    data_df=pd.DataFrame(data=array,columns=columns_name)
    data_df.to_excel("./PlayedData.xlsx",encoding="utf-8")            
    
        
def getGpmData():
    url="http://www.dotamax.com/hero/gpm/?skill=vh&ladder=y"        
    user_agent = random.choice(ua_list)
    headers = {
        "User-Agent": user_agent
    }
    req = request.Request(url, headers=headers)   
    resp = request.urlopen(req)
    html_data = resp.read()

    html = etree.HTML(html_data)
#    li_list_html = html.xpath('//span[@class="hero-name-list"]')
    li_list_html = html.xpath('//tr')
    data_list=[]
    columns_name=['英雄','经济/分钟','经验/分钟']
    for li in li_list_html:
        hero_name = li.xpath('.//span[@class="hero-name-list"]/text()')
        if not hero_name:
            hero_name = None
        else:
            hero_name = hero_name[0]
        
        hero_gpm=li.xpath('.//td[@style="width: 30%"]//div[@style="height: 10px"]/text()')
        if not hero_gpm:
            hero_gpm = None
        else:
            hero_gpm = hero_gpm[0]
            hero_gpm=hero_gpm.replace('.','')
            hero_gpm=int(hero_gpm)/100
        
        hero_xpm=li.xpath('.//td[@style="width: 40%"]//div[@style="height: 10px"]/text()')
        if not hero_xpm:
            hero_xpm = None
        else:
            hero_xpm = hero_xpm[0]
            hero_xpm=hero_xpm.replace('.','')
            hero_xpm=int(hero_xpm)/100
        data_list.append([hero_name,hero_gpm,hero_xpm])
    array=np.array(data_list)
    data_df=pd.DataFrame(data=array,columns=columns_name)
    data_df.to_excel("./GpmData.xlsx",encoding="utf-8") 
        
        
def getKdaData():
    url="http://www.dotamax.com/hero/kda/?skill=vh&ladder=y"
    user_agent = random.choice(ua_list)
    headers = {
        "User-Agent": user_agent
    }
    req = request.Request(url, headers=headers)   
    resp = request.urlopen(req)
    html_data = resp.read()

    html = etree.HTML(html_data)
    li_list_html = html.xpath('//tr')
    data_list=[]
    columns_name=['英雄','KDA','击杀','死亡','助攻']
    for li in li_list_html:
        hero_name = li.xpath('.//span[@class="hero-name-list"]/text()')
        if not hero_name:
            hero_name = None
        else:
            hero_name = hero_name[0]
        
        hero_kda=li.xpath('.//td[@style="width: 25%"]//div[@style="height: 10px"]/text()')
        if not hero_kda:
            hero_kda = None
        else:
            hero_kda = hero_kda[0]
            hero_kda=hero_kda.replace('.','')
            hero_kda=float(hero_kda)/100
        
        hero_kill=li.xpath('.//td[@style="width: 16.5%"]//div[@style="height: 10px"]/text()')
        if not hero_kill:
            hero_kill = None
        else:
            hero_die=hero_kill[1]
            hero_die=hero_die.replace('.','')
            hero_die=float(hero_die)/100
            hero_assist=hero_kill[2]
            hero_assist=hero_assist.replace('.','')
            hero_assist=float(hero_assist)/100
            hero_kill = hero_kill[0]
            hero_kill=hero_kill.replace('.','')
            hero_kill=float(hero_kill)/100
        data_list.append([hero_name,hero_kda,hero_kill,hero_die,hero_assist])
    array=np.array(data_list)
    data_df=pd.DataFrame(data=array,columns=columns_name)
    data_df.to_excel("./KdaData.xlsx",encoding="utf-8") 
            

def getCsData():
    url="http://www.dotamax.com/hero/cs/?skill=vh&ladder=y"
    user_agent = random.choice(ua_list)
    headers = {
        "User-Agent": user_agent
    }
    req = request.Request(url, headers=headers)   
    resp = request.urlopen(req)
    html_data = resp.read()

    html = etree.HTML(html_data)
    li_list_html = html.xpath('//tr')
    data_list=[]
    columns_name=['英雄','正补/10分钟','反补总数']
    for li in li_list_html:
        hero_name = li.xpath('.//span[@class="hero-name-list"]/text()')
        if not hero_name:
            hero_name = None
        else:
            hero_name = hero_name[0]
            
        last_hit=li.xpath('.//td[@style="width: 30%"]//div[@style="height: 10px"]/text()')
        if not last_hit:
            last_hit=None
        else:
            last_hit=last_hit[0]
            last_hit=last_hit.replace('.','')
            last_hit=int(last_hit)/100
        
        deny=li.xpath('.//td[@style="width: 40%"]//div[@style="height: 10px"]/text()')
        if not deny:
            deny=None
        else:
            deny=deny[0]
            deny=deny.replace('.','')
            deny=int(deny)/100
        data_list.append([hero_name,last_hit,deny])
    array=np.array(data_list)
    data_df=pd.DataFrame(data=array,columns=columns_name)
    data_df.to_excel("./CsData.xlsx",encoding="utf-8") 
    
def getDmgData():
    url="http://www.dotamax.com/hero/dmg/?skill=vh&ladder=y"
    user_agent = random.choice(ua_list)
    headers = {
        "User-Agent": user_agent
    }
    req = request.Request(url, headers=headers)   
    resp = request.urlopen(req)
    html_data = resp.read()

    html = etree.HTML(html_data)
    li_list_html = html.xpath('//tr')
    data_list=[]
    columns_name=['英雄','伤害/分钟','治疗/分钟','建筑伤害/分钟']
    for li in li_list_html:
        hero_name = li.xpath('.//span[@class="hero-name-list"]/text()')
        if not hero_name:
            hero_name = None
        else:
            hero_name = hero_name[0]
            
        dps=li.xpath('.//td[@style="width: 25%"]//div[@style="height: 10px"]/text()')
        if not dps:
            dps = None
        else:
            hps=dps[1]
            hps=hps.replace('.','')
            hps=float(hps)/100
            cdps=dps[2]
            cdps=cdps.replace('.','')
            cdps=float(cdps)/100
            dps = dps[0]
            dps=dps.replace('.','')
            dps=float(dps)/100
        data_list.append([hero_name,dps,hps,cdps])
    array=np.array(data_list)
    data_df=pd.DataFrame(data=array,columns=columns_name)
    data_df.to_excel("./DmgData.xlsx",encoding="utf-8") 
    
    
    
    

getDmgData()
    
    
    
    
    
    
    
    