import urllib2
from bs4 import BeautifulSoup

#module to remove html tags and nbsp
def removetags(data):
  check = False
	file = open('tester.txt', 'a')
	for i in data:
		if i == '<':
			check = True
		elif i == '>':
			check = False
		elif check == True:
			pass
		elif ord(i) == 7: #gets rid of '\a'
			pass
		elif ord(i) == 8: #gets rid of '\b'
			pass
		elif ord(i) == 9: #gets rid of '\t'
			pass
		elif ord(i) == 10: #gets rid of '\n'
			pass
		elif ord(i) == 11: #gets rid of '\v'
			pass
		elif ord(i) == 12: #gets rid of '\f'
			pass
		elif ord(i) == 13: #gets rid of '\r'
			pass
		elif i == ';':
			pass
		elif i == '.':
			pass
		elif i == ',':
			pass
		elif i == ':':
			pass
		else:
			file.write(i)
	file.close()
	
#module to remove html tags and nbsp
def containedTags(data):
	check = False
	duplicatesnewtag = []
	temp = []
	newtag = []
	secondcheck = False
	for i in data:
		if i == '>':
			check = True
			temp.append(i)
		elif i == '<':
			check = False
			temp.append(i)
			tag = ''.join(temp)
			del temp[:]
			duplicatesnewtag.append(tag)
		elif check == True:
			temp.append(i)
		else:
			pass
			
	for j in duplicatesnewtag:
		if j in newtag:
			pass
		else:
			newtag.append(j)
	return duplicatesnewtag
			
#module to read text from a file		
def importsoup():
	openfile = open('tester.txt')
	read = file.read(openfile)
	openfile.close()
	return read
	
#module to write final text to dictionary
def exportsoup(finalsoup):
	openfile = open('dictionary.txt', 'a')
	for i in finalsoup:
		openfile.write(i)
		openfile.write('\n')
	openfile.close()

inputsite = raw_input('Enter a url to start on > ')
	
#create the BeautifulSoup tree
soup = BeautifulSoup(urllib2.urlopen(
	inputsite).read())	
	

prettysouptemp = soup.prettify()
prettysoup = prettysouptemp.encode('ascii', 'ignore')






#get rid of the html tags and nbsp
prettysoup = removetags(prettysoup)


#import the tagless words into an array
newsoup = importsoup()
stringynewsoup = str(newsoup)
splitsoup = stringynewsoup.split(' ')

cleansplitsoup = []
for i in splitsoup:
	if i == '':
		pass
	else:
		cleansplitsoup.append(i)

finalsoup = []
for i in cleansplitsoup:
	if i in finalsoup:
		pass
	else:
		finalsoup.append(i)

exportsoup(finalsoup)

f = open('leetDictionary','a')
f.write[for pos in finalSoup[] for letter in range(len(finalSoup[pos])) if charAt(letter) = 'a' for possibility in aArray[]])

	
#to get all of the a tags
#a_soup_temp = []
#for link in soup.find_all('a'):
#	a_soup_temp.append((link.get('href')))
#print a_soup_temp
#
#a_soup = []
#for link in a_soup_temp:
#	if link in a_soup:
#		pass
#	else:
#		a_soup.append(link)
#print a_soup
	
