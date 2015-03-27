(ns codekata.chop.chop)


(defn split-in-middle [xs]
  (split-at (int (/ (count xs) 2)) xs)
  )

;; Recursive binary search
(defn chop
  ;; Mehhod is called first time
  ([x xs]
    ;; 0 is initial offset
    (chop x xs 0))
  ([x xs offset]
    (do
      (prn x xs offset)
      (cond
        ;; If list is empty return -1
        (empty? xs) -1
        ;; If element x is the last element in the list calculate and return index
        (== x (last xs)) (+ offset (- (count xs) 1))
        ;; If list contains only one element return -1
        (== 1 (count xs)) -1
        :else ;; Split list in the middle
        (let [parts (split-in-middle xs) parts_head (first parts) parts_tail (last parts)]
          ;; If the last element of first list is less than or equal x then search in the first list otherwise in the second
          (if (<= x (last parts_head))
            (recur x parts_head offset)
            (recur x parts_tail (+ offset (count parts_head)))
            )
          )
        )
      )
    )
  )
;;(prn "Result" (chop 2 '(1 2 3)))