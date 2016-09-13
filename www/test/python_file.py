# !-_- coding:utf-8 -_-!
"This is a practice about Python file operation"

#fn=open('shell.html','r')
# print "reading position:",fn.tell()
# fn.read(20)
# print "reading position:",fn.tell()
# fn.read(20)
# print "reading position:",fn.tell()
# fn.read(20)
# print "reading position:",fn.tell()

# fn=open('cool.html','w')
# fn.write("")
# i=0
# while i<10000:
#     fn.write("hello world !"+str(i)+"\n")
#     i+=1
# fn.close()

fn=open("shell.html")

print fn.readline().strip().strip('\n')
print fn.readline().strip().strip('\n')
print fn.readline().strip().strip('\n')
print fn.readline().strip().strip('\n')

# li=fn.readlines()
# for s in li:
#     print s



fn.close()





