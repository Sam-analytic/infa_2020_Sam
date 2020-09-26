import turtle as t

def one():
    t.up()
    t.seth(90)
    t.forward(50)
    t.down()
    t.seth(45)
    t.forward(70)
    t.seth(270)
    t.forward(100)
    t.up()
    t.seth(0)
    t.forward(20)
    t.down()

def zero():
    t.seth(90)
    t.forward(100)
    t.seth(0)
    t.forward(50)
    t.seth(270)
    t.forward(100)
    t.seth(180)
    t.forward(50)
    t.backward(50)
    t.up()
    t.seth(0)
    t.forward(20)
    t.down()

def four():
    t.up()
    t.seth(90)
    t.forward(100)
    t.seth(270)
    t.down()
    t.forward(50)
    t.seth(0)
    t.forward(50)
    t.seth(90)
    t.forward(50)
    t.seth(270)
    t.forward(100)
    t.up()
    t.seth(0)
    t.forward(20)
    t.down()

def seven():
    t.up()
    t.seth(90)
    t.forward(100)
    t.seth(0)
    t.down()
    t.forward(50)
    t.seth(225)
    t.forward(70)
    t.seth(270)
    t.forward(50)
    t.up()
    t.seth(0)
    t.forward(70)
    t.down()
    

u = [one, four, one, seven, zero, zero]

for i in u:
    print (i())




