def num_to_words(n):
    nums=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    for d in str(n):
        print(nums[int(d)],end=" ")
    print()
num_to_words(123)
num_to_words(4567890)
