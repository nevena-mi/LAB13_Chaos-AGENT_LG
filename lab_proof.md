## 2
python normalobjects_langgraph.py
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}

## 3
python normalobjects_langgraph.py
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
LangGraph is ready.

## 4
python normalobjects_langgraph.py
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
LangGraph is ready.


python test_4_build_intake_node.py
Example 1 input:
{'complaint': 'There is a portal humming in my basement.', 'category': '', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
Example 1 output:
{'complaint': 'There is a portal humming in my basement.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
----------------------------------------
Example 2 input:
{'complaint': 'A monster keeps knocking on my window at night.', 'category': '', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
Example 2 output:
{'complaint': 'A monster keeps knocking on my window at night.', 'category': 'monster', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
----------------------------------------
Example 3 input:
{'complaint': 'My psychic neighbor says the walls are whispering.', 'category': '', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
Example 3 output:
{'complaint': 'My psychic neighbor says the walls are whispering.', 'category': 'psychic', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
----------------------------------------
Example 4 input:
{'complaint': 'The power keeps going out whenever it rains.', 'category': '', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
Example 4 output:
{'complaint': 'The power keeps going out whenever it rains.', 'category': 'environmental', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
----------------------------------------
Example 5 input:
{'complaint': 'I lost my socks again.', 'category': '', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
Example 5 output:
{'complaint': 'I lost my socks again.', 'category': 'other', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
----------------------------------------

## 5
python normalobjects_langgraph.py
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
LangGraph is ready.

python test_5_build_validation_node.py
Example 1 input:
{'complaint': 'A portal opened in my basement last night.', 'category': 'portal', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
Example 1 output:
{'complaint': 'A portal opened in my basement last night.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
----------------------------------------
Example 2 input:
{'complaint': 'My toaster is emotionally unavailable.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
Example 2 output:
{'complaint': 'My toaster is emotionally unavailable.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
----------------------------------------


## 6
python normalobjects_langgraph.py     
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': 'Investigation Summary:\n\nThe reported issue involves a portal located in the basement emitting strange noises. Upon inspection, it was found that the portal’s mechanical components showed minor wear but no significant damage. The noise appearsto be caused by irregular vibrations linked to fluctuations in the portal’s energy stabilization system. No external interference or structural faults were detected. Further monitoring is recommended to assess whether the vibration levels increaseor if additional maintenance is required.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
LangGraph is ready.

python test_6_investigation_node.py
Example 1 input:
{'complaint': 'There is a portal under the school gym.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
Example 1 output:
{'complaint': 'There is a portal under the school gym.', 'category': 'portal', 'valid': True, 'investigation': 'Investigation Summary:\n\nThe complaint reported the presence of a portal under the school gym. Upon inspection, it was confirmed that there is an access point located beneath the gym area. The portal appears to be part of the building’s maintenance infrastructure, providing access to utility and service conduits. No unauthorized or hazardous materials were found, and the portal is secured to prevent public access. Further monitoring is recommended to ensure continued safety and security.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
----------------------------------------
Example 2 input:
{'complaint': 'A monster keeps following the car at night.', 'category': 'monster', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
Example 2 output:
{'complaint': 'A monster keeps following the car at night.', 'category': 'monster', 'valid': True, 'investigation': 'Investigation Summary:\n\nThe complaint reports a monster consistently following a car at night. Upon thorough review, no physical evidence or credible sightings supporting the presence of a monster were found. Nearby surveillance footage and eyewitness accounts indicate no unusual activity in the area during the reported times. It is possible the experience may be related to natural phenomena or misinterpretations influenced by low visibility and nighttime conditions. Further monitoring is recommended to ensure safety and address any future concerns.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
----------------------------------------
Example 3 input:
{'complaint': 'My psychic dreams are getting louder.', 'category': 'psychic', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
Example 3 output:
{'complaint': 'My psychic dreams are getting louder.', 'category': 'psychic', 'valid': True, 'investigation': 'Investigation Summary:\n\nThe complaint reports an increase in the intensity of psychic dreams, described as "getting louder." Upon review, there is no evidence of external factors or environmental influences contributing to the heightened psychic activity. The claimant’s experiences appear to be internal and subjective, with no reported physical or mental health changes that could account for the symptom escalation. This suggests the phenomenon is likely related to a natural fluctuation in psychic sensitivity rather than an external anomaly or fault in any provided service. Further monitoring is recommended to track any changes or developments.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
----------------------------------------

## 7
python normalobjects_langgraph.py  
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': 'Investigation Summary:\n\nThe reported issue concerns a portal located in the basement making unusual noises. Upon inspection, it was found that the portal’s mechanical components show signs of wear, likely causing the irregular sounds. No structural damage or security risks were detected. Routine maintenance was overdue, which may have contributed to the problem. It is recommended to perform a full service and replace any worn parts to resolve the noise issue.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': 'The portal appears unstable but contained.', 'resolution': 'Resolution: We have inspected the basement portal and confirmed it is unstable, which is causing the unusual noises you’re hearing. Our team has secured the portal to ensure it remains safely contained and will continue monitoring it closely. Please report any further issues immediately.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
LangGraph ready.

python test_7_resolution_node.py
Example 1 input:
{'complaint': 'There is a portal under the school gym.', 'category': 'portal', 'valid': True, 'investigation': 'The portal seems unstable but contained behind debris.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
Example 1 output:
{'complaint': 'There is a portal under the school gym.', 'category': 'portal', 'valid': True, 'investigation': 'The portal seems unstable but contained behind debris.', 'resolution': 'Resolution: The portal under the school gym has been identified and assessed. While it appears unstable, it is currently contained and secured behind debris, preventing any immediate risk. We will continue to monitor the area closely and take necessary measures to ensure the safety of all students and staff.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
----------------------------------------
Example 2 input:
{'complaint': 'A monster keeps following the car at night.', 'category': 'monster', 'valid': True, 'investigation': 'The creature avoids bright lights and loud noise.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
Example 2 output:
{'complaint': 'A monster keeps following the car at night.', 'category': 'monster', 'valid': True, 'investigation': 'The creature avoids bright lights and loud noise.', 'resolution': 'Resolution: We have identified that the creature following your car at night is deterred by bright lights and loud noises. To prevent further encounters, we recommend keeping your car’s headlights on high beam when safe and occasional use of the horn to discourage the creature from approaching. This should help ensure your journeys remain safe and uninterrupted.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
----------------------------------------
Example 3 input:
{'complaint': 'My psychic dreams are getting louder.', 'category': 'psychic', 'valid': True, 'investigation': 'The issue appears connected to repeated psychic strain.', 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
Example 3 output:
{'complaint': 'My psychic dreams are getting louder.', 'category': 'psychic', 'valid': True, 'investigation': 'The issue appears connected to repeated psychic strain.', 'resolution': 'Resolution: After investigating your concern, we have identified that the increased intensity of your psychic dreams is linked to ongoing psychic strain. To help alleviate this, we recommend incorporating regular mental rest periods and grounding techniques to reduce strain. If symptoms persist, please consider consulting a specialist for further guidance.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
----------------------------------------

## 8
python normalobjects_langgraph.py
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': "Investigation Summary:\n\nThe complaint regarding the portal in the basement making strange noises was thoroughly examined. Upon inspection, it was found that the noise originates from the portal's mechanical components, specifically the alignment gears, which appear to be slightly worn and misaligned. No external damage or structural issues were detected around the portal area. The noises are likely caused by increased friction during operation. It is recommended to service the gears and perform realignment to resolve the issue.", 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': 'The portal appears unstable but contained.', 'resolution': 'We have investigated the issue with the portal in your basement and found it to be unstable, which is causing the strange noises you reported. Our team has contained the portal to prevent any further disturbances and will monitor it closely to ensure safety. We recommend avoiding the area until stability is fully restored. Thank you for your patience as we work to resolve this.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': 'The portal appears unstable but contained.', 'resolution': 'Seal the portal and monitor the basement overnight.', 'final_response': 'Thank you for bringing the issue to our attention. We have investigated the strange noises coming from the basement portal and found it to be unstable but contained. The portal has been securely sealed, and the area will be monitored overnight to ensure safety. Please let us know if you experience any further concerns.', 'status': 'closure_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve', 'close']}
LangGraph ready.

python test_8_closure_node.py
Example 1 input:
{'complaint': 'There is a portal under the school gym.', 'category': 'portal', 'valid': True, 'investigation': 'The portal seems unstable but contained behind debris.', 'resolution': 'Seal the portal and monitor the area overnight.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
Example 1 output:
{'complaint': 'There is a portal under the school gym.', 'category': 'portal', 'valid': True, 'investigation': 'The portal seems unstable but contained behind debris.', 'resolution': 'Seal the portal and monitor the area overnight.', 'final_response': "Thank you for bringing this matter to our attention. We have investigated the portal located under the school gym and found it to be unstable but safely contained behind debris. To ensure everyone's safety, the portal has been securely sealed and the area will be monitored overnight. Please rest assured that we are closely managing the situation.", 'status': 'closure_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve', 'close']}
----------------------------------------
Example 2 input:
{'complaint': 'A monster keeps following the car at night.', 'category': 'monster', 'valid': True, 'investigation': 'The creature avoids bright lights and loud noise.', 'resolution': 'Use bright floodlights and keep everyone together.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
Example 2 output:
{'complaint': 'A monster keeps following the car at night.', 'category': 'monster', 'valid': True, 'investigation': 'The creature avoids bright lights and loud noise.', 'resolution': 'Use bright floodlights and keep everyone together.', 'final_response': 'Thank you for bringing this to our attention. After investigating, we found that the creature tends to avoid bright lights and loud noises. To address your concern, we have implemented the use of bright floodlights and advised everyone to stay together when traveling at night. This approach has effectively resolved the issue, ensuring a safer experience for all.', 'status': 'closure_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve', 'close']}
----------------------------------------
Example 3 input:
{'complaint': 'My psychic dreams are getting louder.', 'category': 'psychic', 'valid': True, 'investigation': 'The issue appears connected to repeated psychic strain.', 'resolution': 'Rest, reduce stimulation, and monitor the symptoms.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
Example 3 output:
{'complaint': 'My psychic dreams are getting louder.', 'category': 'psychic', 'valid': True, 'investigation': 'The issue appears connected to repeated psychic strain.', 'resolution': 'Rest, reduce stimulation, and monitor the symptoms.', 'final_response': 'Thank you for bringing your concern to our attention. After investigating, we identified that the increased intensity of your psychic dreams is linked to repeated psychic strain. We recommend resting, reducing stimulation, and monitoring your symptoms closely. Please reach out if you experience any further issues—your well-being is our priority.', 'status': 'closure_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve', 'close']}
----------------------------------------


## 9
ython normalobjects_langgraph.py
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'pending', 'workflow_path': []}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'intake_complete', 'workflow_path': ['intake']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': "Investigation Summary:\n\nThe reported portal located in the customer's basement was inspected for any abnormal activity or mechanical issues. The device was found to be operational, but intermittent strange noises were confirmed during testing. These noises appear to originate from the portal’s internal stabilization mechanisms, likely caused by minor wear or alignment issues. No external damage or malfunction was detected. Further maintenance or calibration is recommended to resolve the noise and prevent potential future faults.", 'resolution': '', 'final_response': '', 'status': 'investigation_complete', 'workflow_path': ['intake', 'validate', 'investigate']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': 'The portal appears unstable but contained.', 'resolution': 'We have identified that the unusual noises from the basement portal are due to its current instability. Our team has secured and stabilized the portal to prevent any further disturbances. We will continue monitoring it closely to ensure it remains safely contained. Please report any new issues immediately.', 'final_response': '', 'status': 'resolution_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'portal', 'valid': True, 'investigation': 'The portal appears unstable but contained.', 'resolution': 'Seal the portal and monitor the basement overnight.', 'final_response': 'Thank you for your report regarding the strange noises coming from the basement portal. Upon investigation, we found the portal to be unstable but contained. We have sealed the portal and will continue to monitor the area overnight to ensure safety. Please let us know if you notice any further issues.', 'status': 'closure_complete', 'workflow_path': ['intake', 'validate', 'investigate', 'resolve', 'close']}
{'complaint': 'The portal in my basement keeps making strange noises.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': 'Complaint rejected because it is unrelated to the Downside Up workflow.', 'status': 'rejection_complete', 'workflow_path': ['intake', 'validate', 'reject']}
LangGraph ready.

python test_9_reject_node.py
Example 1 input:
{'complaint': 'My toaster is emotionally unavailable.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
Example 1 output:
{'complaint': 'My toaster is emotionally unavailable.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': 'Complaint rejected because it is unrelated to the Downside Up workflow.', 'status': 'rejection_complete', 'workflow_path': ['intake', 'validate', 'reject']}
----------------------------------------
Example 2 input:
{'complaint': 'The office stapler is sending me messages from the moon.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
Example 2 output:
{'complaint': 'The office stapler is sending me messages from the moon.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': 'Complaint rejected because it is unrelated to the Downside Up workflow.', 'status': 'rejection_complete', 'workflow_path': ['intake', 'validate', 'reject']}
----------------------------------------
Example 3 input:
{'complaint': 'I need more socks and better vibes.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': '', 'status': 'validation_complete', 'workflow_path': ['intake', 'validate']}
Example 3 output:
{'complaint': 'I need more socks and better vibes.', 'category': 'other', 'valid': False, 'investigation': '', 'resolution': '', 'final_response': 'Complaint rejected because it is unrelated to the Downside Up workflow.', 'status': 'rejection_complete', 'workflow_path': ['intake', 'validate', 'reject']}
----------------------------------------

