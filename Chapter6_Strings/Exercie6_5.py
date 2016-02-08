str = 'X-DSPAM-Confidence:  0.8475'

a = str.find(':')


b = str[a+1:len(str)-1]
print b

c = b.strip()
print c

d = float(c)
print d