# Anagram

The objective of this framework is to implement the algorithm to find the anagram of a given word in provided dictionary of words.

## Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Workflow](#Workflow)
   - [Cloning the module](#Cloning-the-module)
   - [Executing the Utility](#Executing-the-Utility)
   - [Executing Unittest cases](#Executing-Unittest-cases)
3. [Algorithm behind the scenes](#Algorithm-behind-the-scenes)
4. [Time required](#Time-required)
5. [Disclaimer](#Disclaimer)

## Prerequisites
In order to run this utility, we require:
 - Python 3.6.8 +
 - git installed 
 
## Workflow
### Cloning the module
- To get this utility on your machine, use following command on terminal 
  
  *git clone https://github.com/HelloWorld-123/anagram.git*

### Executing the Utility
- Save the dictionary file (should be in .txt format) in the /anagram directory. Make sure it is in the same folder as find_anagrams.py.
- Execute the command 
- make sure you are running python 3 
  *python find_anagrams.py < filename >.txt*
  
 ![image](https://user-images.githubusercontent.com/31774787/91685526-36420a80-eb20-11ea-9b46-d5161c6f5d16.png)
 
- Provide the word for which we want to find anagrams in the dictionary.
- Provide 'exit' as input to terminate the program.
  
### Executing Unittest cases
- For executing unittest cases, run command
*pytest unit_tests/*

## Algorithm behind the scenes
- Algorithm creates a hashmap with sorted string as key and all the words made up from those letters in the form of list as its value.
- hashmap is quick to access the list of anagrams, having complexity of O(1). 
- But overall Complexity of program is O(n) as creating hashmap needs to loop through all the words in input file. 

## Time required
- Time required to complete this project was 4-6 hours.

## Disclaimer
- This project is created by Arpit Saxena.
- For any queries, please contact arpitsaxena239@gmail.com.
