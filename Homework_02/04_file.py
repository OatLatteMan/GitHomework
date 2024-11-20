def append_file():
    with open ('GitHomework/Homework_02/test.txt', mode='a', encoding='utf-8') as file:
        file.write(input('Tell me about your today\'s mood?'))
        file.write('\n')

append_file()