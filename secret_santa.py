import copy
import random

def get_players():
    all_players = []
    with open('./names.txt', 'rb') as in_file:
        for line in in_file:
            all_players.append(line.strip())
    in_file.close()
    return all_players



def _eliminate_self_assignments(player_list, recipient_list):
    for index in xrange(len(player_list)):
        if player_list[index] == recipient_list[index]:
            new_index = random.choice([i for i in xrange(len(player_list)) if i != index])
            temp = recipient_list[index]
            recipient_list[index] = recipient_list[new_index]
            recipient_list[new_index] = temp


def display_assignments(player_list, recipient_list):
    for index in xrange(len(player_list)):
        print "%s will give a gift to %s" % (player_list[index], recipient_list[index])

def assign_gift_recipients(player_list):
    recipient_list = copy.copy(player_list)
    random.shuffle(recipient_list)
    _eliminate_self_assignments(player_list, recipient_list)
    display_assignments(player_list, recipient_list)


def run_simulation():
    player_list = get_players()
    assign_gift_recipients(player_list)

if __name__ == "__main__":
    run_simulation()