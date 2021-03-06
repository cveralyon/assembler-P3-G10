
def partida_lista (inst):
    aux=inst.strip().split(' ')
    for j in range(len(aux)):
        if aux[j]!='':
            i=j
            break
    return i
def agregar_ceros(numero,op):
    for x in range(numero):
        op+='0'
    return op
          

name = "Pruebas/p3F_2inCorr"
archivo=open(name+'.ass','r')


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
fila=0
cero='00000000'
validacion=0
ex_call=False
output_arch=open(name+'.out','w')
def assembler_func():
    global validacion
    for inst in instruccion:
        l = inst.split('&')
        inst=l[0]
        fila=l[1]
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
            if (inst!=''):
                print(f'En la fila {fila} la instrucción {inst} no existe')
                validacion=1
            
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
        dec=0
        if (op=='MOV'):
            if a_par+b_par==0: #No Hay Parentésis
                if a=='A' and b=='B':
                    val =True
                    opcode='000000000000000'
                elif a=='B' and b=='A':
                    val=True
                    opcode='000000100000000'
                elif a=='A' and (b.isdigit() or b in data):
                    val=True
                    opcode='0000010'
                    if(not b.isdigit()):
                        b=data[b]
                        if(b[0]=='#'):
                            b=b[1:]
                            b=int(b, 16)
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                elif a=='B' and (b.isdigit() or b in data):
                    val=True
                    opcode='0000011'
                    if(not b.isdigit()):
                        b=data[b]
                        if(b[0]=='#'):
                            b=b[1:]
                            b=int(b, 16)
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
            elif a_par==1 and b_par==0: #Parentesis en a
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit()))) and b=='A':
                    val=True
                    opcode='010011100000000'
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0100111'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario          
                elif ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit()))) and b=='B':
                    val = True
                    opcode='010100000000000'
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0101000'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and b=='A':
                    val=True
                    opcode='010101100000000'                
            elif a_par==0 and b_par==1: #Parentesis en b
                if a=='A' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='010010100000000'
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0100101'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='010011000000000'
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0100110'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='A' and b=='B':
                    val=True
                    opcode='010100100000000'
                elif a=='B' and b=='B':
                    val=True
                    opcode='010101000000000'
        elif op=='ADD':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                    opcode='0000100'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0000101'+cero
                elif a=='A' and (b.isdigit()):
                    val=True
                    opcode='0000110'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                elif a=='B' and (b.isdigit()):
                    val=True
                    opcode='0000011'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit()))) and b=='NULL':
                    val=True
                    opcode='0101111'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0101111'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
            elif a_par==0 and b_par==1:
                if a=='A' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0101100'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0101100'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0101101'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0101101'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='A' and b=='B':
                    val=True
                    opcode='0101110'+cero
        elif op=='SUB':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                    opcode='0001000'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0001001'+cero
                elif a=='A' and (b.isdigit()):
                    val=True
                    opcode='0001010'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                elif a=='B' and (b.isdigit()):
                    val=True
                    opcode='0001011'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='NULL':
                    val=True
                    opcode='0110011'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0110011'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
            elif a_par==0 and b_par==1:
                if a=='A' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0110000'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0110000'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0110001'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0110001'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='A' and b=='B':
                    val=True
                    opcode='0110010'+cero

        elif op=='AND':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                    opcode='0001100'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0001101'+cero
                elif a=='A' and (b.isdigit()):
                    val=True
                    opcode='0001110'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                elif a=='B' and (b.isdigit()):
                    val=True
                    opcode='0001111'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit()))) and b=='NULL':
                    val=True
                    opcode='0110111'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0110111'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   

            elif a_par==0 and b_par==1:
                if a=='A' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0110100'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0110100'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0110101'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0110101'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='A' and b=='B':
                    val=True
                    opcode='0110110'+cero
        elif op=='OR':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                    opcode='0010000'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0010001'+cero
                elif a=='A' and (b.isdigit()):
                    val=True
                    opcode='0010010'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                elif a=='B' and (b.isdigit()):
                    val=True
                    opcode='0010011'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='NULL':
                    val=True
                    opcode='0111011'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0111011'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
            elif a_par==0 and b_par==1:
                if a=='A' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0111000'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                            
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0111000'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0111001'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0111001'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='A' and b=='B':
                    val=True
                    opcode='0111010'+cero
                
        elif op=='NOT':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                    opcode='0010100'+cero
                elif a=='A' and b=='B':
                    val=True
                    opcode='0010101'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0010110'+cero
                elif a=='B' and b=='B':
                    val=True
                    opcode='0010111'+cero
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='A':
                    val=True
                    opcode='0111100'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0111100'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='B':
                    val=True
                    opcode='0010101'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='0010101'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif a=='B' and b=='NULL':
                    val=True
                    opcode='0010110'+cero

        elif op=='XOR':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                    opcode='0011000'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0011001'+cero
                elif a=='A' and (b.lstrip('-').isdigit()):
                    val=True
                    opcode='0011010'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                    opcode=opcode.replace('b','1')
                elif a=='B' and (b.lstrip('-').isdigit()):
                    val=True
                    opcode='0011011'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                    opcode=opcode.replace('b','1')
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='NULL':
                    val=True
                    opcode='1000010'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='1000010'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
            elif a_par==0 and b_par==1:
                if a=='A' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='0111111'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='0111111'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='1000000'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='1000000'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='A' and b=='B':
                    val=True 
                    opcode='1000001'+cero 
                         
        elif op=='SHL':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                    opcode='0011100'+cero
                elif a=='A' and b=='B':
                    val=True
                    opcode='0011101'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0011110'+cero
                elif a=='B' and b=='B':
                    val=True
                    opcode='0011111'+cero
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='A':
                    val=True
                    opcode='1000011'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='1000011'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='B':
                    val=True
                    opcode='1000100'+cero
                if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='1000100'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif a=='B' and b=='NULL':
                    val=True
                    opcode='1000101'+cero
               
        elif op=='SHR':
            if a_par+b_par==0:
                if a=='A' and b=='A':
                    val=True
                    opcode='0100000'+cero
                elif a=='A' and b=='B':
                    val=True
                    opcode='0100001'+cero
                elif a=='B' and b=='A':
                    val=True
                    opcode='0100010'+cero
                elif a=='B' and b=='B':
                    val=True
                    opcode='0100011'+cero
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='A':
                    val=True
                    opcode='1000110'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='1000110'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='B':
                    val=True
                    opcode='1000111'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='1000111'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif a=='B' and b=='NULL':
                    val=True
                    opcode='1001000'+cero
    
        elif op=='INC':
            if a_par==0 and b_par==0:
                val=True
                opcode='0100100'+cero
            elif a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit()))) and b=='NULL':
                    val=True
                    opcode='1001001'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='1001001'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif a=='B' and b=='NULL':
                    val=True
                    opcode='1001010'+cero
        elif op=='RST':
            if a_par==1 and b_par==0:
                if ((a in data) == True or (((a[0] == '#') and a[1]!='#') or (a.isdigit())))  and b=='NULL':
                    val=True
                    opcode='1001011'+cero
                    if (a in modulos)==False:
                        if a.isdigit()==False:
                            if a[0]=='#':
                                a=a.split('#')[1]
                                dec = int(a, 16)
                        else:
                            dec=int(a)
                        if dec >255:
                            val=False
                        else:
                            opcode='1001011'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario   
                elif a=='B' and b=='NULL':
                    val=True
                    opcode='1001100'+cero
               
        elif op=='CMP':
            if a_par+b_par==0:
                if a=='A' and b=='B':
                    val=True
                    opcode='1001101'+cero
                elif a=='A' and (b.isdigit()):
                    val=True
                    opcode='1001110'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
                elif a=='B' and (b.isdigit()):
                    val=True
                    opcode='1001111'
                    binario=str(bin(int(b))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
            if a_par==0 and b_par==1:
                if a=='A' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='1010000'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='1010000'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='B' and ((b in data)==True or (((b[0] == '#') and b[1]!='#') or (b.isdigit()))):
                    val=True
                    opcode='1010001'+cero
                    if (b in modulos)==False:
                        if b.isdigit()==False:
                            if b[0]=='#':
                                b=b.split('#')[1]
                                dec = int(b, 16)
                        else:
                            dec=int(b)
                        if dec >255:
                            val=False
                        else:
                            opcode='1010001'
                            binario=str(bin(int(dec))[2:])
                            opcode=agregar_ceros(8-len(binario),opcode)
                            opcode+=binario
                elif a=='A' and b=='B':
                    val=True
                    opcode='1010010'+cero
            
        elif (op=='JMP' and (a_par+b_par==0) and ((((a in modulos)==True) and (b=='NULL')) or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit())))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        k=a.split('#')[1]
                        dec = int(k, 16)
                else:
                    dec=int(a)
                if dec > 255:
                    val=False
                else:
                    opcode='1010011'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JEQ' and a_par+b_par==0 and b=='NULL' and (((a in modulos)==True  or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                if dec >255:
                    val=False
                else:
                    opcode='1010100'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JNE' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                #print(dec)
                if dec >255:
                    val=False
                else:
                    opcode='1010101'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JGT' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                if dec >255:
                    val=False
                else:
                    opcode='1010110'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JLT' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                if dec >255:
                    val=False
                else:
                    opcode='1010111'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JGE' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                if dec >255:
                    val=False
                else:
                    opcode='1011000'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JLE' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                if dec >255:
                    val=False
                else:
                    opcode='1011001'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JCR' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            val=True
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                if dec >255:
                    val=False
                else:
                    opcode='1011010'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='JOV' and a_par+b_par==0 and ((((a in modulos)==True and b=='NULL') or (((a[0] == '#') and a[1]!='#' and int(a[1:], 16)<=255) or (a.isdigit() and int(a)>=0 and int(a)<=255)))):
            if (a in modulos)==False:
                if a.isdigit()==False:
                    if a[0]=='#':
                        a=a.split('#')[1]
                        dec = int(a, 16)
                else:
                    dec=int(a)
                if dec >255:
                    val=False
                else:
                    opcode='1011011'
                    binario=str(bin(int(dec))[2:])
                    opcode=agregar_ceros(8-len(binario),opcode)
                    opcode+=binario
        elif op=='CALL' and a_par+b_par==0 and ((a in modulos)==True and b=='NULL'):
            val=True
            ex_call=True
            opcode='1011100'+cero
        elif op=='RET' and a_par+b_par==0 and a=='NULL' and b=='NULL' and ex_call==True:
            val=True
            opcode='1011101'+cero
        elif op=='PUSH' and a_par+b_par==0 and (a=='A' or a=='B') and b=='NULL':
            val=True
            opcode='1011110'+cero
        elif op=='POP' and a_par+b_par==0 and (a=='A' or a=='B') and b=='NULL':
            val=True
            opcode='1011111'+cero
            
        if (val==False and exp==False) and (inst!=''):
            #print(val)
            print(f'En la fila {fila} la instrucción {inst} no existe')
            validacion=1
        elif(val==True and (inst!='')):
            output_arch.write(opcode+'\n')
  

for f in archivo:
    fila=fila+1
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
                if(data[variable[j]][0]=='#'):
                    hex=data[variable[j]][1:]
                    if data[variable[j]][1]=='#':
                        f = f.strip('\n')
                        print(f'En la fila {fila} la instrucción {f} no existe')
                    if ((int(hex, 16)>255) or (a.isdigit() and a<0 and a>255)):
                        print(f'En la fila {fila} la instrucción {f} no existe')

                        
                    
        else:
            if(f!='' and f.find('DATA')==-1):
                if (codebool==False and databool==False): 
                    instruccion.append(f.strip().strip('\n')+'&'+str(fila))
                if(len(data)!=0):
                    if(data[variable[j]][0]=='#'):
                        hex=data[variable[j]][1:]
                        if data[variable[j]][1]=='#':
                            f = f.strip('\n')
                            print(f'En la fila {fila} la instrucción {f} no existe')
                            validacion=1
                        if ((int(hex, 16)>255) or (a.isdigit() and a<0 and a>255)):
                            print(f'En la fila {fila} la instrucción {f} no existe')
                            validacion=1
                    elif f.find(':')==-1 and f!='':                
                        instruccion.append(f.strip().strip('\n')+'&'+str(fila))
                    
                    elif f.find(':')!=-1 and f.find('CODE')==-1 and f.find('DATA')==-1:
                        aux23 = f.split(':') 
                        if(aux23[1]==''):
                            aux23.remove(aux23[1])
                        if(len(aux23)>1):
                            modulos.append((aux23[0]+':')[:-1])
                            instruccion.append(aux23[1].strip().strip('\n')+'&'+str(fila))
                        else:
                            modulos.append((f.strip().strip('\n'))[:-1])
    except:
        f = f.strip('\n')
        if(f!=''):
            print(f'En la fila {fila} la instrucción {f} no existe')
            validacion=1
           
archivo.close()



if(codebool==True and databool==True):
    assembler_func()
elif(codebool==False and databool==False):
    assembler_func()
     
output_arch.close()
if validacion==0:
    print('Son todas las instrucciones correctas')
else:
    output_arch=open(name+'.casi','w')
    output_arch.close()


    