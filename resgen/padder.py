# generates nonsense resume bullet points

import data
import random

action_words = [
    'Implemented',
    'Optimized',
    'Utilized',
]

very_cool_things = [
    'fearless concurrency',
    'zero-cost FFI',
    'zygohistomorphic prepromophisms',
    'a human-in-the-loop control system',
    'a LISP dialect without parentheses',
    'a blockchain-based social network',
    'Browsr.js, the web frontend framework of tomorrow,',
    'a left-pad reimplementation',
]

languages = [language.title() for language in data.languages['data']]

lang_to_tool_chain = [
    'to remove a dependency on',
    'to make web-scale a cluster of servers running',
    'as an excuse to play with',
    'to optimize a microservice using'
]

frameworks_and_tools = [thing.title() for thing in data.frameworks_and_tools['data']]

action_word = random.choice(action_words)
very_cool_thing = random.choice(very_cool_things)
language = random.choice(languages)
chain = random.choice(lang_to_tool_chain)
framework_or_tool = random.choice(frameworks_and_tools)

print(action_word + ' ' + very_cool_thing + ' with ' + language + ' ' + chain + ' ' + framework_or_tool + '.')
