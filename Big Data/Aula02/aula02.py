from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()

spark = SparkSession.builder\
    .master("local")\
    .appName("Colab")\
    .config("spark.ui.port", 4000)\
    .getOrCreate()

data = [("São Paulo", "bourbon", 5000, 400), \
        ("Rio de Janeiro", "Rio Sul", 4500, 300), \
        ("Fortaleza", "Rio Mar", 3800, 250), \
        ("Amazonas", "Manaus Via Norte", 3000, 200), \
        ("São Paulo", "Bourbon", 5000, 400), \
        ("Rio de Janeiro", "Rio Sul", 4800, 320), \
        ("Fortaleza", "Rio Mar", 4000, 280), \
        ("Amazonas", "Manaus Via Norte", 3000, 200), \
        ("Rio Grande do Sul", "Praça Rio Grande", 4500, 320)]

columns = ["estado", "shopping", "qtd_pessoas", "capacidade_estacionamento"]

df = spark.createDataFrame(data = data , schema=columns)
df.printSchema()
df.show()