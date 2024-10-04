#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm BreachBot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the National Health Services Breach!")

#Introduces Breach
print("Would you like to learn about the National Health Services Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains Breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your refelection")
  topic = input()
  
  if topic.lower() == "a":
    print("On May 12th, 2017, over 16 hospitals in the UK were shut down due to the breach. The culprit was a ransomware strain known as 'Wanna Decryptor'. It froze computers, giving a demand of $300 worth of bitcoins. While operations at hospitals were affected, it was believed no patient information was leaked.")
  
  elif topic.lower() == "b":
    print("The service responded by saying they were focusing on supporting affected organizations to manage the situation quickly. It was found that the outdated IT systems were the cause, and the NHS increased their investment in cybersecurity after the incident.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my Take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my Take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, (d) none")
  topic = input()

  if topic.lower() == "a":
    print("Confidentiality is when certain pieces of information is disclosed to authorized people. In this ransomware attack, the hackers encrypted the data, essentially making it inaccessible. This was a breach of confidentiality because the authorized users were denied access.")

  elif topic.lower() == "b":
    print("I agree with the National Health Service's response. They identified the issue and are investing money in order to rectify it.")

  elif topic.lower() == "c":
    print("I would convince victims to take action by shutting off the device and isolating it from any networks. In the case of an attack, make sure to alert the necessary authorities. In order to prevent the loss of any data, I would reccommend regularly backing up your computer.")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")