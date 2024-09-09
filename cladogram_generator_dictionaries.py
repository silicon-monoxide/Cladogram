# imported to allow for proper conversion of the user's input into a list, since pythons standard functions will not work
import json
#tk import
import tkinter as tk

#Creating the dictionaries that contain all the information for each clade
clade_name = {}
clade_children = {}
clade_height = {}
clade_position = {}

#list of all the leaf keys (clades without children)
leaf_list = []

#the key for the root clade
root = ""

#for error checking
has_error = False
error_string = ""
# function for creating a clade
def create_clade(key, name, children, height, position):
    clade_name[key] = name
    clade_children[key] = children
    clade_height[key] = height
    clade_position[key] = position

#calculates height as one more than that of the highest of its children
def calculate_height(self):
    num_children = len(clade_children[self])
    if num_children >= 1:
        for child in clade_children[self]:
            if clade_height[child] > clade_height[self]:
                clade_height[self] = clade_height[child]
        clade_height[self] += 1

#calculates position as the average of its children
def calculate_position(self):
    num_children = len(clade_children[self])
    if num_children > 0:

        #adds all the positions together
        position_sum = 0.0
        for child in clade_children[self]:
            position_sum += clade_position[child]
            
        #divides by the number of children and makes the result the new position of the clade
        clade_position[self] = position_sum/num_children

#generates a parent for a list of clades and calculates its height and position
def create_parent(key, children):
    create_clade(key, key, children, 0, 0.0)
    calculate_height(key)
    calculate_position(key)

#creates all the leaf/terminal/idkwhatelsetocallthem clades. Input is a list of the names of the clades (not keys). Each new clade has 1 higher position than the previous one.
#also adds the keys (in order) to leaf_list
def generate_leaves(name_list):
    leaf_counter = 0
    for clade_name in name_list:
        key = "clade" + str(leaf_counter)
        create_clade(key, clade_name, [], 0, float(leaf_counter))
        leaf_list.append(key)
        leaf_counter += 1

#takes the user input (nested lists with strings) and converts it into something that generate_leaves can process
def locate_leaves(user_input):
    name_list = []
    for item in user_input:
        if type(item) == str:
            name_list.append(item)
        elif type(item) == list:
            name_list = name_list + locate_leaves(item)
    return name_list

#recursive function that converts the names in a user input to keys from a list
def convert_input_to_keys(name_input, key_list, counter):
    output = []
    for item in name_input:
        # if the item is a string, add the appropriate key to its position in the output, then increment the counter by 1 so the next key will be chosen for the next string
        if type(item) == str:
            output.append(key_list[counter])
            counter += 1
        # if the item is a list, run the function recursively on that list using the current counter, add the resulting list to the output in the appropriate position, and then set the counter to the value the function outputs
        elif type(item) == list:
            recursion_output = convert_input_to_keys(item, key_list, counter)
            if recursion_output[0] != "ignore":
                output.append(recursion_output[0])
            counter = recursion_output[1]
    # if the output is an empty list, replace it with something the funtion will ignore
    if output == []:
        output = "ignore"
    #return the current output and counter
    return [output, counter]

#function that generates all the data for the cladogram
def generate_cladogram(instructions):
    children = []
    key = ""

    #generates a list of the children of the clade. If a child is a list, it runs the function recursively on that list to generate the child and receive the key. 
    #generates the key by adding the keys of the children together as a string
    for item in instructions:
        if type(item) == str:
            children.append(item)
            key += item
        elif type(item) == list:
            item_key = generate_cladogram(item)
            children.append(item_key)
            key += item_key
    
    # if there is only one child, alter the key to make it different from that of the child
    if len(children) == 1:
        key = "<" + key + ">"

    #creates the parent clade of the children
    create_parent(key, children)
    
    return key

def calculate_dimensions():
    global leaf_list

    # a list of the lengths of each name in the list
    total = 0

    #adds the name lengths to the list
    for leaf in leaf_list:
        total += (len(clade_name[leaf]))
    # takes the maximum and then sets it to the appropriate units
    if total > 15:
        total = int(total*10)
        return total
    else:
        return 150


# checks for errors
def error_test_general():
    #test if all clade dictionaries have the same keys
    error_test_incomplete_clade()
    error_test_one_input()
    #add more error tests later
def error_test_incomplete_clade():
    name_keys = clade_name.keys()
    if name_keys != clade_children.keys() or name_keys != clade_height.keys() or name_keys != clade_position.keys():
        global has_error
        has_error = True
        global error_string
        error_string += "Error: at least one clade is stored improperly. "
def error_test_one_input():
    global clade_name
    if len(clade_name) == 1:
        global has_error
        has_error = True
        global error_string
        error_string += "Error: there must be more than 1 clade inputted. "



#non-setup data creation code starts here

# ["0123456789012345678901234567890123456789012345", "0123456789012345678901234567890123456789012345"]
#the user input
#test input A: [[["clade zero"]], "clade one", ["clade two", ["clade three", "clade four", [[[0]], "clade five"], "clade six"]]]
#test input B: [[["000", "001"], ["010", "011"]], [["100", "101"], ["110", "111"]]]
#test input C: ["name", ["namename", ["namenamenamename", ["namenamenamenamenamenamenamename", ["namenamenamenamenamenamenamenamenamenamenamenamenamenamenamename"]]]]]
#test input D: [[["clade number one", "second clade", "clade that sure does exist (three)"]], [["this clade is named clade four"], ["clade 5"], ["clade ----> 6"]], ["the evil cursed clade (7)", "clade number eight", 9]]
user_input_string = input("enter input:")
try:
    user_input = json.loads(user_input_string)
except:
    has_error = True
    error_string += "Error: Invalid input "

error_test_general()
if has_error == False:
    #generates the leaves of the user input
    generate_leaves(locate_leaves(user_input))
    error_test_general()
if has_error == False:
    #converts the input into keys
    cladogram_instructions = convert_input_to_keys(user_input, leaf_list, 0)[0]
    error_test_general()
if has_error == False:
    #generates the all clades in the cladogram and the appropriate data
    clade_root = generate_cladogram(cladogram_instructions)
    error_test_general()
if has_error == False:
    #prints data
    # print(clade_name)
    # print(clade_children)
    # print(clade_height)
    # print(clade_position)
    # print(user_input)
    print(leaf_list)
    # print(cladogram_instructions)
else:
    #prints the error message
    print(error_string)




    

if has_error == False:
    # Create the main window
    root = tk.Tk()
    root.title("cladogram")

    # Create a canvas
    dimensions = calculate_dimensions()
    canvas_width, canvas_height = dimensions, dimensions
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack(padx=10, pady=10)

    # Calculate scaling factors and offsets
    max_x = max(clade_position.values())
    max_y = max(clade_height.values())
    offset_x = round(canvas_width/10)
    offset_y = round(canvas_height/10)
    scale_x = (canvas_width - (2*offset_x)) / max_x  # Leave some margin
    scale_y = (canvas_height - (2*offset_y)) / max_y  # Leave some margin

    #appearance variables
    rectangle_width = 1 + round(dimensions/200)
    connection_colour = "#000000"
    text_colour = "#000000"


#draws the lines connecting a parent clade and child clade
def draw_connection(parent, child):
    global offset_x
    global offset_y
    global scale_x
    global scale_y
    global max_y
    global rectangle_width
    global connection_colour

    # calculates the height in pixels
    parent_height = (max_y - clade_height[parent])*scale_y + offset_y - (rectangle_width/2)
    child_height = (max_y - clade_height[child])*scale_y + offset_y # + (rectangle_width/2)

    # if the position of the parent is higher than that of the child, do things one way. If it is lower, do the same thing but with the sign flipped for things being added to the position. 
    # If it is the same, don't draw the horisontal rectangle
    if clade_position[parent] > clade_position[child]:
        # calculates the position in pixels
        parent_position = clade_position[parent]*scale_x + offset_x + (rectangle_width/2)
        child_position = clade_position[child]*scale_x + offset_x - (rectangle_width/2)

        #draws the first (horizontal) rectangle
        canvas.create_rectangle((parent_position, parent_height), (child_position, (parent_height + rectangle_width)), fill=connection_colour, outline=connection_colour)
        #draws the second (vertical) rectangle
        canvas.create_rectangle(((child_position + rectangle_width), parent_height), (child_position, child_height), fill=connection_colour, outline=connection_colour)
    elif clade_position[parent] < clade_position[child]:
        # calculates the position in pixels
        parent_position = clade_position[parent]*scale_x + offset_x - (rectangle_width/2)
        child_position = clade_position[child]*scale_x + offset_x + (rectangle_width/2)

        #draws the first (horizontal) rectangle
        canvas.create_rectangle((parent_position, parent_height), (child_position, (parent_height + rectangle_width)), fill=connection_colour, outline=connection_colour)
        #draws the second (vertical) rectangle
        canvas.create_rectangle(((child_position - rectangle_width), parent_height), (child_position, child_height), fill=connection_colour, outline=connection_colour)
    else:
        # calculates the position in pixels
        parent_position = clade_position[parent]*scale_x + offset_x + (rectangle_width/2)
        child_position = clade_position[child]*scale_x + offset_x - (rectangle_width/2)

        #draws the rectangle
        canvas.create_rectangle((parent_position, parent_height), (child_position, child_height), fill=connection_colour, outline=connection_colour)
        
#draws the main structure of the cladogram
def draw_cladogram(clade):
    for child in clade_children[clade]:
        draw_connection(clade, child)
        draw_cladogram(child)

def write_leaves(leaf_list):
    global offset_x
    global offset_y
    global canvas_height
    global scale_x
    global text_colour

    # sets the height the text is written from
    text_height = canvas_height - (0.8*offset_y)
    for leaf in leaf_list:
        text_position = clade_position[leaf]*scale_x + offset_x
        name = clade_name[leaf]
        canvas.create_text(text_position, text_height, text=name, fill=text_colour)



def draw_root():
    global max_y
    global offset_x
    global offset_y
    global rectangle_width
    global connection_colour
    global clade_root

    # creates the dimentions of the top line
    bottom_height = (max_y - clade_height[clade_root])*scale_y + offset_y
    bottom_position = clade_position[clade_root]*scale_x + offset_x + (rectangle_width/2)
    top_height = (max_y - clade_height[clade_root])*scale_y + (offset_y/2)
    top_position = clade_position[clade_root]*scale_x + offset_x - (rectangle_width/2)

    #draws the rectangle
    canvas.create_rectangle((top_position, top_height), (bottom_position, bottom_height), fill=connection_colour, outline=connection_colour)


if has_error == False:
    draw_cladogram(clade_root)
    write_leaves(leaf_list)
    draw_root()

    root.mainloop()