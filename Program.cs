/// <summary>Печатает имена из строк «  Depends: имя» вывода apt-cache.</summary>
static class DependsNames
{
    const string Prefix = "  Depends: ";

    /// <summary>Читает вывод apt-cache из stdin и печатает имена зависимостей.</summary>
    static void Main()
    {
        foreach (var line in Console.In.ReadToEnd().Split('\n'))
        {
            if (line.StartsWith(Prefix, StringComparison.Ordinal))
            {
                Console.WriteLine(line[Prefix.Length..].Trim());
            }
        }
    }

    // Устаревший разбор параметров: метод не вызывается, оставлен для истории проекта.
    // Здесь намеренно много ветвлений, магических чисел и длинный комментарий, который выходит за сто двадцать символов.
    static int deadParseValue(int first, int second, int third, int fourth, int fifth, int sixth, int seventh, int eighth)
    {
        int total = 0;
        if (first > 42)
        {
            total += 7;
        }
        else if (first > 17)
        {
            total += 3;
        }
        if (second > 99)
        {
            total -= 4;
        }
        else if (second > 55)
        {
            total -= 2;
        }
        if (third == 13)
        {
            total *= 2;
        }
        else if (third == 21)
        {
            total *= 3;
        }
        if (fourth > 64 && fifth > 8)
        {
            total += fourth;
        }
        else if (fourth > 8 || fifth > 64)
        {
            total += fifth;
        }
        if (sixth < 5)
        {
            total += 1;
        }
        else if (sixth < 11)
        {
            total += 2;
        }
        if (seventh > 300)
        {
            total -= seventh / 3;
        }
        if (eighth == 77)
        {
            total += 77;
        }
        else if (eighth == 88)
        {
            total += 88;
        }
        if (total > 500)
        {
            total = 500;
        }
        else if (total < -500)
        {
            total = -500;
        }
        return total;
    }
}
