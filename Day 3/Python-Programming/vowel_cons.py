def vowel_consonant_cnt():
    s='gayathri'
    vcnt=0
    ccnt=0
    for char in s:
        if char in 'AEIOUaeiou':
            vcnt+=1
        else:
            ccnt+=1
    print("No. of voewls : ",vcnt)
    print("No, of consonants : ",ccnt)
vowel_consonant_cnt()