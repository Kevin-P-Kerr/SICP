
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    longest_pals = []
    if len(text)>0:
    	for i in range(len(text)-1):
        	longest_pals.append(pal_check(i, text))
    	print max(longest_pals, key=returner)[1]   
    	return max(longest_pals, key=returner)[1]
    else: 
		print (0, 0)
		return ((0, 0))

def pal_check(i, text):
    n = 0
    if i==0:
		return (0, (0, 0))
    while (i-n)>=0 and (i+n)<=(len(text)-1):
        if text[i-n].lower()==text[i+n].lower():
            n += 1
        else: break
	
    return ((i+n+1)-(i-n), (i-n+1, i+n))
    
def returner(longest_pals):
       return longest_pals[0]
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Racecarr') == (0, 7)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
