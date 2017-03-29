#! python3
#Random Quiz Generator

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama' : 'Montgomery',
            'Alaska' : 'Juneau',
            'Arizona' : 'Phoenix',
            'Arkansas' : 'Little Rock',
            'California' : 'Sacramento',
            'Colorado' : 'Denver',
            'Conecticud' : 'Hartford',
            'Delaware' : 'Dover',
            'Florida': 'Tallahassee',
            'Georgia' : 'Atlanta',
            'Hawaii' : 'Honolulu',
            'Idaho' : ' Boise',
            'Illinois' : 'Springfield',
            'Indiana' : 'Indianapolis',
            'Iowa' : 'Des Moines',
            'Kansas' : 'Topeka',
            'Kentuky' : 'Frankfort',
            'Louisiana' : 'Baton Rouge',
            'Maine' : 'Augusta',
            'Maryland' : 'Annapolis',
            'Massachusetts' : 'Boston',
            'Michigan' : 'Lansing',
            'Minnesota' : 'Saint Paul',
            'Mississippi' : 'Jackson',
            #continuar
    }

    #Generate 9 quiz files.
for quizNum in range (9):
    #TODO : Create the quizand answer key files.
    quizFile = open('CapitalQuiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('CapitalQuizAnswers%s.txt' % (quizNum + 1), 'w')

    #TODO: write out the header for the quiz
    quizFile.write('Name:\n\nDate\n\nPeriod\n\n')
    quizFile.write((' ' * 20) + 'Satate Capital Quiz (From %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    

    #TODO: loop through all 50 states, making a question for each
    for questionNum in range (24): #24 por los estados cargados al momento
        #Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers [wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

    #Write the question and the answer option to the quiz file.
        quizFile.write('%s. What is the capital of %s\n' % (questionNum  + 1, states[questionNum]))
        for i in range (4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #Write the answer key to file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
    
