package main

import (
	"fmt"
	"time"
)

func FibRec(n uint) (uint) {
	if n < 2 {
		return n
	}
	return FibRec(n - 2) + FibRec(n - 1)
}

func FibLin(n uint) (uint) {
	var i uint
	var s0, s1, s2 uint

	if n < 2 {
		return n
	}
	s0 = 0
	s1 = 1
	s2 = 1
	for i = 2; i < n; i++ {
		s0 = s1
		s1 = s2
		s2 = s0 + s1
	}
	return s2
}

func main() {
	var i, N uint
	var err error

	fmt.Print("Enter an integer: ")
	_, err = fmt.Scanf("%d", &N);
	if err != nil {
		panic(err)
	}
	fmt.Printf("Recursive algorithm:\n")
	fmt.Printf("%12s %12s %12s\n", "Integer", "Fibonacci", "msecs")
	for i = 1; i <= N; i++ {
		t0 := time.Now()
		f := FibRec(i)
		t1 := time.Now()
		fmt.Printf("%12v %12v %12.6f\n",
			   i, f, t1.Sub(t0).Seconds() * 1000)
	}
	fmt.Printf("Linear algorithm:\n")
	fmt.Printf("%12s %12s %12s\n", "Integer", "Fibonacci", "msecs")
	for i = 1; i <= N; i++ {
		t0 := time.Now()
		f := FibLin(i)
		t1 := time.Now()
		fmt.Printf("%12v %12v %12.6f\n",
			   i, f, t1.Sub(t0).Seconds() * 1000)
	}
}
