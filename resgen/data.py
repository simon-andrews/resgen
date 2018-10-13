# data.py: where data is stored
# source for all of this stuff is StackOverflow's developer survey

# Structure for data:
"""
variable_name = {
    data: [
        item1,
        item2,
        item3,
    ],
    aliases: {
        item1: [it3m1, 1tem1],
    }
}
"""

# is a token inside the dataset (or is an alias)?
def is_data(token, dataset):
    for datapoint in dataset['data']:
        if token == datapoint:
            return True
    for aliased_thing in dataset['aliases']:
        for alias in dataset['aliases'][aliased_thing]:
            if token == alias:
                return True
    return False

languages = {
    'data': [
        'Assembly',
        'Bash',
        'C', 'C#', 'C++', 'CSS',
        'Go', 'Groovy',
        'HTML',
        'JavaScript',
        'Kotlin',
        'MATLAB',
        'Objective-C',
        'Perl', 'PHP', 'Python',
        'R', 'Ruby',
        'Scala', 'SQL', 'Swift',
        'TypeScript',
        'VB.NET', 'VBA',
    ],
    'aliases': {
        'HTML': ['HTML5'],
    }
}

frameworks_and_tools = {
    'data': [
        '.NET Core',
        'Angular',
        'Cordova',
        'Django',
        'Hadoop',
        'Node.js',
        'PyTorch',
        'React',
        'Spark',
        'Spring',
        'TensorFlow',
        'Xamarin',
    ],
    'aliases': {
        '.NET Core': ['.NET'],
        'Node.js':   ['Node', 'NodeJS'],
        'PyTorch':   ['Torch'],
    }
}
