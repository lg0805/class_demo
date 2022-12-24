"""
角色      攻击          防御
忍者      1刺刀         护盾，闪避
忍者      2飞镖
水果      1果核
水果      果汁
"""

import random


class Characters:
    value = 400

    def __init__(self, name):
        self.name = name

    def defend(self, command):
        if command == 1:
            print(f'{self.name}使出了护盾。')
            return 0.5
        elif command == 2:
            print(f'{self.name}闪避了对方攻击。')
            return random.choice([0.4, 1])


class ninja(Characters):
    def attack(self, command):
        if command == 1:
            print(f'{self.name}扔出了刺刀。')
            return 200
        elif command == 2:
            print(f'{self.name}丢出了飞镖。')
            return random.choice([100, 300])


class fruit(Characters):
    def attack(self, command):
        if command == 1:
            print(f'{self.name}扔出了果核。')
            return 180
        elif command == 2:
            print(f'{self.name}丢出了果汁。')
            return random.choice([120, 300])


if __name__ == '__main__':
    n = input('请输入游戏昵称：')
    player = ninja(n)
    opponent = fruit('水果')

    r = random.choice([1, 2])
    while True:
        attack_command = int(input('\n请输入入击指令（1）普通攻击（2）特殊攻击：'))
        player_attack_value = player.attack(attack_command)
        lost = int(opponent.defend(r) * player_attack_value)
        opponent.value -= lost

        if opponent.value <= 0:
            print(f'{opponent.name}倒下了， {player.name}胜利！')
            break
        else:
            print(f'{opponent.name}受到了伤害，生命值仅剩下{opponent.value}!')


        defend_command = int(input('请输入防御指令（1）护盾（2）闪避：'))
        opponent_attack_value = opponent.attack(r)
        lost = player.defend(defend_command) * opponent_attack_value
        player.value -= lost
        if player.value <= 0:
            print(f'f{player.name}倒下了， {opponent.name}胜利！')
            break
        else:
            print(f'{player.name}受到了{lost}伤害， 生命值剩下{player.value}.')
