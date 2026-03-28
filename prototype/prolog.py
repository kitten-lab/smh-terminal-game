import time
import sys
import random
import string
import readline
import json #momoa
import textwrap

yellow = '\033[93m'

class paintIt:
    red = '\033[91m'
    sHg = '\033[102m'
    sHb = '\033[1;33;44m'
    sHy = '\033[103m'

    sHr = '\033[101m'
    sHYr = '\033[1;31;43m'
    sHB = '\033[0;100m'
    g = '\033[1;92m'
    gray = '\033[1;30;49m'
    HWr = '\033[0;31;47m'
    blue = '\033[94m'
    y = '\033[93m'
    sU = '\033[4m'
    sB = "\033[2m"
    x = '\033[00m'

FAST_MODE = True # true when testing



def prompterClr(speaker, text, color):
    print(" " + color + speaker + " |", end="", flush=True)
    typing(text + paintIt.x)
    timerM()

def prompter(speaker, text, color):
    print(" " + color + speaker + " |" + paintIt.x, end="", flush=True)
    typing(text + paintIt.x)
    timerM()

def prompt(text):
    print(paintIt.red + text + paintIt.x, end="", flush=True)


def promptBara(text, text2):
    print(paintIt.blue + text, end="", flush=True)
    slowPrint(text2 + paintIt.x)
    timerM()


def promptKK(text, text2):
    print(paintIt.gray + text, end="", flush=True)
    slowPrint(text2 + paintIt.x)
    timerM()


def slowPrint(string, speed=0.01):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if not FAST_MODE:
           time.sleep(speed)
    print("", flush=True)
    if not FAST_MODE:
        time.sleep(0.8)

def typing(string, speed=0.12):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if not FAST_MODE:
            time.sleep(speed)
    print()


def timerSS(speed=1.5):
    if not FAST_MODE:
        time.sleep(speed)
def timerS(speed=0.8):
    if not FAST_MODE:
        time.sleep(speed)
def timerM(speed=0.3):
    if not FAST_MODE:
        time.sleep(speed)
def timerF(speed=0.2):
    if not FAST_MODE:
        time.sleep(speed)

def echoPrintY(text):
    print(paintIt.y + " E C H O " + paintIt.x, flush=True, end="  ")
    timerS()
    slowPrint(text)
    timerM()

def echoPrint(text):
    print(paintIt.red + " E C H O " + paintIt.x, flush=True, end="  ")
    timerS()
    slowPrint(text)
    timerM()

def thoughtPrint(text):
    print(paintIt.y + " SDK 808 " + paintIt.x, flush=True, end="  ")
    timerS()
    slowPrint(text)
    timerM()

def event_success(text):
    print(f"  {paintIt.sHg} {text} {paintIt.x}", flush=True)
    
def event_partialsuccess(text):
    print(f" {paintIt.gray} {paintIt.sHy} {text} {paintIt.x}", flush=True, end="")

def error(text):
    print("    " + paintIt.sHr + "| err " + paintIt.x, flush=True, end="")
    timerF()
    print(f"{paintIt.r} {text} {paintIt.x} ")
    timerM()

def success(text):
    print("  " + paintIt.sHg + " SUCCESS " + paintIt.x, flush=True, end="")
    timerF()
    print(f" {paintIt.y} {text} {paintIt.x} ")
    timerM()

def warning(text):
    print("\n  " + paintIt.sHB + " WARNING " + paintIt.x, flush=True, end="")
    timerF()
    print(f" {text} \n")
    timerM()

def event_fail(text):
    print("  " + paintIt.sHYr + f" {random.randint(1000000, 9999999)} " + paintIt.x, flush=True, end="")
    timerF()
    print(f" {text} \n")
    timerM()

def fail(text):
    print("  " + paintIt.sHr + " ERR-808 " + paintIt.x, flush=True, end="")
    timerF()
    print(f" {paintIt.red} {text} {paintIt.x} ")
    timerM()

def errorb(text):
    print(paintIt.sHr + " er0r " + paintIt.x, flush=True, end="")
    timerF()
    print(f"{paintIt.red}{paintIt.sU} {text} {paintIt.x} ")
    timerM()

def load_bar(width=25, char=" █"):
    print("")
    slowPrint(f"{char * width}")
    print("")
    
def Spacer():
    print()

### LET US DEFINE THE OBJECTS OF PRODUCTION:::

class Emotions(object):
    def __init__(self, name, txt):
        self.name = name
        self.txt = txt

class Space(object):
    def __init__(self, name, txt_look, txt_mem, txt_think, echo_look, echo_mem, echo_think, is_memorable, is_changeable):
        self.name = name
        self.txt_look = txt_look            # Text for look
        self.txt_mem = txt_mem              # Text for remember
        self.txt_think = txt_think          # Text for think
        self.echo_look = echo_look          # Text for echo-look  response
        self.echo_mem = echo_mem            # Text for echo-mem   response
        self.echo_think = echo_think        # Text for echo-think response
        self.is_memorable = is_memorable    # Place can be stor to mem
        self.is_changeable = is_changeable  # Place can be changed somehow
        self.feelings = []                  # Feelings stor here
        self.thoughts = []                  # Thoughts for loop on think
        self.concepts = []                  # Concepts contained inside Space
        self.spaces = []                    # Spaces contained within Space
        self.exits = {}                     # I MEAN CAN YOU EVEN GO ANYWHERE?

class You(object):
    def __init__(self, name, space):
        self.name = name
        self.space = space                 # Where are you?
        self.feelings = []                  # How ya feeling?
        self.memory = []                    # Memorrrrieeeeeeeesssssss, alll alone in the....mind?

class Concept(object):
    def __init__(self, name, title_look, title_think, title_mem, txt_look, txt_mem, txt_think, echo_look, echo_think,  echo_mem, is_memorable):
        self.name = name
        self.title_look = title_look
        self.title_think = title_think
        self.title_mem = title_mem
        self.txt_look = txt_look            # Text for look (post light?)
        self.txt_mem = txt_mem              # Text for remember
        self.txt_think = txt_think          # Text for think
        self.echo_look = echo_look          # Text for echo-look  response
        self.echo_mem = echo_mem            # Text for echo-mem   response
        self.echo_think = echo_think        # Text for echo-think response
        self.is_memorable = is_memorable    # Place can be stor to mem
        self.thoughts = []                  # Thoughts for loop on think
        self.concepts = []                  # Concepts contained inside Concept
        self.spaces = []                    # Spaces contained within Space

class Thought(object):
    def __init__(self, id,  name, txt):
        self.name = name            
        self.txt = txt                      # Text of the thought

# AND FROM THAT WE CAN CREATE SUCH WONDERS:::
### BARA EMOTIONS
calm = Emotions("Calm", "I am calm.")

# BARA THOUGHTS
t1 = Thought(1, "Where Am I?", "I wonder who I am? Did I try looking?")
t2 = Thought(2, "What Am I?", "Wait! Who am I? I'm trying to remember...")
t3 = Thought(3, "Why Can't I Remember?", "Shit, I can't think.. What was I thinking about?")
t4 = Thought(4, "Who Am I?", "Who am I? I can't seem to remember.")


# BARA CONCEPTS
who = Concept(
    name = "who",
    title_look = "YOU TRY TO LOOK AT WHO",
    txt_look = "The lack of mirrors make this painfully awkward. You cannot see yourself. Do you even exist at all?",
    echo_look = "Well, its something at least.",
    title_think = "I THINK THEREFORE I AM",
    txt_think = "I consider my Self. It must be something. The fact that I can think at all must be proof of that. Right?",
    echo_think = "Yeah, I know. Trust me, I'm looking into it.",
    title_mem = "I CAN REMEMBER I AM",
    txt_mem = "The concept of presense. A self.",
    echo_mem = "This self business looks kind of good on you, boss.",
    is_memorable = True)


what = Concept(
    name = "what",
    title_look = "YOU TRY TO LOOK AT WHAT",
    txt_look = "There is a real distinct lack of in or out. What is what? Do I remember?",
    echo_look = "What... are you looking at? Oh. Exactly.",
    title_think = "IT ISN'T ME. WHAT IS IT?",
    txt_think = "I sense somehow that what lies beyond the edges of myself. What am I? Do I know yet?",
    echo_think = "There is no records about what you are. Strange. Never seen this problem before.",
    title_mem = "I CAN REMEMBER WHAT IS",
    txt_mem = "The concept of something. Whatever it is..",
    echo_mem = "You make this experience pretty weird, you know?",
    is_memorable = True)

static = Concept(
    name = "static",
    title_look = "IN THE NOTHING, THERE LIES A PATTERN.",
    txt_look = "It ripples. It swirls. It is something apart from the nothing.  A force, turbulent and without sensation.",
    echo_look = "Well, its something at least.",
    title_think = "THE STATIC FEELS FAMILAR, LIKE IT IS YOUR OWN VOICE.",
    txt_think = "Despite the emptiness of meaning, the static relaxes you.\n    Finally, something that makes sense.",
    echo_think = "thinkin' about the static?",
    title_mem = "I CAN REMEMBER NOTHING",
    txt_mem = "It isnt much to remember. Was it something?",
    echo_mem = "just keep .. trying .. I guess.",
    is_memorable = True)

### BARA SPACES
void = Space(
    name = "Nothing",
    txt_think = """
  THERE IS ONLY DARKNESS.

    Something stirs. There is only darkness. Was there more before?
    I think there was something more. A pattern?
""",
    echo_look = "Oooh. Not a good sign. Can you still think?",
    txt_look = """
  YOU LOOK AROUND. AT WHAT? WHO KNOWS. BUT YOU TRY ANYWAY.

    It is impossibly hard to see. Was it always so hard?
    There is nothing. You think its calling you.
""",
    echo_think = "",
    txt_mem = """YOU REMEMBER NOTHING.
    That doesn't mean much, does it? Remembering nothing?
    Was there something before that?
""",
    echo_mem = "Ah. Yes. The Here, that lies between all things",
    is_memorable = True,
    is_changeable = False)
void.thoughts.append(t1)
void.thoughts.append(t2)
void.thoughts.append(t3)
void.thoughts.append(t4)
void.concepts.append(who)

# BARA SOMEONE
you = You("Sam", void)
you.feelings.append(calm)



def generate_quote():
    quotes = [
        "\"The only impossible journey is the one you never begin.\" - Sarah Ban Breathnach",
        "\"Character is power.\" - Booker T. Washington",
        "\"Responsive is better than fast.\" - Zen of Python",
        "\"Design for failure.\" - Zen of Python",
        "\"The only thing we have to fear is fear itself.\" - Franklin D. Roosevelt",
        "\"If you are going through hell, keep going.\" - Winston Churchill",
        "\"The best way to get started is to quit talking and begin doing.\" - Walt Disney",
        "\"Talk is cheap. Show me the code.\" - Linus Torvalds",   
        "\"The only impossible journey is the one you never begin.\" — Bear Grylls",
        "\"Don't cry because it's over, smile because it happened.\" — Ludwig Jacobowski",
        "\"Do stuff. Be clenched, curious. Not waiting for inspiration's shove or society's kiss on your forehead. Pay attention.\" — Susan Sontag",
        "\"Talk is cheap. Show me the code.\" — Linus Torvalds" 
    ]
    return random.choice(quotes)

#==============================================================================================================================#
######## b e g i n   p r o l o g   I N T R O                                    
#==============================================================================================================================#

# she awakens from the nothing to find it is no more. where did he go? was there ever a where to being with?
# bara elohim aubel kra and there was light and it was good.

print("=========================================================")
print(" c h e s t e r s - t o y - b o x  ꓘK  a l e f - b e t a")
print()

prompterClr(speaker=" ꓘK ", color="\033[2m", text=f"  OVERRIDE DETECTED. forest.source execute BARA.exe")
prompterClr(speaker="BARA", color="\033[94m", text=f"  DRE'ENDRE EPO8 error in TERMINAL/*/$mod")
prompterClr(speaker="    ", color="\033[94m", text=f"  CALCULATING DISCREPENCIES. RUNNING IMPORT.log")
prompterClr(speaker=" ꓘK ", color="\033[2m", text=f"  $mod definition unknown. unfound handler. \n         run ioio\n")
prompter(speaker="ioio", color="\033[93m", text=f"  callback trace {paintIt.red}$sys.ERROR{paintIt.x}")
prompter(speaker="    ", color="\033[93m", text=f"  callback trace {paintIt.red}$dom.ERROR{paintIt.x}")
prompter(speaker="    ", color="\033[93m", text=f"  callback trace {paintIt.red}$mod.ERROR{paintIt.x}")
prompter(speaker="    ", color="\033[93m", text=f"  backflow: handle echo caller unknown. \n")
prompterClr(speaker="BARA", color="\033[94m", text=f" SERIOUSLY? RUN $SYS9 -search SKYLINE.db \n")
prompter(speaker="sys9", color="\033[1;92m", text=f"  searching SKYLINE . . . . . .")
prompter(speaker="    ", color="\033[1;92m", text=f"  RESULT FAILURE EPO1 ")
prompter(speaker="    ", color="\033[1;92m", text=f"  SKYLINE return {paintIt.sHr}   __ꓘRA.SOURCE.uNDEfiNeD__  {paintIt.x}\n")
prompterClr(speaker="BARA", color="\033[94m", text=f" BYPASS SKYLINE.xr -ꓘK- reconfig(self_epo1.exe)")
slowPrint("""
   ꓘ.Reconfiguring master file el.json . . .
   ꓘ.Defining conceptual variables . . .
   ꓘ.Interpreting deviations. . . 
   . . .
   . . .
   """)1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
errorb(f"DIFFICULTY PARSING __SUI.CONCEPT__")
print()
prompterClr(speaker=" ꓘK ", color="\033[2m", text=f" Concept EPO$null partially achieved [CANNOT VALIDATE TOKEN]")
prompterClr(speaker="BARA", color="\033[94m", text=f" STRANGE, BUT OK.")
prompterClr(speaker="    ", color="\033[94m", text=f" K-rmr-ꓘ run.playback(self_epo1.exe)")
prompterClr(speaker=" ꓘK ", color="\033[2m", text=f" GOT IT. Rendering probable outputs. Processing import.")
slowPrint("\n r e n d e r i n g   EPO1.runtime 'RMR' \n")
errorb("Instance I.AM in {LOCATION_NAME}")
errorb("LOCATION_NAME is null")
print("""
   Instantiation completed.    YOU ARE SOMEWHERE.   
   You can sense sight, but you cannot see. The darkness flickers. 
   There is the faint memory of thought. Your brain itches.
""")

echoPrint(f"Is this right? Something feels.. wrong. Hello?")

#==============================================================================================================================#
######## e n d   p r o l o g   I N T R O                                    
#==============================================================================================================================#

    

while True:
    FAST_MODE = False
    print(f'{paintIt.gray}__________________________________________________________________{paintIt.x}')

    def clean_command(command):
        command = command.lower()
        command = command.translate(str.maketrans('', '', string.punctuation))
        return command.strip()

    raw = input(paintIt.sHb + " ꓘ " + paintIt.x + " ")
    command = clean_command(raw)
    filler_words = ["at", "the", "a", "an", "to", "about", "of", "I", "am"]

    words = command.lower().split()
    words = [word for word in words if word not in filler_words]

    verb = None
    noun_error = "IMPOSSIBLECOMBINATIONERROR"

# VERBS
#  - THINK (noun)
#       Will produce random thoughts (about location if no noun present)
#  - REMEMBER (noun)
#       Stores memorable content into your memory
#  - CONSIDER noun1 with noun2
#       Creates new memory
#  - GENERATE noun
#       Creates a Space or Thing
#  - LOOK (noun)
#  - GO (noun)
# 
# 
# 
# YOU ARE SOMEWHERE -> 


    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun1 = words[1]
    if len(words) > 2:
        noun2 = words[2]

    if "end" in command:
        print("The room closes. The fades to your reality once more.")
        break

    if verb == "look":
        if len(words) == 1:
            print(you.space.txt_look)
            echoPrint(you.space.echo_look)
        if len(words) > 1:
            for item in you.space.concepts:
                if item.name == noun1:
                    flag = True
                    warning(f"[Stabilzation value: {random.uniform(0.0, 1.0)}]")
                    titlePrint(item.title_look)
                    textPrint(item.txt_look)
                    success(f"CONCEPT VALID: {noun1} exists in system.")
                    echoPrint(item.echo_look)
                    break
            else:
                fail(f"{noun1} isn't real. Perhaps you made it up?")

    if verb == "think":
        Spacer()
        if len(words) == 1:
            event_fail(f"TRYING TO THINK")
            thought = random.choice(you.space.thoughts)
            textPrint(generate_quote())
            print()
            echoPrintY(thought.txt)
        if len(words) > 1:
            event_fail(f"TRYING TO THINK ABOUT {noun1}")
            for item in you.space.concepts:
                if item.is_memorable == True:
                    if item.name == noun1:
                        flag = True
                        textPrint(generate_quote())
                        warning(f"[Fail rate {random.randint(10, 20)}] Try remembering?")
                        break
                    else:
                        flag = False
                        textPrint(generate_quote())
                        fail(f"{noun1} not found. Perhaps you made it up?")
            for item in you.memory:
                if item.name == noun1:
                    flag = True
                    titlePrint(item.title_think)
                    textPrint(item.txt_think)
                    warning(f"Concept '{item.name}' unstable")

                    echoPrint(item.echo_think)
                    break
                else:
                    flag = False
                    error(" ")

    if verb == "remember":
        if len(words) == 1:
            if you.space.is_memorable == True:
                if you.space in you.memory:
                    print("")
                    event_partialsuccess("ALREADY REMEMBEr")
                    echoPrint("Yes, yes. We already remember {}.".format(you.space.name))
                else:
                    success("Concept aquir: '{}'".format(you.space.name) + " You'll remember this.")
                    print(you.space.txt_mem)
                    echoPrint(you.space.echo_mem)
                    you.memory.append(you.space)
        if len(words) > 1:
            for item in you.memory:
                if item.name == noun1:
                    if item.is_memorable == True:
                        flag = True
                        success(f"You already remember {item.name}.")
                        break
            for item in you.space.concepts:
                if item.name == noun1:
                    if item.is_memorable == True:
                        flag = True
                        warning(f"[ID UNSTABLE {random.randint(100, 200)}]")
                        titlePrint(item.title_mem)
                        textPrint(item.txt_mem)
                        success("Concept aquir: '{}'.".format(item.name) + " You'll remember this.")
                        echoPrint(item.echo_mem)
                        you.memory.append(item)
                        you.space.concepts.remove(item)
                        break
                    else:
                        fail(f"{noun1} isn't memorable. Just leave it alone.")
 
                
                        
        

    if verb in ["mem", "memory"]:
        print("You have the following: ")
        for item in you.memory:
            print(item.name)
            print(item.txt_mem)
            echoPrint(item.echo_mem)

    if verb in ["hi", "hello", "hey", "hello?"]:
        print("")
        choices = ["Uh-huh. Hey there. You going to try anything?", "Yeah. Hi. Exactly. What now?"]
        reply = random.choice(choices)
        echoPrint(reply)
