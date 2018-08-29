# Spark

## Getting started

First things first, we need to make sure that java is installed. Spark is primarily powered by Scala which is built on 
java. Its APIs, whether python or R, compile down to Scala at runtime. For this reason, if the code is required to be
performant above and beyond what's provided by the general spark optimisations, the implementation should be written in 
Scala.

Install Java:
```bash
sudo apt update
sudo apt install default-jre
```

Spark isn't strictly installed to allow the running of the spark shell: simply download the target version from
 [here](https://spark.apache.org/downloads.html), unpack and launch the favoured spark shell
 
*Launch the Python Spark shell:*
 ```bash
wget http://mirror.vorboss.net/apache/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
tar -xzvf spark-2.3.1-bin-hadoop2.7.tgz
source spark-2.3.1-bin-hadoop2.7/bin/pyspark
```

Spark can be called from python scripts and from within jupyter notebooks. This requires the pyspark module.
```bash

```

