# coding:utf-8

# name: homework01_count&sort.py
# function: 统计字符数量并打印出现次数前10的字符

# count words
read_me = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

chars_dict = {}

for s in read_me:
    if s in chars_dict:
        chars_dict[s] += 1
    else:
        chars_dict[s] = 1

# print chars_dict

# for k in chars_dict:
#     print "%s counts: %d" %(k, chars_dict[k])

sorted_list = []

# print len(chars_dict)

# for k,v in chars_dict.items():
#     print k, v

for k,v in chars_dict.items():
    if len(sorted_list) == 0:
        sorted_list.append(k)
    else:
        for j in range(len(sorted_list)):
            if v <= chars_dict[sorted_list[j]]:
                sorted_list.insert(j, k)
                break
            elif j == len(sorted_list) - 1:
                sorted_list.insert(j+1, k)
                break

# print sorted_list

# for i in sorted_list:
#     print i, chars_dict[i]

# print "The most 10 chars: ", ', '.join(sorted_list[-1:-11:-1])
print "The most 10 chars: ", sorted_list[-1:-11:-1]

