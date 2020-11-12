import correct_answers
import hashlib


def check_testcase(input, output):
    assert input in correct_answers.d
    correctAnswer = correct_answers.d[input]
    output = hashlib.sha224(output.encode()).hexdigest()
    assert correctAnswer == output


testcase_count = 2

for i in range(1, testcase_count + 1):
    input = open('../src/testcase' + str(i) + '/input.txt', 'r').read()
    output = open('../src/testcase' + str(i) + '/output.txt', 'r').read()
    check_testcase(input, output)

    print('Testcase '+str(i) + ' checked - All ok')

print('All testcases checked')
