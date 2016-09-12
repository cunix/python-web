#coding:utf-8

#1:
# print "hello \n world"
# print """hello "world''"asdasd"""
# # \n 回车换行
# # \t 制表符
# # \" 双引号
# # \' 单引号
# # \\ 输出斜杠
# print r"hello \r \t \\ world "#不转移字符串中的\

#2:
#2.1: string index
# str="https://www.google.com"
# print str[4]
#2.2:string slice
# print "12-18:",str[12:18]
# print "-17:",str[:17]
# print "8-:",str[8:]
# print "ALL:"str[:]
# print "3 STEP:",str[::3]
# print "len(str)-1:",str[-1]
# print str[-15:-1]
# print str[-5]
# print str[10:-13]

#3:
# s1="hello"
# s2="world"
# print s1+s2
# print s1*3
# print "h" in s1
# print "h" not in s1

#4：
# str="www.google.com"*3
# print str.index("world")
# print str.index("cell")#找不到报错
# print str.find("cell")  #找不到不报错
# print str.replace("he","",1)
# print str.count("he")
# print str.split()

# n=str.count("google")
# print n
# i=0
# pos=-1
# print str
# while i<n:
#     pos=str.index("google",pos+1)
#     print "find google in str",pos
#     i+=1
#
# print str.replace("google","GOOGLE",str.count("google"))



s ="11abc22abc33abc44abc55"
print s.replace("abc","ABC",s.count("abc"))
pos=-1
while s.find("abc")!=-1:
    pos=s.find("abc",pos+1)
    s=s[:pos]+"ABC"+s[pos+3:]
print s




