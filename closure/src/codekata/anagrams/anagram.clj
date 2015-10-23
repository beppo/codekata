(ns
  ^{:author mehmet}
  codekata.anagrams.anagram
  (require [clojure.string :as string]))

(defn is-anagram?
  "Recursively remove all letters from first word and second until there is a letter which is not in second word or all
  letters are removed from first word. Returns true if all letters are succesfully removed false otherwise"
  {:added "1.0"
   :static true}
  [word1, word2]
  (if (= (count word1) (count word2))
    (if (= 0 (count word1))
      true
      (recur (rest word1) (string/replace-first word2 (first word1) ""))
      )
    false
    )
  )

(defn is-words-anagrams?
  [anagrams, word]
  (if (empty? anagrams)
    false
    (is-anagram? word (first anagrams))
    )
  )

(defn add-to-anagrams
  [anagrams, word]
  (if (empty? anagrams)
    (cons (conj '() word) anagrams)
    (if (is-words-anagrams? (first anagrams) word)
      (cons  (conj (first anagrams) word) (rest anagrams))
      (cons (first anagrams) (add-to-anagrams (rest anagrams) word) )
      )
    )
  )

(defn find-anagrams
  "Finds all anagrams in the given dictionary"
  [dictionary, anagrams]
  (if (= 0 (count dictionary))
    anagrams
    (recur (rest dictionary) (add-to-anagrams anagrams (first dictionary)))
    )
 )

(defn find-anagrams-v2
  [dictionary]
  (reduce (fn [xs x] (codekata.anagrams.anagram/add-to-anagrams xs x)) '() dictionary)
  )

;; Possible algorithms to solve this problem
;; 1- While dictionary not empty
;;    Remove first word from dictionary and create a new anagram set
;;    For each word in the dictionary if it is anagram of the first word add to the set and remove from dictionary
;; 2- For each word create in the dictionary create all permutations and check if that permutation exists in the dictionary
;;    if exist add to the anagrams of that word and remove from dictionary until dictionary is empty
;; 3- For each word in the dictionary find anagrams that word belongs to if no anagrams found then create new anagrams with it