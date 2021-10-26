from choices import fastfood, advice

#place = fastfood.pick()
#take_out = advice.give()

#print("Let's go to {} for lunch!".format(place))
#print("Should we take out?", take_out)

from choices.fastfood import pick as fastpick, fastfood as available_fastfood
from choices.advice import give as give_advice, responses as available_advice_responses

place = fastfood.pick()
take_out = advice.give()

print("Let's go to {} for lunch!".format(place))
print("Should we take out?", take_out)
print("Available fastfood places:", available_fastfood)
print("available advice responses:", available_advice_responses)
