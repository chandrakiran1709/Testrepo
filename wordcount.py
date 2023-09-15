def words_count(f):
    with open(f,"r") as file:
        data=file.read()
        data_list=data.lower().split()
        data_list.sort()
        frequent_words_dict={}
        for i in data_list :
            if i.isalpha():
                count=data_list.count(i)
                frequent_words_dict[i]=count

    for j in frequent_words:
        print(j,":",frequent_words[j])
        
        
file_name="apple.txt"
words_(file_name)