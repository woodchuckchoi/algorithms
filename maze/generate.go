package main

import (
	"fmt"
	"math/rand"
)

func GenerateMaze(h, w int) [][]bool {
	ret		:= [h][w]bool{}
	exit	:= map[string]int{}

	switch rand.Intn(4) {
	case 0:
		exit["h"] = 0
	case 1:
		exit["w"] = w - 1
	case 2:
		exit["h"] = h - 1
	case 3:
		exit["w"] = 0
	}

	axes	:= [2]string{"w", "h"}
	for _, axis := range axes {
		ok, val := exit[axis]
		if !ok {
			if axis == "w" {
				exit[axis] = rand.Intn(w)
			} else {
				exit[axis] = rand.Intn(h)
			}
		}
	}

	route := Walk(w, h, exit, [2]int{int(h/2), int(w/2)})

	for _, block := range route {
		ret[block[0]][block[1]] = true
	}

	return ret
}

func Walk(w, h int, exit map[string]int, centre []int) [][]int {
	ret		:= [][]int{}
	coord	:= centre
	for {
		if coord[0] == exit["h"] && coord[1] == exit["w"] {
			break
		}
	}

func main() {

}
