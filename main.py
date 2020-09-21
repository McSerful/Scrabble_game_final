letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letter: point for letter, point in zip(letters, points)}

letters_to_points[" "] = 0


def score_word(word):
    point_totall = 0
    for letter in word:
        point_totall += letters_to_points.get(letter.upper(), 0)
    return point_totall


player_to_words = {
    "player1": [""],
    "player2": [""],
    "player3": [""],
}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
      player_points += score_word(word)
  player_to_points[player] = player_points


take_a_game = True

def player_word(player, word):
    while word != "Stop":
        for players in player_to_words:
            if player in players:
                player_to_words[player].append(word)
        player_to_points[player] += score_word(word)
        if word == "Stop":
            break
        return

game_is_on = True
count = 0
while game_is_on == True:

    if count >= 3:
        game_is_on = False
    else:

        for players, words in player_to_words.items():
            player_name = input("Who's turn?: ").lower()

            if player_name in player_to_words.keys():

                word_new = input("Enter a word: ").lower()

                if word_new not in player_to_words.values():
                    player_to_words[player_name].append(word_new)
                    player_to_points[player_name] += score_word(word_new)
                    print(player_to_points)
                    count += 1
                    print(count)
                elif word_new in player_to_words.values():
                    print("There is such a word already!")



            elif player_name == "stop":
                question = input("Are your sure? (Y/N) ").lower()
                if question == "y":
                    game_is_on = False
                elif question == "n":
                    continue

            else:
                print("There is no such a player!")
            break




def winner(dict):
    winner_name = ""
    max_number = 0
    for key, value in dict.items():
        if dict[key] > max_number:
            max_number = dict[key]
            winner_name = str(key)
        elif dict[key] <= max_number:
            continue
    return "The winner is " + winner_name.upper()



print(winner(player_to_points))













