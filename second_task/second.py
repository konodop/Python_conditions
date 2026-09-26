year = int(input("Проверяемый год: "))

year_num = year % 12
match year_num:
    case 0:
        year_type = "год обезьяны"
    case 1:
        year_type = "год петуха"
    case 2:
        year_type = "год собаки"
    case 3:
        year_type = "год свиньи"
    case 4:
        year_type = "год крысы"
    case 5:
        year_type = "год коровы"
    case 6:
        year_type = "год тигра"
    case 7:
        year_type = "год зайца"
    case 8:
        year_type = "год дракона"
    case 9:
        year_type = "год змеи"
    case 10:
        year_type = "год лошади"
    case 11:
        year_type = "год овцы"

print("Это", year_type)
