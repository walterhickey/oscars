import random 
from tqdm import tqdm 
from math import log
winners = []
top_choices = []
for x in tqdm(range(10000)):

	#simulate academy
	academy = range(1,8800)
	derp = [random.randint(-53,53),random.randint(-53,53),random.randint(-53,53),random.randint(-36,53),random.randint(-53,53),random.randint(-53,53),random.randint(-53,53),random.randint(-45,53)]
	picture_votes = []
	for voter in academy:
		black_panther = ["Black Panther",8+log(81.8+derp[0]) + random.random()]
		blackkklansman = ["BlacKkKlansman",8+log(68.8+derp[1]) + random.random()]
		bohemian_rhapsody = ["Bohemian Rhapsody",8+log(58.6+derp[2]) + random.random()]
		the_favourite = ["The Favourite",8+log(36.4+derp[3]) + random.random()]
		roma = ["Roma",8+log(193.1+derp[4]) + random.random()]
		green_book = ["Green Book",8+log(137.6+derp[5]) + random.random()]
		a_star_is_born = ["A Star Is Born",8+log(79.3+derp[6]) + random.random()]
		vice = ["Vice",8+log(45.9+derp[7]) + random.random()]
		rank = []
		rankalg = 8
		while rankalg > 0:	
			floor = 0
			bpa = black_panther[1] + floor
			floor = bpa
			bkk = floor + blackkklansman[1]
			floor = bkk
			bor = floor + bohemian_rhapsody[1]
			floor = bor
			fav = floor + the_favourite[1]
			floor = fav
			rma = floor + roma[1]
			floor = rma
			grb = floor + green_book[1]
			floor = grb
			sib = floor + a_star_is_born[1]
			floor = sib
			vic = floor + vice[1]
			floor = vic
		
			vote = random.uniform(0,floor)
			if vote < bpa:
				rank.append(black_panther[0])
				black_panther[1] = 0
			elif vote < bkk:
				rank.append(blackkklansman[0])
				blackkklansman[1] = 0
			elif vote < bor:
				rank.append(bohemian_rhapsody[0])
				bohemian_rhapsody[1] = 0
			elif vote < fav:
				rank.append(the_favourite[0])
				the_favourite[1] = 0
			elif vote < rma:
				rank.append(roma[0])
				roma[1] = 0
			elif vote < grb:
				rank.append(green_book[0])
				green_book[1] = 0
			elif vote < sib:
				rank.append(a_star_is_born[0])
				a_star_is_born[1] = 0
			elif vote < vic:
				rank.append(vice[0])
				vice[1] = 0
			rankalg = rankalg - 1
		picture_votes.append(rank)	
		top_choices.append(rank[0])	
	k = 1
	#picture_votes2 = picture_votes
	#+while k < 100:
	#	print picture_votes2.pop()
	#	k = k + 1


	#run algo
	nowinner = True
	eliminated = []
	while nowinner:
		bpacount = 0
		bkkcount = 0
		borcount = 0
		favcount = 0
		rmacount = 0
		grbcount = 0
		sibcount = 0
		viccount = 0
		for j in picture_votes:
			#print j[0]
			if len(j) > 0:
				if j[0] == "Black Panther":
					bpacount = bpacount + 1
				elif j[0] == "BlacKkKlansman":
					bkkcount = bkkcount + 1
				elif j[0] == "Bohemian Rhapsody":
					borcount = borcount + 1
				elif j[0] == "The Favourite":
					favcount = favcount + 1
				elif j[0] == "Roma":
					rmacount = rmacount + 1
				elif j[0] == "Green Book":
					grbcount = grbcount + 1
				elif j[0] == "A Star Is Born":
					sibcount = sibcount + 1
				elif j[0] == "Vice":
					viccount = viccount + 1
		maximum = max(bpacount,bkkcount,borcount,favcount,rmacount,grbcount,sibcount,viccount)
		list_movies = [bpacount,bkkcount,borcount,favcount,rmacount,grbcount,sibcount,viccount]
		for i in eliminated:
			if i == "Black Panther":
				list_movies[0] = 200000
			elif i == "BlacKkKlansman":
				list_movies[1] = 200000
			elif i == "Bohemian Rhapsody":
				list_movies[2] = 200000
			elif i == "The Favourite":
				list_movies[3] = 200000
			elif i == "Roma":
				list_movies[4] = 200000
			elif i == "Green Book":
				list_movies[5] = 200000
			elif i == "A Star Is Born":
				list_movies[6] = 200000
			elif i == "Vice":
				list_movies[7] = 200000
		minimum = min(list_movies)
		eliminate = ""
		#print maximum
		#print minimum
		if maximum > 50:
			if bpacount == maximum:
				winners.append("Black Panther")
			elif bkkcount == maximum:
				winners.append("BlacKkKlansman")
			elif borcount == maximum:
				winners.append("Bohemian Rhapsody")
			elif favcount == maximum:
				winners.append("The Favourite")
			elif rmacount == maximum:
				winners.append("Roma")
			elif grbcount == maximum:
				winners.append("Green Book")
			elif sibcount == maximum:
				winners.append("A Star Is Born")
			elif viccount == maximum:
				winners.append("Vice")
			nowinner = False
		else:	
			if bpacount == minimum:
				eliminate = "Black Panther"
				eliminated.append(eliminate)
			elif bkkcount == minimum:
				eliminate = "BlacKkKlansman"
				eliminated.append(eliminate)
			elif borcount == minimum:
				eliminate = "Bohemian Rhapsody"
				eliminated.append(eliminate)
			elif favcount == minimum:
				eliminate = "The Favourite"
				eliminated.append(eliminate)			
			elif rmacount == minimum:
				eliminate = "Roma"
				eliminated.append(eliminate)
			elif grbcount == minimum:
				eliminate = "Green Book"
				eliminated.append(eliminate)
			elif sibcount == minimum:
				eliminate = "A Star Is Born"
				eliminated.append(eliminate)
			elif viccount == minimum:
				eliminate = "Vice"
				eliminated.append(eliminate)
			
			for e in picture_votes:
				if eliminate in e:
					e.remove(eliminate)
				if len(e) == 0:
					del e

print "Black Panther " + str(winners.count("Black Panther"))
print "BlacKkKlansman " + str(winners.count("BlacKkKlansman"))
print "Bohemian Rhapsody " + str(winners.count("Bohemian Rhapsody"))
print "The Favourite " + str(winners.count("The Favourite"))
print "Roma " + str(winners.count("Roma"))
print "Green Book " + str(winners.count("Green Book"))
print "A Star Is Born " + str(winners.count("A Star Is Born"))
print "Vice " + str(winners.count("Vice"))


print "first choices"
print "Black Panther " + str(top_choices.count("Black Panther")/880000.0)+"%"
print "BlacKkKlansman " + str(top_choices.count("BlacKkKlansman")/880000.0)+"%"
print "Bohemian Rhapsody " + str(top_choices.count("Bohemian Rhapsody")/880000.0)+"%"
print "The Favourite " + str(top_choices.count("The Favourite")/880000.0)+"%"
print "Roma " + str(top_choices.count("Roma")/880000.0)+"%"
print "Green Book " + str(top_choices.count("Green Book")/880000.0)+"%"
print "A Star Is Born " + str(top_choices.count("A Star Is Born")/880000.0)+"%"
print "Vice " + str(top_choices.count("Vice")/880000.0)+"%"
		
