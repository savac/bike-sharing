"""
main script to coordinate all the tasks
"""
import os

# Parameters
alpha = 13
beta = 0.1
l1 = 0
l2 = 1e-8
vw_options = '-b 18'
vw_options_training = '-k --passes 1'

# Train
tsv_file = '../data/train.csv'
txt_file = '../data/train.txt'
os.system('python to_vw.py ' + tsv_file + ' ' + txt_file)
os.system('python shuffle_lines.py ' + txt_file + ' ' + txt_file)
os.system('python split_train.py ../data/train.txt ../data/train.txt ../data/test.txt 0.9') # split train file for training and validation

# Test
tsv_test_file = '../data/test.csv'
txt_test_file = '../data/test.txt'
#os.system('python to_vw.py ' + tsv_test_file + ' ' + txt_test_file) # don't use the test file just yet

txt_predictions_file = '../data/predictions.txt'

# Train with VW
print('Training...')
os.system('vw -f model.vw --ftrl --ftrl_alpha ' + str(alpha) + ' --ftrl_beta ' + str(beta) + ' --l1 ' + str(l1) + ' --l2 ' + str(l2) + ' --data ' + txt_file + ' ' + vw_options + ' ' +  vw_options_training)
#os.system('vw -f model.vw  -b 18 --passes 1 -l 0.7 --power_t 0.4 --l1 0 --l2 1e-8 --data ../data/train.txt --loss_function squared')
#os.system('~/vowpal_wabbit-7.9/utl/vw-hypersearch  1e-10 1 '  + 'vw -f model.vw --ftrl --ftrl_alpha ' + str(alpha) + ' --ftrl_beta ' + str(beta) + ' --l1 ' + str(l1) + ' --l2 ' + str(l2) + ' --data ' + txt_file + ' ' + vw_options + ' ' +  vw_options_training)


# Predict the test set
print('Predicting...')
os.system('vw -k -p ' + txt_predictions_file + ' --data ' + txt_test_file + ' -t -i model.vw ' + vw_options)

# Convert predictions to submission format
print('Converting the predictions...')
os.system('python to_submission.py')

# check prediction.txt vs test.txt
os.system('python eval_score.py')


