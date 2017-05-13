import getTweets, createTestSet, svmImplementation
import sys

if __name__ == '__main__':
    # userName = sys.argv[1]
    userName = 'TheEllenShow'
    getTweets.getTweets(userName)
    createTestSet.createTestSet(userName)
    svmImplementation.svmImplementation(userName)