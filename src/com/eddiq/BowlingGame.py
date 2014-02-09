'''
Created on 8 Feb, 2014

@author: Nephilim Faustus
'''
from com.eddiq.Frame import Frame

class BowlingGame:
    FRAMES = 10
    
    def __init__(self):
        self.frames = []
        self.currentFrame = None
    
    def addScore(self, score):
        # 2nd turn of current frame
        if self.currentFrame is not None and not self.currentFrame.isClosed():
            self.currentFrame.addScore(score)
            return
        
        # Create new frame
        newFrame = Frame()
        if self.currentFrame is not None:
            self.currentFrame.nextFrame = newFrame
        self.currentFrame = newFrame
        self.currentFrame.addScore(score)
        self.frames.append(self.currentFrame)
    
    def printScores(self):
        finalScore = 0
        
        for i in xrange(min(len(self.frames), BowlingGame.FRAMES)):    
            frame = self.frames[i]
            finalScore += frame.getScore()
            print "%d) %s" % (i + 1, frame.toString(i + 1 == BowlingGame.FRAMES))
            
        print "Final score is: %d" % finalScore
        
# From this point onwards, main procedure and test code

# All strikes
def tc1_allStrikes():
    bowlingGame = BowlingGame()

    # 1
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 2
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 3
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 4
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 5
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 6
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 7
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 8
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 9
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 10
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    # 11
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    #12
    bowlingGame.addScore(10)
    # bowlingGame.addScore(0)
    
    bowlingGame.printScores()
    
# 9,0 for all frames
def tc2_9nils():
    bowlingGame = BowlingGame()

    # 1
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 2
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 3
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 4
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 5
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 6
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 7
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 8
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 9
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    # 10
    bowlingGame.addScore(9)
    bowlingGame.addScore(0)
    
    bowlingGame.printScores()
    
# 5 for all attempts, including bonus
def tc3_all5s():
    bowlingGame = BowlingGame()

    # 1
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 2
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 3
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 4
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 5
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 6
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 7
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 8
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 9
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 10
    bowlingGame.addScore(5)
    bowlingGame.addScore(5)
    
    # 11
    bowlingGame.addScore(5)
    
    bowlingGame.printScores()

# Main procedure here
if __name__ == '__main__':
    tc1_allStrikes()
    tc2_9nils()
    tc3_all5s()
