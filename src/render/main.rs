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
