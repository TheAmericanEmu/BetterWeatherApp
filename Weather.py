import requests
import json
import time
from datetime import date

CC = 27.8006,-97.3964


temperature =[ 0,"temperature"]
dewpoint =[0,"dewpoint"]
maxTemperature =[0,"maxTemperature"]
minTemperature = [0,"minTemperature"]
relativeHumidity =[0,"relativeHumidity"]
apparentTemperature=[0,"apparentTemperature"]
heatIndex=[0,"heatIndex"]
windChill =[0,"windChill"]
skyCover=[0,"skyCover"]
windDirection=[0,"windDirection"]
windSpeed=[0,"windSpeed"]
windGust=[0,"windGust"]
weather=[0,"weather"]
hazards=[0,"hazards"]
probabilityOfPrecipitation=[0,"probabilityOfPrecipitation"]
quantitativePrecipitation=[0,"quantitativePrecipitation"]
visibility=[0,"visibility"]
transportWindSpeed=[0,"transportWindSpeed"]
transportWindDirection=[0,"transportWindDirection"]
mixingHeight=[0,"mixingHeight"]
hainesIndex=[0,"hainesIndex"]
lightningActivityLevel=[0,"lightningActivityLevel"]
twentyFootWindSpeed=[0,"twentyFootWindSpeed"]
twentyFootWindDirection=[0,"twentyFootWindDirection"]
waveHeight=[0,"waveHeight"]
wavePeriod=[0,"wavePeriod"]
waveDirection=[0,"waveDirection"]
primarySwellHeight=[0,"primarySwellHeight"]
primarySwellDirection=[0,"primarySwellDirection"]
secondarySwellHeight=[0,"secondarySwellHeight"]
secondarySwellDirection=[0,"secondarySwellDirection"]
wavePeriod2=[0,"wavePeriod2"]
windWaveHeight=[0,"windWaveHeight"]
dispersionIndex=[0,"dispersionIndex"]
pressure=[0,"pressure"]
probabilityOfTropicalStormWinds=[0,"probabilityOfTropicalStormWinds"]
probabilityOfHurricaneWinds=[0,"probabilityOfHurricaneWinds"]
potentialOf15mphWinds=[0,"potentialOf15mphWinds"]
potentialOf25mphWinds=[0,"potentialOf25mphWinds"]
potentialOf35mphWinds=[0,"potentialOf35mphWinds"]
potentialOf45mphWinds=[0,"potentialOf45mphWinds"]
potentialOf20mphWindGusts=[0,"potentialOf20mphWindGusts"]
potentialOf30mphWindGusts=[0,"potentialOf30mphWindGusts"]
potentialOf40mphWindGusts=[0,"potentialOf40mphWindGusts"]
potentialOf50mphWindGusts=[0,"potentialOf50mphWindGusts"]
potentialOf60mphWindGusts=[0,"potentialOf60mphWindGusts"]
grasslandFireDangerIndex=[0,"grasslandFireDangerIndex"]
probabilityOfThunder=[0,"probabilityOfThunder"]
davisStabilityIndex=[0,"davisStabilityIndex"]
atmosphericDispersionIndex=[0,"atmosphericDispersionIndex"]
lowVisibilityOccurrenceRiskIndex=[0,"lowVisibilityOccurrenceRiskIndex"]
stability=[0,"stability"]
redFlagThreatIndex=[0,"redFlagThreatIndex"]

Stats =[temperature,
dewpoint,
maxTemperature,
minTemperature,
relativeHumidity,
apparentTemperature,
heatIndex,
windChill,
skyCover,
windDirection,
windSpeed,
windGust,
weather,
hazards,
probabilityOfPrecipitation,
quantitativePrecipitation,
visibility,
transportWindSpeed,
transportWindDirection,
mixingHeight,
hainesIndex,
lightningActivityLevel,
twentyFootWindSpeed,
twentyFootWindDirection,
waveHeight,
wavePeriod,
waveDirection,
primarySwellHeight,
primarySwellDirection,
secondarySwellHeight,
secondarySwellDirection,
wavePeriod2,
windWaveHeight,
dispersionIndex,
pressure,
probabilityOfTropicalStormWinds,
probabilityOfHurricaneWinds,
potentialOf15mphWinds,
potentialOf25mphWinds,
potentialOf35mphWinds,
potentialOf45mphWinds,
potentialOf20mphWindGusts,
potentialOf30mphWindGusts,
potentialOf40mphWindGusts,
potentialOf50mphWindGusts,
potentialOf60mphWindGusts,
grasslandFireDangerIndex,
probabilityOfThunder,
davisStabilityIndex,
atmosphericDispersionIndex,
lowVisibilityOccurrenceRiskIndex,
stability,
redFlagThreatIndex,]




def getDate(timeSlot):
    

    date = ""
    for i in range(len(timeSlot)-1):
        if i <10:
            date+= timeSlot[i]
        else:
            return date
    
def getTime(timeSlot):
    date = ""
    for i in range(len(timeSlot)-1):
        if i >10 and i <13:
            date+= timeSlot[i]
        elif i >15:
            return date



def regtime(value,time,day):
    dayCount = 400
    for valueSlot in value:
        timeSlot = valueSlot["validTime"]
        if getDate(timeSlot) == str(day):
            print(1)
            if getTime(timeSlot)== str(time):
                return valueSlot["value"]
            
            if dayCount> int(str(time))-int(str(getTime(timeSlot))):
                dayCount=int(str((time)))-int(str(getTime(timeSlot)))
                
                
        
        return dayCount


        

def getweather(loc):
    t = time.localtime()
    hour = time.strftime("%H",t)
    day = date.today()
    loction = requests.get(f"https://api.weather.gov/points/{CC[0]},{CC[1]}")
    loctionJson = json.loads(loction.content)
    grindpoints = requests.get(str(loctionJson["properties"]["forecastGridData"]))
    
    weather = json.loads(grindpoints.content)
    for stat in Stats:
        temputureList = weather["properties"][stat[1]]["values"]
        stat[0]  = regtime(temputureList,hour,day)

getweather(1)

for stat in Stats:
    print(stat[0])
        


        

    
    
    
    
    
    
    