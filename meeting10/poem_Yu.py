##function_1: get the second paragraph from the poem

import re

regex = r"(?<=\n\n).+(?=\n\n)"

poem = ("The time will come when, with elation, you will greet yourself arriving at your own door, in your own mirror, and each will smile at the other's welcome, and say, sit here. Eat. You will love again the stranger who was your self. Give wine. Give bread. Give back your heart to itself, to the stranger who has loved you\n\n"
	"all your life, whom you ignored for another, who knows you by heart. Take down the love letters from the bookshelf,\n\n"
	"the photographs, the desperate notes, peel your own image from the mirror. Sit. Feast on your life.")

matches = re.finditer(regex, poem)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

##== RESTART: /Users/QianYu/Desktop/info206_exercises_Yu/meeting10/poem_Yu.py ==
##all your life, whom you ignored for another, who knows you by heart. Take down the love letters from the bookshelf,

## results for mypoem
## results for mypoem: no results since there is no paragraph in that poem.
        
##function_2: prints all words that begin with the letter “p”(lowercase)

poem = """The time will come
when, with elation,
you will greet yourself arriving
at your own door, in your own mirror,
and each will smile at the other's welcome,
and say, sit here. Eat.
You will love again the stranger who was your self.
Give wine. Give bread. Give back your heart
to itself, to the stranger who has loved you

all your life, whom you ignored
for another, who knows you by heart.
Take down the love letters from the bookshelf,

the photographs, the desperate notes,
peel your own image from the mirror.
Sit. Feast on your life."""

p_word=re.findall(r'\b[p]\w+', poem)

print (p_word)
##= RESTART: /Users/QianYu/Desktop/info206_exercises_Yu/meeting10/poem1_Yu.py =
##['photographs', 'peel']
## Results for my poem
##= RESTART: /Users/QianYu/Desktop/info206_exercises_Yu/meeting10/poem1_Yu.py =
##['pay', 'person']


##function_3: returns a list of all letters that end a sentence. (exclude the
#dot/period)

poem = """The time will come
when, with elation,
you will greet yourself arriving
at your own door, in your own mirror,
and each will smile at the other's welcome,
and say, sit here. Eat.
You will love again the stranger who was your self.
Give wine. Give bread. Give back your heart
to itself, to the stranger who has loved you

all your life, whom you ignored
for another, who knows you by heart.
Take down the love letters from the bookshelf,

the photographs, the desperate notes,
peel your own image from the mirror.
Sit. Feast on your life."""

end_letters=re.findall(r'\s[A-Za-z]+([a-z])\.', poem)

for l in end_letters:
    print (l)
##= RESTART: /Users/QianYu/Desktop/info206_exercises_Yu/meeting10/poem2_Yu.py =
e
t
f
e
d
t
r
t
e
## Results for my poem
#= RESTART: /Users/QianYu/Desktop/info206_exercises_Yu/meeting10/poem2_Yu.py =
#s
