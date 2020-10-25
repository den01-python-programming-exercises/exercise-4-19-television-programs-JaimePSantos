from television_program import TelevisionProgram
def main():
    #write your code below this line
    programList = []
    while(True):
      programName = input("Name: ")
      programDuration = int(input("Duration: "))
      if not programName:
        break
      programList.append(TelevisionProgram(programName,programDuration))
    
    inputDuration = int(input("Program's maximum duration? "))
    for program in programList:
      if(program.duration <= inputDuration):
        print(program)

if __name__ == '__main__':
    main()
