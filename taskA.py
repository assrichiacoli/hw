import os
import sys


sys.path.append(os.path.join(sys.path[0], '../../task9'))

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
                else:
                    print('{name}\tDIR'.format(name=item.getname()))
            print()
        elif cmd == 'cd':
            if cmdargs[0] == None:
                os.getenv("HOME")
            elif cmdargs[0] == '..':
                os.chdir(os.path.split(cwd)[0])
            else:    
                os.chdir(cmdargs[0])
        elif cmd == 'cat':
            print(File.getcontent(cmdargs))
            
        elif cmd == 'head':
            if cmdargs[0] == '-n':
                print(File.getcontent(cmdargs[2])[:int(cmdargs[1])]) 
            else:
                print(File.getcontent(cmdargs[1])[:10]) 
                
        elif cmd == 'tail':
            if cmdargs[0] == '-n':
                print(File.getcontent(cmdargs[2])[-(int(cmdargs[1])):]) 
            else:
                print(File.getcontent(cmdargs[2])[-10:])
                
        elif cmd == 'pwd':
            print(os.getcwd())
            
        elif cmd == 'touch':
            file = cmdargs[0]
            open(file,'w+').close
            
        elif cmd == 'find':
            for file in cwd.filesrecursive:
                if file == cmdargs[0]:
                    print(file.path)
        
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
