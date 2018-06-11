start=int(input("시작의 값을 입력하세요:"))
end=int(input("끝 값을 입력하세요:"))
baesh=int(input("배수를 입력하세요:"))
def cal_sum(s, e):
    h=0
    i=s
    while i<=e:
        h+=i
        i+=1
    return h


def baesh_sum(s, e, b):
    h=0
    i=s
    while i<=e:
        if i%b==0:
            h+=i
        i+=1
    return h

print(start,"에서",end,"까지의 합은",cal_sum(start, end))
print(start,"에서",end,"까지",baesh,"의합은",baesh_sum(start, end, baesh))
