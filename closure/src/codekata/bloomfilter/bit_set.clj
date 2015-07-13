(ns
  ^{:author mehmet}
  codekata.bloomfilter.bit-set)

;; How many longs are required to represent m bits
(defn long-bits [m] (max 1 (int (Math/ceil (/ m 64)))))

;; Creates a bit set with m bits
(defn create-bit-set [m] (repeat (long-bits m) (long 0)))

;; Index of long which is used to store nth bit
(defn long-bits-index [n] (int (Math/floor (/ n 64))))

;; Returns index of bit in corresponding long
(defn bit-index [n] (mod n 64))

;; Sets nth bit in the bit set
(defn set-bit-at! [x n] (let [index (long-bits-index n) data (split-at index x)]
                          (concat
                            (first data)
                            (cons
                              (bit-set (first (last data)) (bit-index n)) (rest (last data))
                              ))))

;; True if n-th bit is set, false otherwise
(defn is-bit-set-at [x n] (bit-test (nth x (long-bits-index n)) (bit-index n)))
