import random
import scipy.stats as stats

def perform_test(list1,list2):
    '''
    This function takes two datasets, shuffles them randomly, and selects 30 samples from each.
    Then it performs a Mann-Whitney U test to check for statistically significant differences between these two groups.
    '''
    random.shuffle(list1)
    random.shuffle(list2)
    new_list_1=list1[:30]
    new_list_2=list2[:30]
    return stats.mannwhitneyu(new_list_1, new_list_2)

def count_rejections(list1,list2):
    '''
    This function runs a Mann-Whitney U test 100 times on random samples of 30 elements from two datasets to see how often a significant difference is found.
    '''
    counter=0 #count H0 rejections
    for i in range(100):
        random.shuffle(list1)
        random.shuffle(list2)
        new_list_1=list1[:30]
        new_list_2=list2[:30]
        wynik=stats.mannwhitneyu(new_list_1, new_list_2)
        if wynik[1]<0.05: #wynik<0.05 is considered significant
            counter+=1
    return f"After randomizing the sample 100 times, a significant difference was found {counter} times."