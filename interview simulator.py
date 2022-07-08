### create a function that  runs sections of each story
### use binary tree or liked list to move from function to function
### game is about hiring me, make myself seem charming, 
### make another interview to conatrast me against?
import sys
import time
def print(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/500)
class node():
    def __init__(self, val, left=None , right=None):
        self.val=val
        self.left=left
        self.right=right
    def run(self, arg):
        self.val(arg)
def start(node: node):
    
    print('\n\n\nCongrats! You area hiring manager at a successful company!\nYou find yourself today looking through a stack of resumes when you come accross a particular Christian Trujillo' )
    print('Hes had some experience in the field although he is admittedly newer to programming, what do you do?\n')
    while True:    
        path=input("1: I want to check him out, He looks like he's got potential!\n\n2: I don't care about self taught progammers, all I care about is formal education.\n\n")
        if path=='1':
            node=node.right
            node.run(node)
            break

        elif path=='2':  
            node=node.left
            node.run(node)
            break
        else: print('\n please enter one of the given options:\n\n')
def Interview(node: node):
    print('\n\n\nyou give Christian Trujillo a call and hes excited to work for your company, he sounds pretty confident over the phone.' )
    print('during his interview, he demonstrates an understanding of computer science concepts, mathematical prowess and a willingness to learn.')
    print('after your interview with him goes fantasically, you ask what you always ask:\n\t"Do you have any questions for me?"\n\n\t "Why yes actaully I do." he says "as you well know I am self taught, and that comes with its own distinct advantages and disadvantages, while I am well learned and excited for new opportunities, I always will have room to grow. I appreciate the opportunity to learn, and thrive in working environments that promote learning on the job and guidance by supervisors, would you say this describes your workplace?"\n')
    while True:    

        path=input("1: That accurately describes us here. We can appreciate when a new worker can admit that they do not know everything, and are willing to empart our knowledge to them to help them grow in this ever expanding field\n\n2: No, that does not sound like us. If you want to work here, we expect that you will not learn anything while you are here, your training will be minimal and afterword we expect that you do not ask anything of your supervisors.\n\n")
        if path=='1':
            node=node.right
            node.run(node)
            break

        elif path=='2':  
            node=node.left
            node.run(node)
            break
        else: print('\n please enter one of the given options:\n\n')

def interview_2(node: node):
    print('\t"That is fantastic to hear, I do have 1 other question, and it relates to my previous question."Christian Trujillo asks, "I have ADHD, which is quite misunderstood by most')
    print('I do not have a short attention span or have trouble doing simple tasks, but I do require a certain mount of interest in what Im doing to continue at a good pace, thats why I thrive in an environment where I am able to learn, because to me, learning is fun, no matter what it is I am learning about')
    print('so my question is, is your company willing to make, admittedly minor, accomodations to allow me to work at my full potential for you? these would include:\n being able to choose when I take my breaks, to not disrupt my thought flow\n allowing me to keep atleast 1 headphone in while working, to regulate the amount of white noise I hear\n and simply dealing with the fact that when I learn new concept, I like to learn it inside and out, and get to know every detail about it, so sometimes I will ask a tedious amount of questions\n')
    while True:    

        path=input("1. Of course we can accomodate here! Not only are your requests minimal, but you seem to have quite a grasp on what you need in order to work optimally. Its refreshing that you know what works for you and use that knowledge to your advantage!\n\n2: No. We do not make accomodations for disabilities at this company, no matter how small the request. We would rather give our workers less to work with and get less productivity out of them than to start allowing them what they need to function properly.\n also the mention of ADHD scares me, and although I dont know anything about the subject, I wil assume it means you are less intelligent even though many with ADHD are labeled as 'gifted children' in their school years\n\n")
        if path=='1':
            node=node.right
            node.run(node)
            break

        elif path=='2':  
            node=node.left
            node.run(node)
            break
        else: print('\n please enter one of the given options:\n\n')


def win(node: node):
    print('You decide to hireChristian Trujillo!')
    print("In the first few days, he asks more questions than nearly anyone else ever has since you've been with this company. Though it clearly isnt because He doesnt understand, but rather because he yearns to have a solid understanding of how your company works and what he can do to help.")
    print("When he mentioned having ADHD, you thought he would likely have the attention span of a squirrel, but instead you've noticed that he actually tends to hyper-focus on his work, letting it be literally the only he thinks about for hours at a time. That must be why he takes his breaks only after a section of a project is finished, so that he doesnt lose his pace like he mentioned")
    print("during the short time he's been working for you, he has easily been the fastest growing assocaite in your company, willing to take larger and ever increasingly important workloads, and doesnt seem to buckle under stress. its almost like he thrives when he has more to do. He is by far the best employee you've ever havd and maybe ever will.")
    print("After getting a bonus from your boss for hiring the best worker on the face our our green planet, you decide to buy a lottery ticket for fun, after scratching off the section for the $1,000,000 grand prize you see in clear block text:")
    print("You Win!")
def lose(node: node):
    print('You decide not to hire Christian Trujillo\nand continue searching until you find someone with a formal education, after a short interview you decide to hire!')
    print('With his new computer science degree, shortly after hiring him you come to the realization that he has not retained anything from university! 😦')
    print('your new hire costs the company thousands to train without ever getting a payoff since he quit when he realized the position was too difficult.')
    print('You are fired from your position for choosing literally the worst employee you could, walking home now jobless, you buy a lottery ticket from the gas station. After scratching of the last corner, in clear block text you read:')
    print('You Lose! 😂😂🤣')

main=node(start)
main.left=node(lose)
main.right=node(Interview, node(lose), node(interview_2, node(lose), node(win)))
main.run(main)
print("\n\nIf I have come on too strong in this, please give me feedback, while this is only a silly game, I'm sure it does affect your likelihood of hiring me in one respect or another. any feedback is appreciated!")
time.sleep(300)
