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

#https://www.ziprecruiter.com/c/Fidelity/Job/Principal-Cloud-Software-Engineer/-in-Amherst,MA?ojob=fe282050074060647ddf1ab69eabab00
fidelity_listing = """
An exciting new opportunity has opened for a Cloud Technologist within Incident
Change and Management Squad that is part of Virtualization Tribe in ECC
(Enterprise Cloud Computing). The successful candidate will wear many hats:
first responder as L1 / L2, Consulting to Business partners, Interface with many
DevOps Squads and Tribes, FSC and App support teams. Superlative technical and
communication skills are required for you to be successful within this role. Key
Responsibilities Lead and develop our Infrastructure Operations Team to greater
heights of effectiveness, customer service and accomplishment. Ensure
Infrastructure Operations Team is adhering to Information Security, Regulatory
Compliance, Incident Management, Problem Management and Change Management
processes/practices. Responsible for the proper monitoring and alerting of all
environments Responsible for internal infrastructure projects which may require
cross-departmental coordination to achieve goals. Provide input into product
teams on infrastructure lifecycle, improvement and standardization strategies.
Drive the objectives associated with Problem Management; such as customer
communication and Root Cause Analysis reports. Develop internal SOPs, processes
and training to ensure Infrastructure team members have the needed skills and
tools to support the production environments and deliver on project commitments.
Work with application owners and product teams as requested to assess
applications and recommend infrastructure/cloud solutions. Required Skills 2
years' experience with AWS foundational cloud services for storage, computation,
event processing, messaging, data processing, and analytics 5 years of software
development with object-oriented languages such as Python, Java or C using SOA
principles Strong familiarity with Linux OS (Redhat) Solid experience with JSON,
XML and related notational data representations Solid understanding of DevOps
principles, experience with operational tools (Ansible, Chef, Puppet, TerraForm,
CloudFormation) and best practices for infrastructure and software deployment
Extensive knowledge of APIs, RESTful services and integration with Cloud data
providers Expert scripting skills in at least one of the following: bash, perl
or python Competent in Linux systems administration Server configuration
management knowledge Familiarity with formal risk management policies and
procedures Familiar with scanning and penetration tools and techniques
Application packaging knowledge Able to research, test and implement new
software within the company's infrastructure Qualifications Must love data
Ability to adapt quickly to new technologies and changing business requirements
Able and willing to collaborate as part of a team in various roles Respond to
emergency situations effectively, maintaining poise and focus Willingness to
work after hours on project-related work and pre-scheduled on-call support AWS
Certification is desirable Excellent communication (written and verbal) and
interpersonal skills
"""
