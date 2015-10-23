(ns
  codekata.anagrams.anagram-test
  (require [clojure.test :refer :all] [codekata.anagrams.anagram :refer :all]))

(deftest anagrams-test
  (testing "'a' and 'a' are anagrams" (is (= true (is-anagram? "a" "a"))))
  (testing "'pictures' and 'piecrust' are anagrams" (is (= true (is-anagram? "pictures" "piecrust"))))
  (testing "'dana' and 'mana' are not anagrams" (is (= false (is-anagram? "dana" "mana"))))
  )

(deftest find-anagrams-test
  (testing "{elif, file, ben, sen, ali, lia} has anagrams {{file, elif}, {ben}, {sen}, {lia, ali}}" (is (= '(("file" "elif") ("ben") ("sen") ("lia" "ali")) (find-anagrams '("elif" "file" "ben" "sen" "ali" "lia") '()))))
  )

(deftest find-anagrams-v2-test
  (testing "{elif, file, ben, sen, ali, lia} has anagrams {{file, elif}, {ben}, {sen}, {lia, ali}}" (is (= '(("file" "elif") ("ben") ("sen") ("lia" "ali")) (find-anagrams-v2 '("elif" "file" "ben" "sen" "ali" "lia")))))
  )