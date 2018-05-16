# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:10:54 2018

@author: mai1346
"""
#%%
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import numpy as np

#%%
def getpairID(keyword,source='www'):
    ''' 
    This function helps to match the search keywords with result returned from data
        source. It picks up the very first matching result as output.Please check whether
        the returning result matches your expectation.
    Input:
        search: Search keyword. You can type  the symbol, the full name or anything
                you expect to return. As long as there is a matching from the website. 
                This function will return the first result by default.
        source: The search engine you want to use. 
                i.e: enter uk if you want search from uk.investing.com.
                Default source is U.S.
    Output:
        Related information about the search result will be printed to help you 
        check the rightness of your data.
        
        If match failed, 0 is returned to indicate a failure.
    '''
    url = 'https://%s.investing.com/search/service/search' % source

    post_data = {
        'search_text': '%s' % keyword,
        'country_id': '0',
        'tab_id': 'All',
        }   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }
    page = requests.post(url,headers=headers,data=post_data)

    try:
        pairid = re.findall(r"(?<=\{\"pair_ID\":).*?(?=,)",page.text)
        symbol = re.findall(r"(?<=,\"symbol\":\").*?(?=\",)",page.text)
        name = re.findall(r"(?<=,\"name\":\").*?(?=\",)",page.text)
        exchange = re.findall(r"(?<=,\"exchange_name_short\":\").*?(?=\",)",page.text)
        pair_type = re.findall(r"(?<=,\"pair_type_label\":\").*?(?=\",)",page.text)
        # 储存搜索结果到Dataframe，供使用者选择
        array=np.vstack((pairid,symbol,name,exchange,pair_type)).T
        df=pd.DataFrame(array,columns=['Pair_ID','Symbol','Name','Exchange','Pair_Type'])
        # 转换Unicode为中文显示
        for column in df.columns[2:]:
            df[column]=df[column].str.decode('unicode_escape')
        print ("Keyword: %s "
               "\nMatch Successful!"
               "\nGetting \"%s\" data by default." 
               "\nIf the first result didn't match your need,Please choose the right name as keyword"
               " and try it again."               
               % (keyword,df.Name[0])
               )
        print ('关键词: %s '
               '\n匹配成功!'
               '\n默认返回\"%s\"的数据。'
               "\n如果默认结果与您的需求不匹配，请用正确的名称替代关键词重新搜索。" 
               % (keyword,df.Name[0])
               )
        #调整输出格式
        pd.set_option('display.unicode.east_asian_width', True)
        pd.set_option('expand_frame_repr', False)
        print ('----------------------------------------------------\n',df)
        return pairid[0],symbol[0]
    except:
        print(u'Match Failed. Please try other keywords.(匹配失败，请尝试其他关键词)')
        return 0,0


#%%
def gethistData(keyword,start,end,interval = 'Daily',source='www'):
    '''
    This function gets and stores data in a pandas dataframe, typically with OHLC.
    Inputs:
        keyword: Search Keyword, You can type  the symbol, the full name or anything
                 you expect to return. As long as there is a matching from the website. 
                 This function will return the first result.
        start: Starting date of a time span.
        end: Ending date of a time span. Make sure that this date is later than the start.
        interval: Define the frequency of the data. The data source of this module provide
                  'Daily', 'Weekly' and 'Monthly' data.
        source: Data source you want to search from.
                There is no difference between different sources concerning the data returned.
                But it's better that your keyword is in the language matching your source, or
                it may return nothing.
    Outputs:
        A dataframe consist of OHLCV is return and the tail of this dataframe is printed to
        help check the completeness of the data.
    '''
    try:
        pairid = getpairID(keyword,source)[0]   
        url = 'https://cn.investing.com/instruments/HistoricalDataAjax'
        post_data = {
            'curr_id': '%s' % pairid,
            'st_date': '%s' % start,
            'end_date': '%s'% end,
            'interval_sec': '%s' % interval,
            'sort_col': 'date',
            'sort_ord': 'DESC',
            'action': 'historical_data'
            }   
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        if pairid != 0:
            page = requests.post(url,headers=headers,data=post_data)
            soup = BeautifulSoup(page.text,'html.parser')
        
            tab = soup.table
            cols = [th.attrs['data-col-name'] for th in tab.findAll('th')[:-1]]
            rows = []
            for tr in tab.findAll('tr')[1:]:
                row = []
                for td in tr.findAll('td')[:-1]:  
                    row.append(td.attrs['data-real-value'])
                rows.append(row)
            df1 = pd.DataFrame(rows,columns=cols)
            df1.date=pd.to_datetime(df1['date'],unit='s')
            df1.set_index('date',inplace= True)
            df1.rename(columns={'price':'close'}, inplace= True)
        #    locale.setlocale(locale.LC_NUMERIC, '')
        #    df1=df1.applymap(atof)
            df1 = df1.applymap(lambda x: x.replace(',', '')).astype('float64')
            print ('----------------------------------------------------'
                   '\nPrinting data tail.'
                   '\n打印数据末尾。')
            print ('----------------------------------------------------\n',
                   df1.tail(10))
            return df1
    except AssertionError:
        print ("The data source didn't return any related data, "
               "please try changing the time range."
               "\n没有相应的数据,请尝试更改数据时间范围。"
              )  


#%%
if __name__=='__main__':
    
    hs300 = gethistData('apple','2018/04/01','2018/05/10',source='de')
