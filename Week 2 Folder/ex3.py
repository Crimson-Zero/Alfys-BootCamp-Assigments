def input_list():
    sum = 0
    number_array = []
    user_input = True
    while user_input:
        print("Please enter the Number you want")
        try:
            number_input = float(input("Number Input :"))
            number_array.append(number_input)
            if number_array[0] == " " or number_array[0] == "":
                return [0]
        except ValueError:
            print("Entered Value is not a number please try again")
        
        except KeyboardInterrupt:
            break
        
        print("Do you want to keep going")
        answer = input("Type Y or y for yes and N or n for No : ")
        
        if answer == "Y" or answer == "y":
            continue
        if answer == "N" or answer == "n":
            break
    
    for item in number_array:
        sum = sum + item
    
    number_array.append(sum)
    return number_array    

def calc_the_inner_product(list1,list2):
    sum = 0
    product = 1
    if len(list1) != len(list2):
        return None
    else:
        for i in range(len(list1)):
            product = list1[i] * list2[i]
            sum = sum + product
    
    return sum
        

    
    
    

            
    