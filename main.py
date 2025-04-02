import tkinter as tk
import random

SNAKE_SIZE = 10
WIDTH = 400
HEIGHT = 400

snake = [(100, 100), (90, 100), (80, 100)]
direction = 'Right'
food_pos = None
game_over = False

def main():
    global root, canvas
    root = tk.Tk()
    root.title("Snake Game")
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
    canvas.pack()

    # Key bindings for direction changes
    root.bind('<Left>', lambda e: change_direction('Left'))
    root.bind('<Right>', lambda e: change_direction('Right'))
    root.bind('<Up>', lambda e: change_direction('Up'))
    root.bind('<Down>', lambda e: change_direction('Down'))

    place_food()
    draw_snake()
    draw_food()

    main_loop()
    root.mainloop()

def main_loop():
    global game_over
    if not game_over:
        move()
        root.after(100, main_loop)  # Delay between moves (adjust for speed)

def move():
    global snake, direction, food_pos, game_over

    x, y = snake[0]
    new_head = {
        'Right': (x + SNAKE_SIZE, y),
        'Left': (x - SNAKE_SIZE, y),
        'Up': (x, y - SNAKE_SIZE),
        'Down': (x, y + SNAKE_SIZE)
    }[direction]

    if check_collision(new_head):
        game_over = True
        show_game_over()
        return

    new_snake = [new_head] + snake[:-1]
    
    # Check if food is eaten
    if new_head == food_pos:
        new_snake.append(snake[-1])  # Grow the snake
        place_food()

    snake = new_snake.copy()  # Update snake position

    canvas.delete('all')
    draw_snake()
    draw_food()

def check_collision(head):
    x, y = head
    if (x < 0 or x >= WIDTH) or (y < 0 or y >= HEIGHT):
        return True
    if head in snake[1:]:  # Snake hit itself
        return True
    return False

def show_game_over():
    canvas.create_text(WIDTH//2, HEIGHT//2,
                       text="Game Over!", fill='red',
                       font=('Arial', 30))

def change_direction(new_dir):
    global direction
    if not game_over:
        # Prevent reverse direction (e.g., Left when moving Right)
        if (new_dir == 'Left' and direction != 'Right') or \
           (new_dir == 'Right' and direction != 'Left') or \
           (new_dir == 'Up' and direction != 'Down') or \
           (new_dir == 'Down' and direction != 'Up'):
            direction = new_dir

def place_food():
    global food_pos
    while True:
        x = random.randint(0, (WIDTH//SNAKE_SIZE)-1) * SNAKE_SIZE 
        y = random.randint(0, (HEIGHT//SNAKE_SIZE)-1) * SNAKE_SIZE
        pos = (x, y)
        if pos not in snake:
            food_pos = pos
            break

def draw_snake():
    for segment in snake:
        x,y = segment
        canvas.create_rectangle(x, y,
                                x + SNAKE_SIZE, y + SNAKE_SIZE,
                                fill='green')

def draw_food():
    x,y = food_pos
    canvas.create_oval(x, y,
                       x + SNAKE_SIZE, y + SNAKE_SIZE,
                       fill='red')

if __name__ == "__main__":
    main()
