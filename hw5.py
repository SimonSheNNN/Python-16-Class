#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:37:05 2019

@author: Simon
"""

from Tkinter import Tk, Canvas, Frame, Button, BOTH


class KnightGame(Frame):
    
    
    def __init__(self, parent,N):
        self.parent = parent
        Frame.__init__(self, parent)
        
        self.n=N
        self.WIDTH=self.HEIGHT=40+50*self.n
        self.posX=0
        self.posY=0

        self.parent.title("Knights tour")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=self.WIDTH,
                             height=self.HEIGHT)
        self.canvas.pack()
        

        self.__draw_grid()
        self.canvas.bind("<Button-1>", self.rectangle)
        


        
    def __draw_grid(self):
        #Draws grid divided with grey lines

        for i in xrange(self.n+1):
            color =  "gray"

            
            x0 = 20 + i * 50
            y0 = 20
            x1 = 20 + i * 50
            y1 = self.HEIGHT - 20
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = 20
            y0 = 20 + i * 50
            x1 = self.WIDTH - 20
            y1 = 20 + i * 50
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            
        self.canvas.create_rectangle(20,20,70,70,fill="orange")
            
            
    def rectangle(self,ev):
        #check if in position
        if ev.x>20 and ev.y>20 and ev.x<50*self.n+20 and ev.y<50*self.n+20: 
            newX=(ev.x-1-20)/50
            newY=(ev.y-1-20)/50
            #check if valid move
            if (newX==self.posX+1 and newY==self.posY+2) | \
            (newX==self.posX+2 and newY==self.posY+1)|\
            (newX==self.posX-2 and newY==self.posY-1)|\
            (newX==self.posX-1 and newY==self.posY+2)|\
            (newX==self.posX+1 and newY==self.posY-2)|\
            (newX==self.posX-1 and newY==self.posY-2)|\
            (newX==self.posX-2 and newY==self.posY+1)|\
            (newX==self.posX+2 and newY==self.posY-1):
            
                self.canvas.create_rectangle(self.posX*50+20, self.posY*50+20, \
                                             self.posX*50+70, self.posY*50+70, fill="blue")
                self.posX=(ev.x-1-20)/50
                self.posY=(ev.y-1-20)/50
                self.canvas.create_rectangle(self.posX*50+20, self.posY*50+20, \
                                             self.posX*50+70, self.posY*50+70, fill="orange")
            else:
                print "invalid move"

        else:
            print "invalid position"
 
 

def knights_tour(n):
    root = Tk()
    gui=KnightGame(root,n)
    root.mainloop()
    
if __name__ == "__main__":
    knights_tour(5)
