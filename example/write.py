from stdio import clear
from stdio import write
from stdio import skipline
from stdio import deleteline
from stdio import deletechar

# Usage examples:
clear()             # Clears the terminal
write("start")      # Writes the string "start" to the terminal
skipline()          # Skips one line in the terminal
write("a")          # Writes the string "a" to the terminal
skipline()          # Skips one line in the terminal
write("b")          # Writes the string "b" to the terminal
skipline()          # Skips one line in the terminal
write("c")          # Writes the string "c" to the terminal
deleteline()        # Deletes the last line from the terminal
skipline()          # Skips one line in the terminal
write("123")        # Writes the string "123" to the terminal
write("456")        # Writes the string "456" to the terminal
write("789")        # Writes the string "789" to the terminal
deletechar()        # Deletes the last character in the terminal
skipline(2)         # Skips two lines in the terminal
write("end!!!")     # Writes the string "end!!!" to the terminal
deletechar(2)       # Deletes the last 2 characters in the terminal
skipline(2)         # Skips two lines in the terminal

# Output

'''
start
a
b
12345678

end!

'''
