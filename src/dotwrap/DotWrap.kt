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
