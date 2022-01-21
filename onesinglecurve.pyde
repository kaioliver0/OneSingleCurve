#DRAWS CURVE WITH RANDOM FILLS


#SETS UP CANVAS

def setup():
    size(500,500,P3D)
    background(random(0,15),random(0,15), random(0,15))
    noStroke()
    
def draw(): 
    beginShape()
    fill(random(1,250),random(1,100),random(1,100))

    
    curveVertex(250, 250)
    curveVertex(250, 250)
    curveVertex(mouseX+100, mouseY-100) #mouseY+100)
    curveVertex(mouseX-100, mouseY+100)
    curveVertex(250, 250)
    curveVertex(250, 250)
    
    endShape()
