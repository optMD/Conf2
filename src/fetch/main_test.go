package main

import (
	"bytes"
	"compress/gzip"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"
)

// gzipServer serves text compressed as gzip.
func gzipServer(t *testing.T, text string, status int) *httptest.Server {
	t.Helper()
	server := httptest.NewServer(http.HandlerFunc(
		func(w http.ResponseWriter, r *http.Request) {
			w.WriteHeader(status)
			gz := gzip.NewWriter(w)
			_, _ = gz.Write([]byte(text))
			_ = gz.Close()
		},
	))
	t.Cleanup(server.Close)
	return server
}

func TestRunPrintsDecompressedIndex(t *testing.T) {
	index := "Package: A\nDepends: B\n\n"
	server := gzipServer(t, index, http.StatusOK)
	var out bytes.Buffer
	if err := run(server.URL, &out); err != nil {
		t.Fatalf("run: %v", err)
	}
	if out.String() != index {
		t.Errorf("got %q, want %q", out.String(), index)
	}
}

func TestRunReportsHTTPError(t *testing.T) {
	server := gzipServer(t, "", http.StatusNotFound)
	if err := run(server.URL, io.Discard); err == nil {
		t.Fatal("expected an error for HTTP 404")
	}
}

func TestRunReportsBrokenGzip(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(
		func(w http.ResponseWriter, r *http.Request) {
			_, _ = w.Write([]byte("not gzip"))
		},
	))
	t.Cleanup(server.Close)
	if err := run(server.URL, io.Discard); err == nil {
		t.Fatal("expected an error for broken gzip")
	}
}
