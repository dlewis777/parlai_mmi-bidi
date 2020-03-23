# MMI-Bidi

Implements filtering and MMI-Bidi

To Run:

First run filterdata.py which takes 2 arguments -t [file with top K English Words] -f [file to filter]

Outputs a file named [FILENAME].filter

Next to create datasets for training a P(S|T) model, run swap.py which takes 1 argument -f [file to swap]

Outputs a file named [FILENAME].st

To train, you have to point ParlAI to those files you want.

For decoding, use the included torch_generator_agent.py file. This will create a file named nbest.txt

First run eval on the P(T|S) model to get an nbest list for each entry.
Next run makebi.py to tie the nbest list of targets to source responses into a file named newbi.txt

Next run eval on newbi.txt using the P(S|T) model which will make a file named output.txt. This file contains each line scored by the model.

Finally run getscores.py to get a final output with just the new best result.

Model Problems:
This model didn't really learn anything so it just spits out garbage and reranking has no effect. Probably more train time is needed.
