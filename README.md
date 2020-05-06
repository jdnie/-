## 7zip

sudo apt-get install p7zip

7zr x secondary_houses.7z

## run

pip install selenium

pip install bs4

pip install pandas

download chromedriver from https://sites.google.com/a/chromium.org/chromedriver/home and set the environment "PATH"

python secondary_houses.py

## data

data is from 2017-03-23 to 20200506.

```python
>>> import pandas as pd
>>> df = pd.read_csv('secondary_houses.csv') 
>>> df.head()
       房源核验统一编码  所属城区     小区      面积   委托价格       均价        挂牌时间
0  200416659453  钱塘新区  像之素公寓   89.32  248.0  27765.0  2020-05-06
1  171016029636    下城   德胜东村   60.19  220.0  36550.0  2020-05-06
2  200425940835    江干     领寓   88.66  340.0  38348.0  2020-05-06
3  180410333334    西湖    和家园  167.72  740.0  44121.0  2020-05-06
4  200502741244    西湖  金地自在城   86.08  320.0  37174.0  2020-05-06
```

