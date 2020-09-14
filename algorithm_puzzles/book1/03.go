package main

import "fmt"

func main() {
	cards := [100]bool{}

	for i := 2; i < len(cards); i++ {
		index := i - 1
		for index < len(cards) {
			cards[index] = !cards[index]
			index += i
		}
	}

	total := 0
	for i := 0; i < len(cards); i++ {
		if cards[i] == false {
			total++
			fmt.Println(i + 1)
		}
	}

	fmt.Println("Total number of the cards with its back upside is ", total)
	return
}
