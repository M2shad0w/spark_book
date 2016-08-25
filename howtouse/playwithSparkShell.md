# Spark Shell

## 基本
spark shell  提供的一个简单的方式去学习 spark的 API, 是交互式分析数据的有利工具。它提供了scala python的支持。在spark的根目录运行

* scala

```scala
./bin/spark-shell
``` 
* python

```python
./bin/pyspark
```

Spark 最主要的抽象就是一个被称之为弹性分布式数据集（RDD）的分布式集合项目。RDDs可以从Hadoop的输入格式，或者其他的RDD转换而来。那么我们就在Spark 的根目录内利用 README 文件创建一个RDD实例。

```scala
scala> val textFile = sc.textFile("README.md")
textFile: spark.RDD[String] = spark.MappedRDD@2ee9b6e3
```

RDDs有actions的方法，能够返回一些值，能够转换，指向一个新的RDDs实例。

```scala
scala> textFile.count() // Number of items in this RDD
scala> textFile.first() // First item in this RDD
```

现在我们来使用转换，通过 filter 来返回一个本项目的子集的一个RDD实例。

```scala
scala> val linesWithSpark = textFile.filter(line => line.contains("Spark"))
linesWithSpark: spark.RDD[String] = spark.FilteredRDD@7dd4af09
```