from flask import Flask
import random

app = Flask(__name__)

secret_num = random.randint(0, 9)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center;'>Guess a number between 0 and 9 </h1>" \
           "<img src = 'https://bit.ly/2Ur9KJT'>"

@app.route("/<guess>")
def check_num(guess):
    guess = int(guess)
    global secret_num
    if guess == secret_num:
        return "<h1 style = 'text-align: center; color: red;'>Correct!</h1>" \
               "<img src = 'https://bit.ly/3k9yiA9'>"
    elif guess < secret_num:
        return "<h1 style = 'text-align: center; color: blue;'>Too Low!</h1>" \
               "<img src = 'https://bit.ly/3gf5WmD'>"
    else:
        return "<h1 style = 'text-align: center; color: blue;'>Too High!</h1>" \
               "<img src = 'https://bit.ly/3k9yXS9'>"

if __name__ == "__main__":
# execute only if run as a script
# run the app indebug mode
   app.run(debug=True)
