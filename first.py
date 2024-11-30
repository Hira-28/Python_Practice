def process_words():
   list1=input("enter list of words with 5 character:").split()
   list2=[]
   for i in list1:
      if len(i)>=5:
         list2.append(i)
   print(list2)

   vowels="aeiouAEIOU"
   numOfVowels=[]
   numOfCons=[]
   vowelCount=0
   consCount=0
   for x in list2:
      print(x)
      for y in x:
         print(y)
         if y in vowels:
            vowelCount+=1
            numOfVowels.append(vowelCount)
         else:
            consCount+=1
            numOfCons.append(consCount)
   print(numOfVowels) 
   print(numOfCons)   

process_words()
