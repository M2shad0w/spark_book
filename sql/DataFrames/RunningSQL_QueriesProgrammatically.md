# 运行SQL查询程序
Spark Application可以使用SQLContext的sql()方法执行SQL查询操作，sql()方法返回的查询结果为DataFrame格式。代码如下：

* Scala

```scala
val sqlContext = ...  // An existing SQLContext
val df = sqlContext.sql("SELECT * FROM table")
```
* Java

```java
SQLContext sqlContext = ...  // An existing SQLContext
DataFrame df = sqlContext.sql("SELECT * FROM table")
```