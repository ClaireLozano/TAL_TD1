import os
import sys
import matplotlib.pyplot as plt

def getDataFromTextFile(txtFile):
	data = []
	with open(txtFile) as inp:
		for line in inp:
			data.append(line)
	return data


def splitByWord(data):
	wordsList = []
	for line in data:
		words = line.split()
		for word in words:
			wordsList.append(word.decode('utf-8'))
	return wordsList


def countWord(words):
	dictionnary = {}
	for w in words:
		if len(dictionnary):
			if w in dictionnary.keys():
				dictionnary[len(w)] = dictionnary.get(len(w)) + 1
			else:
				dictionnary[len(w)] = 1
		else : 
			dictionnary[len(w)] = 1
	return dictionnary


def countWord2(words):
	dictionnary = {}
	for w in words:
		dictionnary.setdefault(w, 0)
		dictionnary[w]+=1

	Y = sorted([y for x,y in dictionnary.items()], reverse=True)
	X = range(1, len(Y)+1)

	return X,Y


def countCaracteres(words):
	dictionnary = {}
	for w in words:
		for c in w:
			dictionnary.setdefault(c.upper(), 0)
			if ascii_letters(c.upper()):
				dictionnary[c.upper()]+=1
			else:
				dictionnary.pop(c, None)

	l = sorted([[y, x] for x,y in dictionnary.items()], reverse=True)
	return l


def countCaracteres2(words):
	dictionnary = {}
	for w in words:
		for index, c in w:
			dictionnary.setdefault(c.upper(), 0)
			if ascii_letters(c.upper()):
				dictionnary[c.upper()]+=1
			else:
				dictionnary.pop(c, None)

	l = sorted([[y, x] for x,y in dictionnary.items()], reverse=True)
	return l


def ascii_letters(letter):
	tab = ["A","Z","E","R","T","Y","U","I","O","P","M","L","K","J","H","G","F","D","S","Q","W","X","C","V","B","N"]
	if letter in tab:
		return True
	else:
		return False



words = splitByWord(getDataFromTextFile("text1.txt"))

newListWords = countWord(words)
x, y = countWord2(words)
l = countCaracteres(words)

# Afficher sur un graphique 
#      x = le nombre de lettre dans un mot
#      y = nombre d'apparition
plt.plot(x, y, 'r')
plt.yscale('log')
plt.show()

# Extraire les lettres les plus utilisees de la langue francaise
for i in l:
	print i[1], "=", i[0]


