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
