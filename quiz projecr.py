'''''''''''''''''''''''''''''''''''''''GAMING QUIZ'''''''''''''''''''''''''''''''''''


#PRESENTED BY: NAVRAJ KAUR 



name=input("enter username :")
gamingName=input("enter gaming name :")
Class=input("enter class:")
fatherName=input("enter father name :")
motherName=input("enter mother name :")
address=input("enter address :")
mobile=input("enter phone number :")
email=("enter email :")

score=0
age=int(input("enter age :"))
if  age>=18 :
    print("valid for game")

    attempt=0
    password=input("enter password :")
    cpass=input("enter confirm password")
    
    
    if password==cpass:    
        print("password matched")
     
        print("                                     TERMS AND CONDITIONS                                               ")
    
    
    
        print("                  THE QUESTION ARE BASED ON INFORMATION TECHNOLOGY                                      ")
        print("                    THIS QUIZ CONTAIN TOTAL 7 QUESTION                                                  ")
        print("                   THERE ARE 4 OPTION IN EVERY QUESTION                                                 ")
        print("                     NO NEGATIVE MARKING IS CONDUCTING                                                  ")
        print("                            NO CHEATING ALLOWED                                                         ")
        print("                       NO OUTSIDE HELP IS ALLOWED                                                       ")
        print("                      EACH QUESTION CONTAIN 2 MARKS                                                     ")
        print("                 IN EVERY QUESTION ONLY ONE OPTION IS CORRECT                                           ")
        print("        NO IMFORMATION IS STORED IF A STUDENT QUIT IN MIDWAY OF THE GAME                                ")
        print("                      PLEASE ENTER OPTION IN CAPITAL LETTER                                             ")
        
        
        
        condition=input("do you agree with condition? (yes,/no): ")
        
        if condition=='yes'or condition=='YES' or condition=='Yes':
            print(" you can enter in the game")
            
            print("                                 question answers")
            print("                                                         QUESTION ANSWERS :-")
            score=0

            print("1 : what does CPU stands for:")

            print("A) central process unit")
            print("B) central processing unit")
            print("c) computer personal unit")
            print("D) control procesing unit")


            Correct_answer="B"
            attempt=0
            max_attempt=3

            while attempt<max_attempt: 
                answer=input("enter your answer (A/B/C/D):")

                if answer==Correct_answer:
                 print("correct answer")
                 score+=2
                 break
             
                else:
                    attempt+=1
                    if attempt<max_attempt:
                     print(f"incorrect , you have {max_attempt-attempt}remaining")
                    else:
                     print("incorrect. no more attempts remaing.")
                     print("the correct answer is :B) is central processing unit ")

    
                    #----------------------------------QUESTION------------------------------------------------------------------
    
    

            print("2: which one is not a web browser ")

            print("A) google chrome")
            print("B) mozilla firefox")
            print("c) microsoft edge")
            print("D) linux")


            Correct_answer="D"
            attempt=0
            max_attempt=3

            while attempt<max_attempt: 
                answer=input("enter your answer (A/B/C/D):")

                if answer==Correct_answer:
                 print("correct answer")
                 score+=2
                 break
             
                else:
                    attempt+=1
                    if attempt<max_attempt:
                     print(f"incorrect , you have {max_attempt-attempt}remaining")
                    else:
                     print("incorrect. no more attempts remaing.")
                     print("the correct answer is :D) LINUX ")



                #-------------------------------------------------------------QUESTION----------------------------------------------------------------



            print("3: which is not an option of operating system ")

            print("A) oracle")
            print("B) MacOS")
            print("c) windows")
            print("D) linux")


            Correct_answer="A"
            attempt=0
            max_attempt=3

            while attempt<max_attempt: 
                answer=input("enter your answer (A/B/C/D):")

                if answer==Correct_answer:
                 print("correct answer")
                 score+=2
                 break
             
                else:
                    attempt+=1
                    if attempt<max_attempt:
                     print(f"incorrect , you have {max_attempt-attempt}remaining")
                    else:
                     print("incorrect. no more attempts remaing.")
                     print("the correct answer is :A) ORACLE ")

                     #------------------------------------------------------QUESTION-------------------------------------------------

            print("4: which programming language is used to create web pages ")

            print("A) HTML")
            print("B) C++")
            print("c) PYTHON")
            print("D) Java")


            Correct_answer="A"
            attempt=0
            max_attempt=3

            while attempt<max_attempt: 
                answer=input("enter your answer (A/B/C/D):")

                if answer==Correct_answer:
                 print("correct answer")
                 score+=2
                 break
             
                else:
                    attempt+=1
                    if attempt<max_attempt:
                     print(f"incorrect , you have {max_attempt-attempt}remaining")
                    else:
                     print("incorrect. no more attempts remaing.")
                     print("the correct answer is :A) HTML ")


                     #------------------------------------------------------QUESTION------------------------------------------------



            print("5: which of these is an opensource operating system  ")

            print("A) IOS")
            print("B) MacOS")
            print("c) windows")
            print("D) linux")


            Correct_answer="D"
            attempt=0
            max_attempt=3

            while attempt<max_attempt: 
                answer=input("enter your answer (A/B/C/D):")

                if answer==Correct_answer:
                 print("correct answer")
                 score+=2
                 break
             
                else:
                    attempt+=1
                    if attempt<max_attempt:
                     print(f"incorrect , you have {max_attempt-attempt}remaining")
                    else:
                     print("incorrect. no more attempts remaing.")
                     print("the correct answer is :D) LINUX")


            #------------------------------------------------------QUESTION------------------------------------------------



            print("6: the brain of the computer is    ")

            print("A) RAM")
            print("B) CPU")
            print("c) hard disk")
            print("D) mother board")


            Correct_answer="B"
            attempt=0
            max_attempt=3

            while attempt<max_attempt: 
                answer=input("enter your answer (A/B/C/D):")

                if answer==Correct_answer:
                 print("correct answer")
                 score+=2
                 break
             
                else:
                    attempt+=1
                    if attempt<max_attempt:
                     print(f"incorrect , you have {max_attempt-attempt}remaining")
                    else:
                     print("incorrect. no more attempts remaing.")
                     print("the correct answer is :B) CPU ")


                     #------------------------------------------------------QUESTION------------------------------------------------


            print("7: which is not a type of network  ")

            print("A) LAN")
            print("B) MAN")
            print("c) WAN")
            print("D) FAN")


            Correct_answer="D"
            attempt=0
            max_attempt=3

            while attempt<max_attempt: 
                answer=input("enter your answer (A/B/C/D):")

                if answer==Correct_answer:
                    print("correct answer")
                    score+=2
                    break
                
                else:
                    attempt+=1
                    if attempt<max_attempt:
                     print(f"incorrect , you have {max_attempt-attempt}remaining")
                    else:
                     print("incorrect. no more attempts remaing.")
                     print("the correct answer is :D) FAN ")

            print(f"quiz game is completed . your total quiz score is: {score}/14")

            print("                                                         CERTIFICATE                                                                     ")


            print(f" this is to clarify that {name} and gaming name is {gamingName} has got score {score} in IT quiz")


            if score>=8:
                print("has completed this quiz with good marks which is based on information technology ")
                print(" THANKS FOR YOUR PATICIPATION .HAVE A GOOD DAY ")
    
            else:
    
                print("has completed this quiz but can't achieve good marks in this information technology quiz")
                print(" THANKS FOR YOUR PREPARATION . HAVE A NICE DAY ! BETTER LUCK NEXT TIME !")
        else:
            print("you didn't accept the conditions")
                                        
    else:   
        attempt=2
        
        print("password not matched ")
            
        while attempt>0:
            
            password=input("enter password :")
            cpass=input("enter confirm password:")
            if password==cpass:
                print(" yes ")
                break
            else:
                attempt-=1
                print("no ")
                print("to many failed attempt")  
   
            
                
else:
    print("age is not valid for quiz game")
    
          

    