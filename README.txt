# Wordle_Solver
Bryan Wang
2/7/2022

A quick program I made to solve Wordles inspired by getting creamed by my sister

1) Goal
    - Create a program to cheat and win

2) Idea
    - General overview is create a python solver for the game Wordle
      using information theory on word/letter frequency and code

3) Example Usage
    - Because we don't want to have to enter the hidden word into the script
      and THEN start playing the game on our script, it will require the user
      to enter the outputs of the script into wordle and the outputs of wordle
      back into the script.

    - EX: (Green / G = Correct letter and place  || Yellow / Y = Correct letter wrong place || Black = Both wrong)
        Script Output: Try "NAILS"

        User enters script recommendation

        Wordle Output: BGGGG

        User enters wordle output into script and script processes

        Script Output: Try "TAILS"
        ...

4) Architecture Ideas
    - There's gonna be a few components to the design of this solver
        a) The actual information theory and processing to make guesses based on current info
            - Strategy
                - Pick an initial word that has a wide range of letters to glean information
                - Using the knowledge that these letters are the most used, we can try a word from this combo
                        E – 11.1607%
                        A – 8.4966%
                        R – 7.5809%
                        I – 7.5448%
                        O – 7.1635%
                        T – 6.9509%
                        N – 6.6544%
                        S – 5.7351%
                - TEARS
                - Because TEARS uses extremely common letters, it can be both good and bad as a filtering tool because
                  on one hand, if we don't use alot of these letters, it shrinks the pool of possible words down significantly.
                  On the other hand, if we DO use alot of these letters, our pool of possilbe words isn't decreased too much.
                - Based on the result that we get, we can now start filtering out our word bank.

            - Data Structures:
                - Keep 4 data structures keeping track of...
                        - Letters In (dict)
                            - This will keep track of what letters are in the mystery word
                        - Letters In Order (array)
                            - This will keep track of what letters are confirmed at a certain spot in the word
                        - Letters not in (dict)
                            - This will keep track of what letters we know are NOT in the word at all
                        - letters definitely not in order (dict)
                            - This will keep track of what letters we know are NOT in certain spots in the word
                    - Hedge the solution space iteratively based on the information we gathered from the previous guesses

        b) The 5-letter word bank of possible guesses that abstracts what words a human might pull from
            - There are a couple possible ways we could store this or access this
                a) We could use a web-scraper and find a website with all 5 letter words and just read from there
                       Pro: No storage required
                       Con: The time it would take would most likely be slower than storing it b/c of network connection
                            and API requests, etc
                b) We could manually store all 5-letter words as a .txt file for easy access and just read it in as a
                   list.
                        Pro: Fast and easy to code
                        Con: Lots of storage

            - Final: Found a list of the most common 5 letter words in english from
              https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
              We can use this as our solution space to hedge with each guess.
