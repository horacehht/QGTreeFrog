### 笔记

可视化seaborn

.info()可以看有无缺失值，msno可视化的第三方库，看缺失值

缺失值多就删掉

少可以考虑做填充

fillna填充缺失值，isnull检查是否为缺失值



性别为字符串类型，不是机器能读懂，将其转换为数字（离散化）1，2

pd.df['.'].unique()这个特征有多少种输出



时间大部分会放在数据预处理中。

![image-20210409194200156](https://horacehhtbucket.oss-cn-guangzhou.aliyuncs.com/img/image-20210409194200156.png)

### 特征工程

![image-20210409194319682](https://horacehhtbucket.oss-cn-guangzhou.aliyuncs.com/img/image-20210409194319682.png)数据特征越多，模型泛化能力会下降。

特征合并或特征构造



特征选择sklearn.feature_selection，可得特征的得分。特征重要性

### 训练模型与评估算法

![image-20210409195131743](C:\Users\Horac\AppData\Roaming\Typora\typora-user-images\image-20210409195131743.png)

### 模型优化

调参

可多模型

集成学习：集合多个模型，投票法，少数服从多数

k折验证



### 可视化

很重要的一部分，对数据集的理解



**文件架构分好**，有逻辑性：特征工程，数据探索性分析EDA，

**避免一个文件从头跑到尾**



**做一个详细的文档记录数据挖掘的过程**



详细文档：面向专业人员

ppt：面向普世，不要用





# 数据挖掘过程

#### bug1:

```python
RuntimeError: In FT2Font: Can not load face (error code 0x55)
```

模仿继元师兄的代码，msno.matrix(data, figsize=(16, 6))时跳出该行报错。我以为只是这行代码的问题，结果我换另外一个缺失值图也不行

```python
missing = data.isnull().sum()
missing = missing[missing > 0]
missing.sort_values(inplace=True)
missing.plot.bar()
```

```
同样报错RuntimeError: In FT2Font: Can not load face (error code 0x55)
```

去stackoverflow，csdn，知乎，掘金，google搜索，中国网站基本没找到相关问题。stackoverflow上说检查下字体文件目录有无损坏

检查了下字体文件目录并没有发现问题<img src="https://horacehhtbucket.oss-cn-guangzhou.aliyuncs.com/img/image-20210411105052453.png" alt="image-20210411105052453" style="zoom:80%;" />

或是重新安装matplotlib。

那我就试试重新安装matplotlib把。

重新安装后，运行还是报错。

现在用matplotlib都是报这个错。跑去pycharm画图，能跑但不显示图片。

![image-20210411112808948](https://horacehhtbucket.oss-cn-guangzhou.aliyuncs.com/img/image-20210411112808948.png)

是字体的原因，继元师兄提供了一个问题解决的方案，https://blog.csdn.net/u012111465/article/details/79430365]，成功解决

#### bug2:

大bug，np.dot(_X, theta)报错`can't mutiply sequence by non-int of type 'float'`

很恐慌，我打算直接重装anaconda，重装后也是这样。后来运用sklearn的logistic回归算法，得知我difficulty_level有一项vary hard没有改成数值。这名字我下意识以为是very hard，所以最后没有把他改成数值，还是字符串。

分成1w4的数据，内存也维持在92-96的高位，看来数据确实是比较多

![](https://horacehhtbucket.oss-cn-guangzhou.aliyuncs.com/img/image-20210413010226950.png)