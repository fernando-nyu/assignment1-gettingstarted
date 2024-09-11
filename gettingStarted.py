### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    cases = {
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": "pcap",
        "Are encoding and encryption the same? - Yes/No": "No",
        "Is it possible to decrypt a message without a key? - Yes/No": "No",
        "Is it possible to decode a message without a key? - Yes/No" : "Yes",
        "Is a hashed message supposed to be un-hashed? - Yes/No": "No",
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - ": "7c553fe0663bfe748cf99685d577034519a6913e215abcd57cc2bf6928f9c485",
        "Is MD5 a secured hashing algorithm? - Yes/No": "No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": 5,
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 3
    }
    return cases.get(question, "Question not found.")
# Complete all the questions.

if __name__ == "__main__":
    debug_question = "test"
    print(welcome_assignment_answers(debug_question))