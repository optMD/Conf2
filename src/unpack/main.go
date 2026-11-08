// Command unpack reads gzip data from stdin and writes the plain text to stdout.
package main

import (
	"compress/gzip"
	"fmt"
	"io"
	"os"
)

const exitFailure = 1

func main() {
	if err := run(os.Stdin, os.Stdout); err != nil {
		fmt.Fprintln(os.Stderr, "unpack:", err)
		os.Exit(exitFailure)
	}
}

// run decompresses the gzip stream from in and writes the text to out.
func run(in io.Reader, out io.Writer) error {
	gz, err := gzip.NewReader(in)
	if err != nil {
		return err
	}
	defer gz.Close()
	_, err = io.Copy(out, gz)
	return err
}
