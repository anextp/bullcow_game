# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 11:38:16 2023

@author: anial
"""
import random
import itertools

digit_set = []
guess_set = []
numbers = [i for i in range(1,10)]
answer = []
true_guess = random.sample([i for i in range(9)], 4)
def find_my_guess(true_guess):

    the_guess = input("ENTER YOUR GUESS : ")
    guess_list = [int(i) for i in the_guess]
    if guess_list == true_guess:
        print("______YOU WON_______")
        return None
    digits = 0
    places = 0
    for i in range(4) :
        for j in range(4):
            if guess_list[j] == true_guess[i]:
                digits += 1
                if i == j:
                    places += 1
    print(digits, " : ", places)
    return True



def is_valid_comb(combination, position_matrix, answer):
    
    for i in range(len(combination)):
        
        if position_matrix[answer.index(combination[i])][i] is False:
            return False
        
    return True


def starter(digit_set,guess_set,answer):

    
    return(sum, )


    
def guess(guess_set,numbers,kept):
    guess = 0
    guess_set.append([])
    if kept:
        a =[]

        for i in numbers:
            if i not in kept:
                a.append(i)
                
        a = random.sample(a, 4 - len(kept)) + kept
        random.shuffle(a) 
        for i in range(4):
            guess += a[i] * 10**i
            guess_set[(len(guess_set))-1].insert(0,a[i])      

 
    return(guess)





def game(answer):
    print('''    WELCOME TO THE BULLS AND COWS GAME
          
          
    HOW TO PLAY :
    THINK OF A 4-DIGIT NUMBER CONTAINING THE DIGITS 1-9, WHERE NO DIGIT IS BEING REPEATED
    WE WILL PLAY ONE BY ONE, AT EACH TURN THE OPPONENT SUGGESTS A GUESS AND YOU TELL HOW MANY DIGITS ARE
    IN YOUR TRUE GUESS AND HOW MANY OF THOSE ARE IN THEIR CORRECT PLACEMENTS
    THE INPUT SHOULD BE THE TRUE DIGIT COUNT:THE TRUE PLACEMENT COUNT
    I.E. 2:1 ( X BULLS:Y COWS)
    THE GAME ENDS ONCE ANY OF THE SIDES GUESSES THE OPPONENTS NUMBER\n\n ''')
    """Starter part of the code, generating first 2 calls"""
    print("START!")
    found = None
    guess_set.append([])
    l = [i for i in range(1,10)]
    random.shuffle(l)
    sum = 0
    new_guess = 0
    for i in range(4):
        new_guess += l[i] * 10**i
        guess_set[0].insert(0,l[i])          

    
    print("MY GUESS IS : ", new_guess)
    res = input("X BULLS:Y COWS:").split(":")
    opponent = find_my_guess(true_guess)
    if not opponent:
        return
    
    if int(res[0]) == 4:
        found = True
        if int(res[1] == 4):
            print("-------------I WON-----------------")
            return
        answer = guess_set[0]

    
    sum+= int(res[0])
    digit_set.append(res)
    

    if sum != 4:
        guess_set.append([])
        new_guess = 0
        for i in range(4):
            new_guess += l[4 + i] * 10**i
            guess_set[1].insert(0,l[4+i])   
            
        print("MY GUESS IS : ",new_guess)
        res = input("X BULLS:Y COWS:").split(":")
        opponent = find_my_guess(true_guess)
        if not opponent:
            return
        if int(res[0]) == 4:
            found = True
            if int(res[1] == 4):
                print("-------------I WON-----------------")
                return
            
            answer = guess_set[1]
            
        sum+= int(res[0])
        digit_set.append(res)
        
            
    #print("answer", answer)
    """Continuing to generate calls until all digits are found"""
    
    
    if not found:

        default = l[len(l) - 1]
        #print("default", default)

        if int(digit_set[0][0]) >= int(digit_set[1][0]):
            heavy = guess_set[0]
            loose = guess_set[1]
            #print(heavy)
            dnum = int(digit_set[0][0])
            lnum = int(digit_set[1][0])

            
        else:
            heavy = guess_set[1]
            loose = guess_set[0]
            dnum = int(digit_set[1][0])
            lnum = int(digit_set[0][0])

            #print(heavy)
    
        if sum != 4:
            answer.append(default)
            dnum += 1
            #print(dnum)
            
        default = [default]
        while len(answer) < dnum:
            new_guess = guess(guess_set,heavy,default)
            last_guess = guess_set[len(guess_set)-1]
    
            print("MY GUESS IS: ", new_guess)
            res = input("X BULLS:Y COWS:").split(":")
            opponent = find_my_guess(true_guess)
            if not opponent:
                return
            
            digit_set.append(res)
                
            
            if int(res[0]) == 4 - lnum:
                junk = []
                for i in default:
                    if i not in answer:
                        junk.append(i)
                for i in last_guess:
                    if i not in junk and i not in answer:
                        answer.append(i)
                        
            elif int(res[0]) == len(answer) and 4 - len(default) == dnum - len(answer):
                for i in heavy:
                    if i not in last_guess and i not in answer:
                        answer.append(i)
                    
                        
            for i in heavy:
                if i not in last_guess:
                    default.append(i)
                    break
                
            #print(default,answer,dnum, res[0])
            if int(res[0]) == 4:
                if int(res[1])== 4:
                    print("-------------I WON-----------------")
                    return
                
                answer = last_guess 
             
                
            elif int(res[0]) < dnum:
                        answer.append(i)
                        

                           
                            
                    
            
        default = answer[:1]
        while len(answer) != 4:
            new_guess = guess(guess_set,loose,default)
            last_guess = guess_set[len(guess_set)-1]
            
            print("MY GUESS IS : ", new_guess)
            res = input("X BULLS:Y COWS:").split(":")
            opponent = find_my_guess(true_guess)
            if not opponent:
                return
            digit_set.append(res)
    
            if int(res[0]) == 4 - lnum:
                junk = []
                for i in default:
                    if i not in answer:
                        junk.append(i)
                for i in last_guess:
                    if i not in junk and i not in answer:
                        answer.append(i)
                        
                        
            elif int(res[0]) == len(answer) and 4 - len(default) == lnum - len(answer):
                
                for i in loose:
                    if i not in last_guess and i not in answer:
                        answer.append(i)
                        
                        
            for i in loose:
                if i not in last_guess:
                    default.append(i)
                    break
                
                
            if int(res[0]) == 4:
                if int(res[1])== 4:
                    print("-------------I WON-----------------")
                    return
                answer = last_guess 
             
                
            elif int(res[0]) < lnum +1:
                answer.append(i)
                    
    #print("curr answer", answer)
    
    
    
    place_matrix = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
    final_answer = [None, None, None, None]
    for i in range(len(guess_set)):
        #print(len(guess_set), guess_set)
        #print(digit_set)
        if int(digit_set[i][1]) == int(digit_set[i][0]):
            for j in range(len(guess_set[i])):
                if guess_set[i][j] in answer:
                    pos = answer.index(guess_set[i][j])
                    for k in range(4):
                        if k != j:
                            place_matrix[pos][k] = False
                    for k in range(4):
                        if k != pos:
                            place_matrix[k][j] = False
                    place_matrix[pos][j] = True
                    
        elif int(digit_set[i][1]) == 0:
            for j in range(len(guess_set[i])):
                if guess_set[i][j] in answer:
                    pos = answer.index(guess_set[i][j])
                    place_matrix[pos][j] = False
                    
        else:
            for j in range(len(guess_set[i])):
                if guess_set[i][j] in answer:
                    pos = answer.index(guess_set[i][j])
                    if place_matrix[pos][j] != False:
                        place_matrix[pos][j] = True
                        
                        
    
    # for i in place_matrix:
        #print(i)
    
    # for i in range(len(guess_set)):
    #     for j in range(i, len(guess_set)):
    #         if digit_set[i][1] != 0 and digit_set[i][1] == digit_set[j][1]:
    #             for num in range(4):
    #                 if guess_set[i][num] in answer and guess_set[i][k] == guess_set[j][num]:
    #                     pos = answer.index(guess_set[i][num])
    #                     for k in range(4):
    #                         if k != pos:
    #                             place_matrix[k][num]= False
    #                     place_matrix[pos][num] = True
                        
                        
        
                        
    for num in range(len(place_matrix)):
        count = 0
        corr_pos = None
        for pos in range(len(place_matrix)):
            if place_matrix[num][pos] == False:
                count += 1
                
            elif place_matrix[num][pos] != False:
                corr_pos = pos
                
        if count == 3:
            final_answer[corr_pos] = answer[num]
            
            
    for num in range(len(place_matrix)):
        count = 0
        corr_pos = None
        for pos in range(len(place_matrix)):
            if place_matrix[pos][num] == False:
                count += 1
                
            elif place_matrix[pos][num] != False:
                corr_pos = pos
        if count == 3: 
            final_answer[num] = answer[corr_pos]
                
    #print("arajin ktor@ stugeluc heto ", final_answer)
    
    
    if all(final_answer):
        print("-------------I WON-------------------")
        #print(final_answer)
        return
                    
            
    else:
        temp = []
        
        "NAYI STEX NAYI STEEEEEEEEEEEEEX"
        
        for i in range(len(answer)):
            if answer[i] not in final_answer:
                temp.append(answer[i])

        #print("the floating digits ",temp )
        
        valid_combinations = []            
        for comb in itertools.permutations(answer):
            if is_valid_comb(comb, place_matrix,answer):
                valid_combinations.append(comb)
                
        #print("list of valid combinations")
        valid_combinations.pop(0)
        for v in valid_combinations:
            print(v)
            
        #print("temp is ", temp)
        #print("-----------------")
        final_answer = list(valid_combinations.pop(0))
        while True :
            #print("----------------------")
            print("MY GUESS IS: ")
            print(final_answer)
            res = input("X BULLS:Y COWS:").split(":")
            opponent = find_my_guess(true_guess)
            if not opponent:
                return
            
            digit_set.append(res)             
            
            if int(res[1]) == 4:
                print("I won!")
                return


            if int(res[1]) == 4 - len(temp):
                for i in temp:
                    place_matrix[answer.index(i)][final_answer.index(i)] = False


                for comb in valid_combinations[:]:
                    if not is_valid_comb(comb, place_matrix, answer):
                        valid_combinations.remove(comb)
                            
                print(valid_combinations)
                            
                final_answer = [None, None, None, None]
                
                for num in range(len(place_matrix)):
                    count = 0
                    corr_pos = None
                    for pos in range(len(place_matrix)):
                        if place_matrix[num][pos] == False:
                            count += 1
                            
                        elif place_matrix[num][pos] != False:
                            corr_pos = pos
                            
                    if count == 3:
                        final_answer[corr_pos] = answer[num]
                        if answer[num] in temp:    
                            temp.remove(answer[num])
                                                
                for num in range(len(place_matrix)):
                    count = 0
                    corr_pos = None
                    for pos in range(len(place_matrix)):
                        if place_matrix[pos][num] == False:
                            count += 1
                            
                        elif place_matrix[pos][num] != False:
                            corr_pos = pos
                    if count == 3:
                        final_answer[num] = answer[corr_pos]
                        if answer[corr_pos] in temp:    
                            temp.remove(answer[corr_pos])
                        
                       
            final_answer = list(valid_combinations.pop(0))
            if len(temp) == 0:
                print("----------------I WON-----------------------")
                return

                    
game(answer)             
        
    
# guess_set.append(new_guess)
# print(new_guess)
# res = input("X BULLS:Y COWS:").split(":")
# digit_set.append(res)


#print(numbers)
