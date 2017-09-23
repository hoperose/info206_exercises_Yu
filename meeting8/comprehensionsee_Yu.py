#list the square numbers below 100 that give a remainder of 1 when divided by 3
num_list = [p**2 for p in range(100) if p%3 == 1]


#list the first letters of each word in the given snippet
text = 'A new, a vast, and a powerful language is developed for the future use of analysis, in which to wield its truths so that these may become of more speedy and accurate practical application for the purpose of mankind than the means hitherto in our possession have rendered possible.'

fletters_list = [w.strip()[0] for w in text.split()]


#list all Pythagorean triples with numbers below 25
triplet_list = [(x,y,z) for x in range(1,23) for y in range(x+1,25) for z in range(y+1,26) if x**2+y**2==z**2]


#list all strings that can be formed by deleting exactly one character from a word
word = "welcomed"

nword_list = [word[:i] + word[i+1:] for i in range(len(word))]


#list all strings that can be formed by replacing exactly one vowel in the word with a different vowel.

word = "Booted"
    
nword_list = [word.replace(l, nl) for l in word if l in set('aeiou') for nl in set('aeiou').difference(set(l))]         
              

    

                


                


       
