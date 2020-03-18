import re


class Tinkerhub:
    'Common base class for all employees'
    Name = 'NIL'
    Position = 'NIL'
    Time = []
    stack = []        

    def addStacks(self, program, flag=0, count=0):
        if (self.Position == 'Mentor'):
            print("\n Enter Domains you are Expertised In... \n Enter 'exit' to stop")
        else:
            print("\n Enter Domains you are Interested In... \n Enter 'exit' to stop")
        while (flag != 1):
            count += 1
            print('\n',count,'- ')
            program = input()
            if (program != 'exit'):
                self.stack.append(program)
            else:
                flag = 1
        
    def setMentorOrLearner(self, choice, flag=0):
        while (flag != 1):
            choice = input("  Mentor/Learner (m/l) : ")
            if choice == 'm':
                self.Position = 'Mentor'
                self.Name = input("\n Please Enter Name : ")
                flag = 1
            elif choice == 'l':
                self.Position = 'Learner'
                self.Name = input("\n Please Enter Name : ")
                flag = 1
            else:
                print('\tSorry! Please enter m or l')

    def setAvailableTime(self, Time_string):
        if self.Position == 'Mentor':
            Time_string = input("\n Enter Available Time (HH:MM 24hr format) : ")
            print()
            temp = re.findall(r'\d+', Time_string)
            self.Time = list(map(int, temp))
        print('\n\t\t Congratulations!\n\t You are registered as', self.Position,'\n\n')
    
    def getMentor(check=0):
        print('\n\n\nAvailable Mentors for all Learners are displayed below')
        for obj in range(num):
            if t[obj].Position == 'Learner':
                print('\n\nHi', t[obj].Name)
                for obj_check in range(num):
                    check = 0
                    if t[obj_check].Position == 'Mentor':
                        check = any(item in t[obj].stack for item in t[obj_check].stack)
                    if check == 1:
                        print('Mentor', t[obj_check].Name, 'is available at', t[obj_check].Time[0], ':', t[obj_check].Time[1])


t = []
print('\n\n\tWelcome to Tinkerhub! ')
print('\n Register as Mentors or Learners')
num = int(input("How many entries do you wish to Register : "))
for i in range(num):
    t.append(Tinkerhub())
for obj in range(num):
    print('\n\n\n\n Entry No : ', obj+1)
    t[obj].setMentorOrLearner(0, 0)
    t[obj].addStacks('NIL')
    t[obj].setAvailableTime('NIL')
Tinkerhub.getMentor()
