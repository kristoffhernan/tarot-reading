print("Welcome to Hunkle's Tarot Crops! ")

print("What shall I call you, young traveler?")
name = input()
if name == "Kirei":
    print("Inputting cheat code... Processing files...")
    print("Cheat code activated.")
    print("Good Evening, Queen Kirei Goddess of Dragons. Happy early birthday pants. I hope you enjoy the reading ^_^")
else: 
    print("Good day, " + name + ".")

input("Press Enter to continue...")

while True:
    print("To learn more about Hunkle's Tarot Crops, type 'Learn more'")
    print("If you're rude and uninterested about your host, type 'Continue'")
    learn_more = input()

    if learn_more == "Learn more":
        print("Featured on Forbes, Science Magazine and The Real, Hunkle's Tarot Crops was named the BEST and most accurate readings of 2020.(He even predicted Grammy of the Year.) ")
        input("Press Enter to continue...")
        print("Hunkle's Tarot Crops has also dealt with clients including: Jay Z, Taylor Swift #GetSwifty, The Rock, Elon, and Kristoffer Hernandez. ")
        break

    if learn_more == "Continue":
        print("Too bad, I'll tell you anyways.")
        print("Featured on Forbes, Science Magazine and The Real, Hunkle's Tarot Crops was named the BEST and most accurate readings of 2020.(He even predicted Grammy of the Year.) ")
        input("Press Enter to continue...")
        print("Hunkle's Tarot Crops has also dealt with clients including, but not limited to: Jay Z, Taylor Swift #GetSwifty, The Rock, Elon, and Kristoffer Hernandez. ")
        break

input("Now we can get started. Press enter to continue...")
print("Tarot card reading is an exhilirating prediction of your future.")
input("Press Enter to continue...")
print("In this reading, I will give you three cards that you, yourself will choose at random.")
input("Press Enter to continue...")
print("The three cards you choose are said to be your set future, but in the end, only YOU are the real predicter of what your future holds.")
input("Press Enter to start the reading")

print(name + ", please think of a favorite memory, but don't say it outloud.")
input("Processing... Press Enter to continue...")
print( name + ", put your finger on the Enter bar, close your eyes and count to 5 before pressing it.")
input("Three tarot readings will show up, thus being your three predictions.")

import random
for i in range(3):
    random_number = random.randint(1,79)
   
    if random_number == 1:
        print("The Fool")
    elif random_number == 2:
        print("The Magician")
    elif random_number == 3:
        print("The High Priestess")
    elif random_number == 4:
        print("The Empress")
    elif random_number == 5:
        print("The Emperor")
    elif random_number == 6:
        print("The Hierophant")
    elif random_number == 7:
        print("The Lovers")
    elif random_number == 8:
        print("The Chariot")
    elif random_number == 9:
        print("Strength")
    elif random_number == 10:
        print("The Hermit")
    elif random_number == 11:
        print("The Wheel of Fortune ")
    elif random_number == 12:
        print("Justice")
    elif random_number == 13:
        print("The Hanged Man")
    elif random_number == 14:
        print("Death")
    elif random_number == 15:
        print("Temperance")
    elif random_number == 16:
        print("The Devil")
    elif random_number == 17:
        print("The Tower")
    elif random_number == 18:
        print("The Star")
    elif random_number == 19:
        print("The Moon")
    elif random_number == 20:
        print("The Sun")
    elif random_number == 21:
        print("Judgement or Rejuvination")
    elif random_number == 22:
        print("The World")
    elif random_number == 23:
        print("Ace of Wands")
    elif random_number == 24:
        print("Two of Wands")
    elif random_number == 25:
        print("Three of Wands")
    elif random_number == 26:
        print("Four of Wands")
    elif random_number == 27:
        print("Five of Wands")
    elif random_number == 28:
        print("Six of Wands")
    elif random_number == 29:
        print("Seven of Wands")
    elif random_number == 30:
        print("Eight of Wands")
    elif random_number == 31:
        print("Nine of Wands")
    elif random_number == 32:
        print("Ten of Wands	")
    elif random_number == 33:
        print("Page of Wands")
    elif random_number == 34:
        print("Knight of Wands")
    elif random_number == 35:
        print("Queen of Wands")
    elif random_number == 36:
        print("King of Wands")
    elif random_number == 37:
        print("Ace of Cups")
    elif random_number == 38:
        print("Two of Cups")
    elif random_number == 39:
        print("Three of Cups")
    elif random_number == 40:
        print("Four of Cups")
    elif random_number == 41:
        print("Five of Cups")
    elif random_number == 42:
        print("Six of Cups")
    elif random_number == 43:
        print("Seven of Cups")
    elif random_number == 44:
        print("Eight of Cups")
    elif random_number == 45:
        print("Nine of Cups")
    elif random_number == 46:
        print("Ten of Cups")
    elif random_number == 47:
        print("Page of Cups")
    elif random_number == 48:
        print("Knight of Cups")
    elif random_number == 49:
        print("Queen of Cups")
    elif random_number == 50:
        print("King of Cups")
    elif random_number == 51:
        print("Ace of Swords")
    elif random_number == 52:
        print("Two of Swords")
    elif random_number == 53:
        print("Three of Swords")
    elif random_number == 54:
        print("Four of Swords")
    elif random_number == 55:
        print("Five of Swords")
    elif random_number == 56:
        print("Six of Swords")
    elif random_number == 57:
        print("Seven of Swords")
    elif random_number == 58:
        print("Eight of Swords")
    elif random_number == 59:
        print("Nine of Swords")
    elif random_number == 60:
        print("Ten of Swords")
    elif random_number == 61:
        print("Page of Swords")
    elif random_number == 62:
        print("Knight of Swords")
    elif random_number == 63:
        print("Queen of Swords")
    elif random_number == 64:
        print("King of Swords")
    elif random_number == 65:
        print("Ace of Pentacles")
    elif random_number == 66:
        print("Two of Pentacles	")
    elif random_number == 67:
        print("Three of Pentacles")
    elif random_number == 68:
        print("Four of Pentacles")
    elif random_number == 69:
        print("Five of Pentacles")
    elif random_number == 70:
        print("Six of Pentacles")
    elif random_number == 71:
        print("Seven of Pentacles")
    elif random_number == 72:
        print("Eight of Pentacles")
    elif random_number == 73:
        print("Nine of Pentacles")
    elif random_number == 74:
        print("Ten of Pentacles")
    elif random_number == 75:
        print("Page of Pentacles")
    elif random_number == 76:
        print("Knight of Pentacles")
    elif random_number == 77:
        print("Queen of Pentacles")
    elif random_number == 78:
        print("King of Pentacles")

reading = random_number

while reading != "quit":
    print("To learn more about your readings, type the name of your card")
    print("If you would like to quit the game, type 'quit'")

    reading = input("What would you like to do? ")

    if reading == "The Fool":
        print("Upright: beginnings possibilities, pleasure, thoughtlessness, adventure, opportunity")
        print("Reverse: indecision, hesitation, injustice, apathy, bad choice")
    elif reading == "The Magician":
        print("Upright: creativity, self-confidence, dexterity, sleight of hand,will-power, skill")
        print("Reverse: delay, unimaginative, insecurity, lack of self-confidence")
    elif reading == "The High Priestess":
        print("Upright: knowledge, wisdom, learning, intuition, impatience, virtue, purity")
        print("Reverse: selfishness, shallowness, misunderstanding, ignorance")
    elif reading == "The Empress":
        print("Upright: development, accomplishment action, evolution")
        print("Reverse: inaction, lack on concentration, vacillation, anxiety, infidelity")
    elif reading == "The Emperor":
        print("Upright: authority, father-figure, structure, solid foundation")
        print("Reverse: domination, excessive control, rigidity, inflexibility")
    elif reading == "The Hierophant":
        print("Upright: mercy, conformity, forgiveness, social approval, bonded, inspiration")
        print("Reverse: vulnerability, unconventionality, foolish generosity, impotence, frailty, unorthodoxy")
    elif reading == "The Lovers":
        print("Upright: harmony, trust,romance, optimism, honor, love, harmony")
        print("Reverse: separation, frustration, unreliability,fickleness, untrustworthy")
    elif reading == "The Chariot":
        print("Upright: perseverance, rushed decision, turmoil, vengeance, adversity")
        print("Reverse: vanquishment, defeat, failure, unsuccessful")
    elif reading == "Strength":
        print("Upright: courage, conviction, strength, determination, action, heroism, virility")
        print("Reverse: pettiness, sickness, unfaithfulness, weakness")
    elif reading == "The Hermit":
        print("Upright: inner strength, prudence, withdrawal, caution, vigilance")
        print("Reverse: hastiness, rashness,immaturity, imprudence, foolishness")
    elif reading == "The Wheel of Fortune ":
        print("Upright: unexpected events, advancement, destiny, fortune, progress")
        print("Reverse: interruption, outside influences, failure, bad luck")
    elif reading == "Justic":
        print("Upright: equality, righteousness, virtue, honor, harmony, balance")
        print("Reverse: false accusation, unfairness, abuse, biased")
    elif reading == "The Hanged Man":
        print("change, reversal, boredom, improvement, rebirth, suspension, change")
        print("Reverse: false prophecy, useless sacrifice, unwillingness")
    elif reading == "Death":
        print("Upright: unexpected change, loss, failure, transformation, death, bad luck")
        print("Reverse: immobility, slow changes, cheating, death, stagnation")
    elif reading == "Temperance":
        print("Upright: temperance, patience, good influence, confidence, moderation	")
        print("Reverse: conflict, disunion, frustration, impatience, discord")
    elif reading == "The Devil":
        print("Upright: downfall, unexpected failure, controversy, ravage, disaster, ill tempered")
        print("Reverse: release, enlightenment, divorce, recovery")
    elif reading == "The Tower":
        print("Upright: disruption, abandonment, end of friendship, bankruptcy, downfall, unexpected events	")
        print("Reverse: entrapment, imprisonment, old ways, rustic")
    elif reading == "The Star":
        print("Upright: balance, pleasure, optimism, insight, spiritual love, hope, faith	")
        print("Reverse: disappointment, bad luck, imbalance, broken dreams")
    elif reading == "The Moon":
        print("Upright: double-dealing Deception, disillusionment, trickery, error, danger, disgrace")
        print("Reverse: trifling mistakes, deception discovered, negative advantage")
    elif reading == "The Sun":
        print("Upright: accomplishment, success, love, joy, happy marriage, satisfaction")
        print("Reverse: loneliness, canceled plans, unhappiness, break ups")
    elif reading== "Judgement of Rejuvination":
        print("Upright: awakening, renewal, rejuvenation, rebirth, improvement, promotion, atonement, judgment")
        print("Reverse: disappointment, indecision, death, failure, ill-health, theft, worry")
    elif reading == "The World":
        print("Upright: perfection, recognition, success, fulfillment, eternal life")
        print("lack of vision, disappointment, imperfection")
    elif reading == "Ace of Wands":
        print("Upright: profitable journey, new business, beginning, new career, birth, inheritance	")
        print("Reverse: selfishness, lack of determination, setback")
    elif reading == "Two of Wands":
        print("Upright: generous person, courage, patience, courage	")
        print("Reverse: impatience, domination")
    elif reading == "Three of Wands":
        print("Upright: cooperation, good partnership, success	")
        print("Reverse: carelessness, arrogance, pride, mistakes")
    elif reading == "Four of Wands":
        print("Upright: dissatisfaction, kindness, reevaluation	")
        print("Reverse: new relationship, new ambitions, action")
    elif reading == "Five of Wands":
        print("Upright: lawsuit or quarrel, courage, competition")
        print("Reverse: new opportunities, harmony, generosity")
    elif reading == "Six of Wands":
        print("Upright: leadership, good news, success")
        print("Reverse: postponement, bad news, pride in riches")
    elif reading == "Seven of Wands":
        print("Upright: stiff competition, victory, courage, energy")
        print("Reverse: advantage, patience, indecision")
    elif reading == "Eight of Wands":
        print("Upright: new ideas, love, journey")
        print("Reverse: violence, quarrels, courage")
    elif reading == "Nine of Wands":
        print("Upright: victory, good health, obstinacy")
        print("Reverse: weakness, ill-health, adversity")
    elif reading == "Ten of Wands":
        print("Upright: pain, ruined, failure")
        print("Reverse: cleverness, energy, strength")
    elif reading == "Page of Wands":
        print("Upright: enthusiasm, exploration, discovery, free spirit")
        print("Reverse: setbacks to new ideas, pessimism, lack of direction")
    elif reading == "Knight of Wands":
        print("Upright: generous, journey, impetuous")
        print("Reverse: suspicion, jealousy, narrow-mindedness")
    elif reading == "Queen of Wands":
        print("Upright: fondness, attraction, command")
        print("Reverse: jealous, revengeful, infidelity")
    elif reading == "King of Wands":
        print("Upright: passionate, good leader, noble")
        print("Reverse: unyielding, prejudice, quarrels")
    elif reading == "Ace of Cups":
        print("Upright: good health, love, joy, beauty")
        print("Reverse: egotism, selfishness, hesitancy")
    elif reading == "Two of Cups":
        print("Upright: romance, friendship, cooperation")
        print("Reverse: violent passion, misunderstanding")
    elif reading == "Three of Cups":
        print("Upright: fortune, hospitality, discovery")
        print("Reverse: hidden, overindulgence, pain, gossip")
    elif reading == "Four of Cups":
        print("Upright: dissatisfaction, kindness, reevaluation, redemption")
        print("Reverse: new goals, ambitions, beginning")
    elif reading == "Five of Cups":
        print("Upright: broken marriage,vain regret, sorrow, loss")
        print("Reverse: return, summon, hope")
    elif reading == "Six of Cups":
        print("Upright: acquaintance, good memories, acquaintance, happiness")
        print("Reverse: friendship, disappointment, past")
    elif reading == "Seven of Cups":
        print("Upright: imagination, illusion, directionless")
        print("Reverse: will-power, determination")
    elif reading == "Eight of Cups":
        print("Upright: disappointment, abandonment, misery")
        print("Reverse: pleasure, success, joy")
    elif reading == "Nine of Cups":
        print("Upright: physical well-being, hopes, security")
        print("Reverse: illness, failure, overindulgence")
    elif reading == "Ten of Cups":
        print("Upright: friendship, happiness, life")
        print("Reverse: waste, broken relationships, quarrel")
    elif reading == "Page of Cups":
        print("Upright: sweetness, interest in literature, gentleness")
        print("Reverse: poor imagination, selfishness, no desires")
    elif reading == "Knight of Cups":
        print("Upright: emotional, romantic dreamer, intelligence")
        print("Reverse: idleness, untruthful, fraud, sensuality")
    elif reading == "Queen of Cups":
        print("Upright: loving mother, gentle, happiness")
        print("Reverse: perverse, unhappy, gloom, over-active imagination")
    elif reading == "King of Cups":
        print("Upright: kindness, willingness, enjoyment")
        print("Reverse: double-dealer, scandal, crafty, violent")
    elif reading == "Ace of Swords":
        print("Upright: love, valiant, victory")
        print("Reverse: obstacles, tyranny, power")
    elif reading == "Two of Swords":
        print("Upright: indecision, trouble, balanced")
        print("Reverse: unscrupulous, release")
    elif reading == "Three of Swords":
        print("Upright: broken relationship, civil war")
        print("Reverse: sorrow, loss, confusion")
    elif reading == "Four of Swords":
        print("Upright: temporary exile, strife, retreat")
        print("Reverse: social unrest, labor strikes, renewed activity")
    elif reading == "Five of Swords":
        print("Upright: defeat, cowardliness, empty victory")
        print("Reverse: unfairness, defeat, loss")
    elif reading == "Six of Swords":
        print("Upright: harmony, sorrow, journey")
        print("Reverse: obstacles, difficulties, defeat")
    elif reading == "Seven of Swords":
        print("Upright: betrayal, insolence, unwise attempt")
        print("Reverse: counsel, helpful, advice")
    elif reading == "Eight of Swords":
        print("Upright: weakness, indecision, censure")
        print("Reverse: freedom, new beginnings, relaxation")
    elif reading == "Nine of Swords":
        print("Upright: desolation, illness, suspicion, cruelty")
        print("Reverse: unselfishness, good news, healing")
    elif reading == "Ten of Swords":
        print("Upright: defeat, failure, pain")
        print("Reverse: courage, positive energy, good health")
    elif reading == "Page of Swords":
        print("Upright: grace, diplomacy, dexterity, grace")
        print("Reverse: imposture, ill-health, cunningness")
    elif reading == "Knight of Swords":
        print("Upright: strong man, braver, clever person")
        print("Reverse: troublemaker, a crafty, tyranny")
    elif reading == "Queen of Swords":
        print("Upright: skillful, brave, clever, rush")
        print("Reverse: sly, keen, deceitful")
    elif reading == "King of Swords":
        print("Upright: powerful, friendship, counselor")
        print("Reverse: obstinate, evil intentions, judgments")
    elif reading == "Ace of Pentacles":
        print("Upright: prosperity, happiness, pleasure")
        print("Reverse: misery, greedy, money")
    elif reading == "Two of Pentacles":
        print("Upright: harmony, new projects, helpful")
        print("Reverse: difficulty, discouragement")
    elif reading == "Three of Pentacles":
        print("Upright: abilities, approval,effort, abilities")
        print("Reverse: preoccupation, ambitions")
    elif reading == "Four of Pentacles":
        print("Upright: ungenerous, greed, miserly")
        print("Reverse: spendthrift, obstacles, earthy possessions")
    elif reading == "Five of Pentacles":
        print("Upright: destitution, poor health, despair, loneliness")
        print("Reverse: employment, courage, revival")
    elif reading == "Six of Pentacles":
        print("Upright: prosperity, philanthropy, charity, gifts")
        print("Reverse: jealousy, miserliness, unfairness")
    elif reading == "Seven of Pentacles":
        print("Upright: development, re-evaluation, effort, hard work")
        print("Reverse: impatience, slow progress, investments")
    elif reading == "Eight of Pentacles":
        print("Upright: employment, money, learning, trade")
        print("Reverse: void, no ambition, dislike")
    elif reading == "Nine of Pentacles":
        print("Upright: solitude, well-being, green thumb")
        print("Reverse: caution, possible loss")
    elif reading == "Ten of Pentacles":
        print("Upright: wealth, property, stability")
        print("Reverse: dull, slothfulness, misfortune")
    elif reading == "Page of Pentacles":
        print("Upright: kindness,new ideas/opinions, scholar")
        print("Reverse: luxury, rebellious, bad news")
    elif reading == "Knight of Pentacles":
        print("Upright: dull outlook, patience, animal lover, trustworthy")
        print("Reverse: carelessness, standstill, irresponsible")
    elif reading == "Queen of Pentacles":
        print("Upright: thoughtfulness, intelligence, talents, melancholy")
        print("Reverse: mistrust, suspicion, neglect")
    elif reading == "King of Pentacles":
        print("Upright: reliable person, steadiness")
        print("Reverse: bribes, materialistic, calm")
    elif reading == "quit":
        print("Thank you for playing!")

