
filename="[Ohys-Raws] Otaku ni Koi wa Muzukashii - 02 (CX 1280x720 x264 AAC).mp4"

# Define dictionaries
ignore_chars={"[","]","(",")","."}
ignore_words={"-"}

episode_words={'00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99'}
group_words={"Ohys-Raws"}
channel_words={"CX"}
format_words={"1280x720","x264","AAC","mp4"}

# Initialize output

# Strip punctuations function, replace with space
def rm_punc(word):
	wordlist=list(word)
	for i,_ in enumerate(wordlist):
		if wordlist[i] in ignore_chars:
			wordlist[i]=" "
	return("".join(wordlist))
			

# Extract words
processed_words=[]

for word in filename.split():
	processed_words+=rm_punc(word).split()
# Remove ignore words
for i,word in enumerate(processed_words):
	if word in ignore_words:
		processed_words.pop(i)

#print(processed_words)

# Get tags
group_tags=[]
channel_tags=[]
format_tags=[]
title_name=[]
for i,word in enumerate(processed_words):
	if word in episode_words:
		episode=word
	elif word in group_words:
		group_tags.append(word)
	elif word in channel_words:
		channel_tags.append(word)
	elif word in format_words:
		format_tags.append(word)
	else:
		title_name.append(word)

# Output tag info
print("Title: " + " ".join(title_name))
print("Episode: " + episode)
print("Group: " + " ".join(group_tags))
print("Channel: " + " ".join(channel_tags))
print("Format: " + " ".join(format_tags))
