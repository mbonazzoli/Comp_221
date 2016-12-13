import convert

keypointSimilarity = .80
passwordSimilarity = .50
correctness = None


def compare_data(password, attempt):
    global correctness
    pass_array = stripOutZeros(password)
    attempt_array = stripOutZeros(attempt)
    pass_length = len(pass_array)
    attempt_length = len(attempt_array)
    longest = max(pass_length, attempt_length)

    num_matches = longest_common_substring(pass_array, attempt_array)
    correctness = float(num_matches)/longest

    if correctness >= passwordSimilarity:
        return True
    else:
        return False


def longest_common_substring(password, attempt):
    matrix = []
    for g in range(len(password)+1):
        horlist = []
        for h in range(len(attempt)+1):
            horlist.append(0)
        matrix.append(horlist)

    for i in range(len(password)):
        for j in range(len(attempt)):
            if closeEnough(password[i][0], attempt[j][0]):
                matrix[i+1][j+1] = 1+matrix[i][j]
            else:
                matrix[i + 1][j + 1] = max(matrix[i+1][j], matrix[i][j+1])
    return matrix[-1][-1]


def stripOutZeros(array):
    j = 0
    for i in range(len(array)):
        if array[i][0] == 0:
            j +=1
        else:
            break
    g = 0
    for h in range(len(array)):
        if array[-h][0] ==0:
            g +=1
        else:
            break

    return array[i:len(array)-g]


def closeEnough(A, B):
    C = min(A,B)
    lowerBound = C*keypointSimilarity
    upperBound = C*(2-keypointSimilarity)
    if lowerBound < A < upperBound:
        if lowerBound < B < upperBound:
            return True
    return False


password1 = convert.process_audio("lowHigh.wav")
attempt1 = convert.process_audio("lowHigh1.wav")
attempt2 = convert.process_audio("high.wav")
attempt3 = convert.process_audio("highLow.wav")

print(password1)
print(attempt1)

print(len(password1))
print(len(attempt1))
print(len(attempt2))
print(len(attempt3))


print(compare_data(password1, password1))
print correctness
print(compare_data(password1, attempt1))
print correctness
print(compare_data(password1, attempt2))
print correctness
print(compare_data(password1, attempt3))
print correctness

#
# # array1 = [['g'],['o'],['s'],['c'],['o'],['t'],['s']]
# # array2 = [['g'],['r'],['o'],['s'],['s']]
# # print(lcsMatrix(array1,array2))


