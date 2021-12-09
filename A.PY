
rating_data = soup.find_all('span', class_="ipl-rating-star__rating")
rating = [] #empty list
for i in range(0,len(rating_data),23): #loop
    
    rating.append(rating_data[i].text)
rating


duration_data = soup.find_all('span', class_="runtime")
duration = [] #empty list

for i in range(len(duration_data)):
    duration.append(duration_data[i].text)



  




