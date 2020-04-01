# MMI-Bidi

Implements filtering and MMI-Bidi

To Run:

First run filterdata.py which takes 2 arguments -t [file with top K English Words] -f [file to filter]

Outputs a file named [FILENAME].filter

Next to create datasets for training a P(S|T) model, run swap.py which takes 1 argument -f [file to swap]

Outputs a file named [FILENAME].st

To train, you have to point ParlAI to those files you want. Then run your favorite train settings.
python examples/train_model.py -t opensubtitles --nbest -m transformer/generator -mf [MODEL] ...

For decoding, use the included torch_generator_agent.py file. This will create a file named nbest.txt

First run eval on the P(T|S) model to get an nbest list for each entry.
In my case it was:
python examples/eval_model.py -t personachat --nbest -m transformer/generator -mf [MODEL]

Next run makebi.py to tie the nbest list of targets to source responses into a file named newbi.txt

Next run eval on newbi.txt using the P(S|T) model which will make a file named output.txt. This file contains each line scored by the model. In my case, I just hacked it so you have to replace the default test set with the newbi.txt 
ie cp newbi.txt valid_self_original.txt

To do so set the --score flag, and --location flag with the path to the test set that parlai will use.
python examples/eval_model.py --score True -t personachat --location [PATH] -mf [MODEL]

Finally run getscores.py to get a final output file final.txt with just the new best result.

Mturk code in model_evaluator folder.

Model Problems:
This model didn't really learn anything so it just spits out garbage and reranking has no effect. Probably more train time is needed.
