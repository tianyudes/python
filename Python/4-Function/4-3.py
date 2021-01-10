def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill1 + skill2 * 0.5
    return damage1, damage2
# return a tuple object。
# Use two variable.


damages = damage(10,20)
print(type(damages))

skill1_damage, skill2_damage = damage(10, 30)
print(skill1_damage, skill2_damage)


