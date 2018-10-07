# HOMEWORK ASSIGNMENT 5

# K-MAP MINIMISATION

#USING OOPS CONCEPT


#It involves def __init__ function which includes self as an object
import itertools


#compare two binary strings, check where there is one difference
def compBinary(s1,s2):
    c= 0
    p= 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c+=1
            p = i
    if c == 1:
        return True, p
    else:
        return False, None



def compBinarySame(term,number):      #Compare binary number whether they are same or not.
    for i in range(len(term)):
        if term[i] != '-':
            if term[i] != number[i]:
                return False

    return True


#Combine pairs and make New Group
def combinePairs(group, unchecked):
    X= len(group) -1
    check_list = []
    next_group = [[] for x in range(X)]
    for i in range(X):
        for e1 in group[i]:
            for e2 in group[i+1]:
                b, pos = compBinary(e1,e2)
                if b == True:
                    check_list.append(e1)
                    check_list.append(e2)
                    new_elem = list(e1)
                    new_elem[pos] = '-'
                    new_elem = "".join(new_elem)
                    next_group[i].append(new_elem)
    for k in group:
        for j in k:
            if j not in check_list:
                unchecked.append(j)

    return next_group, unchecked

def remove_redundant(group):     #Function to remove the redundant entries.
    new_group = []
    for i in group:
        new=[]
        for l in i:
            if l not in new:
                new.append(l)
        new_group.append(new)
    return new_group


def remove_redundant_list(list):   #Function to remove the redundant list.           
    elist = []
    for i in list:
        if i not in elist:
            elist.append(i)
    return elist


#Returns True if empty
def check_empty(group):

    if len(group) == 0:
        return True

    else:
        count = 0
        for m in group:
            if (m):
                count+=1
        if count == 0:
            return True
    return False

def find_prime(Chart):                    #Function to find prime implicants
    prime = []
    for colum in range(len(Chart[0])):
        count = 0
        pos = 0
        for rows in range(len(Chart)):
            #find essential
            if Chart[rows][colum] == 1:
                count += 1
                pos = rows

        if count == 1:
            prime.append(pos)

    return prime

def check_all_zero(Chart):
    for i in Chart:
        for j in i:
            if j != 0:
                return False
    return True

#find max value in list
def find_max(li):
    max = -1    #max function for using the maximum value
    ind = 0
    for i in range(len(li)):
        if li[i] > max:
            max = li[i]
            ind=i
    return ind

def multiplication(list1, list2):
    list_result = []
    if len(list1) == 0 and len(list2)== 0:
        return list_result
    elif len(list1)==0:
        return list2    
    elif len(list2)==0:
        return list1
    else:
        for k in list1:
            for l in list2:
                if k == l:
                    list_result.append(k)
                else:
                    list_result.append(list(set(k+l)))

        list_result.sort()
        return list(list_result for list_result,_ in itertools.groupby(list_result))   #Some general methods for grouping
 def petrick_method(Chart):               #Main motive is to implement this function.
    P = []
    for colum in range(len(Chart[0])):
        p =[]
        for rows in range(len(Chart)):
            if Chart[rows][colum] == 1:
                p.append([rows])
        P.append(p)
    for l in range(len(P)-1):
        P[l+1] = multiplication(P[l],P[l+1])           #Multiplication function

    P = sorted(P[len(P)-1],key=len)
    final = []
    min=len(P[0])
    for i in P:
        if len(i) == min:
            final.append(i)
        else:
            break
    return final


def find_minimum_cost(Chart, unchecked):
    P_final = []
    essprime = find_prime(Chart)
    essprime = remove_redundant_list(essprime)

    #print out the essential primes
    if len(essprime)>0:
        s ="Essential Prime Implicants"
        for i in range(len(unchecked)):
            for j in essprime:
                if j == i:
                    s= s+binary_to_letter(unchecked[i])+' , '
        print (s[:(len(s)-3)])

    for i in range(len(essprime)):
        for colum in range(len(Chart[0])):
            if Chart[essprime[i]][colum] == 1:
                for row in range(len(Chart)):
                    Chart[row][colum] = 0

    if check_all_zero(Chart) == True:
        P_final = [essprime]
    else:
        #petrick's method
        P = petrick_method(Chart)
        P_cost = []
        for prime in P:
            count = 0
            for k in range(len(unchecked)):
                for l in prime:
                    if l == k:
                        count = count+ cal_efficient(unchecked[k])
            P_cost.append(count)


        for k in range(len(P_cost)):
            if P_cost[k] == min(P_cost):
                P_final.append(P[k])

        for k in P_final:
            for l in essential_prime:
                if l not in k:
                    k.append(l)

    return P_final

#Calculating the number of literals
def cal_efficient(s):
    count = 0
    for i in range(len(s)):
        if s[i] != '-':
            count+=1

    return count

#Hacks to covert binary to letters !!
def binary_to_letter(s):
    em = ''
    ch = 'a'
    more = False
    n = 0
    for i in range(len(s)):
        #if it is a range a-zA-Z
        if more == False:
            if s[i] == '1':
                em = em + ch
            elif s[i] == '0':
                em = em + ch+ '\''

        if more == True:
            if s[i] == '1':
                em = em + ch + str(n)
            elif s[i] == '0':
                em = em + ch + str(n) + '\''
            n+=1
        #conditions for next operations
        if ch=='z' and more == False:
            ch = 'A'
        elif ch=='Z':
            ch = 'a'
            more = True

        elif more == False:
            ch = chr(ord(ch)+1)
    return em


def main():                         #A general python concentive
    numvar = int(input("Enter the number of variables: "))
    minter =input("Enter the minterms:")
    a = minter.split()
    a = list(map(int, a))

    group = [[] for x in range(numvar+1)]

    for i in range(len(a)):
        a[i] = bin(a[i])[2:]
        if len(a[i]) < numvar:
            for j in range(numvar - len(a[i])):
                a[i] = '0'+ a[i]
        elif len(a[i]) > numvar:
            print ('\nError : Choose the correct number of variables ')
            return
        index = a[i].count('1')
        group[index].append(a[i])


    all_group=[]
    unchecked = []
    #combine the pairs in series until nothing new can be combined
    while check_empty(group) == False:
        all_group.append(group)
        next_group, unchecked = combinePairs(group,unchecked)
        group = remove_redundant(next_group)

    s = "\nPrime Implicants:"
    for i in unchecked:
        s= s + binary_to_letter(i) + " , "
    print (s[:(len(s)-3)])

    #make the prime implicant chart
    Chart = [[0 for x in range(len(a))] for x in range(len(unchecked))]

    for r in range(len(a)):
        for t in range (len(unchecked)):
            #term is same as number
            if compBinarySame(unchecked[t], a[r]):
               Chart[t][r] = 1

    primnum = find_minimum_cost(Chart, unchecked)
    primnum = remove_redundant(primnum)


    print ("~~--Answer is--~~")

    for prime in primnum:
        s=''
        for i in range(len(unchecked)):
            for j in prime:
                if j == i:
                    s= s+binary_to_letter(unchecked[i])+' + '
        print (s[:(len(s)-3)])



if __name__ == "__main__":
    main()           #Way of calling the main() function
    A = input("Press Enter to Quit")   
