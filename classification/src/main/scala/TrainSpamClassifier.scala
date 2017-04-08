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

    //val sc = new SparkContext(conf)

    val sparkSession = SparkSession.builder.getOrCreate
    val basicCSV = sqlContext.read.format("com.databricks.spark.csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load(args.input() + "/summary.csv")
    val basicDF = basicCSV.withColumn("proj", basicCSV("proj"))
      .withColumn("issueKey", basicCSV("issueKey"))
      .withColumn("summary", basicCSV("summary"))
      .withColumn("description", basicCSV("description"))
    val lineitemRDD = basicDF.rdd
    println(lineitemRDD)

    //    val lineitem_t = lineitemRDD({
    //      line=>line.tokenize()
    //    })
    //      .filter(line => line)
    //        .map(x => x(10))
    //
    //      println("ANSWER=" + lineitem_t.count())
    //    }
  }

}