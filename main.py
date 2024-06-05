import random

cards_player_1 = []      # карта на роздачі гравця 1
cards_player_2 = []      # карта на роздачі гравця 2

rank_of_cards = ["six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
card_suit = ["spades", "clubs", "diamonds", "hearts"]
#desk_of_cards = [['six', 'spades'], ['six', 'clubs'], ['six', 'diamonds'], ['six', 'hearts'], ['seven', 'spades'], ['seven', 'clubs'], ['seven', 'diamonds'], ['seven', 'hearts'], ['eight', 'spades'], ['eight', 'clubs'], ['eight', 'diamonds'], ['eight', 'hearts'], ['nine', 'spades'], ['nine', 'clubs'], ['nine', 'diamonds'], ['nine', 'hearts'], ['ten', 'spades'], ['ten', 'clubs'], ['ten', 'diamonds'], ['ten', 'hearts'], ['jack', 'spades'], ['jack', 'clubs'], ['jack', 'diamonds'], ['jack', 'hearts'], ['queen', 'spades'], ['queen', 'clubs'], ['queen', 'diamonds'], ['queen', 'hearts'], ['king', 'spades'], ['king', 'clubs'], ['king', 'diamonds'], ['king', 'hearts'], ['ace', 'spades'], ['ace', 'clubs'], ['ace', 'diamonds'], ['ace', 'hearts']]
desk_of_cards =[]


desc_player_1 = []
desc_player_2 = []

name_player_1 = ""
name_player_2 = ""


def cards_and_suits(a, b):
   y = 5
   for i in a:
      y += 1
      for x in b:
         desk_of_cards.append([f'{i}', f'{x}'])


   return desk_of_cards

#print(desk_of_cards[0][1])

def name_player():  # додавання ім'я ігрока
   global name_player_2, name_player_1
   name_player_1 = input("Enter name player 1: ").upper()
   name_player_2 = input("Enter name player 2: ").upper()


   #return name_player_1, name_player_2
def distribution_of_cards(cards):      # розділ колоди на 2 частини

   while len(cards) != 0:
      i = random.randint(0, (len(cards)-1))
      if random.randint(0, 1):
         #print("2", cards[i])
         desc_player_1.append(cards[i])
         cards.pop(i)
      else:
         #print("3", cards)
         desc_player_2.append(cards[i])
         cards.pop(i)

   while len(desc_player_1) != len(desc_player_2):
        if len(desc_player_1) < len(desc_player_2):
            x = random.randint(0, (len(desc_player_2)-1))
            a = desc_player_2.pop(x)
            desc_player_1.append(a)
        else:
            x = random.randint(0, (len(desc_player_1)-1))
            a = desc_player_1.pop(x)
            desc_player_2.append(a)

   #print("1й", len(desc_player_1), desc_player_1)
   #print("2й", len(desc_player_2), desc_player_2)


def visual_game(name_player_1, name_player_2):
   empty_str = ""
   value_str1 = str(len(desc_player_1))
   value_str2 = str(len(desc_player_2))

   print('(*-*)=(*-*)'*7)
   print(f'Player 1:                                                           Player 2:')
   print(name_player_1.center(38), name_player_2.center(38))
   print('(*-*)=(*-*)' * 7)
   print('(*-*)',empty_str.center(26), '(*-*)=(*-*)',empty_str.center(26), '(*-*)')
   print('(*-*)','Cards'.center(26),'(*-*)=(*-*)','Cards'.center(26), '(*-*)')
   print('(*-*)',value_str1.center(26),'(*-*)=(*-*)',value_str2.center(26), '(*-*)')
   print('(*-*)',empty_str.center(26), '(*-*)=(*-*)',empty_str.center(26), '(*-*)')
   print('(*-*)=(*-*)' * 7)


def put_card():  # покласти карту на роздчуd
   global cards_player_1, cards_player_2
   print()
   print("Press the letter v for Player 1, the letter n for Player 2")
   x = 0
   y = 0
   while (x < 1 or y < 1):

      pres_button = input("Please:  ")
      if pres_button == 'v':
         cards_player_1 = selection_card(desc_player_1)
         x = 1
         #print(len(desc_player_1))
      if pres_button == 'n':
         cards_player_2 = selection_card(desc_player_2)
         y = 1
         #print(len(desc_player_2))


def selection_card(desc_player):  # вибір карти для роздачі
   cards_player = desc_player[0]
   desc_player.pop(0)
   #print(,cards_player)
   #print(len(desc_player),desc_player)
   return cards_player

def viaual_cards(cards_player_1, cards_player_2):
   empty_str = ""
   value_str1 = str(len(desc_player_1))
   value_str2 = str(len(desc_player_2))
   print('(*-*)=(*-*)' * 7)
   print('(*-*)',empty_str.center(26), '(*-*)=(*-*)',empty_str.center(26), '(*-*)')
   print('(*-*)', cards_player_1[0].center(26),  '(*-*)=(*-*)', cards_player_2[0].center(26), '(*-*)')
   print('(*-*)', cards_player_1[1].center(26), '(*-*)=(*-*)', cards_player_2[1].center(26), '(*-*)')
   print('(*-*)',empty_str.center(26), '(*-*)=(*-*)',empty_str.center(26), '(*-*)')
   print('(*-*)=(*-*)' * 7)





def compare_cards(cards_player_1, cards_player_2):  # порівняти карти на роздачі

   rank_suit = {'spades': 1,'clubs': 2, 'diamonds': 3, 'hearts': 4}
   rank_cards_wight = {"six": 60, "seven": 70, "eight": 80, "nine": 90, "ten": 100, "jack": 110, "queen": 120, "king": 130, "ace": 140}

   if (rank_cards_wight.get(cards_player_1[0])+rank_suit.get(cards_player_1[1])) > (rank_cards_wight.get(cards_player_2[0])+rank_suit.get(cards_player_2[1])):
      wins_player(cards_player_1, cards_player_2, desc_player_1)
      print('Victory  Player 1'.center(25))

   else:
      wins_player(cards_player_2, cards_player_1, desc_player_2)
      print('Victory Player 2'.center(25))


def wins_player(player_a, player_b, desc_player):  # забирає виграні карти
   desc_player.append(player_a)
   desc_player.append(player_b)
   return desc_player


def main():
   name_player()
   cards_and_suits(rank_of_cards, card_suit)
   distribution_of_cards(desk_of_cards)
   while (len(desc_player_1) != 0 and len(desc_player_2) != 0): #?????
      visual_game(name_player_1, name_player_2)
      put_card()

      viaual_cards(cards_player_1, cards_player_2)
      compare_cards(cards_player_1, cards_player_2)
   if (len(desc_player_1) > len(desc_player_2)):
         print(f" Game End, Victory Player 1")
   else:
         print(f" Game End, Victory Player 2")


if __name__ == '__main__':
   main()



