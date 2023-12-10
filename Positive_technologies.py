def title(check):
    sp = []
    a = 0
    for i in range(0, len(check)):
        if a > 1:
            a -= 1
            continue
        else:
            if check[i] == ' ':
                for j in range(i, len(check)):
                    if check[j] != ' ':
                        sp.append(check[j].upper())
                        break
                    else:
                        sp.append(check[j])
                        a += 1
            else:
                if a != 0:
                    a -= 1
                    continue
                else:
                    if  i == 0:
                        sp.append(check[i].upper())
                    else:
                        sp.append(check[i])
    itog = ''
    for k in range(0, len(sp)):
        itog += sp[k]
    return print(itog)
title('тесТОвое       задание      для      pt')