def solution(num, total):
    answer = []
    avg = total / num
    #if num%2!=0:
    for i in range(int(avg)-(num-1)//2, int(avg)+(num+2)//2):
        answer.append(i)
    #else:
        #for i in range(int(avg)-(num-1)//2, int(avg)+(num+2)//2):
            #answer.append(i)
    return answer