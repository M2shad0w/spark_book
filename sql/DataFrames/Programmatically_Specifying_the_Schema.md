# 通过编程接口指定Schema
当JavaBean不能被预先定义的时候，编程创建DataFrame分为三步：
* 从原来的RDD创建一个Row格式的RDD
* 创建与RDD中Rows结构匹配的StructType，通过该StructType创建表示RDD的Schema
* 通过SQLContext提供的createDataFrame方法创建DataFrame，方法参数为RDD的Schema

```java
import org.apache.spark.api.java.function.Function;
// Import factory methods provided by DataTypes.
import org.apache.spark.sql.types.DataTypes;
// Import StructType and StructField
import org.apache.spark.sql.types.StructType;
import org.apache.spark.sql.types.StructField;
// Import Row.
import org.apache.spark.sql.Row;
// Import RowFactory.
import org.apache.spark.sql.RowFactory;

// sc is an existing JavaSparkContext.
SQLContext sqlContext = new org.apache.spark.sql.SQLContext(sc);

// Load a text file and convert each line to a JavaBean.
JavaRDD<String> people = sc.textFile("examples/src/main/resources/people.txt");

// The schema is encoded in a string
String schemaString = "name age";

// Generate the schema based on the string of schema
List<StructField> fields = new ArrayList<StructField>();
for (String fieldName: schemaString.split(" ")) {
  fields.add(DataTypes.createStructField(fieldName, DataTypes.StringType, true));
}
StructType schema = DataTypes.createStructType(fields);

// Convert records of the RDD (people) to Rows.
JavaRDD<Row> rowRDD = people.map(
  new Function<String, Row>() {
    public Row call(String record) throws Exception {
      String[] fields = record.split(",");
      return RowFactory.create(fields[0], fields[1].trim());
    }
  });

// Apply the schema to the RDD.
DataFrame peopleDataFrame = sqlContext.createDataFrame(rowRDD, schema);

// Register the DataFrame as a table.
peopleDataFrame.registerTempTable("people");

// SQL can be run over RDDs that have been registered as tables.
DataFrame results = sqlContext.sql("SELECT name FROM people");

// The results of SQL queries are DataFrames and support all the normal RDD operations.
// The columns of a row in the result can be accessed by ordinal.
List<String> names = results.javaRDD().map(new Function<Row, String>() {
  public String call(Row row) {
    return "Name: " + row.getString(0);
  }
}).collect();
```