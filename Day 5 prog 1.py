def LastWordLength(s): 
	words = s.split(' ') 
	return len(words[-1]) 
s = "Hello World"
print(LastWordLength(s)) 
s = "fly me to the moon"
print(LastWordLength(s)) 
s = "luffy is still joyboy"
print(LastWordLength(s)) 
s = "123"
print(LastWordLength(s)) 
s = " 45&29 8*6^4"
print(LastWordLength(s))
