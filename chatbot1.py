#we need to get  list from another python file
import classification_words # importing anuthing which is in the file
#to make the string  to  integer work  we have to import re
import re


#making input to pass through my init method
input_to_break = input("chat here:")

#making a class
class gett_the_value:
    def __init__(self,sentence):
        self.sentence = sentence
        #making the sentence lower case:
        sentence_lower = self.sentence.lower()
        #spliiting the sentence and getting it in to list
        self.to_scan_list = sentence_lower.split()
    
    def changing_sentence(self):
        
        #now compare the list and print the  identified class
        identified_as = "other"
        for scan_word in classification_words.food_list:
            #then iterate every word through my made liist and check similar word
            if scan_word in self.to_scan_list:
                if True:
                    identified_as = "Food"
                    
            else:
                pass
                

        for scan_word in classification_words.shopping_list:
            if scan_word in self.to_scan_list:
                if True:
                    identified_as = "shopping"
                    
            else:
                pass   
            
        for scan_word in classification_words.transportation_list:
            if scan_word in self.to_scan_list:
                if True:
                    identified_as = "transportation"
                    
            else:
                pass
        
        print(identified_as)
    
    #making a function which could print  integer from the list
    def string_list_to_integer(self):
        
        #defining a regular expression pattern to match numbers
        pattern =r'\d+'

        for list_with_number in self.to_scan_list:
            #using re.findall() method to extract all numeric strings
            get_number = re.findall(pattern,list_with_number)
        
            #converting every extracted numeric substring into an float
            
            for number in get_number:
                final_extracted_number = float(number)

                # printing the extracted number
                print("The number got '{}':{}".format(list_with_number,final_extracted_number))
                print(final_extracted_number+2)
        

            
        

        
        
        

#TESTING THE INSTANCE
test1 = gett_the_value(input_to_break)
test1.changing_sentence()
test1.string_list_to_integer()




    

    
