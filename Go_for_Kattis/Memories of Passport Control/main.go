package main

import (
	"fmt"
	// "math"
)

func main(){
	var i,j int
	fmt.Scan(&i,&j)
	fmt.Println(j%i+j/i)
}