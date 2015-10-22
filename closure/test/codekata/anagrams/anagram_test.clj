(ns
  codekata.anagrams.anagram-test
  (require [clojure.test :refer :all] [codekata.anagrams.anagram :refer :all]))

;;(deftest find-anagrams
;;  (testing "0 maps to bit index 0" (is (= 0 (find-anagrams '("pictures" "piecrust" "sunders" "undress")))))
;;  )

(deftest anagrams-test
  (testing "'a' and 'a' are anagrams" (is (= true (anagrams "a" "a"))))
  (testing "'pictures' and 'piecrust' are anagrams" (is (= true (anagrams "pictures" "piecrust"))))
  (testing "'dana' and 'mana' are not anagrams" (is (= false (anagrams "dana" "mana"))))
  )