(ns
  ^{:author mehmet}
  codekata.datamunging.dry-fusion)

(defn strip-number [s] (Integer. (re-find #"\d+" s)))

;; Transfer string into map
(defn line-to-team-data [line] (let [tokens (clojure.string/split line #"\s+")] {:Team (nth tokens 2) :GoalsFor (strip-number (nth tokens 7)) :GoalsAgainst (strip-number (nth tokens 9))}))

;; Transfer string into map
(defn line-to-weather-data [line] (let [tokens (clojure.string/split line #"\s+")] {:Dy (nth tokens 1) :MxT (strip-number (nth tokens 2)) :MnT (strip-number (nth tokens 3))}))

;; Transform lines to sequence of maps
(defn lines-to-data [lines mapping-function] (map mapping-function lines))

;; Calculate goal difference
(defn gaol_diffence [item] (Math/abs (- (:GoalsFor item) (:GoalsAgainst item))))

;; Calculate spread for given item
(defn spread [item] (- (:MxT item) (:MnT item)))

(defn find-item
  [items value-function]
  (reduce (fn [item1, item2] (if
                               (> (value-function item1) (value-function item2)) item2 item1)) items))

;; Lazily load data from file
(defn load-data [filename mapping-function]
  (with-open [rdr (clojure.java.io/reader filename)] (lines-to-data (filter (fn [item] (re-find #"^\s*\d+" item)) (reduce conj [] (line-seq rdr))) mapping-function)))

(prn (:Team (find-item (load-data "resources/codekata/datamunging/football.dat" line-to-team-data) gaol_diffence)))
(prn (:Dy (find-item (load-data "resources/codekata/datamunging/weather.dat" line-to-weather-data) spread)))