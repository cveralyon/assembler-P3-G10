# hexadecimal string
hex = '#A0' 
num = "-120"
hex=hex.split('#')[1]
# conversion
dec = int(hex, 16)

print(num.isdigit())
print('Value in hexadecimal:', hex)
print('Value in decimal:', dec)

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