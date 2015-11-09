# coding:utf-8

# count words
read_me = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

chars_dict = {}

for s in read_me:
    if s in chars_dict:
        chars_dict[s] += 1
    else:
        chars_dict[s] = 1

print chars_dict

for k in chars_dict:
    print "%s counts: %d" %(k, chars_dict[k])


## 

# words_list = read_me.split()
# # print words_list

# words_dict = {}

# for s in words_list:
#     if s in words_dict:
#         words_dict[s] += 1
#     else:
#         words_dict[s] = 1

# print words_dict

# for k in words_dict:
#     print "%s counts: %d" %(k, words_dict[k])


'''
1. 字符串单词反转
I am subin
I ma nibus

边际(455471484)  14:51:28
string = 'I am subin'
new_string = ''
for i in string.split():
    temp = list(i)
    for j in xrange(len(temp)):
        temp.insert(j,temp.pop())
    a = ''.join(temp)
    new_string += a

print new_string
没空格。。
akuanRunning(285111305)  14:52:08
我看明白了

akuanRunning(285111305)  14:53:11

2. 再想想另外一种反转方式
I am subin
subin am I
'''

text_str = "I am subin"
text_list = text_str.split(' ')

for i in xrange(len(text_list)):
    word_list = list(text_list[i])
    word_list.reverse()
    # print word_list
    text_list[i] = ''.join(word_list)

# print text_list
text2_str = ' '.join(text_list)
print text2_str

