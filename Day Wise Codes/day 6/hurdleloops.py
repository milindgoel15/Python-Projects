# Python code for https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

#### ----------- HURDLE 1 ------------
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# with for loop
# for i in range(0,6):
#     move()
#     jump()
# OR
# with while loop 
# i = 5
# while i > 0:
#     move()
#     jump()

#### ----------- HURDLE 2 ------------
# while not at_goal():
#     jump()

#### ----------- HURDLE 3 ------------

# while not at_goal():
#     if not front_is_clear():
#         if not wall_in_front():
#             move()
#         else:
#             jump()
#     else:
#         if not wall_in_front():
#             move()
#         else:
#             jump()

# OR
# while not at_goal():
#     if not wall_in_front():
#         move()
#     else:
#         jump()

#### ----------- HURDLE 4 ------------
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         if right_is_clear():
#             turn_right()
#             move()
#         else:
#             move()
