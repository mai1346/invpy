# invpy
# A financial data scrape project(just for fun)
## һ�� ���ܽ��ܣ�<br>
  ����Ŀ�����������漼����ȡInvesting.com��վ����ؽ������ݡ�������������getpairID�Լ�gethistData
### 1. getpairID(keyword,source='www')
  ��Ҫ�������ݵ�������ƥ�䣬���������������ֱ��ǣ�keyword��source��<br>
  keyword�������Ĺؼ��ʣ���������б�����ʽչʾ���п�����ؼ���ƥ�����Ŀ���û����Ը��ݷ����б���¼�Լ���Ҫ��Ŀ��symbol����name��<br>
  source����Ӧ���Ե�investing.com ��վ��Ĭ��Ϊ�������û�����ѡȡInvesting.com��վ�ṩ���������԰汾��Ϊ������Դ������'cn' �����й���<br>
  Ŀǰ֧�������������Ե�������<br>
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
  ����������pandas.DataFrame ��ʽ�����ݡ����ȵ���getpairID����ƥ��ؼ��ʣ�Ȼ������û�������ѡ�񷵻����ݣ�Ĭ�Ϸ���ƥ��ĵ�һ�<br>
  start��endΪ������ʼ���ڡ�Ĭ�ϸ�ʽΪ'YYYY/MM/DD'����ʱ������������ʽ��<br>
  interval Ϊ����ʱ��������ѡѡ��Ϊ��Daily��Weekly��Monthly��<br>
  �������й��Ĺ�Ʊ���ݣ�investing.com��վ�ṩ������Ϊ**����Ȩ**���ݣ����ݴ�Ŵ�2012��2013�꿪ʼ��

## ������������<br>
  **����Ŀ��������ѧϰʹ�ã�����֤��Ŀ���ݵ�׼ȷ�ԣ�Ҳ���Ի��������������κ�Ͷ�ʾ��߸�����������Ȩ��investing.com��վ���У�������Ȩ������ϵ��ɾ�������Ŀ��**