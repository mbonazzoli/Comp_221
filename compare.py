import convert

keypointSimilarity = .80
passwordSimilarity = .50
correctness = None

'Carries out the comparison between the stored password and the attempted password'
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

'Runs a longest common substring algorithm implemented bottom up, to compare the two arrays of audio key points'
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

'Gets rid of zeros signifying silence at the beingnning and end of the audio data'
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

'determines whether two compared frequencies are within the allotted similarity value'
def closeEnough(A, B):
    C = min(A,B)
    lowerBound = C*keypointSimilarity
    upperBound = C*(2-keypointSimilarity)
    if lowerBound < A < upperBound:
        if lowerBound < B < upperBound:
            return True
    return False


# password1 = convert.process_audio("Test_Files\\lowHigh.wav")
# attempt1 = convert.process_audio("Test_Files\\lowHigh1.wav")
# attempt2 = convert.process_audio("Test_Files\\high.wav")
# attempt3 = convert.process_audio("Test_Files\\highLow.wav")
#
#
# print(compare_data(password1, password1))
# print correctness
# print(compare_data(password1, attempt1))
# print correctness
# print(compare_data(password1, attempt2))
# print correctness
# print(compare_data(password1, attempt3))
# print correctness
