"""
The patterns file is here: https://github.com/ahalterman/GKG-Themes/blob/master/SET_EVENTPATTERNS.xml
A local copy is kept in ./resources

It is not valid XML so we use regex

There are non-theme entries in this file not considered here
"""
import re

globals_p = re.compile(r'^<GLOBAL>\s*<TERMS>([^<]+)</TERMS>', re.M|re.S)
categories_p = re.compile(r'^<CATEGORY NAME="([^"]+)" TYPE="([^"]+)">\s*<TERMS>([^<]+)</TERMS>', re.M|re.S)

global_terms = []
categories = {}

with open('./resources/SET_EVENTPATTERNS.xml') as f:
    s = f.read()
    for text in globals_p.findall(s):
        for line in text.split('\n'):
            ts = line.split('\t')
            if len(ts) == 2:
                global_terms.append( (ts[0], int(ts[1])) )
    for cat, type_, terms in categories_p.findall(s):
        terms = [(t.split('\t')[0], int(t.split('\t')[1])) for t in terms.split('\n') if t and len(t.split('\t')) == 2]
        if terms:
            categories[cat] = {
                'type': type_,
                'terms': terms
            }


def get_theme(text):
    text = text.lower()
    offset = sum([val for term, val in global_terms if term in text])
    scores = {}
    for category, data in categories.items():
        if data['type'] == 'THEME':
            terms = data['terms']
            score = sum([val+offset for term, val in terms if term in text])
            if score > 0:
                scores[category] = score
    print(scores)

text1 = """As a Southwest Airlines jet hurtled 32,000 feet over suburban Philadelphia, a rare engine explosion caused a passenger’s window to burst, partially pulling the woman sitting next to the opening out of the plane.
Fellow passengers frantically worked to yank her back inside the airliner as it depressurized and quickly descended thousands of feet per minute, according to several passengers.
The frightening ordeal played out Tuesday morning onboard Southwest flight 1380 as it headed for Dallas. The Boeing 737-700 was about 20 minutes into its journey from New York’s LaGuardia Airport when the engine failure occurred. The plane, carrying 144 passengers and five crew, diverted to Philadelphia International Airport where it made an emergency landing at 11:20 a.m.
Passengers described hearing a loud explosion from the left engine — one of two onboard — before debris peppered the fuselage and shattered that window.
"""

text2 = """Public humiliation is a rite of passage for many top officials in the Trump administration. But when it was Nikki Haley's turn this week, she fought back, defending herself in a way that reflects her unique status in the Trump administration.

The US ambassador to the United Nations spent much of Tuesday feeling both embarrassed that she had caused controversy by getting ahead of the White House in announcing Russia sanctions and irked by seemingly dismissive and condescending remarks from a fellow administration official, according to two sources close to Haley.
Larry Kudlow, President Donald Trump's newly installed chief economic adviser, said "there might have been some momentary confusion" on her part. Haley found the remark disrespectful and felt she couldn't keep quiet, the sources said.
"With all due respect, I don't get confused," Haley said in a statement.
It was a stunning retort in an administration where the typical response to being put down is to slink away quietly and regroup. That was the playbook for former Secretary of State Rex Tillerson, who was ridiculed on Twitter by President Donald Trump for getting too far ahead on diplomacy with North Korea. Similarly, then-Homeland Security Secretary John Kelly, who is now White House chief of staff, ran afoul of Trump when he insisted the administration's travel ban was really a "travel pause," only to watch the President call it a ban.
Haley didn't endure a presidential putdown, but Kudlow's comments -- for which he later apologized -- were in line with an apparent White House strategy to shift blame to Haley and shield the President. Still, none of her colleagues have so publicly bristled at the egg on their faces."""

text3 = """One of the two Canadian women who documented a lavish cruise trip to Australia on Instagram as a front for smuggling cocaine has been sentenced to at least four and a half years in prison.

Melina Roberge, along with two accomplices, had embarked on a round-the-world cruise, taking in a number of exotic locations, before the 95 kg (210 lb) haul was discovered on their cruise ship when it docked in Sydney.
Roberge broke down in tears in the courtroom, according to CNN's Australian affiliate Channel 7.
"I was meant to just be there and look like I was on holiday and look like a cover for everyone else," the 24-year-old Canadian said at the sentencing hearing.
"I am really sorry, I should have thought about the consequences and not what I would have gotten for it," she said.
Crown prosecutor Tom Muir told the court that she was aware of her role in the crime, and was using it to support her lavish lifestyle.
"She was not doing it for debt," he said. "It's for the lifestyle she wants to enjoy."
At the time, police told CNN affiliate Channel 7 that the seizure was Australia's biggest-ever drug bust through a "passenger stream."""

text4 = """Oil prices kept rising to their highest since late 2014 as U.S. crude inventories declined, moving closer to five-year averages, and after sources told Reuters that top exporter Saudi Arabia aims to push prices even higher.
FILE PHOTO: A pump jack is seen at sunrise near Bakersfield, California October 14, 2014. REUTERS/Lucy Nicholson/File Photo
Brent crude futures LCOc1 reached $74.74 a barrel, the highest since Nov. 27, 2014 — the day OPEC decided to pump as much as it could to defend market share, sending the price to a low of $27 just over a year later.
Brent futures came off slightly to $74.40 a barrel by 1316 GMT, still up 92 cents from the previous close.
U.S. West Texas Intermediate (WTI) crude futures CLc1 were up 53 cents at $69.00. WTI had earlier hit $69.56, its highest since Nov. 28.
The Organization of the Petroleum Exporting Countries (OPEC) and other major producers including Russia started to withhold output in 2017 to rein in oversupply that had depressed prices since 2014."""

get_theme(text4)
