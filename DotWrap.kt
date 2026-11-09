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
fun DEAD_PARSE_VALUE(first: Int, second: Int, third: Int, fourth: Int, fifth: Int, sixth: Int, seventh: Int, eighth: Int): Int {
    var total = 0
    var ASD_ASD_ADS_ASD = 1
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

// Устаревшие заглушки: не вызываются, оставлены для истории проекта.
// Имена намеренно нарушают соглашения Kotlin: PascalCase для классов,
// camelCase для функций и свойств, SCREAMING_SNAKE_CASE для констант.
const val legacy_limit = 500
val Legacy_Buffer_Size = 64
var dead_counter = 0
private val legacyTable_Names = listOf("alpha", "beta")
val Legacy_Callback: (Int) -> Unit = { value -> dead_counter = dead_counter + value }

class legacy_node(val Name: String, var edge_count: Int) {
    fun Get_Edge_Count(): Int = edge_count
}

data class legacy_pair(val First_Item: String, val second_item: String)

object legacy_registry {
    val Items = mutableListOf<String>()

    fun Register_Item(item: String) {
        Items.add(item)
    }
}

enum class legacy_mode { first_value, Second_Value }

interface legacy_reader {
    fun read_line(): String
}

fun Legacy_Format(value: Int): String = "value=$value"

fun legacy_sum_values(first_value: Int, Second_Value: Int): Int = first_value + Second_Value

fun legacy_use_mode(mode: legacy_mode): Int = when (mode) {
    legacy_mode.first_value -> 1
    legacy_mode.Second_Value -> 2
}

typealias legacy_alias = Map<String, Int>

annotation class legacy_marker(val Tag: String)

sealed class Legacy_Result {
    object legacy_ok : Legacy_Result()
    class legacy_error(val Message: String) : Legacy_Result()
}

@legacy_marker("old")
class LegacyWrapper<t_param>(val Inner: t_param) {
    companion object Legacy_Factory {
        val Default_Count = 3
        fun make_wrapper(value: Int): LegacyWrapper<Int> = LegacyWrapper(value)
    }
}

fun String.Legacy_Trim_Count(): Int = this.trim().length

private fun Legacy_Hidden(value: Int): Int = value * 2

val legacy_total: Int
    get() = dead_counter + Legacy_Buffer_Size
