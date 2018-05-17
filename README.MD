# invpy
## A financial data scrape project
## 一、 功能介绍：<br>
  本项目利用网络爬虫技术爬取Investing.com网站的相关金融数据。<br>
  Investing.com 网站提供了种类非常丰富的金融资产数据，包括股票、债券、外汇以及各种商品及衍生品的数据（包括各种加密货币）。使用时可以尝试搜索自己感兴趣的关键词，然后根据返回结果选择正确的选项。<br>
  Investing.com 网站还提供了约30个国家和地区的语言搜索，搜索时可以通过修改getpairID函数的source参数来切换数据来源网站。
  **(注意：搜索的关键词必须于source匹配，否则大概率不会返回任何结果。例如在默认source下搜索中文关键词将没有返回内容)**<br>
  项目包括两个函数getpairID以及gethistData，下面对两个函数做简单介绍。<br>
### 1. getpairID(keyword,source='www')
  主要用于数据的搜索和匹配，接受两个参数，分别是：keyword和source。<br>
  keyword：搜索的关键词，程序会以列表的形式展示所有可能与关键词匹配的项目，用户可以根据返回列表记录自己需要项目的symbol或者name。<br>
  source：对应语言的investing.com 网站，默认为美国。用户可以选取Investing.com网站提供的所有语言版本作为数据来源，例如'cn' 代表中国。<br>
  目前支持以下区域语言的搜索：<br>
  <br>
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
   <br>
### 2. gethistData(keyword,start,end,interval = 'Daily',source='www')<br>
  本函数返回pandas.DataFrame 形式的数据。首先调用getpairID用来匹配关键词，然后根据用户的输入选择返回数据，默认返回匹配的第一项。<br>
  start，end为数据起始日期。默认格式为'YYYY/MM/DD'，暂时不接受其他形式。<br>
  interval 为数据时间间隔，可选选项为：Daily，Weekly，Monthly。<br>
  经测试中国的股票数据，investing.com网站提供的数据为**不复权**数据，数据大概从2012或2013年开始。

## 二、免责声明<br>
  **本项目与Investing.com网站没有任何利益关系，仅供交流学习使用，不保证项目数据的准确性，也不对基于数据做出的任何投资决策负责。数据所有权归Investing.com网站所有，如有侵权，请联系我删除。**
