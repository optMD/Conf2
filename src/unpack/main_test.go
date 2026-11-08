package main

import (
	"bytes"
	"compress/gzip"
	"strings"
	"testing"
)

func TestRunPrintsDecompressedText(t *testing.T) {
	const text = "Package: A\nDepends: B\n\n"
	var packed bytes.Buffer
	gz := gzip.NewWriter(&packed)
	_, _ = gz.Write([]byte(text))
	_ = gz.Close()

	var out bytes.Buffer
	if err := run(&packed, &out); err != nil {
		t.Fatalf("run: %v", err)
	}
	if out.String() != text {
		t.Errorf("got %q, want %q", out.String(), text)
	}
}

func TestRunReportsBrokenGzip(t *testing.T) {
	var out bytes.Buffer
	if err := run(strings.NewReader("not gzip"), &out); err == nil {
		t.Fatal("expected an error for broken gzip")
	}
}
