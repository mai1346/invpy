# invpy
A financial data scrape project(just for fun)
一、 本项目利用网络爬虫技术爬取Investing.com网站的相关金融数据。包括两个函数getpairID以及gethistData。
  1. getpairID(keyword,source='www')
       主要用于数据的搜索和匹配，接受两个参数，分别是：keyword和source。
       keyword：搜索的关键词，程序会以列表的形式展示所有可能与关键词匹配的项目，用户可以根据返回列表记录自己需要项目的symbol或者name。
       source：对应语言的investing.com 网站，默认为美国。用户可以选取Investing.com网站提供的所有语言版本作为数据来源，例如'cn' 代表中国。
       目前支持以下区域语言的搜索：
        (1)	www.investing.com
        (2)	il.investing.com
        (3)	sa.investing.com
        (4)	es.investing.com
        (5)	fr.investing.com
        (6)	cn.investing.com
        (7)	ru.investing.com
        (8)	de.investing.com
        (9)	it.investing.com
        (10)	tr.investing.com
        (11)	jp.investing.com
        (12)	br.investing.com
        (13)	se.investing.com
        (14)	gr.investing.com
        (15)	pl.investing.com
        (16)	nl.investing.com
        (17)	fi.investing.com
        (18)	kr.investing.com
        (19)	mx.investing.com
        (20)	pt.investing.com
        (21)	uk.investing.com
        (22)	vn.investing.com
        (23)	th.investing.com
        (24)	id.investing.com
        (25)	hk.investing.com
        (26)	in.investing.com
        (27)	ms.investing.com
        (28)	ca.investing.com
        (29)	au.investing.com
        (30)	za.investing.com
  2. gethistData(keyword,start,end,interval = 'Daily',source='www')
        本函数返回pandas.DataFrame 形式的数据。首先调用getpairID用来匹配关键词，然后根据用户的输入选择返回数据，默认返回匹配的第一项。
        start，end 为数据起始日期。默认格式为'YYYY/MM/DD',暂时不接受其他形式。

