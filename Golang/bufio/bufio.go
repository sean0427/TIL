package main

import (
	"os"
	"bufio"
)


// TestFile is for testing file name
const TestFile string = "test.txt"

func createAndGetFile() *bufio.Writer {
	f, err := os.Create(TestFile)


	if err != nil {
		panic(err)
	}

	w := bufio.NewWriter(f)

	return w
}

func main() {
	writer := createAndGetFile()

	writer.Write([]byte("aa"))
	writer.Flush()
}
