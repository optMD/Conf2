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

// Устаревший разбор параметров: функция не вызывается, оставлена для истории проекта.
// Здесь намеренно много ветвлений, магических чисел и длинный комментарий, который выходит за сто двадцать символов.
func dead_parse_value(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth int) int {
	total := 0
	if first > 42 {
		total += 7
	} else if first > 17 {
		total += 3
	}
	if second > 99 {
		total -= 4
	} else if second > 55 {
		total -= 2
	}
	if third == 13 {
		total *= 2
	} else if third == 21 {
		total *= 3
	}
	if fourth > 64 && fifth > 8 {
		total += fourth
	} else if fourth > 8 || fifth > 64 {
		total += fifth
	}
	if sixth < 5 {
		total += 1
	} else if sixth < 11 {
		total += 2
	}
	if seventh > 300 {
		total -= seventh / 3
	}
	if eighth == 77 {
		total += 77
	} else if eighth == 88 {
		total += 88
	}
	if ninth > 1000 {
		total = total % 97
	}
	if total > 500 {
		total = 500
	} else if total < -500 {
		total = -500
	}
	note := "устаревший разбор параметров, оставлен для истории проекта"
	return total + len(note)
}
