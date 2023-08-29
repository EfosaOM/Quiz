#Name: Efosa Osagiede
#Course: CSCI 100-02




#Code to read text file of permitted/authorized teachers
auth_teachers = dict()

permit = open("Auth.txt", "r")

for line in permit:
    permit_split = line.split(", ")
    name = permit_split[0]
    password = permit_split[1].strip("\n")
    auth_teachers[name] = password
    
#-------------------------------------Quiz----------------------------------------#
def quiz():
    print("Unavailable. Please try again later")
    home()

#------------------------------------Difficulty-------------------------------------------#
def difficulty():
    no_A = input("Number of questions for Stage A (Capitals) = ")
    no_B = input("Number of questions for Stage B (States) = ")
    print("\nThere will be " + no_A + " questions in Stage A")
    print("There will be " + no_B + " questions in Stage B")
    print("\nThank You!")
    difficulty_set = True
    teacher_lounge()
    
#-------------------------------------Prizes-----------------------------------------#    
def prizes():
    cutoff = input("Enter the cutoff mark: ")
    prizes = input("Enter the prize(s) (if multiple, separate with commas): ")
    print("\nPrize(s) for students who score at least " + cutoff + " in the quiz: " + prizes)
    print("\nThank You!")
    prize_set = True
    teacher_lounge()

#--------------------------------------Rankings-----------------------------------------#
#Firstly read scores from text file and store them in a dictionary
def rankings():
    score = open("Scores.txt", "r")
    #okay = score.read()

    dicki = dict()
    score_list = []
    for line in score:
        score_split = line.split(", ")
        name = score_split[0]
        scores = int(score_split[1].strip("\n"))
        dicki[name] = scores

#                               -----------------------                          

    print('''
        Please select an option
            1. View scores in order of attempt
            2. View scores from highest to lowest
            3. Back to Teacher's Lounge

                                                ''')

    option = input("Option: ")


#                          ---Rank scores in order of attempt---                           #
    if option == "1":
        print("\nRankings: ")
        i = 1
        for key, value in dicki.items():
            print(str(i) + ". " + key + " scored " + str(value))
            i += 1

        rankings()
        

#                       ----Rank scores from highest to lowest--------                  #
    elif option == "2":
        print("\nRankings: ")
        for value in dicki.values():
            score_list.append(value)

        sortedlist = sorted(score_list, reverse = True)

        j = 1
        for num in sortedlist:
            for key, value in dicki.items():
                if value == num:
                    print(str(j) + ". " + key + " scored " + str(value))
                    j += 1

        rankings()

        
#                                   ---Back---                                  #
    elif option == "3":
        teacher_lounge()

        
#                               ----Invalid option---                             #
    else:
        print("\nInvalid Option")
        rankings()

#-----------------------------------Teacher's Lounge---------------------------------------#        
def teacher_lounge():
    print('''
        Welcome to Teacher's Lounge!!

        Please select an option
             1. Difficulty
             2. Prizes
             3. Rankings
             4. Logout
                ''')

    option = input("Option: ")
    if option == "1":
        difficulty()
    elif option == "2":
        prizes()
    elif option == "3":
        rankings()
    elif option == "4":
        print("\nGoodbye")
        pass
    else:
        print("Invalid Option")
        teacher_lounge()
        
#----------------------------------------------------------------------------------------#     
def login_fail():
    print('''
        Invalid login! Sorry, you are not authorized to manage the quiz
            1. Retry login
            2. End the program
    ''')

    option = input("Option: ")
    if option == "1":
        teacher_func(name, password)
    elif option == "2":
        print("\nGoodbye")
        pass
    else:
        print("Invalid Option")
        login_fail()
        
#------------------------------------------------------------------------------------------#    
def teacher_func(name, password):
    auth_login = False
    print("\nPlease enter your name and password to continue")
    name = input("Name: ")
    password = input("Password: ")
    for a, b in auth_teachers.items():
        if name == a and password == b:
            auth_login = True
        

    if auth_login:
        print("\nYou have successfully logged in!")
        teacher_lounge()
    else:
        login_fail()
        
#------------------------------------Homepage-----------------------------------------#        
def home():
    print('''
            Hi! Welcome to EfoTech!!
            Please select your category:
                    1. Teacher
                    2. Student
    ''')

    option = input("Option: ")

    if option == "1":
        teacher_func(name, password)
    elif option == "2":
        quiz()
    else:
        print("\nInvalid Option. Try again\n")
        home()
    
#----------------------------------------------------------------------------------------------#

home()    
    
    
