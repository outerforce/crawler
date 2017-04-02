import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.log4j.Logger
import org.rogach.scallop.ScallopConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.rogach.scallop._
import scala.collection.mutable._
import org.apache.log4j.Logger
import org.rogach.scallop.ScallopConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.rogach.scallop._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.functions
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.types._
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType};
/**
  * @author Irene
  */
import org.apache.spark.mllib.feature.{StandardScaler, StandardScalerModel}
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.util.MLUtils


class Conf1(args: Seq[String]) extends ScallopConf(args) with Tokenizer {
  mainOptions = Seq(input)
  val input = opt[String](descr = "input path", required = true)
  verify()
}

object TrainSpamClassifier {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new Conf1(argv)

    //log.info("Input: " + args.input())

    val conf = new SparkConf().setAppName("TrainSpamClassifier")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
//    val basicDF = new org.apache.spark
//    val sqlcontext = new org.apache.spark.sql.SQLContext(sc)
//    val df = sqlcontext.read.json(args.input())
//    val textFile = sc.textFile(args.input())
//    val lineitem_t = textFile
//      .map(line => line.split(","))
//
//      val num = lineitem_t.count()
//      println("ANSWER=" + num)

   /* val sparkSession = SparkSession.builder.config(conf = conf).getOrCreate()
    val path = "/home/irene/crawler/classification/basic.csv"
    val base_df = sparkSession.read.json(path)*/


    //val sc = new SparkContext(conf)

  /*  val df = sqlContext.read.format("com.databricks.spark.csv")
      .option("header", "true")
      .load(args.input() + "/basic.csv")
    val df2 = sqlContext.read.format("com.databricks.spark.csv")
      .option("header", "true")
      .load(args.input() + "/second.csv")
    val matchesDf = sqlContext.createDataFrame(matches)
    val playersDf = sqlContext.createDataFrame(players)*/
    //val sqlContext = new SQLContext(sc)
   /* val df = sqlContext.read
      .format("com.databricks.spark.csv")
      .option("header", "true") // Use first line of all files as header
      .option("inferSchema", "true") // Automatically infer data types
      .load("basic.csv")

    val df2 = sqlContext.read
      .format("com.databricks.spark.csv")
      .option("header", "true") // Use first line of all files as header
      .option("inferSchema", "true") // Automatically infer data types
      .load("second.csv")*/



    val basicCSV = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load(args.input() + "/basic.csv")
    //val basicDF = basicCSV.withColumn("proj", basicCSV("proj")).withColumn("issueKey", basicCSV("issueKey")).withColumn("summary", basicCSV("summary"))

    val secondCSV = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").load(args.input() + "/second.csv")

    val basicDF = basicCSV.withColumn("proj", basicCSV("proj")).withColumn("issueKey", basicCSV("issueKey")).withColumn("summary", basicCSV("summary"))

    val secondDF = secondCSV.withColumn("issueKey", secondCSV("issueKey")).withColumn("description", secondCSV("description"))
    val joinedDF = basicDF.join(secondDF, basicDF("issueKey") === secondDF("issueKey"), "left")
    val resultset = sqlContext.sql("SELECT basicDF.proj, basicDF.issueKey, basicDF.summary,secondDF.description FROM basicDF,secondDF WHERE basicDF.issueKey = secondDF.issueKey")
    val selectedData = resultset.select("proj", "issueKey","summary","description")
      .write.format("com.databricks.spark.csv")
      .option("header", "true")
      .save("new.csv")
//    if (text == false && parquet == true) {
//      val sparkSession = SparkSession.builder.getOrCreate
//      val lineitemDF = sparkSession.read.parquet(args.input() + "/lineitem")
//      val lineitemRDD = lineitemDF.rdd
//      //val sqlDF = sparkSession.sql("select count(*) from lineitem where l_shipdate = '1996-01-01';")
//      //sqlDF.show()
//      //val date = """(\d\d\d\d)-(\d\d)-(\d\d)""".r
//      val lineitem_t = lineitemRDD
//        .filter(tokens => tokens(10).toString.contains(date_req))
//        .map(x => x(10))
//
//      println("ANSWER=" + lineitem_t.count())
//    }

  }

 /* val data = MLUtils.loadLibSVMFile(sc, "data/mllib/sample_libsvm_data.txt")

  val scaler1 = new StandardScaler().fit(data.map(x => x.features))
  val scaler2 = new StandardScaler(withMean = true, withStd = true).fit(data.map(x => x.features))
  // scaler3 is an identical model to scaler2, and will produce identical transformations
  val scaler3 = new StandardScalerModel(scaler2.std, scaler2.mean)

  // data1 will be unit variance.
  val data1 = data.map(x => (x.label, scaler1.transform(x.features)))

  // data2 will be unit variance and zero mean.
  val data2 = data.map(x => (x.label, scaler2.transform(Vectors.dense(x.features.toArray))))*/

}