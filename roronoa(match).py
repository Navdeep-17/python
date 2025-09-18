month = 5
day = 4
match day :
    case 1 |2|3|4|5 if month == 4:#| refer 'or'
        print("weekday in april")
    case 1 |2|3|4|5 if month == 5:
        print("weekday in may")
    case _ :#_ refers 'default'
        print("no match")
