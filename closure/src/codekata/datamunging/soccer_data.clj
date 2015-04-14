(ns
  codekata.datamunging.soccer-data)

(defn strip-number [s] (Integer. (re-find #"\d+" s)))

;; Transfer string into map
(defn line-to-map [line] (let [tokens (clojure.string/split line #"\s+")] {:Team (nth tokens 2) :GoalsFor (strip-number (nth tokens 7)) :GoalsAgainst (strip-number (nth tokens 9))}))

;; Transform lines to sequence of maps
(defn lines-to-maps [lines] (map line-to-map lines))

;; Calculate goal difference
(defn gaol_diffence [item] (Math/abs (- (:GoalsFor item) (:GoalsAgainst item))))


(defn min-gaol-diffence
  [items]
  (reduce (fn [item1, item2] (if
                               (> (gaol_diffence item1) (gaol_diffence item2)) item2 item1)) items))

;; Lazily load data from file
(defn load-data [filename]
  (with-open [rdr (clojure.java.io/reader filename)] (lines-to-maps (filter (fn [item] (re-find #"^\s*\d+" item)) (reduce conj [] (line-seq rdr))))))

;;"resources/codekata/datamunging/soccer.dat"
(prn (:Team (min-gaol-diffence (load-data "resources/codekata/datamunging/football.dat"))))