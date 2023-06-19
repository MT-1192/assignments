'''1.write a program to fetch all even numbers given list?
l=[10,11,13,14,9,8]
even_numbers = [num for num in list if num%2 == 0]
print(even_numbers)'''

'''2.write a program to fetch all stirng values given list?
l=(10,'a',20,True,30,'b',40)
result = []
for i in l:
    if(type(i) is str):
        result.append(i)
print(result)'''

'''3.write a program to fetch all 5 divisible from the list?
l=[12,15,27,20,5]
div_by_5 = [num for num in l if num%5 == 0]
print(div_by_5)'''

'''4.write a program to count of total of int values in the list
l=[10,'a',True,30,'b',40]
result = []
for i in l:
    if(type(i) is int):
        result.append(i)
x = len(result)
print(x)'''

'''5.write a program to count of total no.of characters in given string(include spaces)
st="python language"
count = 0
for i in range(0,len(st)):
    if (st[i] != ""):
        count = count + 1
print(count)'''

'''6.write a program to count total no.of words in given string?
st='python is good language for beginners'
num_of_words = st.split()
print(len(num_of_words))'''

'''7.write a program to fetch all vowels from the string?
st='python is good language for beginners'
vowels = "AaEeIiOoUu"
l = [x for x in st if x in vowels]
print(l)'''

'''8.write a program to count no.of vowels in str?
st='python is good language for beginners'
count = 0
vowels=["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
for i in range(len(st)):
    if st[i] in vowels:
        count = count + 1
print(count)'''

#9 is same as 5.

'''10.write a program to fetch all no.of consonants in the str?
st='python language'
vowels = "AaEeIiOoUu"
l = [x for x in st if x not in vowels]
print(len(l))'''

'''11.write a program to fetch all words which starts with vowel from given str?
st='python is a simple and easy language'
vowels = "AaEeIiOoUu"
l = st.split()
list = [x for x in l if x[0] in vowels]
print(list)'''

'''12.write a program to fetch all words which endswith consonent in the given str?
st='python is simple and easy language'
vowels = "AaEeIiOoUu"
l = st.split()
list = [x for x in l if x[-1] not in vowels]
print(list)'''

'''13.write a program to fetch all words which 'a' two or more then two times
st='python is simple and easy language'
l = [x for x in st.split() if x.count("a") > 2]
print(l)'''

'''14.write a program to count number of characters of each word in the str?
st='python is simple and easy language'
list = st.split()
for i in list:
    print("In", i,"there are",len(i), "characters.")'''

'''15.write a program to fetch the first  and last charector for each word in str?
st='python is simple and easy language'
l = st.split()
for i in l:
    print("In",i,"the first character is",i[0],"and the last character is",i[-1])'''

'''16.write a program to fetch all words each contains 'a' character in the str?
st='python is simple and easy language'
l = st.split()
list = [x for x in l if "a" in x]
print(list)'''

'''17.write a program to fetch all words does not contain 'e' charector in str?
st='python is simple and easy language'
l = st.split()
list = [x for x in l if "e" not in x]
print(list)'''

'''18.write a program to fetch all words which contain only 4 or lessthen 4 charectors?
st='python is simple and easy language'
l = st.split()
list = [x for x in l if len(x) <= 4]
print(list)'''

'''19.write a program to fetch all words which contain odd number of charectors in str?
st='python is simple and easy language'
l = st.split()
list = [x for x in l if len(x) %2 != 0]
print(list)'''

'''20.write program to fetch all words which starts and ends with vowel in str?
st='python is number one language'
vowels = "AaEeIiOoUu"
l = st.split()
list = [x for x in l if x[0] and x[-1] in vowels]
print(list)'''

'''21.write a program to fetch all palendram words from  lst?
names=['madam','python','dad','language','eye','malayalam']
list = [x for x in names if x[0]==x[-1]]
print(list)'''

'''22.write a program to fetch all  non-palendram words from  lst?
names=['madam','python','dad','language','eye','malayalam']
list = [x for x in names if x[0] != x[-1]]
print(list)'''

'''23.write a program to fetch all  palendram words which starts with 'm' charector?
names=['madam','python','dad','language','eye','malayalam']
list = [x for x in names if x[0]==x[-1] if x[0] == "m"]
print(list)'''

'''24.write a program to fetch all  palendram words which more then 3 charectors?
names=['madam','python','dad','language','eye','malayalam']
list = [x for x in names if x[0]==x[-1] if len(x) > 3]
print(list)'''

'''25.write a program to fetch longest  palendram word
names=['madam','python','dad','language','eye','malayalam','narayaayaran']
list = [x for x in names if x[0]==x[-1]]
word = " "
for x in list:
    if len(word) < len(x):
        word = x
print(word)'''

