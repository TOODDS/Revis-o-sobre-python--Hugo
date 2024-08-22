import time
x = True
y = 5

while x:
    print(f'{y}...')
    y -= 1
    time.sleep(1)
    if y == 0:
        print("Contagem acabou! Feliz ano novo <3")
        break
