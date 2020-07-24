#!/usr/bin/python3

#from hands import Hand

import random

class Hand:
    def __init__(self,lst):
        self.lst = lst
        
    def __str__(self):
        #each item will be either a string or a Hand. nothing else
        out=[]
        for item in self.lst:
            out.append(str(item))

            ''' #was going to have melds within Hand class
            #decided to have faceup and facedown be Hands within Player class
            #in any case this if statement did nothing
            if isinstance(item, Hand):
                out.append(str(item))
            else:
                out.append(str(item))
            '''
        
        return 'melds:' + '\n'+ 'cards:' + '  '.join(out) + '\nindcs:' + ''.join([str(i).zfill(2)+' ' for i in range(len(self.lst))])
     #   return str(self.lst)


    def __getitem__(self, N):
        return self.lst[N]
    
    def __len__(self):
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


    def order(self,perm):#permutation
        try:
            #print([i for i in range(len(self.lst))])
            assert sorted(perm) == [i for i in range(len(self.lst))]
            self.lst = [self.lst[perm[i]] for i in range(len(self.lst))]
        except:
            print('invalid permutation.')

    def add_space(self,N):
        out = []
        for i in range(len(self.lst)):
            if i==N:
                out.append('_')
            out.append(self.lst[i])            
        self.lst=out

    def remove_space(self,N):
        try:
            assert self.lst[N] == '_'
            self.lst = self.lst[:N] + self.lst[N+1:]
        except:
            print('cannot remove; item is not a space')

    def add_card(self, card):
        self.lst.append(card)

    def remove_card(self, N):
        try:
            assert self.lst[N] != '_'
            out=self.lst[N]
            self.lst = self.lst[:N] + self.lst[N+1:]
            return out
        except:
            print('remove space with remove_space; also make sure index is in range')




spade = "\u2660"
heart = "\u2665"
diamond = "\u2666"
club = "\u2663"

all_cards=['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂼', '🂽', '🂾', '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂬', '🂭', '🂮', '🃁','🃂,', '🃃','🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃌', '🃍', '🃎', '🃑', '🃒', '🃓', '🃔','🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃜', '🃝','🃞 ']


class Player():
    def __init__(self, public, private): #lists
        self.public = Hand(public)
        self.private = Hand(private)
               

    def __str__(self):
        return '-----------------------------\n'+'HAND:\n'+str(self.private)+'\n-----------------------------\nTABLE:\n'+str(self.public)

    def public(self):
        return self.public
    
    def private(self):
        return self.private
    
    def lay_down(self, indices, down=True):#list of indices
        #down=True --> facedown->faceup
        #down=False--> faceup->facedown
        try:
            #reverse indices
            pop_list=sorted(indices)[::-1]
            #print(pop_list)
            if down==True:
                for ind in pop_list:
                    card = self.private[ind]
                    self.private.remove_card(ind)
                    self.public.add_card(card)
            else:
                for ind in pop_list:
                    card = self.public[ind]
                    self.public.remove_card(ind)
                    self.private.add_card(card)
        except:
            print('fail')
                


class Deck:
    def __init__(self, num_decks=1):
        try:
            assert num_decks in [1,2]
        except:
            print("only 1 or 2 decks please")


        self.deck = all_cards*num_decks
        self.discard = []

    def __str__(self):
        if len(self.deck)>0:
            if len(self.discard)>0:
                return '🂠 '+self.discard[-1]
            else:
                return '🂠 '
        else:
            if len(self.discard)>0:
                return '🂠 '+self.discard[-1]
            else:
                return ''
        
    def shuffle(self, option):
        if option==1:
            self.deck = self.deck+self.discard
            self.discard=[]
            random.shuffle(self.deck)
        elif option==2:
            random.shuffle(self.deck)

    def add_to_discard(self, card):
        self.discard = self.discard + [card]

    def draw(self, which_pile):
        if which_pile.lower() == 'deck':
            d = self.deck
        elif which_pile.lower() == 'discard':
            d = self.discard
        else:
            print('can only draw from deck or discard')

        if len(d) > 0:
            return d.pop()
        else:
            print('len=0')
    
#class Game(num_players, num_decks, num_cards):
    

#deck and discard are lists treated as stacks; that is, until deck runs out, at which point discard is shuffled and turned into deck
#add a messenger for bets
#make a robot dealer: human dealer is not necessary, is it?
#server host can be robot dealer and clients can use a restricted set of commands; and only see certain things
#host/dealer will have all information (I think this is necessary) so theoretically possible to cheat a game if hosting

#copy-paste some rules for standard games, etc., e.g. poker hand values, and have it as a help command

        
    
            
if __name__=="__main__":
    test1=False
    test2=False
    test3=True
    test4=False
    
    
    if test1==True:
        #dumb tests
        #x = Hand(['ah', 'jh', Hand(['kh', 'qh'])])
        x=Hand([c[9],c[10],c[11],c[9],c[10],c[11],c[9],c[10],c[11],c[9],c[10],c[11],c[9],c[10],c[11],c[12]])
        print(x)
        #x.swap(1,3)
        #print(x)
        #x.move_before(3,1)
        x.move_before(1,3)
        print(x)
        x.add_space(5)
        print(x)
        x.remove_space(6)
        print(x)
        x.remove_space(5)
        print(x)

    if test2==True:
        x = Hand([2,3,4,5,6,7,8])
        print(x)
        x.order([2,0,1])
        print(x)
        print('x[2]=',x[2])

    if test3==True:
        x = Hand([2,3,4,5,6,7,8])
        Adrian = Player(x, [])
        print(Adrian)
        Adrian.lay_down([0,3])
        print(Adrian)
        Adrian.lay_down([0,1], False)
        print(Adrian)
        Adrian.private.add_space(3)
        print(Adrian)


    if test4==True:
        a=Deck()
        print(a)
        x=a.draw('deck')
        #print(x)
        a.add_to_discard(x)
        print(a)
    
        x=a.draw('deck')
        #print(x)
        a.add_to_discard(x)
        print(a)
    
        a.shuffle(2)
        print(a)
    
        x=a.draw('deck')
        #print(x)
        a.add_to_discard(x)
        print(a)
    
        a.shuffle(1)
        print(a)
    
        x=a.draw('deck')
        #print(x)
        a.add_to_discard(x)
        print(a)


'''

[Decided against] put card N after card M
[DONE] put card N before card M
[DONE] swap cards N and M
[DONE] order cards ABCDEF as DEACBF or anything
meld: make a group of cards (remove cards and make a meld object which is then put in the list)

'''
