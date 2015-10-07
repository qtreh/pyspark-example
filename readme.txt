
# using get will return `None` if a key is not present rather than raise a `KeyError`
print os.environ.get('KEY_THAT_MIGHT_EXIST')

# set an environment variable
os.environ["PYSPARK_PYTHON"] = "/Users/quentin/Dev/spark-1.4.1-bin-hadoop2.6/bin/pyspark"

/Users/quentin/Dev/spark-1.4.1-bin-hadoop2.6/bin/pyspark \
--master local[4] \
sparktest.py