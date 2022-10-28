#Quizlet game
#import class Question
from Question import Question

print("Welcome to my networking quiz! ")

#prompt user to play, quit if they type anything but yes
play = input("Do you want to take the quiz? Yes or No? ")

if play.lower() != "yes":
    quit()

print("Good luck!")

#list of questions to be asked with answer
question_prompts = ["Question 1: What does LAN stand for?\n(a) Local area node\n(b) Local area network\n(c) Light area node\n(d) Light area network\n\n", 
    "Question2: All nodes are connected to one single node known as the central node in which network topology?\n(a) Ring Topology\n(b) Bus topology\n(c) Tree topology\n(d) Star topology\n\n", 
    "Question 3: Which is not a layer of the OSI model?\n(a) network\n(b) data link\n(c) nodes\n(d) presentation\n\n", 
    "Question 4: Which of the following OSI layers is resposnsible for routing?\n(a) Physical layer\n(b) Network layer\n(c) Transport layer\n(d) Data link layer\n\n", 
    "Question 5: SMTP uses which protocol at the transport layer?\n(a) TCP\n(b) IP\n(c) DNS\n(d) UDP\n\n"]

#list of answers to be called
ques = [   
   Question(question_prompts[0], "b"),
   Question(question_prompts[1], "d"),
   Question(question_prompts[2], "c"),
   Question(question_prompts[3], "b"),
   Question(question_prompts[4], "a"),
]

#function that adds a score and calls from the class Question
def quiz(ques):
    score = 0
    for question in ques:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            
#print out results of quiz
    print("You got " + str(score) + "/" + str(len(ques)) + " correct!")  
    print("Your score: "+ str((score) / 5 * 100) + "%")

#call the function
quiz(ques)


















































