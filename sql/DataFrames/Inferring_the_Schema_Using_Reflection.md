# 使用反射获取Schema
Spark SQL支持将JavaBean的RDD自动转换成DataFrame。通过反射获取Bean的基本信息，依据Bean的信息定义Schema。当前Spark SQL版本（Spark 1.5.2）不支持嵌套的JavaBeans和复杂数据类型（如：List、Array）。创建一个实现Serializable接口包含所有属性getters和setters的类来创建一个JavaBean。通过调用createDataFrame并提供JavaBean的Class object，指定一个Schema给一个RDD。示例如下：

```java
public static class Person implements Serializable {
  private String name;
  private int age;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }
}
```

```java
// sc is an existing JavaSparkContext.
SQLContext sqlContext = new org.apache.spark.sql.SQLContext(sc);

// Load a text file and convert each line to a JavaBean.
JavaRDD<Person> people = sc.textFile("examples/src/main/resources/people.txt").map(
  new Function<String, Person>() {
    public Person call(String line) throws Exception {
      String[] parts = line.split(",");

      Person person = new Person();
      person.setName(parts[0]);
      person.setAge(Integer.parseInt(parts[1].trim()));

      return person;
    }
  });

// Apply a schema to an RDD of JavaBeans and register it as a table.
DataFrame schemaPeople = sqlContext.createDataFrame(people, Person.class);
schemaPeople.registerTempTable("people");

// SQL can be run over RDDs that have been registered as tables.
DataFrame teenagers = sqlContext.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

// The results of SQL queries are DataFrames and support all the normal RDD operations.
// The columns of a row in the result can be accessed by ordinal.
List<String> teenagerNames = teenagers.javaRDD().map(new Function<Row, String>() {
  public String call(Row row) {
    return "Name: " + row.getString(0);
  }
}).collect();
```