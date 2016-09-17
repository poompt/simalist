#By Avogadro
import subprocess, os
realm=input('Realm name: ')
names=input('Character names (name1,name2,...): ')
names=[x.strip() for x in names.split(',')]
f=open(os.path.dirname(os.path.realpath(__file__))+'\output.csv','w')
for name in names:
    print('Processing...')
    output=str(subprocess.check_output(['simc.exe','armory=us,'+realm+','+name]))
    dps=output[output.find('DPS: ')+5:output.find(' DPS-Error')]
    print(name,dps)
    f.write(name+','+dps+'\n')
f.close()
input('sims done (enter to quit)')