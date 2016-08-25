# DataFrame操作
DataFrames支持Scala、Java和Python的操作接口。下面是Scala和Java的几个操作示例：

* Scala

```scala
val sc: SparkContext // An existing SparkContext.
val sqlContext = new org.apache.spark.sql.SQLContext(sc)

// Create the DataFrame
val df = sqlContext.read.json("examples/src/main/resources/people.json")

// Show the content of the DataFrame
df.show()
// age  name
// null Michael
// 30   Andy
// 19   Justin

// Print the schema in a tree format
df.printSchema()
// root
// |-- age: long (nullable = true)
// |-- name: string (nullable = true)

// Select only the "name" column
df.select("name").show()
// name
// Michael
// Andy
// Justin

// Select everybody, but increment the age by 1
df.select(df("name"), df("age") + 1).show()
// name    (age + 1)
// Michael null
// Andy    31
// Justin  20

// Select people older than 21
df.filter(df("age") > 21).show()
// age name
// 30  Andy

// Count people by age
df.groupBy("age").count().show()
// age  count
// null 1
// 19   1
// 30   1
```

* Java

```java
JavaSparkContext sc // An existing SparkContext.
SQLContext sqlContext = new org.apache.spark.sql.SQLContext(sc)

// Create the DataFrame
DataFrame df = sqlContext.read().json("examples/src/main/resources/people.json");

// Show the content of the DataFrame
df.show();
// age  name
// null Michael
// 30   Andy
// 19   Justin

// Print the schema in a tree format
df.printSchema();
// root
// |-- age: long (nullable = true)
// |-- name: string (nullable = true)

// Select only the "name" column
df.select("name").show();
// name
// Michael
// Andy
// Justin

// Select everybody, but increment the age by 1
df.select(df.col("name"), df.col("age").plus(1)).show();
// name    (age + 1)
// Michael null
// Andy    31
// Justin  20

// Select people older than 21
df.filter(df.col("age").gt(21)).show();
// age name
// 30  Andy

// Count people by age
df.groupBy("age").count().show();
// age  count
// null 1
// 19   1
// 30   1
```

详细的DataFrame API请参考 API Documentation。

除了简单列引用和表达式，DataFrames还有丰富的library，功能包括string操作、date操作、常见数学操作等。详细内容请参考 DataFrame Function Reference。