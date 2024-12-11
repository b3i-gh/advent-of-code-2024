def main(input):
    ans1 = 0
    ans2 = 0

    unzipped_l, unzipped_part_2 = unzip(input)
    rearranged_l = rearrange(unzipped_l)
    rearranged_part_2 = rearrange_part_2(unzipped_part_2)
    ans1 = checksum(rearranged_l)
    ans2 = checksum2(rearranged_part_2)

    return ans1, ans2

def unzip(input):
    unzipped_l = list()
    i = 0
    unzipped_part_2 = list()
    while i < len(input):
        try:
            c = input[i]
            for j in range(int(c)):
                if i%2 == 0:
                    unzipped_l.append(str(int(i/2)))
                    
                else:
                    unzipped_l.append('.')
                    
            if i%2 == 0:
                unzipped_part_2.append((str(int(i/2)), int(c)))
            else:
                unzipped_part_2.append(('.', int(c)))
        except:
            pass
        i += 1
    return unzipped_l, unzipped_part_2

def rearrange(unzipped_l):
    rearranged_l = list(unzipped_l)
    pos = 0
    for i in range(len(unzipped_l) - 1, -1, -1):
        pos = rearranged_l.index('.')
        if(unzipped_l[i] != ".") and i > pos:
            rearranged_l[pos] = unzipped_l[i]
            rearranged_l[i] = "."
    return rearranged_l

def rearrange_part_2(unzipped_part_2):
    za = len(unzipped_part_2) - 1

    while za > 0:
        az = 0
        if(unzipped_part_2[za][0] != '.'):
            while az < za:
                if(unzipped_part_2[az][0] == '.'):
                    d = unzipped_part_2[az][1] - unzipped_part_2[za][1]
                    if d >= 0:
                        unzipped_part_2[az] = unzipped_part_2[za]
                        unzipped_part_2[za] = ('.', unzipped_part_2[za][1])
                        if(d > 0):
                            unzipped_part_2.insert(az+1, ('.', d))
                            za += 1
                        break
                az += 1
        za -= 1
    return unzipped_part_2

def checksum(rearranged_l):
    cs = 0

    for i in range(len(rearranged_l)):
        print(i)
        if rearranged_l[i] != '.':
            cs += i * int(rearranged_l[i])
    return cs


def checksum2(rearranged_l):
    cs = 0
    id = 0
    for a in rearranged_l:
        print(id)
        for _ in range(a[1]):
            if a[0] == '.':
                id += 1
            else:
                cs += id * int(a[0])
                id += 1
        
    return cs
