class Clade:
    def __init__(self):
        #attributes
        self.name = ""
        self.children = []
        self.height = int(0)
        self.position = 0.0
    
    #print the cladogram starting from this point
    def print_tree(self):
        name_length = len(self.name)
        num_children = len(self.children)

        #generating the text arrows, part 1
        arrow_top = " "*(name_length//2)
        arrow_bottom = " "*(name_length//2)

        #printing the name of the clade (and ending the process if there is nothing else to do)
        if num_children == 0:
            print(self.name, end=" ")
            return
        else:
            print(self.name)
        
        #generating the text arrows, part 2
        for child in self.children:
            arrow_top +=  "|" + " "*(len(child.name))
            arrow_bottom += "V" + " "*(len(child.name))
 
        print(arrow_top)
        print(arrow_bottom)

        #recursion
        for child in self.children:
            child.print_tree()
    
    #calculates height as one more than that of the highest of its children
    def calculate_height(self):
        num_children = len(self.children)
        if num_children > 0:
            for child in self.children:
                if child.height > self.height:
                    self.height = child.height
            self.height += 1
    
    #calculates position as the average of its children
    def calculate_position(self):
        num_children = len(self.children)
        if num_children > 0:

            #adds all the positions together
            position_sum = 0.0
            for child in self.children:
                position_sum += child.position
            
            #divides by the number of children
            self.position = position_sum/num_children
            
def generate_parent(title, children):
    # Unsure best way to do this. Doesn't seem like dictionaries or lists would work at all for what I want, and people online said that all other methods were poor practice
    # I tried out using exec() anyway and it didn't work. The generated classes seemed to stop existing outside of this function
    # It is possible to avoid having to create arbitrality named classes within this function specifically, but they will have to be created somewhere in the code
    # If they were not generated somewhere, every single clade would have to be made manually before the code was run (not even as part of the input) which is unfeasible, impractical, inefficient, and defeats the purpose of this program
    # I think I need to either stop using python, or not use classes for this

    title = Clade()
    # [the contents of title].children = children
    # [the contents of title].calculate_height
    # [the contents of title].calculate_position
    return

# ["clade", ["clade", "clade"]]
print("hi")
    
 
clade1 = Clade()
clade1.name = "top clade"
 
clade2 = Clade()
clade2.name = "clade 2"

clade3 = Clade()
clade3.name = "clade 3"

clade4 = Clade()
clade4.name = "clade 4"

clade5 = Clade()
clade5.name = "clade 5"

# clade6 = Clade()
# clade6.name = "clade 6"
# clade6.position = 1.0
 
#Create relationships
clade1.children.append(clade2)
clade1.children.append(clade3)
clade2.children.append(clade4)
clade2.children.append(clade5)

placeholder_children_var = []
generate_parent("parent_clade", placeholder_children_var)

# clade6.calculate_height()
# clade5.calculate_height()
# clade4.calculate_height()
# clade3.calculate_height()
# clade2.calculate_height()
# clade1.calculate_height()
# clade6.calculate_position()
# clade5.calculate_position()
# clade4.calculate_position()
# clade3.calculate_position()
# clade2.calculate_position()
# clade1.calculate_position()

 
# print(clade1.height, end=" ")
# print(clade1.position)
# print(clade2.height, end=" ")
# print(clade2.position)
# print(clade3.height, end=" ")
# print(clade3.position)
# print(clade4.height, end=" ")
# print(clade4.position)
# print(clade5.height, end=" ")
# print(clade5.position)
# print(clade6.height, end=" ")
# print(clade6.position)