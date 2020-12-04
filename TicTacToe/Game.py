import matplotlib.pyplot as plt
import numpy as np
import time
import copy
import os
import sys
from player_objects import T3Player

def sel_point(point):
    possible_points = np.array([1,2,3])

    x = point[0][0]
    y = point[0][1]

    px = np.argmin(np.abs(possible_points-x))
    py = np.argmin(np.abs(possible_points-y))

    return (possible_points[px],possible_points[py])

def tellme(s):
    plt.title(s,fontsize=16)
    plt.draw()


fig = plt.Figure(figsize=(12,10))
plt.clf()
plt.axis([.5,3.5,.5,3.5])
plt.setp(plt.gca(),autoscale_on=False)
plt.gca().axhline(1.5,color='grey')
plt.gca().axhline(2.5,color='grey')
plt.gca().axvline(1.5,color='grey')

a = T3Player('bayes100k_b.json')
board = "EEEEEEEEE"

plt.gca().axvline(2.5,color='grey')
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)

tellme('Welcome to Tic Tac Toe')

plt.waitforbuttonpress()

cel_coord = {0:(1,3),1:(2,3),2:(3,3),3:(1,2),4:(2,2),5:(3,2),6:(1,1),7:(2,1),8:(3,1)}

while (len(set(a.findi(board,'E')))>0) & (not (a.is_winner(set(a.findi(board,'X'))))) & (not (a.is_winner(set(a.findi(board,'O'))))):

    play_x = set(a.findi(board,'X'))
    play_o = set(a.findi(board,'O'))
    for i in play_x:
        plt.plot(cel_coord[i][0],cel_coord[i][1],'kX',markersize=52)
    for j in play_o:
        plt.plot(cel_coord[j][0],cel_coord[j][1],'ro',markeredgewidth=20,markerfacecolor='w',markersize=52)
    plt.draw()

    if len(set(a.findi(board,'X')))>len(set(a.findi(board,'O'))):
        board = a.move(board)
        time.sleep(1)
    else:
        if len(set(a.findi(board,'E')))==9:
            tellme("Select a point to Start")
        else:
            tellme("Select Your Next Move")
        r = plt.ginput(1)
        sp = sel_point(r)
        ind = 3*(3-sp[1])+(sp[0]-1)
        board = a.play_token(board,ind)
    


play_x = set(a.findi(board,'X'))
play_o = set(a.findi(board,'O'))
for i in play_x:
    plt.plot(cel_coord[i][0],cel_coord[i][1],'kX',markersize=52)
for j in play_o:
    plt.plot(cel_coord[j][0],cel_coord[j][1],'ro',markeredgewidth=20,markerfacecolor='w',markersize=52)


if (a.is_winner(set(a.findi(board,'X')))):
    winning_set = a.is_winner(set(a.findi(board,'X')))
    pnt1 = -1
    pnt2 = -1
    for pnt in winning_set:
        if (pnt1==-1)&(pnt2==-1):
            pnt1 = pnt
        else:
            pnt2 = copy.deepcopy(pnt1)
            pnt1 = pnt
            plt.plot([cel_coord[pnt1][0],cel_coord[pnt2][0]],[cel_coord[pnt1][1],cel_coord[pnt2][1]],'g-',\
                    linewidth=4)
    tellme('The player wins!')
elif (a.is_winner(set(a.findi(board,'O')))):
    winning_set = a.is_winner(set(a.findi(board,'O')))
    pnt1 = -1
    pnt2 = -1
    for pnt in winning_set:
        if (pnt1==-1)&(pnt2==-1):
            pnt1 = pnt
        else:
            pnt2 = copy.deepcopy(pnt1)
            pnt1 = pnt
            plt.plot([cel_coord[pnt1][0],cel_coord[pnt2][0]],[cel_coord[pnt1][1],cel_coord[pnt2][1]],'g-',\
                    linewidth=4)
    tellme('The computer wins!')
else:
    tellme('The Game is a Draw!')

plt.draw()
plt.waitforbuttonpress()
tellme('To Play Again Press Y otherwise click anywhere to Close')

click = False
click = plt.waitforbuttonpress()
if click:
    os.exec(sys.argv[0], sys.argv)