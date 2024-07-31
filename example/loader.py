from stdio.write import clear
from stdio.write import skipline
from stdio.write import write
from stdio.loader import Loader
from time import sleep


clear()
write("Example: Basic Usage")
skipline()
ldr = Loader()
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Custom Min and Max Progress")
skipline()
ldr = Loader(
    min_progress=50,
    max_progress=200
)
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Custom Fill and Empty Strings")
skipline()
ldr = Loader(
    fill_string=">",
    empty_string="-"
)

while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Custom Pre-string")
skipline()
ldr = Loader(
    pre_string=""
)
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Starting with Custom Progress")
skipline()
ldr = Loader(
    current_progress=30
)
while ldr.current_progress < ldr.max_progress:
    sleep(0.1)
    ldr.increase(2)

skipline(2)

#######################
write("Example: Decreasing Progress")
skipline()
ldr = Loader(
    current_progress=100
)
while ldr.current_progress > ldr.min_progress:
    sleep(0.1)
    ldr.increase(-2)

skipline(2)

#######################
write("Example: Manual Progress Entry")
skipline()
ldr = Loader(
    current_progress=100
)

ldr.progress(10)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(80)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(10)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(80)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(10)
sleep(0.1)
ldr.progress(10)
sleep(0.1)
ldr.progress(20)
sleep(0.1)
ldr.progress(40)
sleep(0.1)
ldr.progress(80)
sleep(0.1)
ldr.progress(100)

# Output

'''
Example: Basic Usage

100/100 ███████████████████████

Example: Custom Min and Max Progress

200/200 ███████████████████████

Example: Custom Fill and Empty Strings

100/100 >>>>>>>>>>>>>>>>>>>>>>>

Example: Custom Pre-string

███████████████████████████████

Example: Starting with Custom Progress

100/100 ███████████████████████

Example: Decreasing Progress

0/100

Example: Manual Progress Entry

100/100 ███████████████████████
'''
