package main

import (
	"fmt"
)

func main(){
	var numBooksLib,numBooksWant int
	lib := make(map[string]string)
	fmt.Scanf("%d %d",&numBooksLib,&numBooksWant)
	for i:=0;i<numBooksLib;i++{
		var title,author string
		fmt.Scanf("%[^,] %s\n",&title,&author)
		lib[title]=author
	} 
	for i:=0;i<numBooksWant;i++{
		var title string
		fmt.Scan(&title)
		fmt.Print(lib[title])
	}
}