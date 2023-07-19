for x in range (92705608, 92795698 + 1):
    x = str(x)
    if x[:3] == '927' and x[4:6] == '56' and x[7] == '8':
        if (9 + 2 + 7 + int(x[3]) + 5 + 6 + int(x[6]) + 8) % 24 == 0:
            print(x)
