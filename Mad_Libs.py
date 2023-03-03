def madLib(creature, place, verb, thing, adjective, noun, emotion, job, adjective2, verb2, timeOfDay):
    print ("Once upon a time, there was a " + creature + ".")
    print ("Every day, the " + creature + " would go to to " + place + " and " + verb + ".")
    print ("Until one day, they stepped onto a " + thing + " and turned into a " + adjective + " " + noun +" ")
    print ('Because of that, they felt ' + emotion + ' and became a ' + job + '.')
    print ('So that finally, everyone thought they were ' + adjective2 + '!')
    print ('The moral of the story is: always ' + verb2 + ' in the ' + timeOfDay + '.')

madLib(input("Creature: ").lower(), input('Place: ').lower(), input('Verb: ').lower(), input('Object: ').lower(), input('Adjective: ').lower(), input("Noun: ").lower(), input('Emotion: ').lower(), input("Job: ").lower(), input('Adjective: ').lower(), input('Verb: ').lower(), input('Time of day: ').lower())