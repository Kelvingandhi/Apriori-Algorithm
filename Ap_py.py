#C:\Users\Kelvin\eclipse-workspace\Data Mining Apriori Algorithm\input.txt

'''
Step 1: Read data from file
Step 2: Frequent 1 Item set (prune by support & find) L1
Step 3: Give L1 as input and find all frequent k itemset to generate candidate itemset
Step 4: Pass candidate itemset as input and generate association rules
'''

from itertools import combinations


def generateSupportCount(trans):
    
    item_list=[]
    item_count_list=[]
    item_dict={}
    
    for item in trans:
        i = item.strip().split(',')
        
        for j in i:
            if j not in item_list:
                item_list.append(j)
                item_dict[j]=1
            
            else:
                item_dict[j]=item_dict[j] + 1
        
    print(item_list)
    
    print(item_dict)
    
    return item_list, item_dict


def satisfySupport(tr_dict, min_sup,trans_dataset, tran_len):
    
    new_list = []
    
    for i,c in tr_dict.items():
        if c/tran_len >= min_sup:
            new_list.append([i])
            print(f'{i} => {c/tran_len} (support)')
    
    return new_list

def associateTrans(candidateItemSet, k):
    
    #newAssociatedSet = [[i,j] for i in candidateItemSet for j in candidateItemSet if(j>i)]
    #newAssociatedSet = [set().union(i,j) for i in candidateItemSet for j in candidateItemSet if len(set().union(i,j)) == k]
    newAssociatedSet=[]
    
    for i in range(len(candidateItemSet)):
        li = candidateItemSet[i];
        for j in range(i+1,len(candidateItemSet)):
            lj = candidateItemSet[j];
            
            if k == 2:
                s = li[(len(li)-1)],lj[len(lj)-1]
                
                #s = ','.join(sorted(s))
                newAssociatedSet.append(list(s))
            
            elif(li[:len(li)-1] == lj[:len(lj)-1]):
                s = li[0:(len(li)-1)],li[len(li)-1],lj[len(lj)-1]
                new = list(li[0:(len(li)-1)])
                new.append(li[len(li)-1])
                new.append(lj[len(lj)-1])
                #s = ''.join(sorted(s))
                newAssociatedSet.append(new)
                
                #newAssociatedSet.append(temp)
            
            #newAssociatedSet.append(candidateItemSet[i],candidateItemSet[j])
#             if li != j:
#                 gen_str = i+","+j
#                 newAssociatedSet.append(gen_str)
                
    return newAssociatedSet



def reduceBySupport(candidateItemSet, min_sup, trans_len):
    
    itemSet_dict = {}  #List cannot be a key of dictionary so we store in tuple
    
    #first count support
    for t in trans:
    
        for n,itemSet in enumerate(candidateItemSet):
            index = itemSet
            #items = candidateItemSet[itemSet]
            #i = items.strip().split(',')
            if n not in itemSet_dict:
                itemSet_dict[n] = 0
            c=0    
            for i in itemSet:
                #print("item value:", i)
                if i in t:
                    c=c+1;

            if c == len(itemSet):
                print(f'{n}, and trans = {t}')
                itemSet_dict[n] = itemSet_dict[n] + 1
            
    #print(itemSet_dict)
        
    #compare with min support
    reduced_list = []
    
    for index,count in itemSet_dict.items():
        if count/trans_len >= min_sup:
            reduced_list.append(candidateItemSet[index])
            
            print(f'{candidateItemSet[index]} => {count/trans_len} (support)')
    
    return reduced_list


def checkSupportOfList(itemSet):
    #print(itemSet)
    sup_count = 0;
    for t in trans:
        c=0;
        for i in itemSet:
            i = str(i)
            if i in t:
                c=c+1
        
        if c == len(itemSet):
            sup_count = sup_count + 1
            
    sup_val = sup_count/len(trans)
                
    #print(f'{itemSet} -> {sup_count}')
    return sup_val

def checkConf(candi_rule):
    
    temp_list = []
    combine_list = []
    
    #print("candi rule:",candi_rule)
    for i in candi_rule:
        temp_list.append(list(i))
        
    for j in temp_list:
        for k in j:
            combine_list.append(k)       
        
    #print("Combined List : ",combine_list)
    
    rule_confidence = checkSupportOfList(combine_list)/checkSupportOfList(temp_list[0])
    #print(f'{candi_rule} : {rule_confidence}')
    
    if rule_confidence >= min_conf:
        conf_val=rule_confidence
        sup_val=checkSupportOfList(combine_list)
        return candi_rule, sup_val, conf_val
    
    return [],'',''


def gen_combi(itemlists):
    
    for ilist in itemlists:
        k = len(ilist)
        #print(k)
        listset = set(tuple(ilist))
        pruned_freq_itemset = listset
        
        while k > 1:
            antecedent = set()

            for comb in combinations(pruned_freq_itemset, k - 1):
                antecedent = set(comb)
                #print(antecedent)
                candidatae_rule = (antecedent, listset - antecedent)
                valid_rules,sup_val,conf_val = checkConf(list(candidatae_rule))
                #print(candidatae_rule)
                #print(list(candidatae_rule))
                if valid_rules != []:
                    print(f'{valid_rules[0]} -> {valid_rules[1]} => confidence={conf_val} , support={sup_val}')
            
            k=k-1;
while True:
    
    try:
        #inp_file = input("Please enter file name: ")
        #inp_file = 'C:/Users/Kelvin/eclipse-workspace/Data Mining Apriori Algorithm/input3.txt'
        #inp_file = 'C:/Users/Kelvin/eclipse-workspace/Data Mining Apriori Algorithm/sw.txt'
        inp_file = 'C:/Users/Kelvin/eclipse-workspace/Data Mining Apriori Algorithm/amz.txt'
        file=open(inp_file, 'r')

        trans_dict={}

        trans=[]
        for line in file:

            #print(ctr,line)
            (k,v) = line.strip().split('-')
            trans_dict[k]= v
            trans.append(v)

    except FileNotFoundError:
        print('Either file is missing or filename is wrong')

    except:
        print('Error in reading file content')

    print("trans:",trans_dict)
    print('List:', trans)


    #min_sup= float(input("Please enter minimum support="))
    #min_conf=float(input("Please enter minimum confidence="))
    
    min_sup=0.25
    min_conf=0.50

    tr_list, tr_dict = generateSupportCount(trans)
    print(len(tr_dict))
    
    print("Frequent 1 itemset:")
    L1 = satisfySupport(tr_dict, min_sup, trans, len(trans))

    #print("L1 is ",L1)
    
    #for item in L1:
     #   print(f'{item[0]} => ')

    # t1=associateTrans(L1,2)
    # print(t1)
    # t2=associateTrans(t1,3)
    # print(t2)
    # print(associateTrans(t2,4))
    # k=2
    #L2 = reduceBySupport(t1, min_sup, len(trans))
    #print("L2 is ",L2)
    k=2

    freqSetList = []
    
    while(L1 != []):

        #something 
        #make join operation
        #candidateSet = []


        candidate_k_itemSet = associateTrans(L1, k)
        
        print(f'\nFrequent {k} itemset:')
        #generate candidate set
        L1 = reduceBySupport(candidate_k_itemSet, min_sup, len(trans))

        #print(f'k={k} and L1 = {L1}')

        if L1 != []:
            frequent_k_itemSet = L1
            
            freqSetList.append(frequent_k_itemSet)
        
        else:
            print("NULL")

        k =  k + 1
    
    # finalset = generateCandidateKitemset(tr_dict, L1, len(trans))
    #print("Final frequent set : ",frequent_k_itemSet)
    
    #Generate Rules from frequent k item set
    print('Rules:\n')
    if freqSetList != []:
        for iList in freqSetList:
            gen_combi(iList)
            
    else:
        print("No association rules found")

    
    #print(checkSupportOfList(['iPhone', 'Samsung', 'Nokia']))
    
    #Result the final rules which satisfy min confidence

    keepOn = input("Press any key to run again. | Press q to quit")

    if keepOn in ('q','Q'):
        break;

    else:
        continue;