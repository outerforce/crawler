package ca.uwaterloo.cs.bigdata2017w.assignment6

import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.log4j.Logger
import org.rogach.scallop.ScallopConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.rogach.scallop._
import scala.collection.mutable._

/**
  * @author Irene
  */

class Conf1(args: Seq[String]) extends ScallopConf(args) {
  mainOptions = Seq(input, model, shuffle)
  val input = opt[String](descr = "input path", required = true)
  val model = opt[String](descr = "training model", required = true)
  val shuffle = opt[Boolean](descr = "shuffle state", required = true)
  verify()
}

object TrainSpamClassifier {

  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new Conf1(argv)

    log.info("Input: " + args.input())
    log.info("Model: " + args.model())

    val conf = new SparkConf().setAppName("TrainSpamClassifier")
    val sc = new SparkContext(conf)

    val w = Map[Int, Double]()
    val delta = 0.002

    // Scores a document based on its list of features.
    def spamminess(features: Array[Int]): Double = {
      var score = 0d
      features.foreach(f => if (w.contains(f)) score += w(f))
      score
    }

    val outputdir = new Path(args.model())
    FileSystem.get(sc.hadoopConfiguration).delete(outputdir, true)

    val shuffle_state = args.shuffle()

    val textFile = sc.textFile(args.input())
    if(!shuffle_state){
    val trained = textFile.map(line => {
      val tokens = line.split(" ")
      if (tokens(1) == "spam") {
        (0, (tokens(0), true, tokens.drop(2).map(value => value.toInt)))
      } else {
        (0, (tokens(0), false, tokens.drop(2).map(value => value.toInt)))
      }
    }).groupByKey(1)
      .flatMap(item => {
        // feature vector of the training instance
        val sequence = item._2
        sequence.foreach(pair => {
          val isSpam = if (pair._2) 1 else 0

          val features = pair._3
          // Update the weights
          val score = spamminess(features)
          val prob = 1.0 / (1 + Math.exp(-score))

          features.foreach(f => {
            if (w.contains(f)) {
              w(f) += (isSpam - prob) * delta
            } else {
              w(f) = (isSpam - prob) * delta
            }
          })
        })
        w
      })
      trained.saveAsTextFile(args.model())
    }else{
      val trained = textFile.map(line => {
        val tokens = line.split(" ")
        if (tokens(1) == "spam") {
          (0, (tokens(0), true, tokens.drop(2).map(value => value.toInt)))
        } else {
          (0, (tokens(0), false, tokens.drop(2).map(value => value.toInt)))
        }
      }).groupByKey(1)
        .flatMap(item => {
          // feature vector of the training instance
          val sequence = item._2
          sequence.foreach(pair => {
            val isSpam = if (pair._2) 1 else 0

            val features = pair._3
            // Update the weights
            val score = spamminess(features)
            val prob = 1.0 / (1 + Math.exp(-score))

            features.foreach(f => {
              if (w.contains(f)) {
                w(f) += (isSpam - prob) * delta
              } else {
                w(f) = (isSpam - prob) * delta
              }
            })
          })
          w
        })
      trained.saveAsTextFile(args.model())
    }
  }
}