def solution(arr1, arr2):
    answer = []
    index = 0
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            answer[index].append(arr1[i][j] + arr2[i][j])
        index += 1
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))