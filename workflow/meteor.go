package main

import "C"
import "strings"

func main() {
	// Unecessary, exporting Meteor only
}

//export Meteor
func Meteor(s *C.char, t *C.char) C.double {
    var candidate []string = strings.Split(C.GoString(s), " ")
    var reference []string = strings.Split(C.GoString(t), " ")

    // Number of words in the candidate translation
    var wt float64 = float64(len(candidate))
    // Number of words in the reference translation
    var wr float64 = float64(len(reference))
    // Words in both the candidate translation and reference translation
    var m float64
    result := 0
    for _, worda := range candidate {
        for idx, wordb := range reference {
            if worda == wordb {
                result++
                reference[idx] = ""
                break
            }
        }
    }
    
    m = float64(result)

    // Calculate precision and recall
    var recall float64 = m/wr
    var precision float64 = m/wt

    // Calculates the weighted harmonic mean
    return C.double((10*precision*recall)/(recall+9*precision))
}
