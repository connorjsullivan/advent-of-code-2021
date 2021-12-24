
import numpy as np
import copy
input = 'd4_input.txt'
picks = 'd4_pick_input.txt'
read_picks = open(picks)
array_picks = read_picks.read().split(',')
int_array_picks = list(map(int, array_picks))


my_file_handle=open(input)
card_number = my_file_handle.read().split('\n\n')
card_number_rows = []
for card in card_number:
    card_number_rows.append(card.split('\n'))
# print(card_number_rows)
int_card_number_rows = []
int_card_number = []

print(card_number_rows) # [[string row, row, row], [row, row, ...]]
for bingo_card in card_number_rows:
    for string_row in bingo_card:
        split_row = string_row.split(' ')
        for i in split_row:
            if i == '':
                next
            else:
                int_card_number.append(int(i))
# print(int_card_number)


total_cards = int(len(int_card_number)/25)
base_example = np.zeros((5,5), dtype='int')

for i in range(total_cards):
    int_card_number_rows.append(copy.deepcopy(base_example))

# print(int_card_number)

for tc in range(total_cards):
    for i in range(5):
        for j in range(5):
            value = int_card_number[(tc*25)+i+(j*5)]
            print(tc,i,j, value)
            int_card_number_rows[tc][i][j] = value

# print(int_card_number_rows)

#print(array_picks)
#card_number_rows = np.array_split(card_number, '\n')
#card_number_rows = card_number.split('\n')
#print (card_number)
#inputs all bingo ROWS to be put together into bingo cars
#5 rows into each card


#bingo wins / solutions
#5 in 1 line, 1 in each line, 1 in each diangol


# array = picked

def bingo_win_column(array_picked,all):
    pickedset = set(array_picked)
    for i in range(len(all)):
        column_win = set([all[0][i],all[1][i],all[2][i],all[3][i],all[4][i]])
        if column_win.issubset(pickedset):
            print("colw_win", column_win)
            return True
    return False


def bingo_win_diaganol(array_picked,all):
    #win all 5 in column top left to top right
    #or bottom left to top righ
    # 5,4,3,2,1 or 1,2,3,4,5

    diagnol_win_1 = [all[0][0],all[1][1],all[2][2],all[3][3],all[4][4]]
    diagnol_win_2 = [all[0][4],all[1][3],all[2][2],all[3][1],all[4][0]]
    diagnolset1 = set(diagnol_win_1)
    diagnolset2 = set(diagnol_win_2)  
    pickedset = set(array_picked)
    
    if diagnolset1.issubset(pickedset) or diagnolset2.issubset(pickedset):
        print("dig_win")
        print(diagnolset1, diagnolset2, pickedset)
        return True
    return False


#can maybe make row/checked values i
# nto a set to see if it exists?
def bingo_win_row(array_picked,all):
    #run through rows
    pickedset = set(array_picked)
    for i in range(len(all)):
        row_win = set(all[i]) #[all[i][0],all[i][1],all[i][2],all[i][3],all[i][4]])
        if row_win.issubset(pickedset):
            print("row_win", row_win)
            return True
            
    return False

#main Bingo!
 #will be first board to bingo, and  

#for each card number
    #check each three and see if it returns true
    #if it does not return true, add one more onto guessed
flattened = []
hard_break = False
lastLoser = None
# losers = int_card_number_rows
for i in range(5,len(int_array_picks)):
    current_pick_set = int_array_picks[0:i]
    
    #instead of removing ones you dont want, keep ones you do want in here
    losers = [] 
    print("PICKED A NEW NUMBER: ", current_pick_set, "----------------")
    print("LENGTH:", len(int_card_number_rows))
    #Start:End:Steps
    for j in range(len(int_card_number_rows)):
        current_card = int_card_number_rows[j]
        print("CURRENT CARD:", j)
        if (bingo_win_column(current_pick_set,current_card) or bingo_win_row(current_pick_set,current_card)):
                # print(current_card, 'in end loop')
                #hard_break = True
                
                #losers = losers[:j] + losers[j+1:]
                # losers.append(int_card_number_rows[j])
                # int_card_number_rows.remove(current_card)


                # for row in current_card:
                #     for item in row:
                #         flattened.append(item)
                # unmarked =  set(flattened) - set(int_array_picks[0:i])
                # to_multiply = int_array_picks[i-1]

                # print(sum(unmarked) * to_multiply)
                # break
                pass
        else:
        # else didn't win, add to losers
            # print("LOSER")
            # print(int_card_number_rows[j])
            # if len(losers) == 1:
            #     hard_break = True
            j_max = i
            #     break
            losers.append(int_card_number_rows[j])
            
    # if (len(losers) == 0):
    #     break
    # print(len(losers))
    if len(losers) == 1:
        print("got to 1 left")
        # print(losers[0]g)
        lastLoser = losers[0]
    if len(losers) == 0:
        break

for row in lastLoser:
    for item in row:
        flattened.append(item)
print(j_max)
print(flattened)

unmarked =  set(flattened) - set(int_array_picks[0:j_max+1])
print(sum(unmarked))
to_multiply = int_array_picks[j_max]
print(to_multiply)

print(sum(unmarked) * to_multiply)

#split into cards
#iterate through each of the choices starting at 5
#after we have 5 guesses, start iterating through the 3 function
#if 1 returns true - means it is bingo
