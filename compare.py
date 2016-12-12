#import main_app
import convert
import record_data


keypointSimilarity = .90

def longestCommonSubstring(password, attempt):
    # print(password[-1][0], attempt[-1][0])

    if len(password)==0 or len(attempt) == 0:
        return 0
    if password[-1][0] == attempt[-1][0]:
        return 1 + longestCommonSubstring(password[:-1],attempt[:-1])
    else:
        return max(longestCommonSubstring(password[:-1],attempt), longestCommonSubstring(password,attempt[:-1]))


def lcsMatrix(password, attempt):
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

def closeEnough(A,B):
    C = min(A,B)
    lowerBound = C*keypointSimilarity
    upperBound = C*(2-keypointSimilarity)
    if A>lowerBound and A<upperBound:
        if B>lowerBound and B<upperBound:
            return True
    return False




password = (stripOutZeros(convert.process_audio("Test_Files\Password1_hello.wav")))
attempt1 = (stripOutZeros(convert.process_audio("Test_Files\Attempt1_hello_hell.wav")))
attempt2 = (stripOutZeros(convert.process_audio("Test_Files\Attempt2_hello_howdy.wav")))
attempt3 = stripOutZeros(convert.process_audio("Test_Files\Attempt3_hello_hello.wav"))
attempt4 = stripOutZeros(convert.process_audio("Test_Files\Attempt4_hello_hello.wav"))

print(password)
print(attempt1)

print(len(password))
print(len(attempt1))
print(len(attempt2))
print(len(attempt3))
print(len(attempt4))

print(lcsMatrix(password,password))
print(lcsMatrix(password,attempt1))
print(lcsMatrix(password,attempt2))
print(lcsMatrix(password,attempt3))
print(lcsMatrix(password,attempt4))

# array1 = [['g'],['o'],['s'],['c'],['o'],['t'],['s']]
# array2 = [['g'],['r'],['o'],['s'],['s']]
# print(lcsMatrix(array1,array2))


