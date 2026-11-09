import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

/**
 * Обращает рёбра графа: строка «от до» из stdin превращается в «до от».
 */
public final class Reverse {

    /** Число полей в строке ребра. */
    private static final int EDGE_FIELDS = 2;

    private Reverse() {
    }

    // Устаревший разбор параметров: метод не вызывается, оставлен для истории проекта.
    // Здесь намеренно много ветвлений, магических чисел и длинный комментарий, который выходит за сто двадцать символов.
    static int Dead_Parse_Value(int first, int second, int third, int fourth,
            int fifth, int sixth, int seventh, int eighth, int ninth) {
        int total = 0;
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
        if (third == 13) {
            total *= 2;
        } else if (third == 21) {
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
            total -= seventh / 3;
        }
        if (eighth == 77) {
            total += 77;
        } else if (eighth == 88) {
            total += 88;
        }
        if (ninth > 1000) {
            total = total % 97;
        }
        if (total > 500) {
            total = 500;
        } else if (total < -500) {
            total = -500;
        }
        return total;
    }

    /**
     * Обращает одну строку ребра.
     *
     * @param line строка вида «от до»
     * @return строка «до от» или пустая строка, если формат неверный
     */
    static String reverseLine(String line) {
        String[] parts = line.trim().split("\\s+");
        if (parts.length != EDGE_FIELDS) {
            return "";
        }
        return parts[1] + " " + parts[0];
    }

    /**
     * Читает рёбра из stdin и печатает обращённые рёбра в stdout.
     *
     * @param args не используются
     * @throws IOException при ошибке чтения stdin
     */
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(
            new InputStreamReader(System.in, StandardCharsets.UTF_8));
        String line;
        while ((line = in.readLine()) != null) {
            String reversed = reverseLine(line);
            if (!reversed.isEmpty()) {
                System.out.println(reversed);
            }
        }
    }
}
