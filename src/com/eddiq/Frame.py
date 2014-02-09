'''
Created on 8 Feb, 2014

@author: Nephilim Faustus
'''

class Frame:
    STRIKE = 10
    
    def __init__(self):
        self.scores = []
        self.nextFrame = None
        self.closed = False

    def addScore(self, score):
        if len(self.scores) >= 2:
            return False
        
        self.scores.append(score)
        return True
        
    def isClosed(self):
        return len(self.scores) >= 2 \
            or self.getScoreForBothTries() >= Frame.STRIKE
    
    def getScoreForFirstTry(self):
        if (len(self.scores) < 1):
            return 0
        return min(self.scores[0], Frame.STRIKE)
    
    def getScoreForSecondTry(self):
        if (len(self.scores) < 2):
            return 0
        return min(self.scores[1], Frame.STRIKE)
    
    def getScoreForBothTries(self):
        return min(self.getScoreForFirstTry() + self.getScoreForSecondTry(), Frame.STRIKE)
    
    def getScore(self):
        bothTries = self.getScoreForBothTries()
        if (self.nextFrame == None or bothTries < Frame.STRIKE):
            return bothTries
        # Check for strike
        firstTry = self.getScoreForFirstTry()
        if firstTry == Frame.STRIKE:
            if self.nextFrame is None:
                return bothTries

            nextFrameFirstTry = self.nextFrame.getScoreForFirstTry()
            score = bothTries + nextFrameFirstTry
            
            twoFramesForward = self.nextFrame.nextFrame
            if nextFrameFirstTry < Frame.STRIKE:
                score += self.nextFrame.getScoreForSecondTry()
            elif twoFramesForward is not None:
                score += self.nextFrame.nextFrame.getScoreForFirstTry()
            return score
        # It's a spare
        return bothTries + self.nextFrame.getScoreForFirstTry()
    
    def toString(self, showAllFrames = False):
        if showAllFrames and self.nextFrame is not None:
            return "%d,%d, [%s] (%d)" % (self.getScoreForFirstTry(),
                                   self.getScoreForSecondTry(),
                                   self.nextFrame.toString(showAllFrames),
                                   self.getScore())
        else:
            return "%d,%d (%d)" % (self.getScoreForFirstTry(),
                                   self.getScoreForSecondTry(),
                                   self.getScore())
