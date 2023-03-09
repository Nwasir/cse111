# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

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

     #Draw moon front
    draw_moon(canvas, 200, 200, 600, 600)
    moon_light(canvas, 200, 200, 600, 600)
    # Draw the moon and the lights
    moon_light_lighter(canvas, 170, 170, 630, 630)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_clouds(canvas, x0, y0, x1, y1):
    """Draw the clouds"""
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="slategray2")

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")

    # Draw a pine tree.
    tree_center_x = 140
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 100
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 200
    tree_bottom = 100
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

  
        # Draw another pine tree.
    tree_center_x = 250
    tree_bottom = 100
    tree_height = 160
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

     # Draw another pine tree.
    tree_center_x = 50
    tree_bottom = 100
    tree_height = 240
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_moon(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="darkOrchid3")
    """Draw the moon"""
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="seashell")

def moon_light(canvas, x0, y0, x1, y1):
    """Draw the light of the moon"""
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="white")

def moon_light_lighter(canvas, x0, y0, x1, y1):
    """Draw the lighter light of the moon"""
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="slategray2")

# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()