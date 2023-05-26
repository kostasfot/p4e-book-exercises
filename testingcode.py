str = 'DSPAM-Confidence:0.8475'

colpos = str.find(':')
conf = float(str[colpos + 1:])
conf