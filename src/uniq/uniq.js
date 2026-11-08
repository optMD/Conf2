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

main();
