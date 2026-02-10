#Name:Adithi Mahendran
#USN:1RUA25BCA0005
def wordcnt(text):
    count=1
    for i in text:
        if i==' ':
            count+=1
    return count
text=input("enter a sentence:")
print("word count=",wordcnt(text))
