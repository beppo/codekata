(ns
  codekata.bloomfilter.bit-set-test
  (require [clojure.test :refer :all] [codekata.bloomfilter.bit-set :refer :all]))

(deftest long-bits-test
  (testing "0 bits can be represented by 1 long" (is (= 1 (long-bits 0))))
  (testing "64 bits can be represented by 1 long" (is (= 1 (long-bits 64))))
  (testing "65 bits can be represented by 2 long" (is (= 2 (long-bits 65))))
  (testing "128 bits can be represented by 2 long" (is (= 2 (long-bits 128))))
  (testing "129 bits can be represented by 3 long" (is (= 3 (long-bits 129)))))


(deftest bit-index-test
  (testing "0 maps to bit index 0" (is (= 0 (bit-index 0))))
  (testing "64 maps to bit index 0" (is (= 0 (bit-index 64))))
  (testing "3 maps to bit index 3" (is (= 3 (bit-index 3))))
  (testing "67 maps to bit index 3" (is (= 3 (bit-index 67))))
  (testing "128 maps to bit index 0" (is (= 0 (bit-index 128))))
  (testing "129 maps to bit index 1" (is (= 1 (bit-index 129)))))

(deftest long-bits-index-test
  (testing "0 maps to bit index 0" (is (= 0 (long-bits-index 0))))
  (testing "63 maps to bit index 0" (is (= 0 (long-bits-index 63))))
  (testing "64 maps to bit index 1" (is (= 1 (long-bits-index 64))))
  (testing "65 maps to bit index 1" (is (= 1 (long-bits-index 65))))
  (testing "127 maps to bit index 1" (is (= 1 (long-bits-index 127))))
  (testing "128 maps to bit index 2" (is (= 2 (long-bits-index 128))))
  (testing "129 maps to bit index 2" (is (= 2 (long-bits-index 129)))))


(deftest set-bit-test
  ;; set bit at any index and test all other indexes are false except the one which has been set
  (let [index-set (atom 0)]
    (while (< @index-set 128)
      (swap! index-set inc)
      (let [index-unset (atom 0)]
        (while (< @index-unset 128) (doall
                                      (swap! index-unset inc)
                                      (if (not= @index-set @index-unset)
                                        (testing (str "set bit " (str @index-set) "and test bit" (str @index-unset)) (is (false? (is-bit-set-at (set-bit-at! (create-bit-set 128) @index-set) @index-unset))))
                                        )
                                      ))))))

(deftest set-bit-test
  ;; set bit at any index and test all other indexes are false except the one which has been set
  ;(testing (str "set bit " (str @index-set) "and test bit" (str @index-set)) (is (false? (is-bit-set-at (set-bit-at! (create-bit-set 128) @index-set) @index-set))))
  (let [index (atom 0) length 128]
    (while (< @index length)
      (println "index = " @index)
      (testing "set bit " (is (true? (is-bit-set-at (set-bit-at! (create-bit-set length) @index) @index))))
      (swap! index inc)
      ))
  )