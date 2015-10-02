import random
import os
import sys
from questions import question_links

def ask(question_link):
    answer = raw_input("Do you want to open -:\n" + question_link + "\n(y/n/e) ").lower()
    if answer == 'e':
        # Exit the program
        sys.exit(0)
    if answer == 'y':
        os.system('xdg-open ' + question_link)
        answer = raw_input("Was this important? (y/n) ").lower()
        return answer == 'y'
	return False

def start_test(question_links):
	for question_link in question_links:
	    if not ask(question_link):
			question_links.remove(question_link)

def main():
    try:
        random.shuffle(question_links)
        while question_links:
            start_test(question_links)
        print "List of questions exhausted!!"
    except Exception as exception:
        print "Error : {exception}".format(exception=exception.message)

if __name__ == '__main__':
    main()
