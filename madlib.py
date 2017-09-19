story = '''
Once upon a time there was a river and it flowed from the mountain. The river flowed through a town in the mountains. The townspeople lived off the river and got everything from it. A big dragon came one say and stopped the river from flowing into the town. Everybody in the town eventually died.
'''
print(story)

river = input("enter a noun:")
flowed = input("enter a past tense verb:")
mountain = input("enter noun")
townspeople = input("enter a plural noun:")
dragon = input("enter a noun:")
big = input("enter an adjective:")
died = input("enter a past tense verb:")
story = story.replace("river",river)
story = story.replace("flowed",flowed)
story = story.replace("mountain",mountain)
story = story.replace("townspeople",townspeople)
story = story.replace("dragon",dragon)
story = story.replace("big",big)
story = story.replace("died",died)
print(story)
