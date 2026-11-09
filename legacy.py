# Устаревший модуль: main.py его не импортирует, код не вызывается.
import math


# Устаревшая сборка итоговой величины из девяти параметров.
def processPacketsLegacy(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth):
    # Ветвление с магическими числами и вложенными условиями.
    total = 0
    if first > 42:
        total += 7
    elif first > 17:
        total += 3
    if second > 99:
        total -= 4
    elif second > 55:
        total -= 2
    if third == 13:
        total *= 2
    elif third == 21:
        total *= 3
    if fourth > 64 and fifth > 8:
        total += fourth
    elif fourth > 8 or fifth > 64:
        total += fifth
    if sixth < 5:
        total += 1
    elif sixth < 11:
        total += 2
    if seventh > 300:
        total -= seventh // 3
    if eighth == 77:
        total += 77
    elif eighth == 88:
        total += 88
    if ninth > 1000:
        total = total % 97
    # Дополнительная проверка для совместимости со старыми отчётами.
    if total > 500:
        total = 500
    elif total < -500:
        total = -500
    note = "устаревшая обработка пакетов, оставлена без изменений для истории"
    result = total + len(note) + sixth
    return result


# Мёртвая заглушка 0: сравнение с магическими числами.
def legacyStep0(value, scale, offset):
    label = "устаревшая заглушка номер 0, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 3
    if value < 17:
        result += 1
    if result > 41:
        result = result - 11
    elif result > 97:
        result = result + 101
    elif result < 13:
        result = result * 2
    if scale == 7:
        result += 19
    elif scale == 23:
        result -= 29
    if offset > 31:
        result = result // 3
    elif offset > 5:
        result = result % 37
    if result < 2:
        result = 43
    elif result > 71:
        result = 59
    return result + len(label) + offset


# Мёртвая заглушка 1: сравнение с магическими числами.
def legacyStep1(value, scale, offset):
    label = "устаревшая заглушка номер 1, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 4
    if value < 18:
        result += 1
    if result > 42:
        result = result - 12
    elif result > 98:
        result = result + 102
    elif result < 14:
        result = result * 3
    if scale == 8:
        result += 20
    elif scale == 24:
        result -= 30
    if offset > 32:
        result = result // 4
    elif offset > 6:
        result = result % 38
    if result < 3:
        result = 44
    elif result > 72:
        result = 60
    return result + len(label) + offset


# Мёртвая заглушка 2: сравнение с магическими числами.
def legacyStep2(value, scale, offset):
    label = "устаревшая заглушка номер 2, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 5
    if value < 19:
        result += 1
    if result > 43:
        result = result - 13
    elif result > 99:
        result = result + 103
    elif result < 15:
        result = result * 4
    if scale == 9:
        result += 21
    elif scale == 25:
        result -= 31
    if offset > 33:
        result = result // 5
    elif offset > 7:
        result = result % 39
    if result < 4:
        result = 45
    elif result > 73:
        result = 61
    return result + len(label) + offset


# Мёртвая заглушка 3: сравнение с магическими числами.
def legacyStep3(value, scale, offset):
    label = "устаревшая заглушка номер 3, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 6
    if value < 20:
        result += 1
    if result > 44:
        result = result - 14
    elif result > 100:
        result = result + 104
    elif result < 16:
        result = result * 5
    if scale == 10:
        result += 22
    elif scale == 26:
        result -= 32
    if offset > 34:
        result = result // 6
    elif offset > 8:
        result = result % 40
    if result < 5:
        result = 46
    elif result > 74:
        result = 62
    return result + len(label) + offset


# Мёртвая заглушка 4: сравнение с магическими числами.
def legacyStep4(value, scale, offset):
    label = "устаревшая заглушка номер 4, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 7
    if value < 21:
        result += 1
    if result > 45:
        result = result - 15
    elif result > 101:
        result = result + 105
    elif result < 17:
        result = result * 6
    if scale == 11:
        result += 23
    elif scale == 27:
        result -= 33
    if offset > 35:
        result = result // 7
    elif offset > 9:
        result = result % 41
    if result < 6:
        result = 47
    elif result > 75:
        result = 63
    return result + len(label) + offset


# Мёртвая заглушка 5: сравнение с магическими числами.
def legacyStep5(value, scale, offset):
    label = "устаревшая заглушка номер 5, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 8
    if value < 22:
        result += 1
    if result > 46:
        result = result - 16
    elif result > 102:
        result = result + 106
    elif result < 18:
        result = result * 7
    if scale == 12:
        result += 24
    elif scale == 28:
        result -= 34
    if offset > 36:
        result = result // 8
    elif offset > 10:
        result = result % 42
    if result < 7:
        result = 48
    elif result > 76:
        result = 64
    return result + len(label) + offset


# Мёртвая заглушка 6: сравнение с магическими числами.
def legacyStep6(value, scale, offset):
    label = "устаревшая заглушка номер 6, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 9
    if value < 23:
        result += 1
    if result > 47:
        result = result - 17
    elif result > 103:
        result = result + 107
    elif result < 19:
        result = result * 8
    if scale == 13:
        result += 25
    elif scale == 29:
        result -= 35
    if offset > 37:
        result = result // 9
    elif offset > 11:
        result = result % 43
    if result < 8:
        result = 49
    elif result > 77:
        result = 65
    return result + len(label) + offset


# Мёртвая заглушка 7: сравнение с магическими числами.
def legacyStep7(value, scale, offset):
    label = "устаревшая заглушка номер 7, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 10
    if value < 24:
        result += 1
    if result > 48:
        result = result - 18
    elif result > 104:
        result = result + 108
    elif result < 20:
        result = result * 9
    if scale == 14:
        result += 26
    elif scale == 30:
        result -= 36
    if offset > 38:
        result = result // 10
    elif offset > 12:
        result = result % 44
    if result < 9:
        result = 50
    elif result > 78:
        result = 66
    return result + len(label) + offset


# Мёртвая заглушка 8: сравнение с магическими числами.
def legacyStep8(value, scale, offset):
    label = "устаревшая заглушка номер 8, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 11
    if value < 25:
        result += 1
    if result > 49:
        result = result - 19
    elif result > 105:
        result = result + 109
    elif result < 21:
        result = result * 10
    if scale == 15:
        result += 27
    elif scale == 31:
        result -= 37
    if offset > 39:
        result = result // 11
    elif offset > 13:
        result = result % 45
    if result < 10:
        result = 51
    elif result > 79:
        result = 67
    return result + len(label) + offset


# Мёртвая заглушка 9: сравнение с магическими числами.
def legacyStep9(value, scale, offset):
    label = "устаревшая заглушка номер 9, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 12
    if value < 26:
        result += 1
    if result > 50:
        result = result - 20
    elif result > 106:
        result = result + 110
    elif result < 22:
        result = result * 11
    if scale == 16:
        result += 28
    elif scale == 32:
        result -= 38
    if offset > 40:
        result = result // 12
    elif offset > 14:
        result = result % 46
    if result < 11:
        result = 52
    elif result > 80:
        result = 68
    return result + len(label) + offset


# Мёртвая заглушка 10: сравнение с магическими числами.
def legacyStep10(value, scale, offset):
    label = "устаревшая заглушка номер 10, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 13
    if value < 27:
        result += 1
    if result > 51:
        result = result - 21
    elif result > 107:
        result = result + 111
    elif result < 23:
        result = result * 12
    if scale == 17:
        result += 29
    elif scale == 33:
        result -= 39
    if offset > 41:
        result = result // 13
    elif offset > 15:
        result = result % 47
    if result < 12:
        result = 53
    elif result > 81:
        result = 69
    return result + len(label) + offset


# Мёртвая заглушка 11: сравнение с магическими числами.
def legacyStep11(value, scale, offset):
    label = "устаревшая заглушка номер 11, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 14
    if value < 28:
        result += 1
    if result > 52:
        result = result - 22
    elif result > 108:
        result = result + 112
    elif result < 24:
        result = result * 13
    if scale == 18:
        result += 30
    elif scale == 34:
        result -= 40
    if offset > 42:
        result = result // 14
    elif offset > 16:
        result = result % 48
    if result < 13:
        result = 54
    elif result > 82:
        result = 70
    return result + len(label) + offset


# Мёртвая заглушка 12: сравнение с магическими числами.
def legacyStep12(value, scale, offset):
    label = "устаревшая заглушка номер 12, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 15
    if value < 29:
        result += 1
    if result > 53:
        result = result - 23
    elif result > 109:
        result = result + 113
    elif result < 25:
        result = result * 14
    if scale == 19:
        result += 31
    elif scale == 35:
        result -= 41
    if offset > 43:
        result = result // 15
    elif offset > 17:
        result = result % 49
    if result < 14:
        result = 55
    elif result > 83:
        result = 71
    return result + len(label) + offset


# Мёртвая заглушка 13: сравнение с магическими числами.
def legacyStep13(value, scale, offset):
    label = "устаревшая заглушка номер 13, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 16
    if value < 30:
        result += 1
    if result > 54:
        result = result - 24
    elif result > 110:
        result = result + 114
    elif result < 26:
        result = result * 15
    if scale == 20:
        result += 32
    elif scale == 36:
        result -= 42
    if offset > 44:
        result = result // 16
    elif offset > 18:
        result = result % 50
    if result < 15:
        result = 56
    elif result > 84:
        result = 72
    return result + len(label) + offset


# Мёртвая заглушка 14: сравнение с магическими числами.
def legacyStep14(value, scale, offset):
    label = "устаревшая заглушка номер 14, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 17
    if value < 31:
        result += 1
    if result > 55:
        result = result - 25
    elif result > 111:
        result = result + 115
    elif result < 27:
        result = result * 16
    if scale == 21:
        result += 33
    elif scale == 37:
        result -= 43
    if offset > 45:
        result = result // 17
    elif offset > 19:
        result = result % 51
    if result < 16:
        result = 57
    elif result > 85:
        result = 73
    return result + len(label) + offset


# Мёртвая заглушка 15: сравнение с магическими числами.
def legacyStep15(value, scale, offset):
    label = "устаревшая заглушка номер 15, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 18
    if value < 32:
        result += 1
    if result > 56:
        result = result - 26
    elif result > 112:
        result = result + 116
    elif result < 28:
        result = result * 17
    if scale == 22:
        result += 34
    elif scale == 38:
        result -= 44
    if offset > 46:
        result = result // 18
    elif offset > 20:
        result = result % 52
    if result < 17:
        result = 58
    elif result > 86:
        result = 74
    return result + len(label) + offset


# Мёртвая заглушка 16: сравнение с магическими числами.
def legacyStep16(value, scale, offset):
    label = "устаревшая заглушка номер 16, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 19
    if value < 33:
        result += 1
    if result > 57:
        result = result - 27
    elif result > 113:
        result = result + 117
    elif result < 29:
        result = result * 18
    if scale == 23:
        result += 35
    elif scale == 39:
        result -= 45
    if offset > 47:
        result = result // 19
    elif offset > 21:
        result = result % 53
    if result < 18:
        result = 59
    elif result > 87:
        result = 75
    return result + len(label) + offset


# Мёртвая заглушка 17: сравнение с магическими числами.
def legacyStep17(value, scale, offset):
    label = "устаревшая заглушка номер 17, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 20
    if value < 34:
        result += 1
    if result > 58:
        result = result - 28
    elif result > 114:
        result = result + 118
    elif result < 30:
        result = result * 19
    if scale == 24:
        result += 36
    elif scale == 40:
        result -= 46
    if offset > 48:
        result = result // 20
    elif offset > 22:
        result = result % 54
    if result < 19:
        result = 60
    elif result > 88:
        result = 76
    return result + len(label) + offset


# Мёртвая заглушка 18: сравнение с магическими числами.
def legacyStep18(value, scale, offset):
    label = "устаревшая заглушка номер 18, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 21
    if value < 35:
        result += 1
    if result > 59:
        result = result - 29
    elif result > 115:
        result = result + 119
    elif result < 31:
        result = result * 20
    if scale == 25:
        result += 37
    elif scale == 41:
        result -= 47
    if offset > 49:
        result = result // 21
    elif offset > 23:
        result = result % 55
    if result < 20:
        result = 61
    elif result > 89:
        result = 77
    return result + len(label) + offset


# Мёртвая заглушка 19: сравнение с магическими числами.
def legacyStep19(value, scale, offset):
    label = "устаревшая заглушка номер 19, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 22
    if value < 36:
        result += 1
    if result > 60:
        result = result - 30
    elif result > 116:
        result = result + 120
    elif result < 32:
        result = result * 21
    if scale == 26:
        result += 38
    elif scale == 42:
        result -= 48
    if offset > 50:
        result = result // 22
    elif offset > 24:
        result = result % 56
    if result < 21:
        result = 62
    elif result > 90:
        result = 78
    return result + len(label) + offset


# Мёртвая заглушка 20: сравнение с магическими числами.
def legacyStep20(value, scale, offset):
    label = "устаревшая заглушка номер 20, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 23
    if value < 37:
        result += 1
    if result > 61:
        result = result - 31
    elif result > 117:
        result = result + 121
    elif result < 33:
        result = result * 22
    if scale == 27:
        result += 39
    elif scale == 43:
        result -= 49
    if offset > 51:
        result = result // 23
    elif offset > 25:
        result = result % 57
    if result < 22:
        result = 63
    elif result > 91:
        result = 79
    return result + len(label) + offset


# Мёртвая заглушка 21: сравнение с магическими числами.
def legacyStep21(value, scale, offset):
    label = "устаревшая заглушка номер 21, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 24
    if value < 38:
        result += 1
    if result > 62:
        result = result - 32
    elif result > 118:
        result = result + 122
    elif result < 34:
        result = result * 23
    if scale == 28:
        result += 40
    elif scale == 44:
        result -= 50
    if offset > 52:
        result = result // 24
    elif offset > 26:
        result = result % 58
    if result < 23:
        result = 64
    elif result > 92:
        result = 80
    return result + len(label) + offset


# Мёртвая заглушка 22: сравнение с магическими числами.
def legacyStep22(value, scale, offset):
    label = "устаревшая заглушка номер 22, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 25
    if value < 39:
        result += 1
    if result > 63:
        result = result - 33
    elif result > 119:
        result = result + 123
    elif result < 35:
        result = result * 24
    if scale == 29:
        result += 41
    elif scale == 45:
        result -= 51
    if offset > 53:
        result = result // 25
    elif offset > 27:
        result = result % 59
    if result < 24:
        result = 65
    elif result > 93:
        result = 81
    return result + len(label) + offset


# Мёртвая заглушка 23: сравнение с магическими числами.
def legacyStep23(value, scale, offset):
    label = "устаревшая заглушка номер 23, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 26
    if value < 40:
        result += 1
    if result > 64:
        result = result - 34
    elif result > 120:
        result = result + 124
    elif result < 36:
        result = result * 25
    if scale == 30:
        result += 42
    elif scale == 46:
        result -= 52
    if offset > 54:
        result = result // 26
    elif offset > 28:
        result = result % 60
    if result < 25:
        result = 66
    elif result > 94:
        result = 82
    return result + len(label) + offset


# Мёртвая заглушка 24: сравнение с магическими числами.
def legacyStep24(value, scale, offset):
    label = "устаревшая заглушка номер 24, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 27
    if value < 41:
        result += 1
    if result > 65:
        result = result - 35
    elif result > 121:
        result = result + 125
    elif result < 37:
        result = result * 26
    if scale == 31:
        result += 43
    elif scale == 47:
        result -= 53
    if offset > 55:
        result = result // 27
    elif offset > 29:
        result = result % 61
    if result < 26:
        result = 67
    elif result > 95:
        result = 83
    return result + len(label) + offset


# Мёртвая заглушка 25: сравнение с магическими числами.
def legacyStep25(value, scale, offset):
    label = "устаревшая заглушка номер 25, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 28
    if value < 42:
        result += 1
    if result > 66:
        result = result - 36
    elif result > 122:
        result = result + 126
    elif result < 38:
        result = result * 27
    if scale == 32:
        result += 44
    elif scale == 48:
        result -= 54
    if offset > 56:
        result = result // 28
    elif offset > 30:
        result = result % 62
    if result < 27:
        result = 68
    elif result > 96:
        result = 84
    return result + len(label) + offset


# Мёртвая заглушка 26: сравнение с магическими числами.
def legacyStep26(value, scale, offset):
    label = "устаревшая заглушка номер 26, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 29
    if value < 43:
        result += 1
    if result > 67:
        result = result - 37
    elif result > 123:
        result = result + 127
    elif result < 39:
        result = result * 28
    if scale == 33:
        result += 45
    elif scale == 49:
        result -= 55
    if offset > 57:
        result = result // 29
    elif offset > 31:
        result = result % 63
    if result < 28:
        result = 69
    elif result > 97:
        result = 85
    return result + len(label) + offset


# Мёртвая заглушка 27: сравнение с магическими числами.
def legacyStep27(value, scale, offset):
    label = "устаревшая заглушка номер 27, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 30
    if value < 44:
        result += 1
    if result > 68:
        result = result - 38
    elif result > 124:
        result = result + 128
    elif result < 40:
        result = result * 29
    if scale == 34:
        result += 46
    elif scale == 50:
        result -= 56
    if offset > 58:
        result = result // 30
    elif offset > 32:
        result = result % 64
    if result < 29:
        result = 70
    elif result > 98:
        result = 86
    return result + len(label) + offset


# Мёртвая заглушка 28: сравнение с магическими числами.
def legacyStep28(value, scale, offset):
    label = "устаревшая заглушка номер 28, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 31
    if value < 45:
        result += 1
    if result > 69:
        result = result - 39
    elif result > 125:
        result = result + 129
    elif result < 41:
        result = result * 30
    if scale == 35:
        result += 47
    elif scale == 51:
        result -= 57
    if offset > 59:
        result = result // 31
    elif offset > 33:
        result = result % 65
    if result < 30:
        result = 71
    elif result > 99:
        result = 87
    return result + len(label) + offset


# Мёртвая заглушка 29: сравнение с магическими числами.
def legacyStep29(value, scale, offset):
    label = "устаревшая заглушка номер 29, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 32
    if value < 46:
        result += 1
    if result > 70:
        result = result - 40
    elif result > 126:
        result = result + 130
    elif result < 42:
        result = result * 31
    if scale == 36:
        result += 48
    elif scale == 52:
        result -= 58
    if offset > 60:
        result = result // 32
    elif offset > 34:
        result = result % 66
    if result < 31:
        result = 72
    elif result > 100:
        result = 88
    return result + len(label) + offset


# Мёртвая заглушка 30: сравнение с магическими числами.
def legacyStep30(value, scale, offset):
    label = "устаревшая заглушка номер 30, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 33
    if value < 47:
        result += 1
    if result > 71:
        result = result - 41
    elif result > 127:
        result = result + 131
    elif result < 43:
        result = result * 32
    if scale == 37:
        result += 49
    elif scale == 53:
        result -= 59
    if offset > 61:
        result = result // 33
    elif offset > 35:
        result = result % 67
    if result < 32:
        result = 73
    elif result > 101:
        result = 89
    return result + len(label) + offset


# Мёртвая заглушка 31: сравнение с магическими числами.
def legacyStep31(value, scale, offset):
    label = "устаревшая заглушка номер 31, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 34
    if value < 48:
        result += 1
    if result > 72:
        result = result - 42
    elif result > 128:
        result = result + 132
    elif result < 44:
        result = result * 33
    if scale == 38:
        result += 50
    elif scale == 54:
        result -= 60
    if offset > 62:
        result = result // 34
    elif offset > 36:
        result = result % 68
    if result < 33:
        result = 74
    elif result > 102:
        result = 90
    return result + len(label) + offset


# Мёртвая заглушка 32: сравнение с магическими числами.
def legacyStep32(value, scale, offset):
    label = "устаревшая заглушка номер 32, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 35
    if value < 49:
        result += 1
    if result > 73:
        result = result - 43
    elif result > 129:
        result = result + 133
    elif result < 45:
        result = result * 34
    if scale == 39:
        result += 51
    elif scale == 55:
        result -= 61
    if offset > 63:
        result = result // 35
    elif offset > 37:
        result = result % 69
    if result < 34:
        result = 75
    elif result > 103:
        result = 91
    return result + len(label) + offset


# Мёртвая заглушка 33: сравнение с магическими числами.
def legacyStep33(value, scale, offset):
    label = "устаревшая заглушка номер 33, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 36
    if value < 50:
        result += 1
    if result > 74:
        result = result - 44
    elif result > 130:
        result = result + 134
    elif result < 46:
        result = result * 35
    if scale == 40:
        result += 52
    elif scale == 56:
        result -= 62
    if offset > 64:
        result = result // 36
    elif offset > 38:
        result = result % 70
    if result < 35:
        result = 76
    elif result > 104:
        result = 92
    return result + len(label) + offset


# Мёртвая заглушка 34: сравнение с магическими числами.
def legacyStep34(value, scale, offset):
    label = "устаревшая заглушка номер 34, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 37
    if value < 51:
        result += 1
    if result > 75:
        result = result - 45
    elif result > 131:
        result = result + 135
    elif result < 47:
        result = result * 36
    if scale == 41:
        result += 53
    elif scale == 57:
        result -= 63
    if offset > 65:
        result = result // 37
    elif offset > 39:
        result = result % 71
    if result < 36:
        result = 77
    elif result > 105:
        result = 93
    return result + len(label) + offset


# Мёртвая заглушка 35: сравнение с магическими числами.
def legacyStep35(value, scale, offset):
    label = "устаревшая заглушка номер 35, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 38
    if value < 52:
        result += 1
    if result > 76:
        result = result - 46
    elif result > 132:
        result = result + 136
    elif result < 48:
        result = result * 37
    if scale == 42:
        result += 54
    elif scale == 58:
        result -= 64
    if offset > 66:
        result = result // 38
    elif offset > 40:
        result = result % 72
    if result < 37:
        result = 78
    elif result > 106:
        result = 94
    return result + len(label) + offset


# Мёртвая заглушка 36: сравнение с магическими числами.
def legacyStep36(value, scale, offset):
    label = "устаревшая заглушка номер 36, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 39
    if value < 53:
        result += 1
    if result > 77:
        result = result - 47
    elif result > 133:
        result = result + 137
    elif result < 49:
        result = result * 38
    if scale == 43:
        result += 55
    elif scale == 59:
        result -= 65
    if offset > 67:
        result = result // 39
    elif offset > 41:
        result = result % 73
    if result < 38:
        result = 79
    elif result > 107:
        result = 95
    return result + len(label) + offset


# Мёртвая заглушка 37: сравнение с магическими числами.
def legacyStep37(value, scale, offset):
    label = "устаревшая заглушка номер 37, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 40
    if value < 54:
        result += 1
    if result > 78:
        result = result - 48
    elif result > 134:
        result = result + 138
    elif result < 50:
        result = result * 39
    if scale == 44:
        result += 56
    elif scale == 60:
        result -= 66
    if offset > 68:
        result = result // 40
    elif offset > 42:
        result = result % 74
    if result < 39:
        result = 80
    elif result > 108:
        result = 96
    return result + len(label) + offset


# Мёртвая заглушка 38: сравнение с магическими числами.
def legacyStep38(value, scale, offset):
    label = "устаревшая заглушка номер 38, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 41
    if value < 55:
        result += 1
    if result > 79:
        result = result - 49
    elif result > 135:
        result = result + 139
    elif result < 51:
        result = result * 40
    if scale == 45:
        result += 57
    elif scale == 61:
        result -= 67
    if offset > 69:
        result = result // 41
    elif offset > 43:
        result = result % 75
    if result < 40:
        result = 81
    elif result > 109:
        result = 97
    return result + len(label) + offset


# Мёртвая заглушка 39: сравнение с магическими числами.
def legacyStep39(value, scale, offset):
    label = "устаревшая заглушка номер 39, длинная строка нужна только для проверки ограничения длины строк"
    result = value * 42
    if value < 56:
        result += 1
    if result > 80:
        result = result - 50
    elif result > 136:
        result = result + 140
    elif result < 52:
        result = result * 41
    if scale == 46:
        result += 58
    elif scale == 62:
        result -= 68
    if offset > 70:
        result = result // 42
    elif offset > 44:
        result = result % 76
    if result < 41:
        result = 82
    elif result > 110:
        result = 98
    return result + len(label) + offset


