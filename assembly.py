
def partida_lista (inst):
    aux=inst.split(' ')
    for j in range(len(aux)):
        if aux[j]!='':
            i=j
            break
    return i

#archivo=open('p3F_1.ass','r')
#archivo=open('problema1.ass','r')
archivo=open('problema2.ass','r')
a=0
data={}
instruccion=[]
modulos=[]
for f in archivo:
    print(f)
    if f.find('CODE')!=-1:
        a=1
    if a==0 and f.find('DATA')==-1:
        j=partida_lista(f)
        variable=f.split(' ')
        if len(f)>1:
            data[variable[j]]=(variable[j+1].strip('\n'))
        
    else:
        if f.find(':')==-1 and f!='':
            instruccion.append(f.strip('\n'))
           
        elif f.find(':')!=-1 and f.find('CODE')==-1 and f.find('DATA')==-1: 
            modulos.append((f.strip('\n'))[:-1])
           
archivo.close()
validacion=0
ex_call=False
for inst in instruccion:
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
        

    if val==False:
        print(f'La instrucción {inst} no existe')
        validacion=1
if validacion==0:
    print('Son todas las instrucciones correctas')