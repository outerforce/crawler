package ca.uwaterloo.cs.bigdata2017w.assignment6

import org.apache.log4j.Logger
import org.apache.spark.{SparkConf, SparkContext}
import org.rogach.scallop.ScallopConf
import org.apache.hadoop.fs.{FileSystem, Path}

/**
  * @author Irene
  **/
class Conf3(args: Seq[String]) extends ScallopConf(args) {
  mainOptions = Seq(input, model)
  val input = opt[String](descr = "input path", required = true)
  val output = opt[String](descr = "output path", required = true)
  val model = opt[String](descr = "training model", required = true)
  val method = opt[String](descr = "method type", required = true)
  verify()
}

object ApplyEnsembleSpamClassifier {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new Conf3(argv)

    log.info("Input: " + args.input())
    log.info("Output: " + args.output())
    log.info("Model: " + args.model())
    log.info("Method: " + args.method())

    val conf = new SparkConf().setAppName("ApplyEnsembleSpamClassifier")
    val sc = new SparkContext(conf)

    val GroupXFile = sc.textFile(args.model() + "/part-00000")
    val groupX = GroupXFile.map(line => {
      val tokens = line.replaceAll("\\(", "").replaceAll("\\)", "").split(",")
      val key = tokens(0).toInt
      val value = tokens(1).toDouble
      (key, value)
    })

    val groupXBroadcast = sc.broadcast(groupX.collectAsMap())

    val GroupYFile = sc.textFile(args.model() + "/part-00001")
    val groupY = GroupYFile.map(line => {
      val tokens = line.replaceAll("\\(", "").replaceAll("\\)", "").split(",")
      val key = tokens(0).toInt
      val value = tokens(1).toDouble
      (key, value)
    })

    val groupYBroadcast = sc.broadcast(groupY.collectAsMap())

    val britneyFile = sc.textFile(args.model() + "/part-00002")
    val britney = britneyFile.map(line => {
      val tokens = line.replaceAll("\\(", "").replaceAll("\\)", "").split(",")
      val key = tokens(0).toInt
      val value = tokens(1).toDouble
      (key, value)
    })

    val britneyBroadcast = sc.broadcast(britney.collectAsMap())


    val inputFile = sc.textFile(args.input())
    val method = args.method()

    val ensembleSpam = inputFile
      .map(line => {
        val tokens = line.split(" ")
        var score_t = 0d
        var score_r = 0d
        var score_br = 0d
        tokens.drop(2).map(value => value.toInt).foreach(x => {
          if (groupXBroadcast.value.contains(x)) {
            score_t += groupXBroadcast.value.get(x).get
          }
          if (groupYBroadcast.value.contains(x)) {
            score_r += groupYBroadcast.value.get(x).get
          }
          if (britneyBroadcast.value.contains(x)) {
            score_br += britneyBroadcast.value.get(x).get
          }
        })
        if (method == "average") {
          val averageScore = (score_t + score_r + score_br) / 3
          if (averageScore > 0) {
            (tokens(0), tokens(1), averageScore, "spam")
          } else {
            (tokens(0), tokens(1), averageScore, "ham")
          }
        }
        else {
          var vote_t = 0d
          var vote_r = 0d
          var vote_br = 0d
          if (score_t > 0) vote_t += 1
          else vote_t -= 1

          if (score_r > 0) vote_r += 1
          else vote_r -= 1

          if (score_br > 0) vote_br += 1
          else vote_br -= 1

          val vote_score = vote_t + vote_r + vote_br
          if (vote_score > 0) {
            (tokens(0), tokens(1), vote_score, "spam")
          }
          else {
            (tokens(0), tokens(1), vote_score, "ham")
          }
        }
      })
    val outputDir = new Path(args.output())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)
    ensembleSpam.saveAsTextFile(args.output())
  }

}
