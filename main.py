import random

class Characters:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def normal_attack(self, other):
            # normal_power값을 기반으로 랜덤한 데미지 생성
            # normal_power가 10이면 8~12
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 일반공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")

    def magic_attack(self, other):
            # magic_power값을 기반으로 랜덤한 데미지 생성
            # magic_power가 10이면 10~15
            damage = random.randint(self.power - 0, self.power + 5)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Characters):
    def __init__(self, name, hp, mp, power):
        self.max_mp = mp
        self.mp = mp
        super().__init__(name, hp, power)
    # name = input("이름을 입력해주세요 : ")
    # print(f"{name}게임을 시작합니다.")


class Monster(Characters):
    def __init__(self, name, hp, power, alive):
        self.alive = alive
        super().__init__(name, hp, power)

        
    def status_check(self):
        if self.hp > 0:
            print("몬스터가 살아있습니다!")
        else:
            print("몬스터가 쓰러졌습니다.")

player = Player(input("이름을 입력해주세요 : "), hp=100, mp=1, power=10)
monster = Monster(name="Monster", hp=100, power=10, alive="True")

while monster.hp >0 and player.hp >0:
    player.show_status()

    # 몬스터 임의 생성
    # monster = Monster("Monster", random.randint(50, 100), random.randint(5, 10))
    print("몬스터 등장!")
    #상태창출력
    
    monster.show_status()
    
    while True:
        print("====================")
        print("=== 1. 일반공격 2. 마법공격 ===")
        choice = input("1이나 2를 입력해주세요: ")
        print("====================")
        print("")
        
        if choice == "1":
            player.normal_attack(monster)
            monster.show_status()
            monster.status_check()
            print("====================")
            print("")
            monster.normal_attack(player)
            player.show_status()

        elif choice == "2":
            player.magic_attack(monster)
            monster.show_status()
            monster.status_check()
            print("====================")
            print("")
            monster.normal_attack(player)
            player.show_status()

        else:
            print("다시 선택해주세요")
        # 액션 입력
        # action = input()
        # if action == 1:
        #     Player.attack()
    
    # 몬스터나 플레이어의 HP가 0이되면 전투를 종료하고
    # 승리 또는 패배를 출력해야 합니다.
        if monster.hp <= 0:
            print(f"{player.name}의 승리!")
            break
        elif player.hp <= 0:
            print("패배")
            break


    


