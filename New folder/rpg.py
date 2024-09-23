import random,time
name = input("введите имя")
HERO = {
    "name": "test"
}
CHRS = {
    "сила": random.randint(15,45),
    "Выносливость" : random.randint(15,45)
}
print(CHRS)
MODEL_HERO = "$"
HERO["Хар-ки"] = CHRS
HERO["Модель"] = MODEL_HERO

MAP = ["0","0","0","0","0"]
i = 0
MAP[i] = MODEL_HERO
print(MAP)

#while MAP.index(MODEL_HERO) < len(MAP) - 1:
    #tmp = i
    #i = MAP.index(MODEL_HERO) + 1
    #MAP[i] = MODEL_HERO
    #MAP[tmp] = "0"
    #print(MAP)
    
input("Нажмите enter")

#while MAP.index(MODEL_HERO) != 0:
    #tmp = i
    #i = MAP.index(MODEL_HERO) - 1
    #MAP[i] = MODEL_HERO
    #MAP[tmp] = "0"
    #print(MAP)

inventory = {
    "Броня игрока" : 25,
    "Зелье Здоровья" : 1
}

HERO["З"] = 100 + CHRS["Выносливость"]*0.5
HERO["ЗН"] = HERO["З"]
print("Здоровье Игрока:", HERO["З"])
print("Здоровье Игрока:", HERO["ЗН"])
HERO["И"] = inventory
HERO["БУ"] = 15 + CHRS["сила"]*0.5

ENEMY = {
    "health":100,
    "Hand":{"Картошка":100},
    "damage":20
}
def heart_icons():
    health_icon = '‪‪❤︎'
    hero_health_bar= int(HERO['З']//10)*health_icon
    print(f'HEADER STATISTIC\nHERO-{hero_health_bar}')
while True:
    max=1000
    symb_load='⟳↻'
    lenght_load = len(symb_load)
    height = 5
    count = 0
    for iter in range(max):
        time.sleep(0.001)
        temp = int(round(iter*100/1000)//2)
        if count >= lenght_load-1:
            count = 0
        else:
            count += 1
        print(height*'\n',f'{symb_load[count]} - Загрузка', height*'\n')
    
    input("Нажмите enter")
    if random.randint(1,6) in [1,2]:
        while True:
            print("вы встретили врага")
            input("Нажмите enter")
            if random.randint(1,6) in [1,3,6]:
                print("вы встретили врага")
                ENEMY["health"] = ENEMY["health"] - HERO["БУ"] 
                HERO["З"] = HERO['З'] - ENEMY["damage"]
                print("здоровье :", HERO["З"])
                print("здоровье врага", ENEMY["health"])
                health_icon = '‪‪❤︎'
                hero_health_bar= int(HERO['З']//10)*health_icon
                enemy_health_bar=int(ENEMY["health"]//10)*health_icon
                print(f'HEADER STATISTIC\nHERO-{hero_health_bar}\nENEMY-{enemy_health_bar}')
                if HERO["З"] <= 0:
                    print("вы умерли")
                    exit()
                elif ENEMY["health"] <= 0:
                    print("враг повержен")
                    break
            else:
                 print("промах")
                 heart_icons()
                 HERO["З"] = HERO['З'] - ENEMY["damage"]
                 print("здоровье :", HERO["З"])
    elif  random.randint(1,6) in [3,4,5,6]:
        while True:
            print("вы нашли фонтан востановления")
            heart_icons()
            HERO["З"] = HERO["ЗН"]
            print("Здоровье Игрока:", HERO["З"])
            break
    else:
        print("вы ничего не нашли")

