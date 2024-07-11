import sys
import time

def quiz_game():
    name = input("Enter your name: ")
    print("Hello " + name)
    text = ("Welcome to the game!").center(50)
    print(text)

    # Ten languages which user can select to play quiz on that language
    languages = ["Python", "Java", "C++", "C", "JavaScript", "Ruby", "PHP", "HTML", "CSS", "SQL"]

    print("Select the language you want to play quiz on it.")
    for i in range(0, len(languages), 2):
        print(f"{i + 1}. {languages[i]}", end="")
        if i + 1 < len(languages):
            print(f"   {i + 2}. {languages[i + 1]}")

    try:
        lang = int(input("Select the language you want to play quiz on it: "))
        sel_lang = languages[lang - 1]
        print(f"Your selected language is {sel_lang}")

        # Import quiz questions based on selected language
        if sel_lang.lower() == "python":
            from python import python as quiz
        elif sel_lang.lower() == "java":
            from java import java as quiz
        elif sel_lang.lower() == "c++":
            from cpp import cpp as quiz
        elif sel_lang.lower() == "c":
            from c import c as quiz
        elif sel_lang.lower() == "javascript":
            from javascript import javascript as quiz
        elif sel_lang.lower() == "ruby":
            from ruby import ruby as quiz
        elif sel_lang.lower() == "php":
            from php import php as quiz
        elif sel_lang.lower() == "html":
            from html import html as quiz
        elif sel_lang.lower() == "css":
            from css import css as quiz
        elif sel_lang.lower() == "sql":
            from sql import sql as quiz
        else:
            print("Sorry, the selected language is not supported.")
            sys.exit()

        # Display quiz questions
        score = 0
        total_questions = len(quiz)

        for idx, question in enumerate(quiz, 1):
            print(f"\nQuestion {idx}: {question['question']}")
            print("Options:")
            for option, text in question['options'].items():
                print(f"   {option}. {text}")
            
            user_answer = input("Enter your answer (A/B/C/D): ").upper()

            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}.")

            # Adding a small delay to allow the message to be displayed before proceeding
            time.sleep(0.5)

        # Print total score
        print(f"\n{name}, your total score is {score}/{total_questions}. Well done!")
        # Wait for a few seconds before closing the command prompt window
        print("Closing in 5 seconds...")
        time.sleep(5)
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Invalid selection. Please select a number within the given range.")
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the quiz game function to start the quiz
quiz_game()
