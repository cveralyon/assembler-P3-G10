
def partida_lista (inst):
    aux=inst.strip().split(' ')
    for j in range(len(aux)):
        if aux[j]!='':
            i=j
            break
    return i

#archivo=open('problema1.ass','r')
#archivo=open('problema2.ass','r')
#archivo=open('p3-ej_correcto.ass','r')
#archivo=open('p3-ej_incorrecto.ass','r')
#archivo=open('p3F_1Corr.ass','r')
#archivo=open('p3F_1v2Corr.ass','r')
#archivo=open('p3F_2inCorr.ass','r')
#archivo=open('p3_1-correccion1.ass','r')
archivo=open('p3_1-correccion2.ass','r')

auxA=0
a=''
b=''
op=''
codebool=False
databool=False
paso1 = False
paso2 = False
data={}
instruccion=[]
modulos=[]
for f in archivo:
    f = f.strip()
    f = f.strip('\n')
    #print(f)
    try:
        if('DATA' in f) and paso1!=True:
            databool=True
            paso1=True
        if('CODE' in f) and paso2!=True:
            codebool=True
            paso1=True
        if f.find('CODE')!=-1:
            auxA=1
            
        if ((auxA==0 and f.find('DATA')==-1) and (codebool==True or databool==True)):
            
            j=partida_lista(f)
            variable=f.strip().split(' ')
            if len(f)>1:
                data[variable[j]]=(variable[j+1].strip('\n'))
                if(data[variable[j]][0]=='#' and data[variable[j]][1]=='#'):
                    f = f.strip('\n')
                    print(f'La instrucción {f} no existe')
                    
        else:
            if(f!=''):
                if (codebool==False and databool==False): 
                    instruccion.append(f.strip().strip('\n'))
                
                elif f.find(':')==-1 and f!='':                
                    instruccion.append(f.strip().strip('\n'))
                
                elif f.find(':')!=-1 and f.find('CODE')==-1 and f.find('DATA')==-1:
                    aux23 = f.split(':') 
                    if(aux23[1]==''):
                        aux23.remove(aux23[1])
                    if(len(aux23)>1):
                        modulos.append((aux23[0]+':')[:-1])
                        instruccion.append(aux23[1].strip().strip('\n'))
                    else:
                        modulos.append((f.strip().strip('\n'))[:-1])
    except:
        f = f.strip('\n')
        if(f!=''):
            print(f'La instrucción {f} no existe')
           
archivo.close()


validacion=0
ex_call=False
if(codebool==True and databool==True):   
       
    for inst in instruccion:
        inst = inst.strip()
        inst = inst.strip('\n')
        exp=False
        try:
            if (',' in inst)==True:
                aux=inst.split(' ')
                for j in range(len(aux)):
                    if aux[j]!='':
                        i=j
                        break
            
                op=(inst.split(' '))[j]
                a=(((inst.split(' '))[j+1]).split(','))[0]
                b=(((inst.split(' '))[j+1]).split(','))[1]
            elif inst=='RET':
                op=inst
                a='NULL'
                b='NULL'
            else:
                if inst!='':
                    aux=inst.split(' ')
                    for j in range(len(aux)):
                        if aux[j]!='':
                            i=j
                            break
                    op=(inst.split(' '))[j]
                    a=(inst.split(' '))[j+1]
                    b='NULL'
        except:
            exp=True
            if(inst!=''):
                print(f'La instrucción {inst} no existe')
            
        a_par=0
        b_par=0
        if ('(' in a):
            a_par=1
            a=a[1:]
            a=a[:-1]
        if ('(' in b):
            b_par=1
            b=b[1:]
            b=b[:-1]
        val=False #validacion
        
        if (op=='MOV'):
            if a_par+b_par==0: #No Hay Parentésis
                if a=='A' and b=='B':
                    val =True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0: #Parentesis en a
                if (a in data) == True and b=='A':
                    val=True
                elif (a in data) == True and b=='B':
                    val = True
                elif a=='B' and b=='A':
                    val=True
            elif a_par==0 and b_par==1: #Parentesis en b
                if a=='A' and (b in data)==True:
                    val=True
                elif a=='B' and (b in data)==True:
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='B':
                    val=True
        elif op=='ADD':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A' and (b in data)==True:
                    val=True
                elif a=='B' and (b in data)==True:
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='SUB':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A' and (b in data)==True:
                    val=True
                elif a=='B' and (b in data)==True:
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='AND':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A' and (b in data)==True:
                    val=True
                elif a=='B' and (b in data)==True:
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='OR':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A' and (b in data)==True:
                    val=True
                elif a=='B' and (b in data)==True:
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='NOT':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='B' and b=='B':
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='A':
                    val=True
                elif (a in data)==True and b=='B':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='XOR':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A' and (b in data)==True:
                    val=True
                elif a=='B' and (b in data)==True:
                    val=True
                elif a=='A' and b=='B':
                    val=True    
        elif op=='SHL':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='B' and b=='B':
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='A':
                    val=True
                elif (a in data)==True and b=='B':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='SHR':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='B' and b=='B':
                    val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='A':
                    val=True
                elif (a in data)==True and b=='B':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='INC':
            if a_par==0 and b_par==0:
                val=True
            elif a_par==1 and b_par==0:
                if (a in data)==True and b=='NULL':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='RST':
            if a_par==1 and b_par==0:
                if (a in data)==True and b=='NULL':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='CMP':
            
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            if a_par==0 and b_par==1:

                if a=='A' and (b in data)==True:
                    val=True
                elif a=='B' and (b in data)==True:
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='JMP' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JEQ' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JNE' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JGT' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JLT' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JGE' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JLE' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JCR' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='JOV' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
        elif op=='CALL' and a_par+b_par==0 and (a in modulos)==True and b=='NULL':
            val=True
            ex_call=True
        elif op=='RET' and a_par+b_par==0 and a=='NULL' and b=='NULL' and ex_call==True:
            val=True
        elif op=='PUSH' and a_par+b_par==0 and (a=='A' or a=='B') and b=='NULL':
            val=True
        elif op=='POP' and a_par+b_par==0 and (a=='A' or a=='B') and b=='NULL':
            val=True
            
        if (val==False and exp==False) and (inst!=''):
            print(f'La instrucción {inst} no existe')
            validacion=1

elif(codebool==False and databool==False): 
          
    for inst in instruccion:
        exp=False

        try:
            if (',' in inst)==True:
                aux=inst.split(' ')
                for j in range(len(aux)):
                    if aux[j]!='':
                        i=j
                        break
            
                op=(inst.split(' '))[j]
                a=(((inst.split(' '))[j+1]).split(','))[0]
                b=(((inst.split(' '))[j+1]).split(','))[1]
            elif inst=='RET':
                op=inst
                a='NULL'
                b='NULL'
            else:
                if inst!='':
                    aux=inst.split(' ')
                    for j in range(len(aux)):
                        if aux[j]!='':
                            i=j
                            break
                    op=(inst.split(' '))[j]
                    a=(inst.split(' '))[j+1]
                    b='NULL'
        except:
            exp=True
            if (inst!=''):
                print(f'La instrucción {inst} no existe')
            
        a_par=0
        b_par=0
        if '(' in a:
            a_par=1
            a=a[1:]
            a=a[:-1]
        if '(' in b:
            b_par=1
            b=b[1:]
            b=b[:-1]
        val=False #validacion
        
        if op=='MOV':
            if a_par+b_par==0: #No Hay Parentésis
                if a=='A' and b=='B':
                    val =True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0: #Parentesis en a
                if  b=='A':
                    val=True
                elif  b=='B':
                    val = True
                elif a=='B' and b=='A':
                    val=True
            elif a_par==0 and b_par==1: #Parentesis en b
                if a=='A' :
                    val=True
                elif a=='B' :
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='B':
                    val=True
        elif op=='ADD':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if  b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A' :
                    val=True
                elif a=='B' :
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='SUB':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if  b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A' :
                    val=True
                elif a=='B' :
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='AND':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if  b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A':
                    val=True
                elif a=='B' :
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='OR':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            elif a_par==1 and b_par==0:
                if  b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A':
                    val=True
                elif a=='B' :
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif op=='NOT':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='B' and b=='B':
                    val=True
            elif a_par==1 and b_par==0:
                if  b=='A':
                    val=True
                elif b=='B':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='XOR':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='A' and (b.isdigit()):
                    val=True
                elif a=='B' and (b.isdigit()):
                    val=True
            elif a_par==1 and b_par==0:
                if b=='NULL':
                    val=True
            elif a_par==0 and b_par==1:
                if a=='A':
                    val=True
                elif a=='B' :
                    val=True
                elif a=='A' and b=='B':
                    val=True    
        elif op=='SHL':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='B' and b=='B':
                    val=True
            elif a_par==1 and b_par==0:
                if  b=='A':
                    val=True
                elif  b=='B':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='SHR':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                elif a=='A' and b=='B':
                    val=True
                elif a=='B' and b=='A':
                    val=True
                elif a=='B' and b=='B':
                    val=True
            elif a_par==1 and b_par==0:
                if  b=='A':
                    val=True
                elif b=='B':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='INC':
            if a_par==0 and b_par==0:
                val=True
            elif a_par==1 and b_par==0:
                if  b=='NULL':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='RST':
            if a_par==1 and b_par==0:
                if  b=='NULL':
                    val=True
                elif a=='B' and b=='NULL':
                    val=True
        elif op=='CMP':
            
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                elif a=='A' and (b=='1' or b=='0'):
                    val=True
                elif a=='B' and (b=='1' or b=='0'):
                    val=True
            if a_par==0 and b_par==1:

                if a=='A':
                    val=True
                elif a=='B' :
                    val=True
                elif a=='A' and b=='B':
                    val=True
        elif (op=='JMP' and (a_par+b_par==0) and ((((a in modulos)==True) and (b=='NULL')) or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JEQ' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JNE' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JGT' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JLT' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JGE' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JLE' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JCR' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='JOV' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))):
            val=True
        elif op=='CALL' and a_par+b_par==0 and ((a in modulos)==True and b=='NULL'):
            val=True
            ex_call=True
        elif op=='RET' and a_par+b_par==0 and a=='NULL' and b=='NULL' and ex_call==True:
            val=True
        elif op=='PUSH' and a_par+b_par==0 and (a=='A' or a=='B') and b=='NULL':
            val=True
        elif op=='POP' and a_par+b_par==0 and (a=='A' or a=='B') and b=='NULL':
            val=True
            

        if (val==False and exp==False) and (inst!=''):
            print(f'La instrucción {inst} no existe')
            validacion=1

   
      

if validacion==0:
    print('Son todas las instrucciones correctas')