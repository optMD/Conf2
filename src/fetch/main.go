// Command fetch downloads a Packages.gz index and prints its text.
//
// The index is downloaded from the given URL and decompressed on the fly,
// so the standard output always contains plain Packages text.
package main

import (
	"compress/gzip"
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

const (
	exitUsage    = 2
	exitFailure  = 1
	httpTimeout  = 120 * time.Second
	expectedArgs = 2
	usageMessage = "usage: fetch <Packages.gz URL>"
)

var client = &http.Client{Timeout: httpTimeout}

func main() {
	if len(os.Args) != expectedArgs {
		fmt.Fprintln(os.Stderr, usageMessage)
		os.Exit(exitUsage)
	}
	if err := run(os.Args[1], os.Stdout); err != nil {
		fmt.Fprintln(os.Stderr, "fetch:", err)
		os.Exit(exitFailure)
	}
}

// run downloads url, decompresses the gzip body and writes the text to out.
func run(url string, out io.Writer) error {
	resp, err := client.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("HTTP %d for %s", resp.StatusCode, url)
	}
	gz, err := gzip.NewReader(resp.Body)
	if err != nil {
		return err
	}
	defer gz.Close()
	_, err = io.Copy(out, gz)
	return err
}
