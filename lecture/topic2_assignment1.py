'''
Write a function get_test_scores()
Create an empty dictionary scores_dict = dict()
Prompt the user to input the number of test scores, store in num_scores
Write a loop to get each of the num_scores test scores
Prompt the user to input each test score and store in score. (Validate the input!)
Add score to scores_dict  # HINT: update the dictionary

Write a second function average_scores() that accepts the dictionary as the only parameter and returns the average scores
Use len() to determine your num_scores for calculation
Note a dictionary is a set of key, value pairs.
You can get the keys with .keys() function
You can access the value using a key variable scores_dict.get(k)
What about testing?
Write a main to test your functions
Unit Tests can also help test average_scores()
'''

def get_test_scores():
    scores_dict = dict()
    #Prompt the user to input the number of test scores, store in num_scores
    num_scores = 6 #as an example, 6 test scores
    #loop...ask for num_scores test scores
        #in example case, ask 6 times
    #store in dictionary, such as {'Score1':98, ...etc}

def average_scores(a_dict):
    #calculate an average
    #HINT: might be able to copy/paste some of your code from before

#main or drver code
if __name__ == '__main__':
    pass
