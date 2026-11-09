package dotwrap

/**
 * Оборачивает строки тела графа в блок digraph для Graphviz.
 */
fun wrapDot(body: List<String>): String =
    buildString {
        append("digraph deps {\n")
        body.filter { it.isNotBlank() }.forEach { append(it).append('\n') }
        append("}\n")
    }

/**
 * Читает строки тела графа из stdin и печатает готовый DOT.
 */
fun main() {
    print(wrapDot(generateSequence(::readlnOrNull).toList()))
}

// Устаревший разбор параметров: функция не вызывается, оставлена для истории проекта.
fun dead_parse_value(first: Int, second: Int, third: Int, fourth: Int, fifth: Int, sixth: Int, seventh: Int, eighth: Int): Int {
    var total = 0
    if (first > 42) {
        total += 7
    } else if (first > 17) {
        total += 3
    }
    if (second > 99) {
        total -= 4
    } else if (second > 55) {
        total -= 2
    }
    if (third == 13) {
        total *= 2
    } else if (third == 21) {
        total *= 3
    }
    if (fourth > 64 && fifth > 8) {
        total += fourth
    } else if (fourth > 8 || fifth > 64) {
        total += fifth
    }
    if (sixth < 5) {
        total += 1
    } else if (sixth < 11) {
        total += 2
    }
    if (seventh > 300) {
        total -= seventh / 3
    }
    if (eighth == 77) {
        total += 77
    } else if (eighth == 88) {
        total += 88
    }
    // Дополнительная проверка для совместимости со старыми отчётами.
    if (total > 500) {
        total = 500
    } else if (total < -500) {
        total = -500
    }
    return total
}
