"""You would like to set a password for a bank account. However, there are three
restrictions on the format of the password:

It has to contain only alphanumeric characters (a−z, A−Z, 0−9);

There should be an even number of letters;

There should be an odd number of digits.

You are given a string S consisting of N characters. String S can be divided into words
by splitting it at, and removing, the spaces. The goal is to choose the longest word that is
a valid password. You can assume that if there are K spaces in string S then there are
exactly K + 1 words.
For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them
are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007"
and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is
not an alphanumerical character and "test" contains an even number of digits (zero).
Write a function:
def solution(S)
that, given a non-empty string S consisting of N characters, returns the length of the
longest word from the string that is a valid password. If there is no such word, your
function should return −1.
For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as
explained above.
Assume that:
N is an integer within the range [1..200];
string S consists only of printable ASCII characters and spaces."""

class Password():

    #Count number of alphabets in string
    def count_letter(self,S):
        count=0
        for i in S:
            if i.isalpha():
                count+=1
        return count

    #Count number of digits in string
    def count_digit(self,S):
        count=0
        for i in S:
            if i.isnumeric():
                count+=1
        return count


    def solution(self,S):
        longest_word_length = -1
        for i in S:
            """ To check if the string is alphanumeric """
            if i.isalnum():
                if self.count_letter(i)%2==0 and self.count_digit(i)%2 !=0:
                    longest_word_length = max(len(i), longest_word_length)
        return longest_word_length


if __name__ == '__main__':
    S = list(map(str,input().split())) #S = "test 5 a0A pass007 ?xy1"
    P=Password()
    print(P.solution(S)) #7