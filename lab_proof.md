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


