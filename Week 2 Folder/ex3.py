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

def check_monotonic_sequence(seq_list):
    
    seq_copy = []
    for item in seq_list:
        seq_copy.append(item)
    
    seq_copy.sort()
    bool_list = [False,False,False,False]
    if seq_copy == seq_list:
        bool_list[0] = True
        bool_list[1] = True
        
        for i in range(1,len(seq_copy)):
            if seq_copy[i-1] == seq_copy[i]:
                bool_list[1] = False
                break
    
    seq_copy.reverse()
    if seq_copy == seq_list:
        bool_list[2] =True
        bool_list[3] = True
        for i in range(1,len(seq_copy)):
            if seq_copy[i-1] == seq_copy[i]:
                bool_list[3] =False
                break
    
    return bool_list
def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status


def primes_generator(get_number_of_primes):
    
    prime = []
    if get_number_of_primes == 0:
        return []
    for number in range(2,1000):
        if is_prime(number):
            prime.append(number)
    
    result = prime[:get_number_of_primes]
    return result
                


def vectors_list_sum(vec_lst1):
    
    
    output = []
    for column in zip(*vec_lst1):
        result = 0
        for item in column:
            result = result + item
        output.append(result)
        
        print(column)
    
    #result = [sum(col) for col in zip(*vec_lst1)]
    return output

def orthogonal_number(vector_list):
    orth_number = 0
    for i in range(len(vector_list)):
        for j in range(i+1,len(vector_list)):
            if calc_the_inner_product(vector_list[i],vector_list[j]) == 0:
                orth_number +=1
    
    return orth_number
    
