import subprocess

try:
	f1=open('mdp-family.txt', 'r')
except:
	print('No file found with the name mdp-family.txt')
	exit(1)

keys=[0.11, 0.22, 0.03, 0.44, 0.55, 0.66, 0.77, 0.88, 0.99]
destFiles={}
for key in keys:
	destFiles[key]=open('mdp-family-'+str(key)+'.txt', 'w')

contents=f1.read()
numLines=contents.strip().count('\n')+1

for i, line in enumerate(contents.strip().split('\n')):

	for key in destFiles:
		if(i!=numLines-2):
			destFiles[key].write(line+'\n')
		else:
			destFiles[key].write(str(key)+'\n')

f1.close()
for key in destFiles:
	destFiles[key].close()


prevOutput=None

for i, key in enumerate(keys):
	cmd=['./planner.sh', '--mdp', 'mdp-family-'+str(key)+'.txt', '--algorithm', 'lp']
	temp=subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
	currentOutput=[]
	for line in temp.split('\n'):

		if len(line.strip())<2: continue
		currentOutput.append(int(line.split()[1]))

	if i!=0 and ( i%3==0 and currentOutput==prevOutput or i%3!=0 and currentOutput!=prevOutput ) :
		print('Wrong')
	prevOutput=currentOutput
