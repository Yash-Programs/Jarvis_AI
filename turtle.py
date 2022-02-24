import turtle


yash_turtle= turtle.Turtle()

yash_turtle.speed(50000)
def square():
  yash_turtle.forward(100)
  yash_turtle.right(90)
  yash_turtle.forward(100)
  yash_turtle.right(90) 
  yash_turtle.forward(100)
  yash_turtle.right(90)
  yash_turtle.forward(100)

def triangle():
  yash_turtle.forward(100)
  yash_turtle.right(90)
  yash_turtle.forward(100)
  yash_turtle.right(135)
  yash_turtle.forward(145)


for i in range(100):
  square()
  yash_turtle.right(5)



 
  
