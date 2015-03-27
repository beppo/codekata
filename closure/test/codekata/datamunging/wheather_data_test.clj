(ns
  codekata.datamunging.wheather-data-test
  (require [clojure.test :refer :all] [codekata.datamunging.weather-data :refer :all]))

(deftest spread-test
  (testing "spread" (is (= 6 (spread {:MxT 10 :MnT 4})))))

(deftest min-spread-test
  (testing "min-spread one entry" (is (= {:MxT 10 :MnT 4} (min-spread [{:MxT 10 :MnT 4}]))))
  (testing "min-spread two entries" (is (= {:MxT 10 :MnT 4} (min-spread [{:MxT 10 :MnT 4} {:MxT 11 :MnT 3}]))))
  (testing "min-spread many entries" (is (= {:MxT 10 :MnT 4} (min-spread [{:MxT 10 :MnT 3} {:MxT 10 :MnT 4} {:MxT 11 :MnT 3}])))))