import random

def typoglycemia(str):
    tpg = []
    tmp = []
    head = True
    l = 0
    for c in list(str):
        if head:
            tpg.append(c)
            head = False
            l += 1
            continue
        if c == ' ':
            head = True
            if len(tmp) == 0:
                tpg.append(c)
                l = 0
                continue
            if l <= 4:
                tpg = tpg + tmp
            else:
                randomed = tmp[:(l-2)]
                random.shuffle(randomed) 
                tpg = tpg + randomed + list(tmp[-1])
            tpg.append(c)
            l = 0
            tmp = []
            continue
        tmp.append(c)
        l += 1

    return ''.join(tpg)


if __name__ == "__main__":
    print(typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
