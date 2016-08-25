# Spark安装

## mac上安装
**mac 上用brew命令行安装spark**

```sh
brew install apache-spark
```

**查看spark版本**

```sh
brew info apache-spark
apache-spark: stable 1.5.2, HEAD
Engine for large-scale data processing
https://spark.apache.org/
/usr/local/Cellar/apache-spark/1.5.2 (686 files, 305M) *
  Built from source
From: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/apache-spark.rb
```

**安装java**

```sh
brew cask install java
```

**查看java版本**

```sh
brew cask info java or java -version
```
```sh
java -version
java version "1.8.0_66"
Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)
```

**安装scala**

```sh
brew install scala
```

**查看scala版本**

```sh
brew info scala
```

**info**
回显信息中比较重要的是用idea开发的scala的时候，scala路径设置成
> To use with IntelliJ, set the Scala home to:
> /usr/local/opt/scala/idea

spark 1.5.2 使用（scala2.10.x）编译的,**经实践, scala版本设置需要2.10.5, 以免带来奇怪的问题**

## Running the Examples and Shell

这样安装的spark自带一些例子， Scala, Java, Python and R 的例子在 examples/src/main目录，可以在安装的spark根目录使用命令 bin/run-example <class> [params] 跑一些例子，例如计算Pi

```sh
./bin/run-example SparkPi 100
```

可以直接在控制台中敲入spark-shell，开始spark之旅了。


