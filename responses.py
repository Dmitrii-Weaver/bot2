import random
from func import getvid
from func import getbullet

def get_response(message: str) -> str :
    p_message = message.lower()
    if p_message == "!hello" :
        return "Hey there!"
    if p_message == "!roll":
        return str(random.randint(1,6))
    if p_message == "!help":
        return " `YOUR MESSAGE IN HERE` "
    if p_message == "!getvid":
        return getvid.getvid()
    

    
    if p_message[:5] == "!tweet":
        return "currently under construction"
    
    

    #live stream/freechat get /
    if p_message[:6] == "!frame":
        if p_message.split(" ")[1] == "ame" or p_message.split(" ")[1] == "amelia" :
            return "https://www.youtube.com/@WatsonAmelia/live"
        if p_message.split(" ")[1] == "gura" :
            return "https://www.youtube.com/@GawrGura/live"
        if p_message.split(" ")[1] == "calli" or p_message.split(" ")[1] == "mori" :
            return "https://www.youtube.com/@MoriCalliope/live"
        if p_message.split(" ")[1] == "kiara" or p_message.split(" ")[1] == "wawa" or p_message.split(" ")[1] == "kiawa":
            return "https://www.youtube.com/@TakanashiKiara/live"
        if p_message.split(" ")[1] == "ina" :
            return "https://www.youtube.com/@NinomaeInanis/live"
        if p_message.split(" ")[1] == "irys" :
            return "https://www.youtube.com/@IRyS/live"
        if p_message.split(" ")[1] == "bae" or p_message.split(" ")[1] == "baelz" : 
            return "https://www.youtube.com/@HakosBaelz/live"
        if p_message.split(" ")[1] == "kronii" :
            return "https://www.youtube.com/@OuroKronii/live"
        if p_message.split(" ")[1] == "mumei" or p_message.split(" ")[1] == "moom" or p_message.split(" ")[1] == "moomers" :
            return "https://www.youtube.com/@NanashiMumei/live"
        if p_message.split(" ")[1] == "fauna" :
            return "https://www.youtube.com/@CeresFauna/live"
        if p_message.split(" ")[1] == "FWMK" or p_message.split(" ")[1] == "fuwamoco" or p_message.split(" ")[1] == "fuwawa" or p_message.split(" ")[1] == "mococo":
            return "https://www.youtube.com/@FUWAMOCOch/live"
        if p_message.split(" ")[1] == "shiori" or p_message.split(" ")[1] == "shiorin" :
            return "https://www.youtube.com/@ShioriNovella/live"
        if p_message.split(" ")[1] == "bijou" or p_message.split(" ")[1] == "biboo" :
            return "https://www.youtube.com/@KosekiBijou/live"
        if p_message.split(" ")[1] == "nerissa" or p_message.split(" ")[1] == "risa" :
            return "https://www.youtube.com/@NerissaRavencroft/live"


    if p_message == "!freechat":
        return "https://www.youtube.com/watch?v=xcdlTH2FZEo&list=PLdV-bBPbIWm44iC9TfwtA8TqS-TC5nT24&index=1"
    
    
    #bullet /researching more on the api/data, will take even more time/ get
    if p_message[:5] == "!ammo": 
        bulletName = ""
        for i in p_message.split(" ")[1:]:
            bulletName = bulletName + i + " "
        
        bulletInfo = getbullet.getammo(bulletName.strip())
        response = "Damage : " +  str(bulletInfo[0]["damage"]) + "\n" + "Armor Damage : " + str(bulletInfo[0]["armorDamage"]) + "\n" + "Fragmentation Chance : " + str(bulletInfo[0]["fragmentationChance"]) + "\n" + "Ricochet Chance : " + str(bulletInfo[0]["ricochetChance"]) + "\n" + "Penetration Power : " + str(bulletInfo[0]["penetrationPower"]) + "\n"+ "Accuracy : " + str(bulletInfo[0]["accuracy"]) + "\n"+ "Recoil : " + str(bulletInfo[0]["recoil"]) + "\n"+ "Initial Speed : " + str(bulletInfo[0]["initialSpeed"]) + "\n"

        return response
         
    