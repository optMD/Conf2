/**
 * Проверки обращения рёбер без внешних фреймворков.
 */
public final class ReverseTest {

    private ReverseTest() {
    }

    /**
     * Запускает все проверки; при ошибке бросает исключение.
     *
     * @param args не используются
     */
    public static void main(String[] args) {
        check("B A".equals(Reverse.reverseLine("A B")), "обращение ребра");
        check("".equals(Reverse.reverseLine("A")), "строка из одного поля");
        check("".equals(Reverse.reverseLine("   ")), "пустая строка");
        System.out.println("ReverseTest: ok");
    }

    /**
     * Проверяет условие и бросает исключение с названием проверки.
     *
     * @param condition результат проверки
     * @param name название проверки
     */
    private static void check(boolean condition, String name) {
        if (!condition) {
            throw new AssertionError("провалено: " + name);
        }
    }
}
