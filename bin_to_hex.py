import binascii

def line_return(file_name:str):
    with open(file_name) as f:
        for line in f:
            yield line

def clean_data(line:str):
    line=line.replace(',','')
    line=line.replace('\n','')

    return line
if __name__ =='__main__':
    output=''
    i=0
    for line in line_return('bin.txt'):
        clean_line=clean_data(line)
        if(clean_line):
            output+=f'0x{int(clean_line,2):02x},'
            i+=1
            if(i%16 == 0):
                output+='\n'
        else:
            output+='\n'
    print(f'Successfully Converted {i} number of Binary Values to Hex')
    with open('hex.txt','w') as f:
        f.write(output)          
    print(f'Data Written to \'hex.txt\'')