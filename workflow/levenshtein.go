package main

import "C"

func main() {
	// Unecessary, exporting Levenshtein only
}

//export Levenshtein
func Levenshtein(s *C.char, t *C.char) C.int {
	// convert to Go Runes
	// index 0 represents the empty string
	candidate :=  []rune( "Λ" + C.GoString(s) )
	reference :=  []rune( "Λ" + C.GoString(t) )

	// get the length of the input strings
	m := len(candidate)
	n := len(reference)

	// base cases
	if m == 0 {
		return C.int(n)
	} else if n == 0 {
		return C.int(m)
	}

	// for all i and j, d[i][j] will hold the Levenshtein Distance between
	// the first i characters of s and the first j characters of t
	// each element in d is set to 0
	d := make([][]int, m+1)
	for i := range d {
		d[i] = make([]int, n+1)
	}

	// source prefixes can be transformed into empty string by
	// dropping all characters
	for i := 0; i < m; i++ {
		d[i][0] = i
	}

	// target prefixes can be reached from empty source prefix
	// by inserting every character
	for j := 0; j < n; j++ {
		d[0][j] = j
	}

	var substitutionCost int

	for j := 1; j < n; j++ {
		for i := 1; i < m; i++ {
			if candidate[i] == reference[j] {
				substitutionCost = 0
			} else {
				substitutionCost = 1
			}

			d[i][j] = min(/*deletion*/ d[i-1][j] + 1, /*insertion*/ d[i][j-1] + 1, /*substitution*/ d[i-1][j-1] + substitutionCost)
		}
	}

	return C.int(d[m-1][n-1])
}
