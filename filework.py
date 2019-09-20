with open('referat.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    words = content.split()
    lencontent = len(content)
    lenwords = len(words)
    newcontent = content.replace('.',"!")
    print(lencontent)
    print(lenwords)
    
with open('referat2.txt', 'w', encoding='utf-8') as newfile:
    newfile.write(newcontent)
    