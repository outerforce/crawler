package ca.uwaterloo.cs.bigdata2017w.assignment6

import org.apache.log4j.Logger
import org.apache.spark.{SparkConf, SparkContext}
import org.rogach.scallop.ScallopConf
import org.apache.hadoop.fs.{FileSystem, Path}

/**
  * @author Irene
  */
class Conf2(args: Seq[String]) extends ScallopConf(args) {
  mainOptions = Seq(input, output, model)
  val input = opt[String](descr = "input path", required = true)
  val output = opt[String](descr = "output path", required = true)
  val model = opt[String](descr = "training model", required = true)
  verify()
}

object ApplySpamClassifier {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new Conf2(argv)

    log.info("Input: " + args.input())
    log.info("Output: " + args.output())
    log.info("Model: " + args.model())

    val conf = new SparkConf().setAppName("ApplySpamClassifier")
    val sc = new SparkContext(conf)

    // w is the weight vector (make sure the variable is within scope)
    val wBroadcast = sc.broadcast(sc.textFile(args.model())
      .map(line => {
        val tokens = line.replaceAll("\\(", "").replaceAll("\\)", "").split(",")
        val key = tokens(0).toInt
        val value = tokens(1).toDouble
        (key, value)
      }).collectAsMap())

    def spamminess(features: Array[Int]): Double = {
      var score = 0d
      features.foreach(f =>
        if (wBroadcast.value.contains(f)) score += wBroadcast.value.get(f).get)
      score
    }

    val inputFile = sc.textFile(args.input())

    val AfterTraining = inputFile
      .map(line => {
        val tokens = line.split(" ")
        var score = spamminess(tokens.drop(2).map(value => value.toInt))
        if (score > 0) {
          (tokens(0), tokens(1), score, "spam")
        } else {
          (tokens(0), tokens(1), score, "ham")
        }
      })
    val outputDir = new Path(args.output())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)

    AfterTraining.saveAsTextFile(args.output())

  }
}