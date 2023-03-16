def line(queue):
    if len(queue) == 0:
        print("The line is currently empty.")
    else:
        print("The line is currently:", end=" ")
        for i, name in enumerate(queue):
            if i == len(queue) - 1:
                print(f"{i+1}. {name}")
            else:
                print(f"{i+1}. {name}", end=" ")

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    if position > 0:
        print(f"Welcome, {name}. You are number {position} in line.")
    return(queue)

def now_serving(queue):
    if len(queue) == 0:
      print("There is nobody waiting to be served!")
    else:
      next_person = queue.pop(0)
      print(f"Currently serving {next_person}.")