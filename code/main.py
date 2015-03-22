"""
main script to coordinate all the tasks
"""
import os

# Parameters
alpha = 10
beta = 5
l1 = 0
l2 = 1e-8
vw_options = '-c -b 26'
vw_options_training = '-k --passes 1'

# Train
tsv_file = '../data/train.csv'
txt_file = '../data/train.txt'
os.system('python to_vw.py ' + tsv_file + ' ' + txt_file)

# Test
tsv_test_file = '../data/test.csv'
txt_test_file = '../data/test.txt'
os.system('python to_vw.py ' + tsv_test_file + ' ' + txt_test_file)

txt_predictions_file = '../data/predictions.txt'

optim_hyperparam = False

# Train with VW
print('Training...')
os.system('vw -f model.vw --ftrl --ftrl_alpha ' + str(alpha) + ' --ftrl_beta ' + str(beta) + ' --l1 ' + str(l1) + ' --l2 ' + str(l2) + ' --data ' + txt_file + ' ' + vw_options + ' ' +  vw_options_training)

#os.system('vw -f model.vw  -b 18 -c --passes 1 -l 1 --power_t 0.01 --l1 0 --l2 1e-3 --data ../data/train.txt --loss_function squared')

# Predict the test set
print('Predicting...')
os.system('vw -p ' + txt_predictions_file + ' --data ' + txt_test_file + ' -t -i model.vw ' + vw_options)

# Convert predictions to submission format
print('Converting the predictions...')
os.system('python to_submission.py')
