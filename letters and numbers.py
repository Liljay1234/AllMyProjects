#function created to have a module i can call to save my code to a text file as a back up
def My_save(x,y):
    import os
    if not os.path.exists(r"C:\Users\joshw\Desktop\Python text saves\Saves"):
        os.makedirs(r"C:\Users\joshw\Desktop\Python text saves\Saves")
    My_file = open(r"C:\Users\joshw\Desktop\Python text saves\Saves\-"+ x + ".txt", "w")
    My_file.write("""start\n"""+ y + """
    end""")
    My_file.close()
