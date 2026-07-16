def spam():
    global eggs
    eggs = "global in local"
    print(eggs)
    eggs = "spam local"

eggs = "global"
spam()