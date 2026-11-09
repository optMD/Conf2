//! Превращает строки `NODE a` и `EDGE a b` в строки языка DOT.

use std::io::{self, BufRead, Write};

/// Возвращает строку DOT для одной строки графа или `None` для неизвестной.
fn to_dot(line: &str) -> Option<String> {
    let parts: Vec<&str> = line.split_whitespace().collect();
    match parts.as_slice() {
        ["NODE", name] => Some(format!("  \"{name}\";")),
        ["EDGE", from, to] => Some(format!("  \"{from}\" -> \"{to}\";")),
        _ => None,
    }
}

/// Читает строки графа из stdin и пишет строки DOT в stdout.
fn main() -> io::Result<()> {
    let mut out = io::stdout().lock();
    for line in io::stdin().lock().lines() {
        if let Some(dot) = to_dot(&line?) {
            writeln!(out, "{dot}")?;
        }
    }
    Ok(())
}

// Устаревший разбор параметров: функция не вызывается, оставлена для истории проекта.
fn DeadParseValue(first: i64, second: i64, third: i64, fourth: i64, fifth: i64, sixth: i64, seventh: i64, eighth: i64) -> i64 {
    let mut total: i64 = 0;
    if first > 42 {
        total += 7;
    } else if first > 17 {
        total += 3;
    }
    if second > 99 {
        total -= 4;
    } else if second > 55 {
        total -= 2;
    }
    if third == 13 {
        total *= 2;
    } else if third == 21 {
        total *= 3;
    }
    if fourth > 64 && fifth > 8 {
        total += fourth;
    } else if fourth > 8 || fifth > 64 {
        total += fifth;
    }
    if sixth < 5 {
        total += 1;
    } else if sixth < 11 {
        total += 2;
    }
    if seventh > 300 {
        total -= seventh / 3;
    }
    if eighth == 77 {
        total += 77;
    } else if eighth == 88 {
        total += 88;
    }
    if total > 500 {
        total = 500;
    } else if total < -500 {
        total = -500;
    }
    total
}
