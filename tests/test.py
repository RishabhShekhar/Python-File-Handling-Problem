from correct_answers import solutions


def check_testcase(dictionary, paragraph, alien):
    print(dictionary, paragraph, alien)
    t = (dictionary, paragraph)
    assert t in solutions
    correct_answer = solutions[(dictionary, paragraph)]
    assert correct_answer == alien


testcases_count = 2

for i in range(1, testcases_count + 1):
    dictionary = open('../src/testcase' + str(i) +
                      '/dictionary.txt', 'r').read()
    paragraph = open('../src/testcase' + str(i) + '/paragraph.txt', 'r').read()
    alien = open('../src/testcase' + str(i) + '/alien.txt', 'r').read()
    check_testcase(dictionary, paragraph, alien)

    print('Testcase '+str(i) + ' checked - All ok')


print('All testcases checked')
