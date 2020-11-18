from correct_answers import solutions
import hashlib


def check_testcase(one, second, output):
    output = hashlib.sha224(output.encode()).hexdigest()
    t = (one, second)
    assert t in solutions
    correct_answer = solutions[t]
    assert correct_answer == output


testcase_count = 2

for i in range(1, testcase_count + 1):
    one = open('../src/testcase' + str(i) + '/one.txt', 'r').read()
    second = open('../src/testcase' + str(i) + '/second.txt', 'r').read()
    output = open('../src/testcase' + str(i) + '/output.txt', 'r').read()
    check_testcase(one, second, output)

    print('Testcase '+str(i) + ' checked - All ok')

print('All testcases checked')
