#====Imports=====
import db_manager
import decision_maker
import util
import traditional_mcdm
import heuristic_mcdm

#====Configuration Settings=====
TOTAL_NUMBER_OF_CRITERIA = [2]
TOTAL_SOLUTION_SPACE = [10]
MCDM_TECHNIQUE = [1]
SEED = 2
TOTAL_DECISION_MAKER_PREFERENCES = 5
REMOVAL_COMBINATION = [[1,7],[3,6],[5,5]]


db_manager.create_database()

#====Experiment Design=====
for total_number_of_criteria in TOTAL_NUMBER_OF_CRITERIA:
  #print("total_number_of_criterion: " + str(total_number_of_criteria))
  
  for total_solution_space in TOTAL_SOLUTION_SPACE:
    #print("total_solution_space: " + str(total_solution_space))
    
    for required_set in util.required_set_generator(total_solution_space):
      #print("required_set: " + str(required_set))
      
      for mcdm_technique in MCDM_TECHNIQUE:
        #print("mcdm_technique: " + str(mcdm_technique))
        
        for margine in util.margin_generator(total_solution_space, required_set):
          #print("margine: " + str(margine))
          
          TO_REMOVE = util.removal_tracker(total_solution_space, required_set, margine)
          
          for seed in  range(1, SEED):
            #print("seed: " + str(seed))              
            
            db_manager.create_dataset_table(total_number_of_criteria)
            db_manager.create_dataset(total_number_of_criteria,total_solution_space)
            
            for decision_id in range(1, TOTAL_DECISION_MAKER_PREFERENCES):
              #print("decision_id: " + str(decision_id))
              DECISION_MAKER_PREFERENCE = decision_maker.generate_prefernce(total_number_of_criteria)
              #print("Decision Maker Preference:" + str(DECISION_MAKER_PREFERENCE))
              
              #print("===================================")
              #print("seed: " + str(seed)) 
              #print("total_number_of_criterion: " + str(total_number_of_criteria))
              #print("total_solution_space: " + str(total_solution_space))
              #print("required_set: " + str(required_set))
              #print("mcdm_technique: " + str(mcdm_technique))
              #print("margine: " + str(margine))
              #print("TO_REMOVE: " + str(TO_REMOVE))
              #print("Decision Maker Preference:" + str(DECISION_MAKER_PREFERENCE))
              
              TRADITIONAL_TOP_k = []
              TRADITIONAL_TOP_k = traditional_mcdm.top_k_finder(required_set, mcdm_technique, DECISION_MAKER_PREFERENCE)
              HEURISTIC_TOP_k = []
              HEURISTIC_TOP_k  = heuristic_mcdm.top_k_finder(required_set, mcdm_technique, DECISION_MAKER_PREFERENCE,TO_REMOVE, total_number_of_criteria, total_solution_space)
              
              accuracy = heuristic_mcdm.accuracy(TRADITIONAL_TOP_k, HEURISTIC_TOP_k)
              print("HEURISTIC_TOP_k" + str(HEURISTIC_TOP_k))
              print(accuracy)
              print("=======")
              #for combination in REMOVAL_COMBINATION:
                #str1 = "".join(str(e) for e in combination)
                #print("combination: " +str1)
                
                #add_record_to_master_table()
           
              
            
            
            
            
    