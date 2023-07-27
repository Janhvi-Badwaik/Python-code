def game():
    return 120

score = game()
with open('highscore.txt') as f:
    highscor = (f.read())
if highscor=='':
    with open('highscore.txt','w') as f:
        f.write(str(score))
elif int(highscor)<score:
    with open('highscore.txt','w') as f:
        f.write(str(score))