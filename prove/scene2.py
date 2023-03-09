# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    #draw_clouds(canvas, scene_width, scene_height)
    # Draw the top cloud
    x0 = 50
    y0 = 650
    x1 = 150
    y1 = 700
    for i in range(2):
        draw_clouds(canvas, x0, y0, x1, y1)
        y0 += 18
        y1 += 18
        for j in range(2):
            draw_clouds(canvas, x0, y0, x1, y1)
            x0 += 18
            x1 += 18

    #Bottom cloud
    # Draw the bottom cloud
    x0 = 600
    y0 = 150
    x1 = 700
    y1 = 200
    for k in range(2):
        draw_clouds(canvas, x0, y0, x1, y1)
        y0 -= 18
        y1 -= 18
        for l in range(2):
            draw_clouds(canvas, x0, y0, x1, y1)
            x0 -= 18
            x1 -= 18
    


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")
    

"""def draw_clouds(canvas, scene_width, scene_height):
    draw_oval(canvas, 200, 400, 550, 450, outline="white", fill="white")
    draw_oval(canvas, 100, 400, 500, 450, outline="white", fill="white")
    draw_oval(canvas, 100, 400, 300, scene_height, outline="white", fill="white")
    #draw_oval(canvas, 150, 400, 350, scene_height, outline="white", fill="white")
    draw_oval(canvas, 200, 400, 300, 400, outline="white", fill="white")   """

def draw_clouds(canvas, x0, y0, x1, y1):
    """Draw the clouds"""
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="darkOrchid2")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_bottom, tree_height)
    
    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 100
    tree_height = 220
    draw_pine_tree(canvas, tree_bottom, tree_height)

def draw_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")
    

    
# Call the main function so that
# this program will start executing.
main()