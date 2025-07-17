 # Profile Information System Using Different Data Types

#Online App Name
app_name = input("Enter the app name: ")                               

#User ID (int)
user_id = int(input("Enter your LinkedIn user ID: "))                 

#Full Name (str)
full_name = input("Enter your full name: ")                           

#Skills (list)
skills_input = input("Enter your skills (comma-separated): ")         
skills = [skill.strip() for skill in skills_input.split(',')]

#Experience Details (tuple)
Role = "Inter"
Company = "Goolge"
Experience =  (Role, Company)
total_projects = int(input("Enter number of completed projects: "))   
Experience = (Experience, total_projects)
Connection = int(input("Enter the Connections: "))
profile_url = input("Enter the profile url: ")                                                    

# Profile Completion Percentage (float)
completion_percentage = float(input("Enter profile completion %: "))  

# Certifications (set)
certs_input = input("Enter certifications (comma-separated): ")       
certifications = set(c.strip() for c in certs_input.split(','))

# Contact Info (dict)
contact_info = {
    "Email": input("Enter your email: "),                              
    "Phone": input("Enter your contact number: "),                    
    "Location": input("Enter your city and country: ")                
}

#Education Details
education = {
    "B.Tech" : "ECE - JNTUA University",
    "year" : 2025
}

#Job Preferences (dict)
job_preferences = {
    "Preferred Role": input("Enter preferred job role: "),             
    "Work Mode": input("Enter work mode (Remote/Onsite): "),    
    "Preferred Location": input("Enter preferred job location: ")      
}


#Open to Work (bool)
open_to_work_input = input("Are you open to new opportunities? (yes/no): ").strip().lower()
is_open_to_work = open_to_work_input == "yes"  # Converts to boolean

#Display LinkedIn Profile Information
print("\n--- LinkedIn Profile Summary ---\n")

# Using comma separation
print(f"Welcome to {app_name}")                                       #Enter the app name: LinkedIn
print(f"User ID: {user_id}")                                           #Enter your LinkedIn user ID: 10523
print(f"Name:{full_name}")                                            #Enter your full name: Tharuni chowdhary

# Using Percentage Formatting
print("Profile Completion: %.1f%%" % completion_percentage)           #Enter profile completion %: 92.8

# Using f-strings

print(f"Experience: {Role} at {Company}")
print(f"Projects Completed: {total_projects}")                      #Enter number of completed projects: 5
print(f"Connections: {Connection}+")                                #Enter the Connections: 500
print(f"Profile URL: {profile_url}")                                #Enter the profile url: "https://www.linkedin.com/in/username123" 
print(f"Skills: {skills}")                                          ##Enter your skills (comma-separated): Python,Data Analysis,SQl,Aws
print(f"Certifications: {certifications}")                          #Enter certifications (comma-separated): Basics of Python,Data science with python 
print(f"Contact Email: {contact_info['Email']}")                    #Enter your email: name123@gmail.com
print("\neducation:")                                                  
for key, value in education.items():
    print(f" {key}: {value}")
print(f"Phone: {contact_info['Phone']}")                           #Enter your contact number: 987654321
print(f"Location: {contact_info['Location']}")                     #Enter your city and country: Hyderabad,India
print(f"Job Role: {job_preferences['Preferred Role']}")            #Enter preferred job role:Data scientist
print(f"Work Mode: {job_preferences['Work Mode']}")                #Enter work mode (Remote/Onsite): Remote
print(f"Preferred Location: {job_preferences['Preferred Location']}") #Enter preferred job location: Bangalore
print(f"Open to Work: {is_open_to_work}")                            #Are you open to new opportunities? (yes/no): yes

#--- LinkedIn Profile Summary ---


'''Welcome to LinkedIn
User ID: 10523
Name:Tharuni chowdhary
Profile Completion: 92.8%
Experience: Inter at Goolge
Projects Completed: 5
Connections: 500+
Profile URL: "https://www.linkedin.com/in/username123"
Skills: ['Python', 'Data Analysis', 'SQl', 'Aws']
Certifications: {'Data science with python', 'Basics of Python'}
Contact Email: name123@gmail.com

education:
 B.Tech: ECE - JNTUA University
 year: 2025
Phone: 987654321
Location: Hyderabad,India
Job Role: Data scientist
Work Mode: Remote
Preferred Location: Bangalore
Open to Work: True'''
