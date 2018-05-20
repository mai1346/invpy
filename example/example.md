
# invpy 使用教程

### 1.首先载入invpy。因为现在invpy包含scrape一个script，所以可以直接载入该script下的所有函数。

  **`from invpy.scrape import *`**


```python
from invpy.scrape import *
```

### 2.使用 getpairID 函数。

getpairID 函数接受两个argument：keyword 和 source。keyword 为搜索关键词， source为搜索网站来源（主要针对investing.com网站的不同语言版本）。

#### Example 1：

我们想要搜索有关 **比特币/美元** 的报价信息，但是并不知道准确的symbol。我们可以尝试: `getpairID('比特币',source = 'cn')`


```python
getpairID('比特币',source = 'cn')
```

    Keyword: 比特币 
    Match Successful!
    Getting "比特币 美元" data by default.
    If the first result didn't match your need,Please choose the right name as keyword and try it again.
    关键词: 比特币 
    匹配成功!
    默认返回"比特币 美元"的数据。
    如果默认结果与您的需求不匹配，请用正确的名称替代关键词重新搜索。
    ----------------------------------------------------
         Pair_ID     Symbol               Name    Exchange Pair_Type
    0    945629   BTC\/USD        比特币 美元    Bitfinex      货币
    1   1031333   BCH\/USD    比特币现金 美元    Bitfinex      货币
    2   1056127        XBT    比特币期货 CBOE        CBOE  外汇期货
    3   1055949        BTC     比特币期货 CME         CME  外汇期货
    4   1010776   ETH\/BTC      以太坊 比特币    Poloniex      货币
    5    997700   BTC\/XAU    比特币 黄金现货   Synthetic      货币
    6   1010777   XRP\/BTC      瑞波币 比特币    Poloniex      货币
    7    997699   XAU\/BTC    黄金现货 比特币                  货币
    8   1010783  DASH\/BTC      达世币 比特币    Poloniex      货币
    9   1010882   ETC\/BTC  以太坊经典 比特币    Poloniex      货币
    10  1010801   BTC\/EUR        比特币 欧元        GDAX      货币
    11   940808   BTC\/KRW        比特币 韩元     Bithumb      货币
    12  1010779   LTC\/BTC      莱特币 比特币    Poloniex      货币
    13  1010778    SC\/BTC      云储币 比特币    Poloniex      货币
    14       36   BTC\/THB        比特币 泰铢  BXThailand      货币
    15       26   BTC\/CHF    比特币 瑞士法郎         ANX      货币
    16       25   BTC\/GBP        比特币 英镑         ANX      货币
    17       24   BTC\/CAD    比特币 加拿大元         ANX      货币
    18       23   BTC\/JPY        比特币 日元         ANX      货币
    19       29   BTC\/AUD  比特币 澳大利亚元         ANX      货币
    20       32   BTC\/HKD        比特币 港币         ANX      货币
    21       38   BTC\/NZD    比特币 新西兰元         ANX      货币
    22       35   BTC\/SGD    比特币 新加坡元       itBit      货币
    23       33   BTC\/PLN  比特币 波兰兹罗提      BitBay      货币
    24    53078   BTC\/CNY      比特币 人民币         ANX      货币
    




    ('945629', 'BTC\\/USD')



从上面返回的表格我们可以看出，investing.com网站默认匹配了25项和比特币有关的资产类别。其中Pair_ID是investing.com网站使用的识别码，同时也是`gethistData()`函数获取数据所需要的。其他条目都顾名思义。  

**注意： 关键词的语言必须与 source 相匹配，否则可能不会返回任何结果。**

#### Example 2：

我们尝试在默认source（美国）中搜索'比特币':`getpairID('比特币')`,将会得到以下结果。



```python
getpairID('比特币')
```

    Match Failed. Please try other keywords.(匹配失败，请尝试其他关键词)
    




    (0, 0)



这时我们可以更换搜索关键词为`bitcoin`。


```python
getpairID('bitcoin')
```

    Keyword: bitcoin 
    Match Successful!
    Getting "Bitcoin US Dollar" data by default.
    If the first result didn't match your need,Please choose the right name as keyword and try it again.
    关键词: bitcoin 
    匹配成功!
    默认返回"Bitcoin US Dollar"的数据。
    如果默认结果与您的需求不匹配，请用正确的名称替代关键词重新搜索。
    ----------------------------------------------------
         Pair_ID     Symbol                        Name    Exchange  Pair_Type
    0    945629   BTC\/USD           Bitcoin US Dollar    Bitfinex   Currency
    1   1031333   BCH\/USD      Bitcoin Cash US Dollar    Bitfinex   Currency
    2   1011883      NYXBT                NYSE Bitcoin        NYSE      Index
    3   1056127        XBT        Bitcoin Futures CBOE        CBOE  FX Future
    4   1055949        BTC         Bitcoin Futures CME         CME  FX Future
    5    997700   BTC\/XAU           Bitcoin Gold Spot   Synthetic   Currency
    6    997699   XAU\/BTC           Gold Spot Bitcoin               Currency
    7    940808   BTC\/KRW          Bitcoin Korean Won     Bithumb   Currency
    8   1010776   ETH\/BTC            Ethereum Bitcoin    Poloniex   Currency
    9   1010779   LTC\/BTC            Litecoin Bitcoin    Poloniex   Currency
    10  1010801   BTC\/EUR                Bitcoin Euro        GDAX   Currency
    11  1010783  DASH\/BTC                Dash Bitcoin    Poloniex   Currency
    12    53078   BTC\/CNY        Bitcoin Chinese Yuan         ANX   Currency
    13  1010778    SC\/BTC             Siacoin Bitcoin    Poloniex   Currency
    14  1010777   XRP\/BTC              Ripple Bitcoin    Poloniex   Currency
    15       35   BTC\/SGD    Bitcoin Singapore Dollar       itBit   Currency
    16       25   BTC\/GBP       Bitcoin British Pound         ANX   Currency
    17       24   BTC\/CAD     Bitcoin Canadian Dollar         ANX   Currency
    18       23   BTC\/JPY        Bitcoin Japanese Yen         ANX   Currency
    19       26   BTC\/CHF         Bitcoin Swiss Franc         ANX   Currency
    20       29   BTC\/AUD   Bitcoin Australian Dollar         ANX   Currency
    21       36   BTC\/THB           Bitcoin Thai Baht  BXThailand   Currency
    22       33   BTC\/PLN        Bitcoin Polish Zloty      BitBay   Currency
    23       32   BTC\/HKD    Bitcoin Hong Kong Dollar         ANX   Currency
    24       38   BTC\/NZD  Bitcoin New Zealand Dollar         ANX   Currency
    




    ('945629', 'BTC\\/USD')



我们可以看到，返回的结果和`source ='cn'`的结果一致，唯一不同的只有显示语言。不同的source 方便检索不同国家区域金融资产的信息。

#### Example 3：

由于本项目使用的就是investing.com网站自己的搜索接口，其检索性能和原网站一致。如果您知道更准确的检索信息，如股票的代码或者symbol，都可以直接进行搜索。下面我们尝试搜索：**600050（中国联通）**，结果成功匹配。


```python
getpairID('600050', source = 'cn')
```

    Keyword: 600050 
    Match Successful!
    Getting "中国联通" data by default.
    If the first result didn't match your need,Please choose the right name as keyword and try it again.
    关键词: 600050 
    匹配成功!
    默认返回"中国联通"的数据。
    如果默认结果与您的需求不匹配，请用正确的名称替代关键词重新搜索。
    ----------------------------------------------------
        Pair_ID  Symbol                    Name  Exchange Pair_Type
    0   100310  600050                中国联通      上海      股票
    1  1003513   WSGAX  Ivy Small Cap Growth A  纳斯达克      基金
    




    ('100310', '600050')



#### Example 4：

用户可以自行尝试不同类型的关键词来尝试匹配理想的结果，比如我想知道中国10年期国债的利率，可以调用函数：

`getpairID('中国10年国债', source = 'cn')`


```python
getpairID('中国10年期', source = 'cn')
```

    Keyword: 中国10年期 
    Match Successful!
    Getting "中国 10年期" data by default.
    If the first result didn't match your need,Please choose the right name as keyword and try it again.
    关键词: 中国10年期 
    匹配成功!
    默认返回"中国 10年期"的数据。
    如果默认结果与您的需求不匹配，请用正确的名称替代关键词重新搜索。
    ----------------------------------------------------
       Pair_ID     Symbol         Name Exchange   Pair_Type
    0   29227  CN10YT=RR  中国 10年期     上海  债券收益率
    




    ('29227', 'CN10YT=RR')



### 3.使用gethistData() 函数

`gethistData()` 函数首先调用`getpairID`函数得到pairID，并通过pairID来获取对应的数据，数据只包含open，high，low，close，volume等。

**注意：investing.com网站的数据为未复权数据。请酌情使用。**

#### Example 1：

比如我们想查询沪深300指数的数据。调用函数：`gethistData('沪深300', '2018/01/01', '2018/05/01', interval ='Daily'，source = 'cn')`

程序默认返回pandas.DataFrame, 用户可直接调用pandas的自带功能来储存为各种形式的数据文件。


```python
gethistData('沪深300','2018/01/01', '2018/05/01',interval ='Daily', source= 'cn')
```

    Keyword: 沪深300 
    Match Successful!
    Getting "沪深300" data by default.
    If the first result didn't match your need,Please choose the right name as keyword and try it again.
    关键词: 沪深300 
    匹配成功!
    默认返回"沪深300"的数据。
    如果默认结果与您的需求不匹配，请用正确的名称替代关键词重新搜索。
    ----------------------------------------------------
       Pair_ID  Symbol                    Name Exchange       Pair_Type
    0  940801  CSI300                 沪深300     上海            指数
    1  941616   CIFc1         沪深300指数期货     上海        指数期货
    2  941434    ASHR  德银嘉实沪深300指数ETF     纽约  交易所交易基金
    ----------------------------------------------------
    Printing data tail.
    打印数据末尾。
    ----------------------------------------------------
                   close     open     high      low       vol
    date                                                    
    2018-01-15  4225.24  4229.84  4262.93  4216.36  170908.0
    2018-01-12  4225.00  4205.14  4227.39  4199.03  111355.0
    2018-01-11  4205.59  4197.11  4211.80  4181.96  121579.0
    2018-01-10  4207.81  4187.20  4211.05  4175.14  151122.0
    2018-01-09  4189.30  4157.54  4191.28  4153.50  139034.0
    2018-01-08  4160.16  4140.85  4166.32  4127.31  173878.0
    2018-01-05  4138.75  4133.34  4151.28  4123.28  149010.0
    2018-01-04  4128.81  4114.12  4137.64  4105.89  134544.0
    2018-01-03  4111.39  4091.46  4140.05  4088.73  151852.0
    2018-01-02  4087.40  4045.21  4087.78  4045.21  146935.0
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>vol</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-04-27</th>
      <td>3756.88</td>
      <td>3771.04</td>
      <td>3776.98</td>
      <td>3714.64</td>
      <td>89532.0</td>
    </tr>
    <tr>
      <th>2018-04-26</th>
      <td>3755.49</td>
      <td>3823.39</td>
      <td>3828.71</td>
      <td>3744.89</td>
      <td>87151.0</td>
    </tr>
    <tr>
      <th>2018-04-25</th>
      <td>3828.70</td>
      <td>3824.59</td>
      <td>3838.69</td>
      <td>3817.03</td>
      <td>78173.0</td>
    </tr>
    <tr>
      <th>2018-04-24</th>
      <td>3843.49</td>
      <td>3769.88</td>
      <td>3854.43</td>
      <td>3769.88</td>
      <td>114220.0</td>
    </tr>
    <tr>
      <th>2018-04-23</th>
      <td>3766.33</td>
      <td>3754.69</td>
      <td>3787.40</td>
      <td>3735.18</td>
      <td>90356.0</td>
    </tr>
    <tr>
      <th>2018-04-20</th>
      <td>3760.85</td>
      <td>3801.21</td>
      <td>3815.44</td>
      <td>3750.10</td>
      <td>99283.0</td>
    </tr>
    <tr>
      <th>2018-04-19</th>
      <td>3811.84</td>
      <td>3774.78</td>
      <td>3824.03</td>
      <td>3767.80</td>
      <td>99054.0</td>
    </tr>
    <tr>
      <th>2018-04-18</th>
      <td>3766.28</td>
      <td>3785.31</td>
      <td>3789.66</td>
      <td>3708.11</td>
      <td>106677.0</td>
    </tr>
    <tr>
      <th>2018-04-17</th>
      <td>3748.64</td>
      <td>3812.87</td>
      <td>3822.63</td>
      <td>3745.44</td>
      <td>90611.0</td>
    </tr>
    <tr>
      <th>2018-04-16</th>
      <td>3808.86</td>
      <td>3862.47</td>
      <td>3869.16</td>
      <td>3789.61</td>
      <td>99218.0</td>
    </tr>
    <tr>
      <th>2018-04-13</th>
      <td>3871.14</td>
      <td>3920.74</td>
      <td>3929.95</td>
      <td>3866.19</td>
      <td>71544.0</td>
    </tr>
    <tr>
      <th>2018-04-12</th>
      <td>3898.64</td>
      <td>3935.67</td>
      <td>3937.78</td>
      <td>3896.18</td>
      <td>82699.0</td>
    </tr>
    <tr>
      <th>2018-04-11</th>
      <td>3938.34</td>
      <td>3934.17</td>
      <td>3958.71</td>
      <td>3924.96</td>
      <td>111933.0</td>
    </tr>
    <tr>
      <th>2018-04-10</th>
      <td>3927.17</td>
      <td>3860.72</td>
      <td>3927.42</td>
      <td>3851.80</td>
      <td>106174.0</td>
    </tr>
    <tr>
      <th>2018-04-09</th>
      <td>3852.93</td>
      <td>3851.95</td>
      <td>3870.67</td>
      <td>3827.41</td>
      <td>84105.0</td>
    </tr>
    <tr>
      <th>2018-04-04</th>
      <td>3854.86</td>
      <td>3873.63</td>
      <td>3898.61</td>
      <td>3852.50</td>
      <td>88731.0</td>
    </tr>
    <tr>
      <th>2018-04-03</th>
      <td>3862.48</td>
      <td>3850.15</td>
      <td>3878.15</td>
      <td>3839.93</td>
      <td>95137.0</td>
    </tr>
    <tr>
      <th>2018-04-02</th>
      <td>3886.92</td>
      <td>3897.01</td>
      <td>3937.02</td>
      <td>3882.89</td>
      <td>111243.0</td>
    </tr>
    <tr>
      <th>2018-03-30</th>
      <td>3898.50</td>
      <td>3893.75</td>
      <td>3915.35</td>
      <td>3879.21</td>
      <td>97512.0</td>
    </tr>
    <tr>
      <th>2018-03-29</th>
      <td>3894.05</td>
      <td>3854.59</td>
      <td>3913.96</td>
      <td>3794.26</td>
      <td>116629.0</td>
    </tr>
    <tr>
      <th>2018-03-28</th>
      <td>3842.72</td>
      <td>3865.05</td>
      <td>3907.28</td>
      <td>3835.88</td>
      <td>101495.0</td>
    </tr>
    <tr>
      <th>2018-03-27</th>
      <td>3913.27</td>
      <td>3927.49</td>
      <td>3936.78</td>
      <td>3881.87</td>
      <td>113701.0</td>
    </tr>
    <tr>
      <th>2018-03-26</th>
      <td>3879.89</td>
      <td>3862.69</td>
      <td>3883.90</td>
      <td>3829.92</td>
      <td>115139.0</td>
    </tr>
    <tr>
      <th>2018-03-23</th>
      <td>3904.94</td>
      <td>3896.74</td>
      <td>3928.51</td>
      <td>3834.94</td>
      <td>180080.0</td>
    </tr>
    <tr>
      <th>2018-03-22</th>
      <td>4020.35</td>
      <td>4062.07</td>
      <td>4072.38</td>
      <td>4003.72</td>
      <td>89095.0</td>
    </tr>
    <tr>
      <th>2018-03-21</th>
      <td>4061.05</td>
      <td>4097.02</td>
      <td>4110.12</td>
      <td>4046.24</td>
      <td>97609.0</td>
    </tr>
    <tr>
      <th>2018-03-20</th>
      <td>4077.70</td>
      <td>4045.74</td>
      <td>4080.19</td>
      <td>4040.31</td>
      <td>80605.0</td>
    </tr>
    <tr>
      <th>2018-03-19</th>
      <td>4074.25</td>
      <td>4054.62</td>
      <td>4074.52</td>
      <td>4033.52</td>
      <td>81503.0</td>
    </tr>
    <tr>
      <th>2018-03-16</th>
      <td>4056.42</td>
      <td>4096.89</td>
      <td>4110.05</td>
      <td>4055.82</td>
      <td>84896.0</td>
    </tr>
    <tr>
      <th>2018-03-15</th>
      <td>4096.16</td>
      <td>4058.71</td>
      <td>4098.99</td>
      <td>4058.71</td>
      <td>88161.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2018-02-12</th>
      <td>3890.10</td>
      <td>3846.27</td>
      <td>3907.84</td>
      <td>3828.07</td>
      <td>116183.0</td>
    </tr>
    <tr>
      <th>2018-02-09</th>
      <td>3840.65</td>
      <td>3896.17</td>
      <td>3911.29</td>
      <td>3759.15</td>
      <td>206350.0</td>
    </tr>
    <tr>
      <th>2018-02-08</th>
      <td>4012.05</td>
      <td>4022.88</td>
      <td>4071.67</td>
      <td>3974.68</td>
      <td>159270.0</td>
    </tr>
    <tr>
      <th>2018-02-07</th>
      <td>4050.50</td>
      <td>4205.74</td>
      <td>4212.57</td>
      <td>4048.42</td>
      <td>203127.0</td>
    </tr>
    <tr>
      <th>2018-02-06</th>
      <td>4148.89</td>
      <td>4182.33</td>
      <td>4211.52</td>
      <td>4131.56</td>
      <td>214910.0</td>
    </tr>
    <tr>
      <th>2018-02-05</th>
      <td>4274.15</td>
      <td>4204.46</td>
      <td>4274.15</td>
      <td>4200.14</td>
      <td>161348.0</td>
    </tr>
    <tr>
      <th>2018-02-02</th>
      <td>4271.23</td>
      <td>4213.94</td>
      <td>4271.76</td>
      <td>4181.78</td>
      <td>146067.0</td>
    </tr>
    <tr>
      <th>2018-02-01</th>
      <td>4245.90</td>
      <td>4276.34</td>
      <td>4287.39</td>
      <td>4214.29</td>
      <td>190003.0</td>
    </tr>
    <tr>
      <th>2018-01-31</th>
      <td>4275.90</td>
      <td>4234.11</td>
      <td>4287.86</td>
      <td>4232.77</td>
      <td>145210.0</td>
    </tr>
    <tr>
      <th>2018-01-30</th>
      <td>4256.10</td>
      <td>4286.68</td>
      <td>4308.51</td>
      <td>4251.57</td>
      <td>139035.0</td>
    </tr>
    <tr>
      <th>2018-01-29</th>
      <td>4302.02</td>
      <td>4387.06</td>
      <td>4395.91</td>
      <td>4287.11</td>
      <td>191100.0</td>
    </tr>
    <tr>
      <th>2018-01-26</th>
      <td>4381.30</td>
      <td>4352.22</td>
      <td>4403.34</td>
      <td>4351.49</td>
      <td>177227.0</td>
    </tr>
    <tr>
      <th>2018-01-25</th>
      <td>4365.08</td>
      <td>4381.98</td>
      <td>4392.20</td>
      <td>4336.24</td>
      <td>195375.0</td>
    </tr>
    <tr>
      <th>2018-01-24</th>
      <td>4389.89</td>
      <td>4389.45</td>
      <td>4397.82</td>
      <td>4349.09</td>
      <td>219819.0</td>
    </tr>
    <tr>
      <th>2018-01-23</th>
      <td>4382.61</td>
      <td>4346.89</td>
      <td>4383.57</td>
      <td>4346.79</td>
      <td>201868.0</td>
    </tr>
    <tr>
      <th>2018-01-22</th>
      <td>4336.60</td>
      <td>4276.48</td>
      <td>4338.48</td>
      <td>4275.90</td>
      <td>174643.0</td>
    </tr>
    <tr>
      <th>2018-01-19</th>
      <td>4285.40</td>
      <td>4281.94</td>
      <td>4316.57</td>
      <td>4269.62</td>
      <td>209491.0</td>
    </tr>
    <tr>
      <th>2018-01-18</th>
      <td>4271.42</td>
      <td>4259.38</td>
      <td>4292.64</td>
      <td>4246.68</td>
      <td>172033.0</td>
    </tr>
    <tr>
      <th>2018-01-17</th>
      <td>4248.12</td>
      <td>4261.78</td>
      <td>4283.34</td>
      <td>4230.54</td>
      <td>214311.0</td>
    </tr>
    <tr>
      <th>2018-01-16</th>
      <td>4258.47</td>
      <td>4215.62</td>
      <td>4260.21</td>
      <td>4213.13</td>
      <td>161495.0</td>
    </tr>
    <tr>
      <th>2018-01-15</th>
      <td>4225.24</td>
      <td>4229.84</td>
      <td>4262.93</td>
      <td>4216.36</td>
      <td>170908.0</td>
    </tr>
    <tr>
      <th>2018-01-12</th>
      <td>4225.00</td>
      <td>4205.14</td>
      <td>4227.39</td>
      <td>4199.03</td>
      <td>111355.0</td>
    </tr>
    <tr>
      <th>2018-01-11</th>
      <td>4205.59</td>
      <td>4197.11</td>
      <td>4211.80</td>
      <td>4181.96</td>
      <td>121579.0</td>
    </tr>
    <tr>
      <th>2018-01-10</th>
      <td>4207.81</td>
      <td>4187.20</td>
      <td>4211.05</td>
      <td>4175.14</td>
      <td>151122.0</td>
    </tr>
    <tr>
      <th>2018-01-09</th>
      <td>4189.30</td>
      <td>4157.54</td>
      <td>4191.28</td>
      <td>4153.50</td>
      <td>139034.0</td>
    </tr>
    <tr>
      <th>2018-01-08</th>
      <td>4160.16</td>
      <td>4140.85</td>
      <td>4166.32</td>
      <td>4127.31</td>
      <td>173878.0</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>4138.75</td>
      <td>4133.34</td>
      <td>4151.28</td>
      <td>4123.28</td>
      <td>149010.0</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>4128.81</td>
      <td>4114.12</td>
      <td>4137.64</td>
      <td>4105.89</td>
      <td>134544.0</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>4111.39</td>
      <td>4091.46</td>
      <td>4140.05</td>
      <td>4088.73</td>
      <td>151852.0</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>4087.40</td>
      <td>4045.21</td>
      <td>4087.78</td>
      <td>4045.21</td>
      <td>146935.0</td>
    </tr>
  </tbody>
</table>
<p>77 rows × 5 columns</p>
</div>



**教程完毕，如有疑问请联系邮箱maihaoyuan@gmail.com**
