from __future__ import division

def lecture(fic): 
    f = open(fic, 'r')
    l = f.readlines()
    f.close()
    lu = ""
    for line in l[1:]: 
        lu += line[:-1]
    return lu



def CreaTab(text1, text2, gap, M, MM):
	matrice = [0,0]*size(text1)
	for i in xrange(size(text1)):
		matrice[i]=[0,0]*size(text2)
	print M 


CreaTab("coucouc", "oui");