import os

class Raid:
    def raidZeroWrite(dataIn, fileName):
        raidType = 'raid0'
        fileName0 = 'data/' + fileName + raidType + '-' + "0.txt"
        fileName1 = 'data/' + fileName + raidType + '-' + "1.txt"
        f1 = open(fileName0, 'w')
        f2 = open(fileName1, 'w')

        dataIn = iter(dataIn)

        for char in dataIn:
            f1.write(char)
            try:
                f2.write(next(dataIn))
            except StopIteration:
                pass
        f1.close()
        f2.close()

    def raidZeroRead(fileName):
        raidType = 'raid0'
        raidSize = 2
        #fileNames[raidSize] = ["" for i in range(raidSize)]
        #print(fileNames)
        fileName0 = 'data/' + fileName + raidType + '-' + "0.txt"
        fileName1 = 'data/' + fileName + raidType + '-' + "1.txt"
        f1 = open(fileName0, 'r')
        f2 = open(fileName1, 'r')
        file_string_01 = f1.read()
        file_string_02 = f2.read()

        dataout = ""
        while True:
            if len(file_string_01) != 0:
                dataout += file_string_01[0]
            if len(file_string_02) != 0:
                dataout += file_string_02[0]
            #print(dataout, file_string_01 ,file_string_02)
            
            file_string_01 = file_string_01[1:]
            file_string_02 = file_string_02[1:]
            if (len(file_string_01)==0) and (len(file_string_02)==0):
                break
        return dataout


    def raidOne(dataIn, fileName):
        raidType = 'raid1'
        fileName0 = fileName + raidType + '-' + "0.txt"
        fileName1 = fileName + raidType + '-' + "1.txt"
        f1 = open(fileName0, 'w')
        f2 = open(fileName1, 'w')

        for char in dataIn:
            f1.write(char)
            f2.write(char)
        f1.close()
        f2.close()



if __name__ == '__main__':
    
    aString = "1234567890abcdefghijklmnopqrstuvwxyz"
    
    
    Raid.raidZeroWrite(aString, "newFile")
    print(Raid.raidZeroRead("newFile"))



    
