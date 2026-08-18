# ---------------------------------------------------------
#              BUDDY CHATBOT 🤖
#        A Simple Rule-Based AI Chatbot
# ---------------------------------------------------------

# Display welcome messages when the chatbot starts
print("Namste! welcome toc chatbot")
print("i am your BUDDY Chat_bot Click Bye for Exit")


# Dictionary containing user questions and chatbot responses
respone = {

    # Response for greeting
    "hello": 'HI, Welcome  How can i help you',

    # Response when the user asks about the chatbot's health
    "how are you": "I Am Very Fine Thank You",

    # Response when the user asks about the chatbot's identity
    "who are you": "I Am Your Smart Ai Chat Bot",

    # Motivational response
    "motivate me ": "Be focused on your goals",

    # Response when the user says they are happy
    "happy": "Great to hear that"

}


# This function checks the user's question
# and returns the matching chatbot response
def getresponce_bot(user_question):

    # Convert the user's question into lowercase
    # so that uppercase and lowercase letters don't matter
    user_question = user_question.lower()

    # Check every keyword stored in the response dictionary
    for eachkey in respone:

        # Check whether the keyword exists
        # inside the user's question
        if eachkey in user_question:

            # Return the response connected to that keyword
            return respone[eachkey]

    # Default response when no keyword is matched
    return 'I AM NOT ABLE TO TELL THAT YET I WILL LERN SOON'


# Keep the chatbot running continuously
# until the user enters "bye"
while True:

    # Take a question from the user
    user_input = input("Entre youre question :")

    # Send the user's question to the chatbot function
    reply = getresponce_bot(user_input)

    # Display the chatbot's response
    print("bot responce", reply)


    # Check if the user wants to exit the chatbot
    if "bye" in user_input.lower():

        # Display goodbye message
        print("Thanks for using me, see you soon")

        # Stop the while loop and exit the chatbot
        break