import os
import subprocess
from scipy import stats
import numpy as np

def reject_outliers_2(data, m = 2):
	d = np.abs(data - np.median(data))
	#print('ANTES:')
	#print(data)
	mdev = np.median(d)
	s = d/(mdev if mdev else 1.)
	#print('DEPOIS:')
	#print(data[s<m])
	return data[s<m]

def run_all(inp):
	input_dir = "{}/{}".format(os.getcwd(), inp)
	aes_outs = os.listdir(input_dir)
	for binaryout in aes_outs:
		array = np.zeros((60,21))
		if ('data.' in binaryout):
			pver = np.zeros(21)
			ppp=0
			k=0
			np.set_printoptions(precision=2,suppress=True)
			print('\n\n\n')
			print(".{}/{} > {}".format(input_dir, binaryout, "output_file"))
			fullpath=inp+binaryout
			text_file = open(fullpath, "r")
			lines = text_file.read()
			lines = lines.replace('\n','')
			lines = lines.replace(' ','')
			lines = lines.split(',')
			lines = filter(None, lines)
			array=np.asarray(lines,dtype=np.float32)
			num=len(array)/21
			#print(array)
			array = array.reshape(num,21,-1)
			array = np.transpose(array)
			p1=0
			p2=0
			#print('ANTES:')
			#print(array[0])
			#if 'non' in input_dir:
				#name='non'+binaryout
			#else:
				#name=binaryout
			#name2 = 'std'+name
			#f = open(name,'a')
			#f2 = open(name2,'a')
			print(".{}/{}".format(input_dir, binaryout))
			#print(array[0][1])
			p1=array[0][1][0]/array[0][1][1]
			p2=array[0][1][1]/array[0][1][2]
			print(p1,p2)
			#print('DEPOIS:')
			#print(array[0])
			#k2,p = stats.normaltest(array[0],1)
			#print('  STATS   ')
			#print('k2=',k2)
			#print('p-val=')
			#print(p)
			#for pval in p:
				#if pval<0.05:
					#pver=np.insert(pver,ppp,1)
					#print('\n\n\nNAO SERVE  {}   \n\n\n'.format(pval))
					#k=k+1
				#ppp=ppp+1
	#print(lines)
			#print(pver[:21])
			#print('NUMERO DE NAO DISTRIBUICOES:',k)


if __name__ == "__main__":
	np.set_printoptions(linewidth=210,precision=4)
	run_all('CDN data/')
	run_all('non CDN data/')


