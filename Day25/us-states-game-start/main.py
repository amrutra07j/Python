import turtle

import pandas

screen = turtle.Screen()
screen.title("U S title game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
lis = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    ans = screen.textinput(title="State Game", prompt="Guess the US state name").title()
    if ans in lis:
        guessed_states.append(ans)
        t = turtle.Turtle()
        t.up()
        t.hideturtle()
        data_ans = data[data.state == ans]
        t.goto(int(data_ans.x), int(data_ans["y"]))
        t.write(data_ans["state"].item())
    if ans == "Stop":
        break



for state in guessed_states:
    lis.remove(state)
lis = pandas.DataFrame(lis)
lis.to_csv("remaiming_states.csv")

# print(learn_states_list)
# turtle.mainloop()



