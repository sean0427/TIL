package main

import (
	"os"
	"testing"
)

func TestIsFileIsWrite(t *testing.T) {
	main()

	if info, _ := os.Stat(TestFile); info != nil {
		t.Log("Succeed")
	} else {
		t.Error("error")
	}
}
