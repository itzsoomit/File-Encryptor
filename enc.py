from cryptography.fernet import Fernet,InvalidToken
import os.path
from home.models import Files
import io

def generate_key(file):
    key=Fernet.generate_key()
    
    # print(key)
    return key


    

def encrypt(file,key):
    f=Fernet(key)
    # with open(file,"rb") as file:
    file_data=file.read()
    f.encrypt(file_data)
    encrypted_data=f.encrypt(file_data)
    file_buffer = io.BytesIO()
    file_buffer.write(encrypted_data)
    file_buffer.seek(0)
    #file.write(encrypted_data)
    
    k=Files.objects.create(key=key)
    k.file.save(file.name,file_buffer) 
    

def decrypt(file,key):
    try:
        f=Fernet(key)
    except InvalidToken:
        print("Invalid Key")
        return "sorry"
    # with open(file,"rb") as file:
    encrypted_data=file.read()
        
    decrypted_data=f.decrypt(encrypted_data)
    file_buffer = io.BytesIO()
    file_buffer.write(decrypted_data)
    file_buffer.seek(0)
    k=Files.objects.create(key=key)
    k.file.save(file.name,file_buffer) 
    
    # print(decrypted_data)
    # with open(file,"wb") as file:
    # file.write(decrypted_data)


# choice=input("Enter 'E' to encrypt or 'D' to decrypt : ").lower()
def encryption(file):
    
        # file=input("Enter the name of file with extension : ")
        file=file
        # if(os.path.exists(file)):
        key=generate_key(file)
        
        encrypt(file,key) 
        
        return key
        print("File encrypted Successfully")
        # else:
            # print("File Not found !! ")

def decryption(file,dkey):
        # file = input("Enter the name of file with extension : ")
        # if (os.path.exists(file)):
            
        decrypt(file, dkey)
        print("File decrypted Successfully")
        # else:
        #     print("File Not found !! ")


