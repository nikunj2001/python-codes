from covid import Covid 
import pyttsx3 
engine = pyttsx3.init() 


# os.system()
covid=Covid()
ind_data=covid.get_status_by_country_name("India")
Act=covid.get_total_active_cases()
con=covid.get_total_confirmed_cases()
engine.say("number of active cases in india")
engine.say( ind_data)
engine.say("nuber of active cases ") 
engine.say(Act) 
engine.runAndWait() 

