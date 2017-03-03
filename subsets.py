def sublists(big_list, selected_so_far):
    if big_list == []:
        print selected_so_far
    else:
        current_element = big_list[0]
        rest_of_big_list = big_list[1:]
        sublists(rest_of_big_list, selected_so_far + [current_element])
        sublists(rest_of_big_list, selected_so_far)

dinner_guests = ["LM", "ECS", "SBA"]
sublists(dinner_guests, [])

'''
['LM', 'ECS', 'SBA']
['LM', 'ECS']
['LM', 'SBA']
['LM']
['ECS', 'SBA']
['ECS']
['SBA']
[]
'''
