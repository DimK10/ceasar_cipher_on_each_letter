# This program gets a number, duplicates it unltil length_of_number_digits = length_of_txt_to_cipher
# and then, it reads each leatter and for each letter, it uses as n the corresponding digit (so for 
# each letter a new alphabet for ceaser cipher is used).
# Finally, it creates a new file, and fills it with the ciphered text.
# The decryption process is basically the same steps in reversed order. 

#General menu, the user makes a choice, depending of what he wants the program to do
cipher_text = ''
decipher_text = ''
cipher_num = ''
import random as rn
while True:

    menu = ''' Welcome to Extended Ceasar Cypher Program.
Plase choose one of the following options (enter the desired number or letter)

           1 : Encrypt a txt file

           2 : Decrypt a txt file

           3 : Exit the program'''
    print(menu)

# Check for valid input

    while True:
        try:
            option_num = int(input())
            if option_num<1 or option_num>3:
                print('Please give a number between 1 and 3')
                continue
            break
        except ValueError:
            print('Please enter a valid number from the options above')

        

# if option_num == 1, enter the txt file a ssosiated
    if option_num == 1:
        print('You selected to encrypt a txt file\n')
        print('Please put the txt file you want to encrypt, in the same folder as the ceasr.py, and give the name of file only\n')
        print('example: if c:\pytho34\ceasar.py, then the file should be in the same folder, c:\python34\<name_of_file>.txt\n')
        print('Please note, that the text iside must not have any spaces\n')
        txtname = str(input())#Need to add FileNotFoundError exception handler- also on decipher aption 2

        txtname = txtname +'.txt'

        file = open(txtname, 'r+', encoding='utf-8')

        plain_text = file.read()
        li =[None]*len(plain_text)
#Fill list li with random numbers, so that, if user input is smaller that lenght of text in file to encrypt, there will be available numbers to encrypt
        for  i in range(len(plain_text)):
            li[i] = rn.randint(0,9)
        print(plain_text)
        print('The letters of the text you want to encrypt are: ', len(plain_text))
        file.close()
#Make the user give a number , that will be used for encrypting the plain_text to cipher_text
        while True:
            try:
                ceasar_num = int(input('Now, please give a number that will be used to cipher the text\nIt can be as long as the letters of text, but all the digits may not be used, depending on the length of the text you want to encrypt\n'))
                if len(str(ceasar_num)) > len(plain_text):
                    print('Please enter a number that its digits are as much as the letters in the text you want to cipher, not more\n')
                    
                    continue
                else:
                    break
                
            except ValueError:
                print('Please give digits, not letters')

#Checking the length of digits given with the length of the plain_text letters, and make then equal
        if len(str(ceasar_num)) == len(plain_text):
            for index,i in enumerate(str(ceasar_num)):
                li[index] = int(i)
                
            for index,i in enumerate(plain_text):
                cipher_text = cipher_text + chr(ord(i) + li[index])

           
        else:

# Encrypt             
            for index,i in enumerate(str(ceasar_num)):
                li[index] = int(i)
            print(li)
            for index,i in enumerate(plain_text):
                cipher_text = cipher_text + chr(ord(i) + li[index])
# Lets make a new file called cipher
                                 
        file = open('cipher.txt', 'w',encoding='utf-8')
        file.write(cipher_text)# ascii encoding problem SOS
        file.close()
# Add the contents of list li to a valiable called cipher_num
        for i in range(len(plain_text)):
            cipher_num +=  str(li[i])
        print('Your encrypted txt file is created and named cipher.txt\n')
        print('The number you gave is smaller than the letters needed to encrypt, so random numbers are generated to compensate with the encryption\n')
        print('IMPORTANT!!! KEEP THIS NUMBER AND SAVE IT, FOR DECRYPTION!!!\n')
        print('The number used to encrypt is: ', cipher_num)
        print('\n'*10000)
    elif option_num == 2:
        
#Ask for the cipher text
        print('You selected to dencrypt a txt file\n')
        print('Please put the txt file you want to dencrypt, in the same folder as the ceasar.py, and give the name of file only\n')
        print(' example: if c:\pytho34\ceasar.py, then the file should be in the same folder, c:\python34\<name_of_file>.txt\n')
        print('Please note, that the text iside must not have any spaces\n')
        txtname = str(input())

        txtname = txtname +'.txt'

        file = open(txtname, 'r+',encoding='utf-8')

        plain_text = file.read()
        li =[None]*len(plain_text)
        print(plain_text)
        print(len(plain_text))
        file.close()

#Ask for the number that was used in encryption in the first place
        while True:
            try:
                ceasar_num = int(input('Now, please give the number that will be used to decipher the text\nIt must be the same number you gave when you encrypted your file\n'))
            
                break
            except ValueError:
                print('Please give digits, not letters\n')                                

# Same check for lengths as above
        #Checking the length of digits given with the length of the plain_text letters, and make then equal
        if len(str(ceasar_num)) >= len(plain_text):
             for index,i in enumerate(str(ceasar_num)):
                 li[index] = int(i)
                
             for index,i in enumerate(plain_text):
                decipher_text = decipher_text + chr(ord(i) - li[index])
        else:
#lets give ceasar_num the same length as plain_text, looping the digits in ceasar_num
            for i in ceasar_num:
                if len(str(ceasar_num))<len(plain_text):
                    ceasar_num += i
                else:
                     break                         
            for index, i in enumerate(str(ceasar_num)):
                li[index] = int(i)
                
            for index,i in enumerate(plain_text):
                decipher_text = decipher_text + chr(ord(i) - li[index])
# Lets make a new file called decipher
                                 
        file = open('decipher.txt', 'w',encoding='utf-8')
        file.write(decipher_text)
        file.close()
        print('Your dencrypted txt file is created and named decipher.txt\n')
        print('\t')
        print('\n'*10000)
        
    else:
        print('The program will now close')
        break