# Spark拓展阅读

1. 为什么用Spark而不是MySQL？
	> 在很多任务中MySQL（开箱即用的）表现并不太好。MySQL的限制之一在于：1次查询=1个CPU内核。也就是说，即便你有48个速度飞快的内核，外加一个大型数据集可用，也无法充分利用所有的计算能力，相反Spark却能充分使用CPU内核。

	> l MySQL使用所谓的“写时模式（schema on write）”——需要将数据转化到MySQL中，如果未包含在MySQL里，就无法使用sql来查询。

	> l Spark（还有Hadoop/Hive）使用“读时模式（schema on read）”——比如在一个压缩txt文件顶部使用表格结构（或者其他支持的输入格式	），将其看作表格；然后我们可以用SQL来查询这个“表格”。

	> 也就是说，MySQL负责存储+处理，而Spark只负责处理，并可直接贯通数据与外部数据集（Hadoop、Amazon S3，本地文件、JDBC MySQL或其他数据集）的通道。Spark支持txt文件（压缩的）、SequenceFile、其他Hadoop输入格式和Parquet列式存储。相对Hadoop来说，Spark在这方面更为灵活：例如Spark可以直接从MySQL中读取数据。

2. 向MySQL加载外部数据的典型管道（pipeline）是：

	* 解压缩（尤其是压缩成txt文件的外部数据）；

	* 用“LOAD DATA INFILE”命令将其加载到MySQL的存储表格中；

	* 只有这样，我们才能筛选/进行分组，并将结果保存到另一张表格中。

	这会导致额外的开销；在很多情况下，我们不需要“原始”数据，但仍需将其载入MySQL中。


3. 为什么将Spark与MySQL用在一起：
	> 相反，我们的分析结果（比如聚合数据）应当存在MySQL中。将分析结果存在MySQL中并非必要，不过更为方便。假设你想要分析一个大数据集（即每年的销售额对比），需要使用表格或图表的形式展现出来。由于会进行聚合，结果集将会小很多，将其存在MySQL中与很多标准程序一同协作处理将会容易许多。