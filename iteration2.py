count = 0
score = 80

while count < 100:
    if count < 50:
        count += 1
        continue
    print(count)
    count += 1
    if count == score:
        print(score)
        break