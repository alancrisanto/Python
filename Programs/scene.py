import tkinter as tk
import random

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.

    tree_parameters = [[550, 200, 150],[400, 300, 120], [750, 250, 160], [50,250, 75],[475, 250, 125], [675, 225, 150], [35, 325, 75]]

    cloud_parameter = [[300, 50], [320, 60], [250, 100], [390, 75]]

    lake_parameter = [[500, 400], [600, 420], [460, 400], [550, 410]]
    
    sun_x = 650
    sun_y = 50

    house_x = 100
    house_y = 300

    window_x = 175
    window_y = 325
     
    
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom, 1)

    draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom, 1)
   
    for i in cloud_parameter:

        draw_cloud(canvas, i[0], i[1])

    for j in range(4000):
        draw_grass(canvas, scene_left, scene_right, scene_top, scene_bottom)

    for h in lake_parameter:

        draw_lake(canvas, h[0], h[1])

    for parameter in tree_parameters:

        draw_pine_tree(canvas, scene_left + parameter[0], scene_top + parameter[1], parameter[2])

    draw_sun(canvas, sun_x, sun_y)

    draw_house(canvas, house_x, house_y)

    draw_window(canvas, window_x, window_y)

    draw_fence(canvas, scene_left, scene_top, scene_right, scene_bottom, 20)

    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 50)



# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_fence(canvas,left, top, right, bottom, grid_spacing):


    #Horizontal lines --------------------------------------------
    for i in range(400, 450, grid_spacing):

        canvas.create_line(50, i , 350, i , width = 6, fill = "chocolate")

    # Vertical lines

    for i in range(75, 330, grid_spacing):

        canvas.create_line(i , 390, i,  450, width = 6, fill = "chocolate")

def draw_grid(canvas,left, top, right, bottom, grid_spacing):

    text_horizontal_margin = 20
    text_vertical_margin = 5

    #Horizontal lines --------------------------------------------
    for i in range(top, bottom, grid_spacing):

        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")

    # Vertical lines

    for i in range(left, right, grid_spacing):

        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text = f"{i}")


    # Sky  --------------------------------------------

def draw_sky(canvas, left, top, right, bottom, grid_spacing):

    bottom = 320

    for i in range(top, bottom, grid_spacing):

        canvas.create_line(left, i, right, i, fill = "dodgerBlue")

def draw_ground(canvas, left, top, right, bottom, grid_spacing):

    top = 320

    for i in range(top, bottom, grid_spacing):

        canvas.create_line(left, i, right, i, fill = "goldenrod")
    
def draw_house(canvas, house_x, house_y):

    # Draw the walls
    house_width = 200 # 75 x 100
    house_height = 150 # 250 y 300

    # Roof

    side_a = house_x - 25
    side_b = house_y
    side_c = house_width
    side_d = house_width
    side_e = house_x + house_width + 25
    side_f = house_y

    # House walls
    canvas.create_rectangle(house_x, house_y, house_x + house_width, house_y + house_height, outline="khaki1", fill="khaki1")
    

    # # Draw the ceiling
    canvas.create_polygon(side_a, side_b, side_c, side_d,side_e, side_f, fill = "red")

def draw_sun(canvas, sun_left, sun_top):

    sun_width = 100
    sun_height = 100

    canvas.create_oval(sun_left, sun_top, sun_left + sun_width, sun_top + sun_height,  outline = "yellow", fill = "yellow")

def draw_grass(canvas, left, right, top, bottom):
    
    grass_top = int((bottom - top) * 0.63)
    grass_left = random.randint(left, right)
    grass_top = random.randint(grass_top, bottom)
    grass_width = 4
    grass_heigth = 15

    canvas.create_rectangle(grass_left, grass_top, grass_left + grass_width, grass_top + grass_heigth, outline = "light green", fill = "green" )

def draw_cloud(canvas, cloud_left, cloud_top):

    cloud_width = 120
    cloud_height = 40

    canvas.create_oval(cloud_left, cloud_top, cloud_left + cloud_width, cloud_top + cloud_height,  outline = "white", fill = "white")

def draw_lake(canvas, cloud_left, cloud_top):

    cloud_width = 120
    cloud_height = 40

    canvas.create_oval(cloud_left, cloud_top, cloud_left + cloud_width, cloud_top + cloud_height,  outline = "RoyalBlue1", fill = "RoyalBlue1")

def draw_window(canvas, win_x, win_y):

    canvas.create_rectangle(win_x, win_y, win_x + 25, win_y + 25, outline = "black", fill = "white")
    canvas.create_rectangle(win_x + 25, win_y, win_x + 50, win_y + 25, outline = "black", fill = "white")
    canvas.create_rectangle(win_x, win_y + 25, win_x + 25, win_y + 50, outline = "black", fill = "white")
    canvas.create_rectangle(win_x + 25, win_y + 25, win_x + 50, win_y + 50, outline = "black", fill = "white")


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()

