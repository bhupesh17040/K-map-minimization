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
