def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill1 + skill2 * 0.5
    return damage1, damage2
# 上面得返回方式得到的是元组，获取得时候要用damage[0], damage[1],但是不推荐因为不方便阅读。
# 推荐用两个变量接受这个元组


damages = damage(10,20)
print(type(damages))
# 序列解包，以后尽量使用有意义的变量名
skill1_damage, skill2_damage = damage(10, 30)
print(skill1_damage, skill2_damage)


