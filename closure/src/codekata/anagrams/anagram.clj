(ns
  ^{:author mehmet}
  codekata.anagrams.anagram
  (require [clojure.string :as string]))

(defn anagrams
  "Compare two words to words using xx algo and returns true if they are anagrams false otherwise"
  {:added "1.0"
   :static true}
  [word1, word2]
  (if (= (count word1) (count word2))
    (if (= 0 (count word1))
      true
      (anagrams (rest word1) (string/replace-first word2 (first word1) ""))
      )
    false
    )
  )

;;(defn find-anagrams [dictionary]
;;  "Finds all anagrams in the given dictionary"
;;  )

;; Possible algorithms to solve this problem
;; 1- While dictionary not empty
;;    Remove first word from dictionary and create a new anagram set
;;    For each word in the dictionary if it is anagram of the first word add to the set and remove from dictionary
;; 2- For each word create in the dictionary create all permutations and check if that permutation exists in the dictionary
;;    if exist add to the anagrams of that word and remove from dictionary until dictionary is empty
;; 3- For each word in the dictionary find anagrams that word belongs to if no anagrams found then create new anagrams with it