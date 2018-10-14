# generates nonsense resume bullet points

import data
import json
import random

action_words = [
    'Implemented',
    'Optimized',
    'Utilized',
    'Programmed a robot with',
    'Split a monolith into microservices using',
    'Encouraged adoption of',
    'Wrote unit tests for',
    'Used Jenkins CI server to test',
]

very_cool_things = [
    'fearless concurrency',
    'zero-cost FFI',
    'zygohistomorphic prepromophisms',
    'a human-in-the-loop control system',
    'a LISP dialect without parentheses',
    'blockchain-based social networks',
    'Browsr, the web frontend framework of tomorrow,',
    'left-pad libraries',
]

languages = data.languages['data']

lang_to_tool_chain = [
    'to remove a dependency on',
    'to make web-scale a cluster of servers running',
    'as an excuse to play with',
    'to optimize a microservice using',
    'to download documentation for',
    'to justify switching to a stack without',
    'to prove the fragility of',
    'to replace a Slack bot made with'
]

frameworks_and_tools = data.frameworks_and_tools['data']

def get_bullet():
    action_word = random.choice(action_words)
    very_cool_thing = random.choice(very_cool_things)
    language = random.choice(languages)
    chain = random.choice(lang_to_tool_chain)
    framework_or_tool = random.choice(frameworks_and_tools)
    return {
        'text': action_word + ' ' + very_cool_thing + ' with ' + language.title() + ' ' + chain + ' ' + framework_or_tool.title() + '.',
        'tags': [language, framework_or_tool]
    }

def get_string():
    return get_bullet()['text']

if __name__ == '__main__':
    import sys
    try:
        arg = sys.argv[1]
        n = int(arg)
    except IndexError:
        n = 1
    except ValueError:
        print('not a number: ' + arg)
        sys.exit(1)
    bullets = list()
    for i in range(n):
        bullets.append(get_bullet())
    print(json.dumps(bullets))
