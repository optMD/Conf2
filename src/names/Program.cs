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
}
