import tkinter
from tkinter import messagebox
import random
import maze_map

key = ""
px = 0
py = 0
maze = maze_map.blank_map

def key_up(e):
    global key 
    key = ""
    
def key_down(e):
    global key
    key = e.keysym
    main()
    
root = tkinter.Tk()
root.title("迷路")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800,height=800,bg="white")
canvas.pack()
img = tkinter.PhotoImage(file="player.png")

def map_create():
    global px,py,maze
    seed = random.randint(1,3)
    if seed == 1:
        maze = maze_map.map1
        px = 0
        py = 1
    elif seed == 2:
        maze = maze_map.map2
        px = 0
        py = 18
    elif seed == 3:
        maze = maze_map.map3
        px = 0
        py = 8
        
    for y in range(20):
        for x in range(20):
            if maze[y][x] == 1:
                canvas.create_rectangle(x*40, y*40, x*40+39, y*40+39,
                                        fill="black", width=0)
            elif maze[y][x] == 2:
                canvas.create_rectangle(x*40, y*40, x*40+39, y*40+39,
                                        fill="red", width=0)

    canvas.create_image(px*40+20, py*40+20, image=img, tag="Player")

def main():
    global px,py
    if key == "Up" and maze[py-1][px] != 1:
        py = py - 1
    if key == "Down" and maze[py+1][px] != 1:
        py = py + 1
    if key == "Right" and maze[py][px+1] != 1:
        px = px + 1
    if key == "Left" and maze[py][px-1] != 1:
        px = px - 1
    if maze[py][px] != 1:
        canvas.delete("Player")
        canvas.create_image(px*40+20, py*40+20, image=img, tag="Player")
    if maze[py][px] == 2:
        canvas.update()
        messagebox.showinfo("ゲームクリア","おめでとう！ゴールしました！")
        
if __name__ == "__main__":
    map_create()
    root.mainloop()
