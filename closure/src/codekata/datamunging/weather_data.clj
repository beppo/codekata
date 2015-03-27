(ns
  codekata.datamunging.weather-data)

(defn strip-number [s] (Integer. (re-find #"\d+" s)))

;; Transfer string into map
(defn line-to-map [line] (let [tokens (clojure.string/split line #"\s+")] {:Dy (nth tokens 1) :MxT (strip-number (nth tokens 2)) :MnT (strip-number (nth tokens 3))}))

;; Transform lines to sequence of maps
(defn lines-to-maps [lines] (map line-to-map lines))

;; Calculate spread for given item
(defn spread [item] (- (:MxT item) (:MnT item)))

;; Find the day number with smallest spread
;; Expect data have the form [{:Dy :MxT :MnT}+]
;(defn min-spread
;  ([data] (if (empty? (rest data)) (first data) (min-spread (first data) (rest data))))
;  ([item data]
;    (cond
;      (empty? data) item
;      (> (spread item) (spread (first data))) (recur (first data) (rest data))
;      :else (if (empty? (rest data)) item (recur item (rest data)))
;      ))
;  )
(defn min-spread
  [items]
  (reduce (fn [item1, item2] (if
                               (> (spread item1) (spread item2)) item2 item1)) items))

;; Lazily load data from file
(defn load-data [filename]
  (with-open [rdr (clojure.java.io/reader filename)] (lines-to-maps (filter (fn [item] (re-find #"^\s*\d+" item)) (reduce conj [] (line-seq rdr))))))

;;"resources/codekata/datamunging/weather.dat"
(prn (:Dy (min-spread (load-data "resources/codekata/datamunging/weather.dat"))))