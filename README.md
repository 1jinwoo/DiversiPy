# DiversiPy
NLTK program that detects redundant words and suggests synonyms for diversified diction

# What does DiversiPy do?
- My project takes a text (academic essay, personal journals, etc.) and a number `num` (number of words to suggest synonyms for) and outputs the top `num` most frequently used nouns, verbs, adjectives, and adverbs in their base form and synonyms for each of the words.
- Using the synonym suggestions, it is possible to improve the writing by reducing redundant vocabulary.
- Example run:

```
Project\jw3580>python Diversi.py
Please copy and paste your input text here: These excellant intentions were strengthed when he enterd the Father Superior's diniing-room, though, stricttly speakin, it was not a dining-room, for the Father Superior had only two rooms alltogether; they were, however, much larger and more comfortable than Father Zossima's. But tehre was was no great luxury about the furnishng of these rooms eithar. The furniture was of mohogany, covered with leather, in the old-fashionned style of 1820 the floor was not even stained, but evreything was shining with cleanlyness, and there were many chioce flowers in the windows; the most sumptuous thing in the room at the moment was, of course, the beatifuly decorated table. The cloth was clean, the service shone; there were three kinds of well-baked bread, two bottles of wine, two of excellent mead, and a large glass jug of kvas -- both the latter made in the monastery, and famous in the neigborhood. There was no vodka. Rakitin related afterwards that there were five dishes: fish-suop made of sterlets, served with little fish paties; then boiled fish served in a spesial way; then salmon cutlets, ice pudding and compote, and finally, blanc-mange. Rakitin found out about all these good things, for he could not resist peeping into the kitchen, where he already had a footing. He had a footting everywhere, and got informaiton about everything. He was of an uneasy and envious temper. He was well aware of his own considerable abilities, and nervously exaggerated them in his self-conceit. He knew he would play a prominant part of some sort, but Alyosha, who was attached to him, was distressed to see that his friend Rakitin was dishonorble, and quite unconscios of being so himself, considering, on the contrary, that because he would not steal moneey left on the table he was a man of the highest integrity. Neither Alyosha nor anyone else could have infleunced him in that.
Please enter the number of words you want to get synonyms for: 5

most used nouns: {suggested synonyms}
('room', {'board', 'elbow_room', 'room', 'way'})
('thing', {'thing', 'affair', 'matter'})
('intention', {'intention', 'design', 'intent', 'purpose', 'aim'})
('diniing-room', set())
('dining-room', {'dining-room', 'dining_room'})
('tehre', set())
('luxury', {'sumptuousness', 'sumptuosity', 'luxuriousness', 'opulence', 'lavishness', 'luxury'})



most used verbs: {suggested synonyms}
('be', {'live', 'Be', 'follow', 'equal', 'represent', 'glucinium', 'be', 'embody', 'make_up', 'atomic_number_4', 'personify', 'comprise', 'constitute', 'cost', 'beryllium', 'exist'})
('have', {'take_in', 'wealthy_person', 'feature', 'give', 'throw', 'possess', 'induce', 'suffer', 'have_got', 'cause', 'stimulate', 'own', 'get', 'have', 'consume', 'accept', 'sustain', 'receive', 'birth', 'experience', 'make', 'hold', 'take', 'let', 'give_birth', 'deliver', 'ingest', 'bear', 'rich_person'})
('serve', {'serve_up', 'service', 'help', 'dish', 'wait_on', 'dish_up', 'function', 'suffice', 'swear_out', 'answer', 'process', 'attend_to', 'assist', 'do', 'serve', 'dish_out', 'serve_well', 'attend'})
('strengthed', set())
('enterd', set())
('eithar', set())
('cover', {'incubate', 'address', 'binding', 'plow', 'screen', 'enshroud', 'covert', 'concealment', 'handle', 'compensate', 'pass_over', 'encompass', 'cross', 'comprehend', 'breed', 'spread_over', 'screening', 'top', 'overlay', 'deal', 'cut_across', 'wrap_up', 'get_across', 'book_binding', 'cut_through', 'cover_charge', 'traverse', 'brood', 'hatch', 'shroud', 'extend', 'covering', 'natural_covering', 'overcompensate', 'hide', 'cover_song', 'blanket', 'covering_fire', 'cover_version', 'continue', 'insure', 'cover', 'track', 'masking', 'underwrite', 'get_over', 'treat', 'embrace', 'cover_up', 'back', 'report'})



most used adjectives: {suggested synonyms}
('large', {'prominent', 'large', 'declamatory', 'with_child', 'bombastic', 'orotund', 'magnanimous', 'heavy', 'gravid', 'boastfully', 'vauntingly', 'great', 'turgid', 'enceinte', 'expectant', 'big', 'tumid'})
('fish', {'Pisces_the_Fishes', 'Pisces', 'angle', 'Fish', 'fish'})
('excellant', set())
('much', {'practically', 'a_lot', 'much', 'a_great_deal', 'often', 'very_much', 'a_good_deal', 'lots'})
('comfortable', {'well-situated', 'well-fixed', 'comfortable', 'prosperous', 'well-to-do', 'well-off', 'well-heeled', 'comfy', 'easy'})
('great', {'groovy', 'heavy', 'great', 'big', 'neat', 'peachy', 'dandy', 'gravid', 'keen', 'smashing', 'outstanding', 'cracking', 'slap-up', 'majuscule', 'corking', 'bully', 'capital', 'nifty', 'bang-up', 'enceinte', 'expectant', 'large', 'with_child', 'swell', 'not_bad'})
('old-fashionned', set())



most used adverbs: {suggested synonyms}
('not', {'not', 'non'})
('then', {'and_so', 'so', 'then', 'and_then'})
('stricttly', set())
('only', {'exclusively', 'simply', 'solitary', 'just', 'lone', 'but', 'alone', 'only_when', 'sole', 'lonesome', 'merely', 'solely', 'only', 'entirely', 'only_if'})
('alltogether', set())
('however', {'however', 'nevertheless', 'yet', 'withal', 'all_the_same', 'still', 'notwithstanding', 'even_so', 'nonetheless'})
('more', {'more', 'more_than', 'Thomas_More', 'Sir_Thomas_More', 'More', 'to_a_greater_extent'})


Please copy and paste your input text here:
```

# Attribution
Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
