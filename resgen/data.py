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

languages = {
    'data': [
        'assembly', 'ada', 'alef'
        'bash', 'beanshell',
        'c', 'c#', 'c++', 'css', 'chapel', 'clojure', 'clu', 'cyclone', 'crystal', 
        'd', 'dart', 'dylan',
        'eiffel', 'ecmascript', 'erlang', 'elm', 'elixir',
        'fantom', 'f#',
        'go', 'groovy', 'gambas', 'genie',
        'html', 'hack', 'haxe', 'haskell', 'hermes',
        'idris', 'icon', 'intercal',
        'java', 'javascript', 'j#', 'j++',
        'kotlin',
        'lua', 'limbo',
        'matlab', 'mesa', 'modula-3', 'ml', 'monkey',
        'nim', 'newsqueak', 'nil', 'nemerle', 
        'objective-c', 'oberon', 'ocaml', 'oxygene',
        'perl', 'php', 'python',
        'qore',
        'r', 'ruby', 'rust', 'ring', 'racket',
        'scala', 'sql', 'swift', 'seed7', 'simula', 'scheme', 'standard ml', 'smalltalk', 'strongtalk',
        'typescript', 'tcl',
        'ucsd pascal',
        'vb.net', 'vba', 'vala',
    ],
    'aliases': {
        'html': ['html5'],
        'bash': ['bourne shell'],
    }
}

frameworks_and_tools = {
    'data': [
        '.net core',
        'angular',
        'cordova',
        'django',
        'hadoop',
        'node.js',
        'pytorch',
        'react',
        'spark',
        'spring',
        'tensorflow',
        'xamarin',
    ],
    'aliases': {
        '.net core': ['.net'],
        'node.js':   ['node', 'nodejs'],
        'pytorch':   ['torch'],
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

# https://careers.google.com/jobs?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic#!t=jo&jid=/company/sales-engineer-machine-learning-google-355-main-st-cambridge-ma-02142-usa-3874830108
google_listing = """
Note: By applying to this position your application is automatically submitted
to the following locations: Chicago, IL, USA; New York, NY, USA; Sunnyvale, CA,
USA; Cambridge, MA, USA; Seattle, WA, USA; San Francisco, CA, USA

The Google Cloud Platform team helps customers transform and evolve their
business through the use of Google’s global network, web-scale data centers and
software infrastructure. As part of an entrepreneurial team in this rapidly
growing business, you will help shape the future of businesses of all sizes use
technology to connect with customers, employees and partners.

As a Sales Engineer, you will work hand-in-hand with technical Sales teams as a
machine learning subject matter expert to differentiate Google Cloud to our
customers. You will help prospective customers and partners understand the power
of Google Cloud, explaining technical features, helping customers design
architectures, and problem-solving any potential roadblocks. You will also have
the opportunity to help customers to leverage specialized machine learning (ML)
hardware developed by Google, called Tensor Processing Unit (TPU). The TPU is
Google’s most advanced ML technology and in this role you will work hand-in-hand
with customers and product development to shape the future of the platform.

Google Cloud helps millions of employees and organizations empower their
employees, serve their customers, and build what’s next for their business — all
with technology built in the cloud. Our products are engineered for security,
reliability and scalability, running the full stack from infrastructure to
applications to devices and hardware. And our teams are dedicated to helping our
customers — developers, small and large businesses, educational institutions and
government agencies — see the benefits of our technology come to life.
Responsibilities
• Work with the team to identify and qualify business opportunities, understand
  key customer technical objections and develop the strategy to resolve
  technical blockers.
• Provide in-depth machine learning expertise to support the technical
  relationship with Google’s customers, including product and solution
  briefings, proof-of-concept work, and partner directly with product management
  to prioritize solutions impacting customer adoption to Google Cloud.
• Work hands-on with customers to demonstrate and prototype Google Cloud product
  integrations in customer/partner environments.
• Recommend integration strategies, enterprise architectures, platforms and
  application infrastructure required to successfully implement a complete
  solution using best practices on Google Cloud.
• Travel to customer sites, conferences, and other related events as required.

Qualifications Minimum qualifications:
• BA/BS degree in Computer Science or Electrical Engineering, or equivalent
  practical experience.
• 5 years of experience serving in the capacity of a technical sales engineer in
  a cloud computing environment or equivalent experience in a customer-facing
  role (including working as a member of a professional services or systems
  engineering team).
• Experience with big data and machine learning frameworks such as Tensorflow,
  Theano or Caffe, as well as numerical programming frameworks such as Python or
  MATLAB.
• Experience presenting and delivering technical pitches.

Preferred qualifications:
• Master's degree in Computer Science or other technical field.
• Experience in and understanding of data and information management -
  especially as it relates to big data trends and issues within businesses.
• Experience with building machine learning solutions and leveraging specific
  machine learning architectures (e.g. deep learning, LSTM, convolutional
  networks, etc).
• Experience architecting and developing software or infrastructure for
  scalable, distributed systems.
• Ability to quickly learn, understand, and work with new emerging technologies,
  methodologies, and solutions in the Cloud/IT technology space.

At Google, we don’t just accept difference - we celebrate it, we support it, and
we thrive on it for the benefit of our employees, our products and our
community. Google is proud to be an equal opportunity workplace and is an
affirmative action employer. We are committed to equal employment opportunity
regardless of race, color, ancestry, religion, sex, national origin, sexual
orientation, age, citizenship, marital status, disability, gender identity or
Veteran status. We also consider qualified applicants regardless of criminal
histories, consistent with legal requirements. If you have a disability or
special need that requires accommodation, please let us know.

To all recruitment agencies: Google does not accept agency resumes. Please do
not forward resumes to our jobs alias, Google employees or any other company
location. Google is not responsible for any fees related to unsolicited resumes.
"""
