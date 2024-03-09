import zipfile
import time

folderpath = input("C:\Users\ACER\Desktop:")
zipf = zipfile.zipfile(folderpath)

if not zipf:
    print('the zipped file/folder is not password protected! You can successfully open it.')

else:
    starttime = time.time()
    result=0
    c = 0

if(result == 0):
    print("checking for 4 character password....")
    for i in characters:
        for j in characters:
            for k in characters:
                for l in characters:
                    guess = str(i) + str(j) + str(k) + str(l)
                    password = guess.encode('utf-8').strip()
                    print(guess)
                    c = c+1
                    try:
                        with zipfile.Zipfile(folderpath,'r') as zf:
                            zf.extractall(pwd=password)
                            print("success! The password is :" + guess)
                            endtime = time.time()
                            result = 1
                            break
                    except:
                        pass
                if result == 1 :
                    break
            if result == 1:
                break
        if result == 1:
            break
if(result == 0):
    print("sorry, password not found. A total of "+str(c)" +possible combinations tried in " +str(duration) +"seconds.password is not of 4 characters.")
else:
    duration = endtime-starttime
    print("congratulations!!! password found after trying '+str(c)'combinations in '+str(duration) +seconds'")