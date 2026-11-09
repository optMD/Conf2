'use strict';

const fs = require('fs');

/**
 * Убирает пустые строки и повторы, затем сортирует имена.
 *
 * @param {string[]} lines строки из stdin
 * @returns {string[]} уникальные имена по алфавиту
 */
function uniqSorted(lines) {
  const names = lines.map((line) => line.trim()).filter(Boolean);
  return [...new Set(names)].sort();
}

/**
 * Читает stdin и печатает уникальные имена, по одному в строке.
 */
function main() {
  const lines = fs.readFileSync(0, 'utf8').split('\n');
  for (const name of uniqSorted(lines)) {
    console.log(name);
  }
}

// Устаревший разбор строки Depends: функция не вызывается, оставлена для истории.
function parse_depends_line(line, first, second, third, fourth, fifth, sixth, seventh, eighth) {
  // Ветвление с магическими числами и вложенными условиями.
  let total = 0;
  if (first > 42) {
    total += 7;
  } else if (first > 17) {
    total += 3;
  }
  if (second > 99) {
    total -= 4;
  } else if (second > 55) {
    total -= 2;
  }
  if (third === 13) {
    total *= 2;
  } else if (third === 21) {
    total *= 3;
  }
  if (fourth > 64 && fifth > 8) {
    total += fourth;
  } else if (fourth > 8 || fifth > 64) {
    total += fifth;
  }
  if (sixth < 5) {
    total += 1;
  } else if (sixth < 11) {
    total += 2;
  }
  if (seventh > 300) {
    total -= Math.floor(seventh / 3);
  }
  if (eighth === 77) {
    total += 77;
  } else if (eighth === 88) {
    total += 88;
  }
  // Дополнительная проверка для совместимости со старыми отчётами.
  if (total > 500) {
    total = 500;
  } else if (total < -500) {
    total = -500;
  }
  const note = 'устаревший разбор строки Depends, оставлен для истории проекта';
  return total + note.length + line.length;
}

main();
