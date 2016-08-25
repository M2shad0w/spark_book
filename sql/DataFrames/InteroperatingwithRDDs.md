# DataFrames与RDDs的相互转换
Spark SQL支持两种RDDs转换为DataFrames的方式：

* 使用反射获取RDD内的Schema 
	- 当已知类的Schema的时候，使用这种基于反射的方法会让代码更加简洁而且效果也很好。

* 通过编程接口指定Schema 
	- 通过Spark SQL的接口创建RDD的Schema，这种方式会让代码比较冗长。
	- 这种方法的好处是，在运行时才知道数据的列以及列的类型的情况下，可以动态生成Schema