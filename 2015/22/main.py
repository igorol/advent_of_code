from random import sample
from tqdm import tqdm


def cast_spell(player_spell, game):
    match player_spell:
        case 'magic_missile':
            game['boss_hp'] -= 4
        case 'drain':
            game['boss_hp'] -= 2
            game['player_hp'] += 2
        case 'shield':
            game['shield_timer'] = 6
            game['player_armor'] += 7
            game['active_spells'].append('shield')
        case 'poison':
            game['poison_timer'] = 6
            game['active_spells'].append('poison')
        case 'recharge':
            game['recharge_timer'] = 5
            game['active_spells'].append('recharge')
    return game


def spell_effects(game):
    if game['shield_timer'] > 0:
        game['shield_timer'] -= 1
        if game['shield_timer'] == 0:
            game['player_armor'] = 0
    else:
        try:
            game['active_spells'].remove('shield')
        except ValueError:
            pass
    if game['poison_timer'] > 0:
        game['boss_hp'] -= 3
        game['poison_timer'] -= 1
    else:
        try:
            game['active_spells'].remove('poison')
        except ValueError:
            pass
    if game['recharge_timer'] > 0:
        game['player_mana'] += 101
        game['recharge_timer'] -= 1
    else:
        try:
            game['active_spells'].remove('recharge')
        except ValueError:
            pass
    return game


def play(game, hard_mode=False):
    while True:
        # player turn
        available_spells = [spell for spell, cost in spells.items() if
                            spell not in game['active_spells'] and cost <= game['player_mana']]

        if len(available_spells) > 0:

            if hard_mode:
                game['player_hp'] -= 1
                if game['player_hp'] <= 0:
                    return 'boss', game

            player_spell = sample(available_spells, 1)[0]
            game['player_mana'] -= spells[player_spell]
            game['mana_spent'] += spells[player_spell]
            game = cast_spell(player_spell, game)

        if game['player_mana'] < 0:
            return 'boss', game

        game = spell_effects(game)

        if game['boss_hp'] <= 0:
            return 'player', game

        # boss turn
        game['player_hp'] -= max(1, (game['boss_damage'] - game['player_armor']))

        game = spell_effects(game)
        # check if game over
        if game['player_hp'] <= 0:
            return 'boss', game


def part1():
    play_wins = []
    for _ in tqdm(range(20_000)):
        winner, game_stats = play(start.copy())
        if winner == 'player':
            play_wins.append([winner, game_stats['mana_spent']])

    print('part 1:', min(play_wins, key=lambda x: x[1])[1])


def part2():
    play_wins = []
    for _ in tqdm(range(200_000)):
        winner, game_stats = play(start.copy(), hard_mode=True)
        if winner == 'player':
            play_wins.append([winner, game_stats['mana_spent']])
    print('part 2:', min(play_wins, key=lambda x: x[1])[1])


spells = {
    'magic_missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229,
}

start = {
    'player_hp': 50,
    'player_mana': 500,
    'player_armor': 0,
    'boss_hp': 51,
    'boss_damage': 9,
    'shield_timer': 0,
    'poison_timer': 0,
    'recharge_timer': 0,
    'mana_spent': 0,
    'active_spells': [],
}

part1()
part2()

# part 1: 900
# part 2: 1216
