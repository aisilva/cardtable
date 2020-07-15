#!/usr/bin/python3
'''# -*- coding: utf-8 -*-'''

#from hands import Hand

spade = "\u2660"
heart = "\u2665"
diamond = "\u2666"
club = "\u2663"

#all_cards = ['🂱 ','🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾', '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫' ,'🂭', '🂮', '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎', '🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞']

#facedown='🂠 '

all_cards = [spade+'K', spade+'Q']
print(all_cards)

class Hand:
    def __init__(self,lst):
        self.lst = lst
        
    def __str__(self):
        return str([str(y) for y in self.lst])
    #return 'cards:' + str(self.lst) + '\nindcs:' + str([str(i)+' ' for i in range(len(self.lst))])
     #   return str(self.lst)

    def len(self):
        return len(self.lst)
    
    def swap(self, N,M):
        try:
            x = self.lst[N]
            y = self.lst[M]

            out=[]
            
            for i in range(len(self.lst)):
                if i==N:
                    out.append(y)
                elif i==M:
                    out.append(x)
                else:
                    out.append(self.lst[i])
            self.lst = out
            
        except:
            print('try again.')

    def move_before(self, N, M): #move card N to immediately before card M
        #to move to end do x.move_before(N, x.length)
        try:
            x = self.lst[N]
            out=[]
            for i in range(len(self.lst)):
            
                if i == N:
                    continue
                elif i == M:
                    out.append(x)
                    
                out.append(self.lst[i])
                

            if M == len(self.lst):
                out.append(x)
                
            self.lst=out
        except:
            print('try again.')


    def order(perm):#permutation
        pass
        

if __name__=="__main__":
    #dumb tests
    x = Hand(['ah', 'jh', Hand(['kh', 'qh'])])
    print(x)
    #x.swap(1,3)
    #print(x)
    #x.move_before(3,1)
    x.move_before(1,3)
    print(x)



'''

put card N after card M
put card N before card M
[DONE] swap cards N and M
order cards ABCDEF as DEACBF or anything
meld: make a group of cards (remove cards and make a meld object which is then put in the list)

'''









b='🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾 🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞 '



#, '🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂼', '🂽', '🂾', '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂬', '🂭', '🂮', '🃁','🃂,', '🃃','🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃌', '🃍', '🃎', '🃑', '🃒', '🃓', '🃔','🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃜', '🃝','🃞 ']


