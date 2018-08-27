#!/usr/bin/env python3
#-*-coding:utf-8 -*-

import os,sys,datetime

#py脚本模板
py='''#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
'''

#c模板
c='''*---------------------------------------
*TO:
*---------------------------------------
*BY:
*---------------------------------------
'''


if os.path.isfile(sys.argv[1]):
    print('%s already exists!' % sys.argv[1])
    sys.exit()
# file=open(sys.argv[1],'w')
today=datetime.date.today()    
date=today.strftime('%Y')+'-'+today.strftime('%m')+'-'+today.strftime('%d')
# filetypes=str.split(sys.argv[1],'.')
# length=len(filetypes)
# filetype=filetypes[-1]
filetype=os.path.splitext(sys.argv[1])[-1]
# print(filetype)
with open(sys.argv[1],'w') as file:
    if filetype=='.py':
        print('use python mode')
        file.writelines('#!/usr/bin/env python3')
        file.write('\n')
        file.writelines('# -*- coding:utf-8 -*-')
        file.write('\n')
        file.writelines('# File:'+sys.argv[1])
        file.write('\n')
        file.write(py)
        file.write('# Date:'+date)
        file.write('\n')
        file.write('#---------------------------------------')
    elif filetype=='.c' or filetype=='.cpp':
        print('use c mode')
        file.writelines('/*')
        file.write('\n')
        file.writelines('*---------------------------------------')
        file.write('\n')
        file.writelines('* File:'+sys.argv[1])
        file.write('\n')
        file.write(c)
        file.write('* Date:'+date)
        file.write('\n')
        file.write('*---------------------------------------')
        file.write('\n')
        file.write('*/ \n')
    else:
        print('just create %s' % sys.argv[1])
# file.close() 