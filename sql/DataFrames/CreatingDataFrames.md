# 创建DataFrames
使用SQLContext，spark应用程序（Application）可以通过RDD、Hive表、JSON格式数据等数据源创建DataFrames。下面是基于JSON文件创建DataFrame的示例：

```scala
val sc: SparkContext // An existing SparkContext.
val sqlContext = new org.apache.spark.sql.SQLContext(sc)

val df = sqlContext.read.json("examples/src/main/resources/people.json")

// Displays the content of the DataFrame to stdout
df.show()
```

```java
JavaSparkContext sc = ...; // An existing JavaSparkContext.
SQLContext sqlContext = new org.apache.spark.sql.SQLContext(sc);

DataFrame df = sqlContext.read().json("examples/src/main/resources/people.json");

// Displays the content of the DataFrame to stdout
df.show();
```