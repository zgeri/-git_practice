def get_boundaries(target,margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit,high_limit

low,high=get_boundaries(100,20)
print ("Low limit: " +str(low)+"," " high limit: " +str(high))

##########################################################################
def calculate_age(current_year, birth_year):
      return  current_year - birth_year
      
  
my_age=calculate_age(2018,1993)
dads_age =calculate_age(2018,1953)
print("I am " + str(my_age) +  " years old and my dad is " + str(dads_age) + " years old" )

##################################################
def create_spreadsheet(title, row_count = 10):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")

create_spreadsheet("Applications")
#############################################
stylish_settee_price=180.50
nice_sweater = 100
fun_books = 200
nice_sweater=300
total_price=nice_sweater + fun_books
total_price+=nice_sweater
print (total_price)

###########################################


greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + " " + question_text
print(full_text)
##################################################

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
full_birthday_string = birthday_string + str(age) + birthday_string_2
print(full_birthday_string)#
###############################################
modulo_variable = 14 % 4
print(modulo_variable)
#################################################################



lovely_loveseat_price = 254.00

luxurious_lamp_description='''Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'''

sales_tax= 0.088
customer_one_total=0

customer_one_itemization= ""
customer_one_total+=lovely_loveseat_price
print (str(customer_one_total) + "     "+  luxurious_lamp_description)

####################################################################################