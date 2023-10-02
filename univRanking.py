# Name: Orayda Shagifa
# CS1026A Assignment 3: Universities Ranking
# Description: Program reads the content of two .csv files and displays information extracted from these files
# Due Date: 11.16.2022

# loads and sorts data from the two given files
def loadFiles(selectedCountry, uniFile, capitalFile):
    try:
        # open files
        topUnis = open(uniFile, "r", encoding='utf8')
        capitals = open(capitalFile, "r", encoding='utf8')

        # remove headers
        topUnis.readline()
        capitals.readline()

        # lists for uni data
        worldRank = []
        uniName = []
        uniCountry = []
        uniNatRank = []
        uniScore = []

        # lists for capitals data
        countryName = []
        capital = []
        continent = []

        # sort data in topUnis file
        for line in topUnis:
            line = line.strip()
            unis = line.split(",")
            worldRank.append(unis[0])
            uniName.append(unis[1])
            uniCountry.append(unis[2])
            uniNatRank.append(unis[3])
            uniScore.append(unis[8])

        # sort data in capitals file
        for line in capitals:
            line = line.strip()
            country = line.split(",")
            countryName.append(country[0])
            capital.append(country[1])
            continent.append(country[5])

        # close files
        topUnis.close()
        capitals.close()

        # return lists
        return worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent

    except FileNotFoundError:
        # prints error message and exits program
        print("file not found")
        quit()


# 1
def uniCount(selectedCountry, uniFile, capitalFile):
    # get lists from loadFiles function
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    # takes the length of list that stores the university names
    count = len(worldRank)

    # returns number of universities
    return count


# 2
def availableCountries(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    # list to store available countries
    availCountries = []

    for i in range(len(uniCountry)):
        # adds countries to lists, if not already in list
        if uniCountry[i] not in availCountries:
            availCountries.append(uniCountry[i])

    # returns list of available countries
    return availCountries


# 3
def availableContinents(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)
    # import list of available countries from previous function
    availCountries = availableCountries(selectedCountry, uniFile, capitalFile)

    # list to store available continents
    availContinents = []

    for i in range(len(availCountries)):
        # checks each country's continent and adds the continent to the list, if not already in list
        for x in range(len(countryName)):
            if availCountries[i].upper() == countryName[x].upper():
                if continent[x] not in availContinents:
                    availContinents.append(continent[x])

    # returns list of available continents
    return availContinents


# 4
def topUniRank(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    selWorldRank = 5000
    for i in range(len(uniCountry)):
        # finds the highest ranking university in the selected country
        if selectedCountry.upper() == uniCountry[i].upper() and int(selWorldRank) > int(worldRank[i]):
            selWorldRank = worldRank[i]
            selUniName = uniName[i]

    # returns the world rank and name of the university
    return selWorldRank, selUniName


# 5
def topNationalRank(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    selNatRank = 5000
    for i in range(len(uniCountry)):
        # finds university located in selected country and checks if rank is the highest
        if selectedCountry.upper() == uniCountry[i].upper() and int(selNatRank) > int(uniNatRank[i]):
            selNatRank = uniNatRank[i]
            selNatUniName = uniName[i]

    # returns the national rank and university name
    return selNatRank, selNatUniName


# 6
def averageScore(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    # list to store scores of universities in selected country
    scores = []
    for i in range(len(uniCountry)):
        # finds universities in selected country and adds their score to the list
        if selectedCountry.upper() == uniCountry[i].upper():
            scores.append(float(uniScore[i]))

    # calculate average score of universities in selected country
    avgScore = (sum(scores) / len(scores))

    # returns the average score
    return avgScore


# 7
def contRelScore(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    # function only finds relative score since average score is already found in the averageScore function

    # list for countries in the same continent as selected country
    countryCont = []

    # finds continent of selected country
    for x in range(len(countryName)):
        if countryName[x].upper() == selectedCountry.upper():
            curContinent = continent[x]

    # adds all country in the continent to the countyCont list
    for x in range(len(countryName)):
        if continent[x].upper() == curContinent.upper():
            countryCont.append(countryName[x].upper())

    # finds the highest ranking university whose country is in the countryCont list and retrieves its score
    relScore = 0
    for i in range(len(uniCountry)):
        if uniCountry[i].upper() in countryCont and (float(relScore) < float(uniScore[i])):
            relScore = uniScore[i]

    # returns the continent of the selected country and the relative score of the top university in that continent
    return curContinent, relScore


# 8
def capCity(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    # finds capital city of selected country
    for i in range(len(countryName)):
        if selectedCountry.upper() == countryName[i].upper():
            selCapCity = capital[i]
            break

    # returns the capital city
    return selCapCity


# 9
def uniCapitalName(selectedCountry, uniFile, capitalFile):
    worldRank, uniName, uniCountry, uniNatRank, uniScore, countryName, capital, continent = loadFiles(selectedCountry, uniFile, capitalFile)

    # finds capital city of selected country
    for i in range(len(countryName)):
        if selectedCountry.upper() == countryName[i].upper():
            selCapCity = capital[i]
            break

    # list for universities that hold the capital name
    uniCapName = []

    # checks if each university contains the capital city name
    for i in range(len(uniName)):
        if selCapCity.upper() in uniName[i].upper():
            uniCapName.append(uniName[i])

    # returns list of universities that hold the capital name
    return uniCapName


# writes results to output.txt
def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    # gets data from functions
    count = uniCount(selectedCountry, rankingFileName, capitalsFileName)
    availCountries = availableCountries(selectedCountry, rankingFileName, capitalsFileName)
    availContinents = availableContinents(selectedCountry, rankingFileName, capitalsFileName)
    selWorldRank, selUniName = topUniRank(selectedCountry, rankingFileName, capitalsFileName)
    selNatRank, selNatUniName = topNationalRank(selectedCountry, rankingFileName, capitalsFileName)
    avgScore = averageScore(selectedCountry, rankingFileName, capitalsFileName)
    curContinent, relScore = contRelScore(selectedCountry, rankingFileName, capitalsFileName)
    selCapCity = capCity(selectedCountry, rankingFileName, capitalsFileName)
    uniCapName = uniCapitalName(selectedCountry, rankingFileName, capitalsFileName)

    # opens output file
    output = open("output.txt", "w")

    # writes data to output file
    output.write("Total number of universities => " + str(count))
    output.write("\nAvailable countries => " + str((", ".join(availCountries)).upper()))
    output.write("\nAvailable continents  => " + str((", ".join(availContinents)).upper()))
    output.write("\nAt international rank => " + str(selWorldRank).upper() + " the university name is => " + str(selUniName).upper())
    output.write("\nAt national rank => " + str(selNatRank).upper() + " the university name is => " + str(selNatUniName).upper())
    output.write("\nThe average score => " + str("%.2f" % avgScore) + "%")
    output.write("\nThe relative score to the top university in " + curContinent.upper() + " is => " + "(" + str("%.2f" % float(avgScore)) + " / " + str("%.2f" % float(relScore)) + ")" + " x 100% = " + str("%.2f" % float((float(avgScore) / float(relScore)) * 100)) + "%")
    output.write("\nThe capital is => " + selCapCity.upper())
    output.write("\nThe universities that contain the capital name =>")
    for i in range(len(uniCapName)):
        output.write("\n\t# " + str(i+1) + " " + str(uniCapName[i]).upper())

    # closes output file
    output.close()


# getInformation("usa", "TopUni.csv", "capitals.csv")
