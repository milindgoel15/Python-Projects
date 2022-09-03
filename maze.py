# my solution but comes with infinite loop for 3 test cases:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def right_move():
#     turn_right()
#     move()
    
# while not at_goal():
#     if wall_in_front():
#         if wall_on_right():
#             turn_left()
#         else:
#             right_move()
#     else:
#         if right_is_clear():
#             right_move()
#         else:
#             move()

# actual solution from udemy:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()