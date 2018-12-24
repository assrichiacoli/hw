import os
import sys


sys.path.append(os.path.join(sys.path[0], '../../task9'))

from task9 import *

def main(args):
    cwd = Directory(os.getcwd())
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd.path)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        if cmd == 'ls':
            print()
            path = cwd.path if not cmdargs else cmdargs[0]
            directory = cwd.getsubdirectory(path)
            for item in directory.items():
                if item.isfile():
                    print('{name}\tFILE\t{size}'.format(name=item.getname(), size=len(item)))
                elif item.isdirectory():
                    print('{name}\tDIR'.format(name=item.getname()))
            print()
        elif cmd == 'cd':
            print()
            if cmdargs[0] == '.':
                cwd = Directory(os.environ['HOME'])
            elif cmdargs[0] in os.listdir(cwd.path):
                cwd = Directory(os.path.join(cwd.path,cmdargs[0]))
            elif cmdargs[0] == '..':
                cwd = Directory(os.path.split(cwd.path)[0])
            else:
                if os.path.exists(cmdargs[0]):
                    cwd = Directory(cmdargs[0])
                else:
                    print('(_!_)')
            print()
        elif cmd == 'cat':
            print()
            for line in File(cmdargs[0]).getcontent():
                print(line)
            print()
        elif cmd == 'head':
            print()
            a = cmdargs
            if a[0] == '-n':
                for line in File(a[2]).getcontent()[:int(a[1])]:
                    print(line) 
            else:
                for line in File(a[0]).getcontent()[:10]:
                    print(line) 
            print()    
        elif cmd == 'tail':
            print()
            a = cmdargs
            if a[0] == '-n':
                for line in File(a[2]).getcontent()[-int(a[1]):]:
                    print(line) 
            else:
                for line in File(a[0]).getcontent()[-10:]:
                    print(line) 
            print()  
        elif cmd == 'pwd':
            print()
            print(cwd.path)
            print()
        elif cmd == 'touch':
            print()
            file = cmdargs[0]
            if os.path.exists(file):
                print('"'"{0}"'" already exists'.format(file))
            else:
                open(file,'w+').close
                print('"'"{0}"'" file is created!'.format(file))
            print()
        elif cmd == 'find':
            print()
            for root, directories, files in os.walk(cwd.path):
                if str(cmdargs[0]) in str(root):
                    print(root)
            for x in cwd.filesrecursive():
                if str(cmdargs[0]) in str(x.path):
                    print(x.path)
            print()
        elif cmd == 'grep':
            print()
            for line in File(cmdargs[1]).getcontent():
                if str(cmdargs[0]) in str(line):
                    print(line)
            print()
        elif cmd == 'cp':
            print()
            f = open(cmdargs[1], 'w+')
            for line in File(cmdargs[0]).getcontent():
                print(line, file = f)
            f.close()
            print()
        elif cmd == 'mv':
            print()
            f = open(cmdargs[1], 'w+')
            for line in File(cmdargs[0]).getcontent():
                print(line, file = f)
            f.close()
            os.remove(cmdargs[0])
            print()
        elif cmd == 'rm':
            print()
            os.remove(cmdargs[0])
            print()
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
