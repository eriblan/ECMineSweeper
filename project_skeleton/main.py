import pygame
import sys
from cell import Cell
from calcs import measure_distance
import time

""" This is the main file you work on for the project"""

pygame.init()

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.1  # Change to prefered value or use default 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells  # how large can each cell be? 46px?
READJUSTED_SIZE = CELL_SIZE * amount_of_cells
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE  # Probably not needed, just use cell_size

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("MineSweeper")

cells = []


def create_cells():
    """This function is meant to initialy generate all the cells and create the boundaries"""
    # This is a good base to go from (think about it thoroughly before you code!! We want to create 16x16 list with each object being a cell):
    # for a_row in range(amount_of_cells):
    #     row = []
    #     for a_column in range(amount_of_cells):
    #         pass

    for a_row in range(amount_of_cells):
        row = []
        for a_column in range(amount_of_cells):
            # Position of a given cell
            position_x = a_column * CELL_SIZE
            position_y = a_row * CELL_SIZE
            # Create cell object
            cell = Cell(position_x, position_y, CELL_SIZE, CELL_SIZE, bomb_chance) 
            row.append(cell)
        cells.extend(row)  




def draw_cells():
    """In this function we want to draw each cell, i.e call upon each cells .draw() method!"""
    # Hint: take inspiration from the forloop in create_cells to loop over all the cells
    # For each cell in cells, call the cell's draw method
    for cell in cells:
        cell.draw(screen)


def draw():
    """This function handles all the drawings to the screen, such as drawing rectangles, objects etc"""
    draw_cells()


def event_handler(event):
    """This function handles all events in the program"""
    if event.type == pygame.QUIT:
        terminate_program()
    
    # If mouseclick
    buttons = pygame.mouse.get_pressed()
    if event.type == pygame.MOUSEBUTTONDOWN and buttons[0] == True:

        # Get mouse position from event
        mouse_position = event.pos
        print(f"Clicked mouse position: {mouse_position[0]},{mouse_position[1]}")

        for cell in cells:
            # Calculate Pythagorean distance between mouse position and cell center
            distance = measure_distance(mouse_position[0], mouse_position[1], cell.cell_center[0],cell.cell_center[1])
            # If distance is under or equal to cell size divided by two, the given cell is the one that is clicked on
            if distance <= CELL_SIZE // 2:
                # Prints location where cell begins, neighboring bombs and if cell has a bomb
                print(f"Clicked cell: {cell.x}, {cell.y}, Neighboring bombs: {cell.neighboring_bombs}, Cell has a bomb: {cell.bomb}")
                

                # Set cell to be selected

                #cell.selected = True
                # Check if neighboring cells are 0
                reveal_cell(cell)


                # TODO: Simple restart function
                """
                if cell.bomb:
                    show_restart_screen()
                """



def reveal_cell(input_cell):
    """Recursive function that reveals other cells that are also without neighboring bombs, like the original minesweeper"""   

    input_cell.selected = True
    # If input cell has zero neighboring bombs and is not a bomb itself
    if input_cell.neighboring_bombs == 0 and not input_cell.bomb:
        for cell in cells:
            # Check if cell is a neighbor, if the delta distance between the cell that is controlled and another cell is smaller or equal to the cell size for x and y, it should be a neighbor
            if cell is not input_cell and abs(cell.x - input_cell.x) <= CELL_SIZE and abs(cell.y - input_cell.y) <= CELL_SIZE:
                # If this cell has not been marked as selected already
                if not cell.selected:
                    reveal_cell(cell)    


def run_setup():
    """This function is meant to run all code that is neccesary to setup the app, happends only once"""
    create_cells()

    # Add neighboring bombs count to each cell
    find_neighboring_bombs()
    #print(f"Neighboring bombs: {cell.neighboring_bombs}")


def find_neighboring_bombs():
        
    for input_cell in cells:
        # Init amount of neighboring bombs to 0
        input_cell.neighboring_bombs = 0
        for cell in cells:
            # Check if cell is a neighbor, if the delta distance between the cell that is controlled and another cell is smaller or equal to the cell size for x and y, it should be a neighbor
            if cell is not input_cell and abs(cell.x - input_cell.x) <= CELL_SIZE and abs(cell.y - input_cell.y) <= CELL_SIZE:
                # Check if neighbor contains a bomb
                if cell.bomb:
                    input_cell.neighboring_bombs += 1

def terminate_program():
    """Functionality to call on whenever you want to terminate the program"""
    pygame.quit()
    sys.exit()

def show_restart_screen():
    running = True
    while running:
        screen.fill((0, 0, 0))

        # Display the restart message
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("GAME OVER. Press Y to restart, N to quit", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate_program()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # If Y is pressed, restart the game
                    running = False
                    restart_game()
                elif event.key == pygame.K_n:  # If N is pressed, quit the game
                    running = False
                    terminate_program()


def restart_game():
    cells.clear()  # Clear the cells list
    run_setup()  # Create a new grid of cells

def main():
    run_setup()

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            event_handler(event)

        draw()
        pygame.display.flip()



    terminate_program()


if __name__ == "__main__":
    main()


