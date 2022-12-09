def search_word():    
    file = open("text.txt", "r")
    text = file.readlines()
    number_abzath = 1
    my_word = input("Введіть слово яке шукаєте: ")
    answer = []
    for line in text:
        stroka = line[:-1]
        if line == "\n":
            number_abzath += 1
        else:
            list_word = stroka.split(" ")
            for word in list_word:
                if word.lower() == my_word.lower():
                    if answer.count(number_abzath) == 0:
                        answer.append(number_abzath)
            
    abzath = ""                    
    
    for number in answer:
        abzath += str(number) + "; "
    
    if answer == []:
        print("Такого слова немає у тесті")
    else:
        print(f"Це слово є у абзаці: {abzath}")
        



while True:
    operation = input("Для пошуку слова введіть 's', для виходу натисніть 'Enter': ")
    if operation == "s":
        search_word()
    else:
        break    


    